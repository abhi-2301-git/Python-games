import random
def check_guess(rand_select,tries):
    display=["_","_","_","_","_"]
    while tries < 7:
        user_input = input("guess a letter:").lower()
        
        if user_input in rand_select:
            print("Yay you guessed a letter !")
            # Replacing _ with letter
            display[rand_select.index(user_input)]=user_input
            # displaying output without , & ""
            output = ' '.join(display)
            print(output)
        else:
            print("Wrong guess")
        # Inc tries and printing remaining tries
        tries += 1
        print(f"tries remaining {7-tries}") 
        # checking if all letters gussed right
        for letter in display:
            if letter == "_":
                isWon=False
                break
            else:
                isWon=True
        # printing won or lose
        if isWon:
            print("Yay you guessed the word")
        elif tries == 7:
            print("Sorry you have ran out of tries")


# Start
print("A 5 letter fruit is choosen from random, You have 7 guesses to guess each letter of that fruit")
# Definind a list of fruits
collection = ["mango","lemon","grape","peach"]
rand_select= random.choice(collection)
tries=0


check_guess(rand_select,tries)
