
# Problem 1
# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.

# Input
# Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.
# Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

# Output
# Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.


def main():
    balance = 2000
    withdrawamount = float(input("Enter the amount you want to withdraw : "))
    bankcharges = 0.5
    if (withdrawamount <= balance) and (withdrawamount>=0) :
        print(f"Transaction made of ${withdrawamount}")
        print(f"Balance after transaction : ${balance - withdrawamount - bankcharges}")
    elif (withdrawamount>200):
        print("Your account does not have enough balance!")
        print(f"Account Balance : {balance}")

while True:
    value = input("Want to make transaction ? (Y or N) : ")

    if (value == "y") or (value=="Y"):
        main()

    elif (value == "n") or (value == "N"):
        break


    




