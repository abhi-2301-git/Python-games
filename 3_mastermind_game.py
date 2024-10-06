import random
rand_ = str(random.randint(1000,9999))

def play():
    global rand_
    progress = ['X','X','X','X']
    print(rand_)
    tries=0
    while True:
        guess = input("Enter a guess")
        
        while len(guess) != 4 or not guess.isdigit():
            print("Please enter exactly 4 numeric digits.")
            guess = input("Enter a 4-digit guess: ")

        tries += 1

        if guess == rand_ and tries == 1:
            print("Great! You guessed the number in your 1st try You're a Mastermind!")
            break

        elif guess == rand_:
            print(f"yay you got it in {tries} try")
            break

        for i in range(0,4):
            if rand_[i] == guess[i]:
                progress[i] = guess[i]
            

        print("current progress",''.join(progress))  

play()
