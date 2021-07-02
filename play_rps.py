from rps_game import RPS

print("Played best of 3.")

while not RPS.game_over():
    RPS.ask_user_for_choice()
    print("------------------")
