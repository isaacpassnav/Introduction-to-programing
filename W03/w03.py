## Isaac Pasapera ## 
print("Wellcome to Adventure Game")
print()
print("Nivel 1")
print("You find yourself on a dark path. To your left, You see a dense forest. To you right, there is a mysterious cave. In front of You, there is a hanging bridge.")
choice = input("Which path do you chose? (LEFT, RIGHT, FRONT): ")

if choice.upper() == "LEFT":
    print("Level 2:")
    print("Inside the forest, you come across a shine treasure, but you also enconter a giant bear.")
    choice = input ("What do you do? (GRAB TREASURE / CONFRONT BEAR): ")

    if choice.upper() == "GRAB TREASURE":
        print("Congratulation! you have obtained a treasure, but you have awakened the bear. You most flee quickly.")
        print("GAME OVER")
    elif choice.upper() == "CONFRONT BEAR":
        print("Brave choice! you have fought againts the bear and emerged victorious.")
        print("Level 3:")
        print("After defearing the bear, you arrive the snowy montain. There is a dark cave and steep path.")
        choice = input("Which path do you take? (Cave / Path):")

        if choice.upper() == "CAVE":
            print("Inside de cave")
            print("Game over")
        elif choice.upper() == "PATH":
            print("You climb up the steep path and reach the montain's peak. You have an amazing view. ")
            print("Congratulation!! You completed the game.")
        else:
            print("Invalid choice. Game over")
    else:
        print("Invalid choice. Game over")
elif choice.upper() == "FRONT":
    print("Level 2: ")
    print("As you cross the bridge, a troll appears. You must solve it's riddle to proceed.") 
    answer = input("What is the fastest animal in the world? ")
    if answer.upper() == "CHEETAH":
        print("Correct answer")
        print("Game over") 
    else:
        print("Wrong answer") 
        print("Game over")

else:
     print("Invalid choice. Game over T.T")