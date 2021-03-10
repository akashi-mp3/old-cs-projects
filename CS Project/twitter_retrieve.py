#!/usr/bin/python
print 'Content-Type: text/html'
print ''
#-------------essentials!--------------------------

#------------- Opening Bookends -------------------
import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved
import operator

#import for Twitter access and encoding
import string
import sys
import requests, json, urllib, urllib2, base64


print '<html>'
print '<head><title> Tweet Analysis </title></head>'
style = """<style>
		head, body {
			background: #58ACFA;
			   }
		a:link, a:visited, a:hover, a:active {
			color: black;
			}
	</style>"""
print style
print '<body>'

#=============== API functions ===================

# This prepates the credentials for Twitter
def get_credentials():
    #initialize to empty
    creds = {}
    creds['consumer_key'] = str()
    creds['consumer_secret'] = str()
    #get credentials
    creds['consumer_key'] = "JRRQwIBrhimuwIffw9ZlncDSg" #might have to change as API key expires
    creds['consumer_secret'] = "kfsbDKfo8VHVhb1IKhhmX45I1sMnyfSqDJrBdK2MRkURWwAwxD"
    return creds

def oauth(credentials):
    try:
        #Encode creds
        encoded_credentials = base64.b64encode(credentials['consumer_key'] + ':' + credentials['consumer_secret'])
        #Prepare URL and HTTP parameters
        post_url = "https://api.twitter.com/oauth2/token"
        parameters = {'grant_type' : 'client_credentials'}
        #Prepare headers
        auth_headers = {
            "Authorization" : "Basic %s" % encoded_credentials,
            "Content-Type"  : "application/x-www-form-urlencoded;charset=UTF-8"
            }

        # Make a POST call
        results = requests.post(url=post_url, data=urllib.urlencode(parameters), headers=auth_headers)
        response = results.json()

        # Store the access_token and token_type for further use
        auth = {}
        auth['access_token'] = response['access_token']
        auth['token_type']   = response['token_type']

        return auth
    except Exception as e:
        print "Failed to authenticate with Twitter credentials:", e
        print "Twitter consumer key:", credentials['consumer_key']
        print "Twitter consumer secret:", credentials['consumer_secret']
        sys.exit()

def get_tweets_timeline(screen_name, num_tweets, auth):
    # This collection will hold the Tweets as they are returned from Twitter
    collection = []
    
    # Prepare GET call, timeline URL, headers, parameters
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    timeline_headers = {
        "Authorization" : "Bearer %s" % auth['access_token']
    }
    parameters = {
        'screen_name' : screen_name,
        'count' : num_tweets,
        'lang' : 'en'
    }
    
    # Construct actual url to send to Twitter to get the timeline tweets
    get_url = url + '?' + urllib.urlencode(parameters)

    # Make the GET call to Twitter
    results = requests.get(url=get_url, headers=timeline_headers)
    #Twitter RESPONSE in JSON format.. YAY!
    response = results.json()
    #if (response.empty()):
    #    print "Twitter gave an empty response.  Do you have a valid username? Do you have tweets?"
    return response

def twitter_form_text():
    d = {}
    form_data = cgi.FieldStorage()
    for k in form_data.keys():
       d[k] = form_data[k].value
    return d['handle']
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#================ JSON Analysis ===================

word_count = {}
hashtag_count = {}

stopwords_list = []



def load_stopwords():
    in_stream = open('stopwords_list.txt','r')
    output = in_stream.read()
    in_stream.close()
    global stopwords_list 
    stopwords_list = output.split('\n')
    
    
def analyze_response_text(response):
    for t_tweet in response:
        t_text = t_tweet["text"]
        t_text = t_text.encode('ascii', 'ignore').decode('ascii') #converts all utf chars to ASCII, flattens, fix this later
        t_text = t_text.lower()
        word_list = t_text.split(' ')
        for word in word_list:
            word = str(word)
            word = word.strip('''.!?,;:-()[]{}'"''')
            word = word.replace('\'','')
            if is_valid_word(word): #if not stopword
                if word in word_count:
                    word_count[word] += 1 #add to bucket
                else:
                    word_count[word] = 1 #create a bucket
    #Time to sort word_count
    sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1))
    print sorted_word_count # make this prettier later on

def analyze_response_hashtag(response):
    for t_tweet in response:
        t_text = t_tweet["text"]
        t_text = t_text.encode('ascii', 'ignore').decode('ascii') #converts all utf chars to ASCII, flattens, fix this later
        t_text = t_text.lower()
        word_list = t_text.split(' ')
        for word in word_list:
            word = str(word)
            word = word.strip(".!?,;:-()[]{}'")
            word = word.replace('\'','')
            if is_hashtag(word): #if hashtag
                if word in hashtag_count:
                    hashtag_count[word] += 1 #add to bucket
                else:
                    hashtag_count[word] = 1 #create a bucket
    #Time to sort word_count
    sorted_hash_count = sorted(hashtag_count.items(), key=operator.itemgetter(1))
    print sorted_hash_count # make this prettier later on


def is_numeric(word): #helper
    try:
        i = float(word)
    except (ValueError, TypeError):
        return False
    return True

def is_hashtag(word):
    if word != "":
	if word[0]=="#":
            return True
	else:
            return False

#to be added to as we find cases to fix
def is_valid_word(word): #boolean, T if not valid, F otherwise
    if word in stopwords_list:
        return False
    elif "#" in word:
        return False
    elif "http" in word:
        return False
    elif "$" in word:
        return False
    elif is_numeric(word):
        return False
    elif "@" in word:
        return False
    elif word == '':
        return False
    elif "~" in word:
        return False
    elif "%" in word:
        return False
    else:
        return True
#==================================================

# ~~~~~~~~~~~~~~~ main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    creds = get_credentials()
    auth = oauth(creds)
    # text data from form
    screen_name = twitter_form_text()
    num_tweets = 200
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    response = get_tweets_timeline(screen_name, num_tweets, auth)
    load_stopwords()
    print '<p>Top buzzwords in ' + str(screen_name) + "'s timeline!</p>"
    analyze_response_text(response)
    print '<br><br>'
    print '<p>Trending tags in ' + str(screen_name) + "'s timeline!</p>"
    print 'Disclaimer: A little buggy right now. Non-hashtag text might make it through. We are working on it as you read this!'
    print '<br><br>'
    analyze_response_hashtag(response)
    
    
main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  

#------------- Closing Bookends -------------------
print '</body>'
print '</html>'

