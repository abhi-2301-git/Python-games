
def loop(n,fact):
    for i in range(1,n+1):
        fact *= i
    return fact
def rec(n,fact):
    if n == 1 or n == 0:
        return fact
    return rec(n-1, fact * n)
    

def main():
    fact=1
    n= int(input("Enter #:"))
    option = int(input("1.using loop \n2.using recursion :"))
    if option == 1:
        print(loop(n,fact))
    elif option == 2:
        print(rec(n,fact))
    else:
        print("Wrong input!")

if __name__ == "__main__":
    main()