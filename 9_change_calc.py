#Program to return change in quarters, dimes, nickels, pennies 
def calculate(price ,given):
    price_in_cents = int(round(price * 100))
    given_in_cents = int(round(given * 100))

    if given_in_cents < price_in_cents:
        return "Not enough money given."
    
    change_in_cents = given_in_cents - price_in_cents

    quarter = change_in_cents // 25
    change_in_cents %= 25

    dime = change_in_cents // 10
    change_in_cents %= 10

    nickel = change_in_cents // 5
    change_in_cents %= 5

    penny = change_in_cents

    return{
        "quarter": quarter,
        "dime": dime,
        "nickel":nickel,
        "penny": penny
    }

def main():
    print("Welcome to Change Calculator")
    price = float(input("Enter the Price of product:"))
    given = float(input("$ bill given :"))
    change = calculate(price ,given)

    if isinstance(change , str):
        print(change) # handing input error
    else:
        print(f"Quarters: {change['quarter']}")
        print(f"Dimes: {change['dime']}")
        print(f"Nickles: {change['nickel']}")
        print(f"Pennies: {change['penny']}")
if __name__ == "__main__":
    main()