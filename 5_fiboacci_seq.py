def print_fib(n):
    if n== 1 or n==0:
        return n
    elif n > 1:
        return print_fib(n-1)+print_fib(n-2)
    else:
        print("Invalid input, please enter a non-negative integer.")
        return None
def main():
    n=int(input("Enter #:"))
    print(print_fib(n))



if __name__ == "__main__":
    main()