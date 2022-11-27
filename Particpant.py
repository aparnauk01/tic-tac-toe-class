import GameRound
import random
class Participant:
    def __init__(self) -> None:
        self.choice = None


    def choose(self):
        pass

class computer(Participant):
    def __init__(self) -> None:
        super().__init__()
    def choose(self):
        switcher = [
             "rock",
             "paper",
             "scissor",
             "lizard",
             "spock"
        ]
        key,value = random.choice(list((enumerate(switcher))))
        print("Computer chose "+value)
        return value,key

class human(Participant):
    def __init__(self) -> None:
        super().__init__()
    def choose(self):
        self.choice = input('Enter the choice (rock,paper,scissor,lizard,spock): ')
        switcher = {
             "rock": 0,
             "paper": 1,
             "scissor": 2,
             "lizard": 3,
             "spock": 4
        }
        print("Human chose "+str(switcher[self.choice]))
        #print("Your choice is: "+ str(switcher[self.choice]))
        return self.choice,switcher[self.choice]




    

