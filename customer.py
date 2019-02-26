class Customer:
    customerID = ""
    customerName = ""
    address = ""
    contact_details = ""

    def __init__(self, customerID, customerName, address, contact_details):
        self.customerID = customerID
        self.customerName = customerName
        self.address = address
        self.contact_details = contact_details
