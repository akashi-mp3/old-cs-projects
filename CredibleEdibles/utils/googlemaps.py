import cgi
import urllib2
import urllib
import key

import json #requests > urllib2 any day of the week

def locate():
	token = ""
	token = key.getkeydict()['googlemaps_key']
	url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + token
	query_args = {}
	#url for accessing google maps geolcation api
	data = urllib.urlencode(query_args)
	#gets page info
	request = urllib2.Request(url, data)
	response = urllib2.urlopen(request)
	stuff = response.read()
	#encodes into utf
	#turns into dictionary
	dic = json.loads(stuff)
	loc = []
	loc.append(float(unicode(dic['location']['lat']).encode('utf-8')))
	loc.append(float(unicode(dic['location']['lng']).encode('utf-8')))
	return loc

print locate()
