class Bank:
    IFSC_code = ""
    bank_name = ""
    branch_name = ""
    location = ""

    # Constructor
    def __init__(self, IFSC_code, bank_name, branch_name,location):
        self.IFSC_code = IFSC_code
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.location = location
