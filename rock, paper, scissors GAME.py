import random
while True:
    choices = ["piatra","foarfeca","hartie"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("piatra,foarfeca,fartie?: ").lower()
    if player == computer:
        print("Computer: ",computer)
        print("Player: ",player)
        print("Egal!")
    elif player == "piatra":
     if computer == "hartie":
        print("Computer: ", computer)
        print("Player: ", player)
        print("Computer a castigat!")
    if computer == "foarfeca":
        print("Computer: ", computer)
        print("Player: ", player)
        print("Player a castigat")


    elif player == "hartie":
     if computer == "foarfeca":
        print("Computer: ", computer)
        print("Player: ", player)
        print("Computer a castigat!")
     if computer == "piatra":
        print("Computer: ", computer)
        print("Player: ", player)
        print("Computer a castigat")
    elif player == "foarfeca":
     if computer == "hartie":
        print("Computer: ", computer)
        print("Player: ", player)
        print("Player a castigat!")
        if computer == "piatra":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer a castigat!")
    else: print("Jucati din nou!")

    play_again = input("Play again? (yes/no)")
    if play_again != "yes":
        break
print("Bye")