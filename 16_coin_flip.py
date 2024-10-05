import random

def flip(n):
    prob=['Head','Tail']
    for i in range(n):
        choice = random.choice(prob)
        print(f"{i+1} : {choice}")
    print("Program completed")
    
n = int(input("Enter # of flips:"))
flip(n)