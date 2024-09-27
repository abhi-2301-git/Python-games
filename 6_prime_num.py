def prime_check(n):
    default=1
    factors=0
    if n==1:
        return False
    while factors < 3 and default <= n:
        if n % default == 0:
            factors+=1
            
        default+=1
    if factors < 3:
        return True

def main():
    try:
        n=(int(input("Enter a number and lets check if It is prime or now:")))
    
        if prime_check(n):
            print(f"{n} is a prime number")
        else:
            print(f"{n} is not a prime number")
    except ValueError:
        print("Invalid input!!!")
        

if __name__ == "__main__":
    main()