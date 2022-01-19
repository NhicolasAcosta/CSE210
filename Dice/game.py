import random

class Dice:
    def __init__(self):
        self.value = 0
        self.points = 0

    def roll(self):
        self.value = random.randint(1, 6)
        if self.value == 5:
            self.points = 50
        elif self.value == 1:
            self.points = 100
        else:
            self.points = 0

class Player:

    def __init__(self):

        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            self.dice.append(Dice())

    def start_game(self):
        roll = True
        while roll:
            roll_dice = input("Roll dice? [y/n] ")
            if roll_dice == "y":
                self.scores()
                self.prints()
            else: 
                roll = False

       
    def scores(self):

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score

    def prints(self):        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
