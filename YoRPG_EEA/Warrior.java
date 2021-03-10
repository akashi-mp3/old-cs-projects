/*=============================================
  class Warrior -- protagonist of Ye Olde RPG
  =============================================*/
 
public class Warrior extends Character {

    /*=============================================
      default constructor
      pre:  instance vars are declared
      post: initializes instance vars.
      =============================================*/
    public Warrior() {
	_hitPts = 125;
	_strength = 100;
	_defense = 40;
	_attack = .4;
    }


    /*=============================================
      overloaded constructor
      pre:  instance vars are declared
      post: initializes instance vars. _name is set to input String.
      =============================================*/
    public Warrior( String name ) {
	    this();
	    _name = name;
    }
    
    public void specialize(){
      _attack=1;
      defense=20;
    }
    
    public void normalize(){
      _attack=.4;
      _defense=40;
    }
    
    public string about(){
      return "Me warrior varry strong, but knot sew smart. Pick me if you want to bash in som monster skulls."
    }

}//end class Warrior

