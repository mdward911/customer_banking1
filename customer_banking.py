# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained."""
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = check_valid_num("Enter the initial savings account balance: ", float)
    savings_interest = check_valid_interest("Enter the annual savings account interest rate (0-100% or 0-1): ") 
    savings_maturity = check_valid_num("Enter the number of months for savings maturity: ", int)
    

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("\nSavings Account")
    print(f"Interest earned on savings account: ${savings_interest_earned:,.2f}")
    print(f"Updated savings account balance: ${updated_savings_balance:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = check_valid_num("Enter the initial CD account balance: ", float)
    cd_interest = check_valid_interest("Enter the annual interest rate for CD (0-100% or 0-1): ")
    cd_maturity = check_valid_num("Enter the number of months for CD maturity: ", int)
    

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("\nCD Account:")
    print(f"Interest earned on CD account: ${cd_interest_earned:,.2f}")
    print(f"Updated CD account balance: ${updated_cd_balance:,.2f}")

def check_valid_interest(question):
    while True:
        user_input = input(question).strip()

        try:
            if user_input.endswith("%"):
                # Handle percentage input
                interest = float(user_input[:-1]) / 100
            else:
                # Handle decimal input
                interest = float(user_input)
            
            if 0 <= interest < 1:
                return interest
            
            else:
                print("Invalid Input. Please enter Valid Interest Rate (0-100% or 0-1).\n")
        except ValueError:
            print("Invalid Input. Please enter a valid number,\n")

            print("Example: '10% or '.10'\n")

def check_valid_num(question, data_type= float):
    """Takes a question and a data type as input. Prompts use with question and only accepts input if it corresponds to the 
    data type and is greater than 0."""

    while True:
        number = input(question)
        try:
            number = data_type(number)
            if number > 0:
                return number
            else:
                print("Invalid Input. Please enter a number greater than 0.\n")
        except ValueError:
            print("Invalid Input. Please enter a valid number.\n") 

if __name__ == "__main__":
    # Call the main function.
    main()
