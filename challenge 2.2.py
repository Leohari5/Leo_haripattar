'''implement a class called player that represents a cricket player.the player class should have a method called play () which prints "the player is playing cricket".derive two classes,batsman and bowler,from the player class.override the play() method in each derived class to print,"the batsman is batting" and "the bowler is bowling", respectively.'''


#define the base class player
class player:

  def play(self):
    print("the player is cricket player.")


#define the derived class batsman
class Batsman(player):

  def play(self):
    print("the batsman is batting.")


#define the derived class bowler
class Bowler(player):

  def play(self):
    print("the bowler is bowling.")


#create objects of batsman and bowler class
batsman = Batsman()
bowler = Bowler()
#call the play() method for each object
batsman.play()
bowler.play()
