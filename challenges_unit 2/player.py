class player:
    def play(self):
        print("the player is playing cricket")
class batsman(player):
    def play(self):
        print("the batman is batting")
class bowler(player):
    def play(self):
        print("the bowler is bowling")
batsman=batsman()
bowler=bowler()
#call the play()method for each object
batsman.play()
bowler.play()
