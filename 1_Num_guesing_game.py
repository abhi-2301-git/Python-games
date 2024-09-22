import random
def check_guess(rand_num,total_guess):
    while total_guess < 3:
        #try block so that user enters valid number
        try:
            user_num=int(input("Enter a guess #:"))
        except:
            print("Invalid input")
        # checking conditions
        if user_num < rand_num:
            print("Low")   
        elif user_num > rand_num:
            print("high")    
        elif user_num == rand_num:
            print("You win the number was "+str(rand_num))  
            break
        #incrementing guess & displaying guess
        total_guess += 1
        print("guess remaining "+str(total_guess)+"/3")
        #if block so that on 3rd guess try again is not printed
        if total_guess < 3:
             print("Try again")
    #User lost
    if total_guess == 3:
        print(f"Sorry you lost , the number was {rand_num}")
        
rand_num=random.randint(0,100)
total_guess=0
check_guess(rand_num,total_guess)
