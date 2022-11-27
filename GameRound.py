import Particpant
class Game:
    def __init__(self) -> None:
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        self.winner = None


def play(game, comp, human):
    human_choice, human_val = human.choose()
    comp_choice,comp_val = comp.choose()
    print(game.rules[human_val][comp_val])
    decision =game.rules[human_val][comp_val]
    if(decision == 0):
        print("Game is Tie")
    elif(decision == 1):
        print("Game is won by  human: "+human_choice)
    else:
        print("Game is failed by human: "+human_choice)

    


def main():
    game = Game()
    comp = Particpant.computer()
    human = Particpant.human()
    play(game,comp,human)

if __name__ == '__main__':
    main()