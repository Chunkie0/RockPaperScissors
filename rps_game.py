from random import sample

class RPS:
    rpsList = ["rock", "paper", "scissors"]
    bof = 3
    scoreP = 0
    scoreAI = 0

    def random_word():
        return sample(RPS.rpsList, 1)[0]

    def play(choice, choiceAI):
        if choiceAI == choice:
            return print("Draw!")
        if choiceAI == choice - 1 or choiceAI - 2 == choice:
            print(f"Player gets a point: Player-{RPS.rpsList[choice]} AI-{RPS.rpsList[choiceAI]}")
            RPS.scoreP += 1
        else:
            print(f"AI gets a point: Player-{RPS.rpsList[choice]} AI-{RPS.rpsList[choiceAI]}")
            RPS.scoreAI += 1

    def ask_user_for_choice():
        choice = input("rock, paper, scissors?-> ")
        while choice not in RPS.rpsList:
            choice = input("No such option. rock, paper, scissors?-> ")
        RPS.play(RPS.convert_to_index(choice), RPS.convert_to_index(RPS.random_word()))

    def convert_to_index(self):
        return RPS.rpsList.index(self)

    def AI_win():
        if RPS.scoreAI == RPS.bof:
            print(f"AI Won! Score Player-{RPS.scoreP} AI-{RPS.scoreAI}")
            return True
        else:
            return False
    
    def player_win():
        if RPS.scoreP == RPS.bof:
            print(f"Player Won! Score Player-{RPS.scoreP} AI-{RPS.scoreAI}")
            return True
        else:
            return False
    
    def game_over():
        if RPS.player_win() or RPS.AI_win():
            return True
        else:
            return False