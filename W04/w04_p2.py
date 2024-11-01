import random 

word_list = ["ether", "moroni", "isaac", "mahonri","temple", "body"]
secret_word = random.choice(word_list)
word_length = len(secret_word)
print ("Wellcome to the word guessing game!")
print ()
print("Your hint is :", "_" * word_length)

guess_count = 0
correct_guess = False
correct_letters = ["_"] * word_length

while not correct_guess:
    guess = input("What is your guess? ")

    if len(guess) != word_length:
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        correct_letters = ["_" if guess[i] != secret_word[i] else secret_word[i] for i in range(word_length)]
        
        if "_" not in correct_letters:
            print("Congratulations! You guessed it!")
            correct_guess = True
        else:
            print("Incorrect guess.")
            print("Your hint is:", " ".join(correct_letters))
            guess_count += 1

print(f"It took you {guess_count} guesses.")
print("Thanks for playing!")