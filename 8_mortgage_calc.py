def mortgage_calc(principle_amt, loan_period, int_rate):
    month_int_rate = (int_rate / 100)/12
    month_loan_period = loan_period*12
    off_calc = pow(( 1+ month_int_rate) , month_loan_period)

    mortgage = principle_amt * month_int_rate * off_calc / (off_calc - 1)
    return mortgage
def main():
    print("Welcome to Mortgage calculator")
    principle_amt= int(input("Enter Principle amount:"))
    loan_period = int((input("Enter loan period:")))
    int_rate = float(int(input("Enter Interest rate:")))

    mortgage = mortgage_calc(principle_amt, loan_period, int_rate)
    print(f"For {principle_amt}$ property and {loan_period} year loan period at {int_rate}% the mortgage monthly will be {mortgage}" )

if __name__ == "__main__":
    main()