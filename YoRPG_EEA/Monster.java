/*=============================================
  class Monster -- Represents random incarnations of 
  the adventurer's natural enemy in Ye Olde RPG
  =============================================*/

public class Monster extends Character {

  // ~~~~~~~~~~~ INSTANCE VARIABLES ~~~~~~~~~~~
  // inherited from superclass
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  /*=============================================
    default constructor
    pre:  instance vars are declared
    post: initializes instance vars.
    =============================================*/
  public Monster() {
	  super();
	  _hitPts = 150;
	  _strength = 20 + (int)( Math.random() * 45 ); // [20,65)
    _defense = 40;
	  _attack = .4;
    }
    
  public string about(){
    return "how the heck are you reading this right now?"
  }
  
  public void normalize(){
  }
  public void specialize(){
  }
}//end class Monster

