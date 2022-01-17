
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


def calc_payment():
    while True:  # loop until valid input
        value = (input("What is your monthly payment in GBP?: £"))
        if float_validation(value):  # if input is valid (true) move on
            return value


def calc_months_remaining():
    while True:  # loop until valid input
        value = (input("How many months left on the term?: "))
        if int_validation(value):  # if input is valid (true) move on
            return value


def calc_loan_term():
    while True:  # loop until valid input
        value = (input("How many months is the loan term?: "))
        if int_validation(value):  # if input is valid (true) move on
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
    print("£", f'{payment:.2f}', "has been payed. Loan has accumulated £", f'{interest_paid:.2f}', "in interest\n")
    print("£", f'{money_owed:.2f}', "is still owed")
    # f'{variable:.2f}' this formats the enclosed variable to 2 decimal places (using f strings)

def main():
    # instantiate variables
    money_owed = 0
    apr_rate = 0
    payment = 0
    loan_term = 0
    months_remaining = 0

    # assign them values as per user input
    money_owed = float(calc_money_owed())
    apr_rate = float(calc_apr_rate())
    payment = float(calc_payment())
    loan_term = int(calc_loan_term())
    months_remaining = int(calc_months_remaining())

    # calculate loan details
    payment = payment * (loan_term - months_remaining)
    monthly_rate = apr_rate / 100 / (loan_term - months_remaining)
    interest_paid = money_owed * monthly_rate
    money_owed = (money_owed + interest_paid) - payment

    # print results
    print_results(payment, interest_paid, money_owed)


main()
