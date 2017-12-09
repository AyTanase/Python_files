import random
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to the cavern of secrets!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("You enter a dark cavern out of curiosity.",
      "It is dark and you can only make out a small glowing object.",
      "Do you pick up the object?")
if input("Do you pick up the object? [Y/N]: ") in ["y", "Y", "Yes", "YES", "yes"]:
    print("You picked up a key")
    print("As you proceed further into the cave,",
          "you notice something moving up ahead")
    print("You draw closer.... and suddenly the thing turns to face you!")
    print("It is a gient spider!")
    if input("Do you try to fight it or run? [Fight/Run]: ") in ["f", "F", "Fight", "FIGHT", "fight"]:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                     Fighting...                    ")
        print("   YOU HAVE THREE SHOTS AT BEATING THE SPIDER AT ROCK PAPER SCISSORS")
        print("                       IF THE SPIDER DEFEATS YOU, YOU DIE           ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        count = 1
        player_score = 0
        choice = { "R": 0, "P": 1, "S": 2 }
        inv_choice = ["rock", "paper", "scissors"]
        while count < 4:
            s_choice = int(random.randint(0, 2))
            p_choice = choice[input(f"Round {count}: Enter rock, paper, or scissors [R/P/S]: ")]
            print(f"spider: {inv_choice[s_choice]}")
            if p_choice == s_choice:
                print("draw! - play again")
            else:
                if p_choice == s_choice + 1 or (p_choice == 0 and s_choice == 2):
                    print("you win", end="")
                    player_score += 1
                else:
                    print("spider wins", end="")
                print(f" round {count}!")
                count += 1
        if player_score >= 2:
            print("you win!")
            print("you step over the cowering spider and proceed down the tunnel!")
        else:
            print("you lose! \n The spider eats you")
    else:
        print("You run! That was foolish! \n The spider is much faster. \n It chases and eats you. \n You are now dead.")
else:
    print("The small glowing object grows into a huge glowing giraffe and eats you. You die!")
input("\nPress Any Key to Continue...")
