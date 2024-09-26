pi = 3.141592653589793238462643383279502884197

def main():
    try:
        n = int(input("How many decimale places you want to print:"))
        if n <= 39 and n > 0:
            print(f"{pi:.{n+1}}")
        else:
            print("Sorry Maximum decimals value we have is 39")
    except:
        print("Invalid input")
    
if __name__ == "__main__":
    main()

