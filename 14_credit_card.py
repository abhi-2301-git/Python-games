card_number = input("Enter your card number:")
num_list = list(card_number)
num_list.reverse()
try:
    num_list = [int(i) for i in num_list]

    for i in range(len(num_list)):
        if i % 2 != 0:
            num_list[i] *= 2

            if num_list[i] > 9:
                num_list[i] = num_list[i] - 9

    sum=0
    for i in num_list:
        sum += num_list[i]
    if sum % 10 == 0:
        print("Valid card numebr")
    else:
        print("Not a vlid card numebr")
except ValueError:
    print("Enter only numbers!")
