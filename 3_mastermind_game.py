import random

random_num=random.randint(1000,10000)
random_num_str=str(random_num)
correct = ['X']*4 
tries=0
while True: 
    n = input("Enter a guess :")
    tries += 1
    if n == random_num_str and tries == 1:
        print("Great! You guessed the number in just 1 try! You're a Mastermind!")
        break
    elif n == random_num_str:
        print(f"yay you got it in {tries} try")
        break
    else:
        try:
            for i in range(0,4):
                if n[i] == random_num_str[i]:
                    correct[i]=n[i]
                    tries+=1
        except IndexError as err:
            print(err,"Enter a 4 digit guess")

        else:
            correct[i]='X'
                
    print("current progress",''.join(correct))  

print("The random number was:", random_num)  
        

    
