"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance."""

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    cd_account = Account(balance, 0)

    # Calculate interest earned
    interest_earned = balance * (interest_rate * months/12)

    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cd_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return  updated_balance, interest_earned 

