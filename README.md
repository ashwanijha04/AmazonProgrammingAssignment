# AmazonProgrammingAssignment
Programming Course-End Project: Banking Domain

In this project, we have replicated the functions of a bank by using the concepts of object-oriented programming.

# Note: This program uses Python 3 and this can only be run properly using the python3 command.
# Please do not use Python 2.x or the string inputs will cause problems.


## Downloading and Installing Python:
	To install python 3 on a mac, we use the following command:
		brew install python3
		(Please do not use python 2)
	
	If brew is not already installed, we need to install it from here.



## Requirements:
	To run the code, you need to use python 3.
	

## Cloning and Running Immediately:
	Use the following commands in your terminal.
		cd Desktop
		git clone https://github.com/ashwanijha04/AmazonProgrammingAssignment
		
	After the folder is downloaded,
		cd AmazonProgrammingAssignment
		python3 BankRunner.py


## Code Description:

	The solution code contains the following files:


##### •bank.py 
Contains Bank class with the following attributes:
    IFSC_code
    bank_name
    branch_name
    location
Also contains a constructor that initializes the values dynamically.



##### •customer.py
Contains the customer class with the following attributes:
    customerID
    customerName
    address
    contact_details


##### •account.py
Contains the account class with the following attributes:
    account_ID 
    balance

The following functions are defined:
    getAccountInfo()
    deposit()
    withdraw()
    getBalance()
 


##### •SavingsAccount.py
Contains the savings account logic.
It has one attribute – SMinBalance
It also contains methods such as withdraw(), deposit() etc locally.


##### •BankRunner.py
This file imports the other classes and uses them to run the main logic.
This file has been created to ensure the separation of concerns and modularity during development for easy improvements and maintainance.
It contains the following functions:
customerDetails()
BankDetails()
AccountDetails()


## Usage – Using the command line bank app from a terminal
1)	Open a terminal.
2)	Navigate to the project folder.
cd Desktop/Phase\ 1/Programming
		
3)	We need to run the BankRunner.py which has all the other classes imported. By this implementation, we keep the logic away from the user and it is also easy to maintain code.
python BankRunner.py 


