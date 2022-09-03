import random


#GAME CLASS FOR RUN THE GAME LOGIC
class Game:
    counter = 1
    def Player(self, name):
        self.name = name
        print("Player: %s" % self.name)

    #LOGIC OF THE GAME
    def startGame(self, y, x):
        if y != x:
            Game.counter += 1
            main2()
            self.startGame(y)
        else:
            print("GOOD JOB YOUR ARE GASS RIGHT NO \n YOUR CHOSE! ATTAMPT NO IS : ", Game.counter)
            print("The random number is : " + str(x))
            exit()


#GAME RANDOM NUMBER GENARETOR
def random_no():
    x = random.randint(0, 10)
    return x

#MAIN FUNCTION FOR PLAYER NAME INPUT
def main1():
    c = Game()
    n1 = input("Enter the name of the player : ")
    c.Player(n1)

#2ND MAIN FUNCTION FOR PLAYER IMPUT IN THE PLAYING TIME
def main2():
    c = Game()
    ran = random_no()
    n2 = int(input("Enter your gauss number(0 to 10): "))
    c.startGame(n2,ran)


if __name__ == "__main__":
    main1()
    random_no()
    main2()
