import random


#GAME CLASS FOR RUN THE GAME LOGIC
class Game:
    counter = 1
    ran = random.randint(0, 10)
    def Player(self, name):
        self.name = name
        print("Player: %s" % self.name)

    #LOGIC OF THE GAME
    def startGame(self, y):
        if y != Game.ran:
            Game.counter += 1
            main2()
            self.startGame(y)
        else:
            print("GOOD JOB YOUR ARE GASS RIGHT NO \n YOUR CHOSE! ATTAMPT NO IS : ", Game.counter)
            print("The random number is : " + str(Game.ran))
            exit()




#MAIN FUNCTION FOR PLAYER NAME INPUT
def main1():
    c = Game()
    n1 = input("Enter the name of the player : ")
    c.Player(n1)

#MAIN FUNCTION FOR START THE GAME
def main2():
    c = Game()
    n2 = int(input("Enter your gauss number(0 to 10): "))
    c.startGame(n2)


if __name__ == "__main__":
    main1()
    main2()

