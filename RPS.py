from random import sample
class RPS:
    rps = ["rock", "paper", "scissors"]

    def __init__(self, choice):
        self.choice = choice

    def play(self):
        randomChoice = sample(self.rps, 1)[0]
        indP = self.rps.index(self.choice)
        indAI = self.rps.index(randomChoice)
        win = ""
        if self.choice == randomChoice:
            print("Draw!")
            print(self.choice, randomChoice)
        else:
            if indAI == indP-1 or indAI - 2 == indP:
                print(self.choice, randomChoice)
                win = "player"
            if indP == indAI-1 or indP - 2 == indAI:
                print(self.choice, randomChoice)
                win = "computer"
        return win

print("Welcome to Rock, paper, scissors.")
print("This is best of 5.")

scorePlayer = 0
scoreComputer = 0

gameOver = False

while gameOver != True:
    choice = input("Choose rock , paper or scissors: ")
    while choice not in RPS.rps:
        choice = input(f"No such choice {choice}. Choose rock , paper or scissors: ")
    player = RPS(choice)
    game = player.play()
    if game == "computer":
        scoreComputer += 1
        print(f"Computer wins! Score: Player {scorePlayer} AI {scoreComputer}")
    if game == "player":
        scorePlayer += 1
        print(f"Player wins! Score: Player {scorePlayer} AI {scoreComputer}")
    if scorePlayer == 3 or scoreComputer == 3:
        gameOver = True
