from bank import Bank
from customer import Customer

class Account(Bank):
    account_ID = ""
    #cust = Customer(Customer.customerID, Customer.customerName, Customer.address, Customer.contact_details)
    balance = 0.0

    # Constructor
    def __init__(self, account_ID, cust, balance, IFSC_code, bank_name, branch_name,location):
        super().__init__(IFSC_code, bank_name, branch_name,location)
        self.account_ID = account_ID
        self.cust = cust
        self.balance = balance

    def getAccountInfo(self, cust, bank):
        """\
            This function prints the account information of a customer.
            Prints the following:
            1) Customer Name
            2) Bank Name
            3) Customer ID
            4) Account ID
            5) Balance
            6) Contact


            Input:
                1) cust: The customer object to access the customer details.
                2) acc: The account object to access the account details.
        """

        print("\nHello {name}, your balance is {bal}.\n".format(name=cust.customerName, bal=self.balance))
        print("Account Details:\n")
        print("Bank Name: {bank_name} \t Account ID: {account_ID} \t Customer ID: {customer_id}".format(bank_name=bank.bank_name, account_ID=self.account_ID, customer_id=cust.customerID))
        print("Customer Name: {}".format(cust.customerName))
        #print("Customer ID: " + Customer.customerID)
        print("Balance: {}".format(self.balance))
        print("Contact: {}".format(cust.contact_details))


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

            #if(float(amount<SavingsAccount.SMinBalance)):
            #print("Your balance is savings account is low. You cannot withdraw. Please add more money.")

        if self.balance>=float(amount):
            self.balance-=float(amount)
            print("An amount of Rs. {} has been withdrawn from your account.\nCurrent Balance: {}".format(amount, self.balance))

        else:
            print("Insufficient Balance. Please enter a valid amount.")

    def getBalance(self):
        print("Your current balance is {}".format(self.balance))
