# We are seperating the concerns by importing different modules
from bank import Bank
from customer import Customer
from account import Account

#import SMinBalance
# re is required to use regular expressions for validation checks like phone number
import re


def customerDetails():
    """
        The customer details are collected from the user in this function.

        Parameters: None

        Returns:
            customerID(String): The customer ID.
            customerName(String): The customer Name.
            address(String): The customer address.
            contact_details(String): The contact details of the customers.

    """


    customerID = input("Enter the customer ID: ")
    customerName = input("Enter the customer name: ")
    address = input("Enter the customer address: ")
    contact_details = input("Enter the phone number:")
    while not(re.match("^[0-9 -]+$", contact_details)) or len(contact_details)!=10:
        contact_details = input("Invalid. Enter a valid 10 digit phone number again: ")

    return customerID, customerName, address, contact_details

def BankDetails():
    """\
        The bank details are collected from the user in this function.

        Parameters: None

        Returns:
            bank_name(String): Name of the bank.
            branch_name(String): Name of the brancah.
            IFSC_code(String): The IFSC code of the bank.
            location(String): The location of the bank.
    """

    bank_name = input("Enter the Bank name: ")
    branch_name = input("Enter the branch name: ")
    IFSC_code = input("Enter the IFSC code: ")
    location = input("Enter the location: ")

    return bank_name,branch_name, IFSC_code, location


def AccountDetails():
    """\
        The account details are collected from the user in this function.

        Parameters: None

        Returns:
            account_ID(String): The account ID of the customer.
            balance(Float): The available balance.
    """
    print("\nIt is recommended that the account details are only edited by the administrator.\n")

    account_ID = input("Enter the account ID: ")
    balance = float(input("Enter the availabe balance: "))

    return account_ID, balance


def runTheBank():
    print("\nWelcome to the Rick and Morty Scientific Bank!\n")
    print("We'll take some steps from here.")
    print("First, you will enter your details and initial balance will be entered by Rick(admin).\n")
    print("After entering the details, you will be able to use normal bank functions like deposit, withdraw, steal.\n")
    print("Also, a minimum balance of Rs. 499 is required in savings account to make withdrawls.")

    customerID, customerName, address, contact_details = customerDetails()
    bank_name,branch_name, IFSC_code, location = BankDetails()
    account_ID, balance = AccountDetails()


    bank = Bank(IFSC_code, bank_name, branch_name, location)
    customer = Customer(customerID, customerName, address, contact_details)
    acc = Account(account_ID, customer, balance, IFSC_code, bank_name, branch_name,location)

    print(bank.bank_name)
    acc.getAccountInfo(customer, bank)

    keepRunning = True
    while(keepRunning==True):
        print("\nSelect an option.\n")
        print("1) Deposit money in the Rick Fund.\n")
        print("2) Withdraw money from the Morty fund.(Because Rick never returns.)\n")
        print("3) Get balance.\n")
        print("4) View account details again.")
        print("5) Exit from this weird bank\n")

        option = int(input("Enter a choice: "))

        if(option==1):
            amt = input("Enter the amount to be deposited: ")
            acc.deposit(amt)
            continue
        elif(option==2):
            amt = input("Enter the amount to be withdrawn: ")
            acc.withdraw(amt)
            continue
        elif(option==3):
            acc.getBalance()
            continue
        elif(option==4):
            acc.getAccountInfo(customer,bank)
            continue
        elif(option==5):
            keepRunning = False
            break
        else:
            print("Try Again.")
            continue


if __name__ == '__main__':
    runTheBank()
