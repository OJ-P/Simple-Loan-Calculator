def calc_money_owed():  # function to get the loan details
    while True:
        value = (input("How much is owed in GBP?: £"))
        if float_validation(value):
            return value


def calc_apr_rate():
    while True:  # loop until valid input
        value = (input("What is the annual percentage rate?: "))
        if float_validation(value):  # if input is valid (true) move on
            return value
        return value


def calc_payment():
    while True:  # loop until valid input
        value = (input("What is your monthly payment in GBP?: £"))
        if float_validation(value):  # if input is valid (true) move on
            return value
        return value


def calc_months():
    while True:  # loop until valid input
        value = (input("How many months until full payback?: "))
        if int_validation(value):  # if input is valid (true) move on
            return value
        return value


def float_validation(value):  # function to validate input that should be a float
    try:  # if value evaluated to be float exit function, if value error thrown prompt user
        value = float(value)
        return True
    except ValueError:
        print("invalid input")


def int_validation(value):  # function to validate input that should be an int
    try:  # if value evaluated to be int exit function, if value error thrown prompt user
        value = int(value)
        return True
    except ValueError:
        print("invalid input")


def print_results(payment, interest_paid, money_owed):
    print("£", payment, "has been payed, of which £", interest_paid, "was interest\n")
    print("£", money_owed, "is still owed")


# instantiate variables
money_owed = 0
apr_rate = 0
payment = 0
months = 0

# assign them values as per user input
money_owed = float(calc_money_owed())
apr_rate = float(calc_apr_rate())
payment = float(calc_payment())
months = int(calc_months())


# calculate loan details
monthly_rate = apr_rate / 100 / 12
interest_paid = money_owed * monthly_rate
money_owed = (money_owed + interest_paid) - payment

# print results
print_results(payment, interest_paid, money_owed)
