from bank import Bank
from customer import Customer
from account import Account

class SavingsAccount(Account):
    SMinBalance = 499.0


    def __init__(self, SMinBalance, account_ID, cust, balance, IFSC_code, bank_name, branch_name,location):
        super().__init__(self, account_ID, cust, balance, IFSC_code, bank_name, branch_name,location)
        self.SMinBalance = SMinBalance

    # This function gives the savings account info.
    def getSavingAccountInfo(self, cust, bank):
        print("\nHello {name}, your balance is {bal}.\n".format(name=cust.customerName, bal=self.balance))
        print("Account Details:\n")
        print("Bank Name: {bank_name} \t Account ID: {account_ID} \t Customer ID: {customer_id}".format(bank_name=bank.bank_name, account_ID=self.account_ID, customer_id=cust.customerID))
        print("Customer Name: {}".format(cust.customerName))
        #print("Customer ID: " + Customer.customerID)
        print("Balance: {}".format(self.balance))
        print("Contact: {}".format(cust.contact_details))
        print("Minimum balance to maintain in Savings Account: {} ".format(SMinBalance))



    def deposit(self, amount, flag=True):
        """\
            This function takes as input an amount to be deposited and
            a flag which is set to true by default and updates the balance and
            prints it to the console.

            Parameters:
                amount: The amount to be deposited.
                flag: The flag determines whether the deposit can be made. It lets
                us know that the account is either disabled or the amount is greater
                than the maximum deposit amount at a time.

            Return Type: Void

        """

        if flag==False:
            return


        if float(amount)<=0:
            print('Amount cannot be negative or zero.')
            amt = float(input("Please enter the correct amount(>0) again."))
            deposit(amt, flag=True)

        self.balance += float(amount);
        print("The amount of Rs. {} has been deposited. Current Balance: {}".format(amount, self.balance))


    # Withdrawls for savings account.
def withdraw(self, amount):
    """\
        This function takes in input an amount to be withdrawn,
        updates the balance and prints it to the console.

        Parameters:
            amount: The amount to be withdrawn.

        Return Type: Void

    """

    if(float(amount)<0.0):
        return

    if self.balance>=float(amount):
        self.balance-=float(amount)
        print("An amount of Rs. {} has been withdrawn from your account.\nCurrent Balance: {}".format(amount, self.balance))

    else:
        print("Insufficient Balance. Please enter a valid amount.")


    def getBalance(self):
        """\
            This function prints the account balance to the console.

            Return Type: Void

        """
        print("Your current balance is {}".format(self.balance))
