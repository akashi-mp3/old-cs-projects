/*=============================================
  class Rogue -- protagonist of Ye Olde RPG
  =============================================*/
 
public class Rogue extends Character {

    /*=============================================
      default constructor
      pre:  instance vars are declared
      post: initializes instance vars.
      =============================================*/
    public Rogue() {
	    _hitPts = 90;
	    _strength = 135;
	     _defense = 40;
	    _attack = .4;
    }


    /*=============================================
      overloaded constructor
      pre:  instance vars are declared
      post: initializes instance vars. _name is set to input String.
      =============================================*/
    public Rogue( String name ) {
	    this();
	    _name = name;
    }
    
    public String about(){
      return "I am the rogue, my greatest weapon is my silence. Pick me if you want to be a ninja."
    }
    
    public void specialize(){
      attack = .8;
      deffense = 25;
    }
    
    public void normalize(){
      attack = .4;
      defense = 40;
    }

}//end class Rogue

