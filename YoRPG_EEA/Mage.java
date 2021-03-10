/*=============================================
  class Mage -- protagonist of Ye Olde RPG
  =============================================*/
 
public class Mage extends Character {

    /*=============================================
      default constructor
      pre:  instance vars are declared
      post: initializes instance vars.
      =============================================*/
    public Mage() {
	    _hitPts = 140;
	_strength = 85;
	_defense = 40;
	_attack = .4;
    }


    /*=============================================
      overloaded constructor
      pre:  instance vars are declared
      post: initializes instance vars. _name is set to input String.
      =============================================*/
    public Mage( String name ) {
	this();
	_name = name;
    }
public string about(){
  return "I am the mystical mage, and I am capable of incredible feats. Pick me if you wish to focus on potions and spells"
}

public void specialize(){
  _defense = 15;
  _attack = 1.2;
}

public void specialize(){
	_defense = 40;
	_attack = .4;
}

}//end class Mage

