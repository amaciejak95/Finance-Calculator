"""
This program allows the user to access two financial calculators:
investment calculator and home loan repayment calculator
"""

import math


print('=' * 10 + " Welcome to the finance calculator " + '=' * 10)
print("Please select from the following options:\n")

while True:

    # Options available for the user

    print("investment - to calculate the amount of interest "
            "you'll earn on your investment")
    print("bond - to calculate the amount "
            "you'll have to pay on a home loan\n")
    print("Enter either 'investment' or 'bond' "
          "from the menu above to proceed. ")

    user_input = input("Please select your option: ").lower()

    # To calculate user's investment


    if user_input == "investment":
        print("You have selected an option to calculate your investment.\n")

        investment_amount = float(input("How much money are you investing? "
                                        "Please enter a number: "))
        interest_rate = float(input("What is the interest rate in %? "
                                    "Please enter a number: "))
        years_investing = int(input("How many years "
                                    "are you investing your money for? "))
        interest = input("Are you choosing simple or compound interest? "
                        "Please enter 'simple' or 'compound'. ").lower()


        # To calculate the total amount of money for simple interest

        if interest == "simple":
            interest_total = investment_amount * (1 + (interest_rate/100)
                            * years_investing)
            print(f"Your total amount is: {interest_total}")
            break

        # To calculate the total amount of money for compound interest

        elif interest == "compound":
            interest_total = (
            investment_amount
            * math.pow((1 + (interest_rate/100)), years_investing)
            )
            print(f"Your total amount is: {interest_total}")
            break

        else:
            print("\nYou have selected an invalid option. Please try again.")

    # To calculate user's bond repayment each month

    elif user_input == "bond":

        print("You have selected an option to calculate your bond.\n")

        house_value = float(input("What is the current value of your house? "
                                  "Please enter only a number: "))
        interest_rate = float(input("What is the interest rate? "
                                    "Please enter only a number: "))

        # Convert the interest rate to the percentage

        interest_rate = interest_rate/100

        monthly_interest_rate = interest_rate/12
        months = int(input("How many months are you planning "
                           "to take to repay the bond? "))

        # To calculate the amount
        # user will have to pay monthly to repay the bond

        repayment = (
        (monthly_interest_rate * house_value)
        /(1- (1 + monthly_interest_rate)**(-months))
        )
        print(f"The amount you have to pay each month is: {repayment}")
        break

    else:
        print("You have entered an invalid option. Please try again.")
        