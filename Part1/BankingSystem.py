"""

The BankingSystem class is responsible for creating and logging in to customer accounts,
as well as viewing the profitability of the banking system.

@Author Hengran Wu
"""
from CustomerAccount import CustomerAccount
from Fee import Fee
class BankingSystem :
    customerAccount = []
    loginAccoumt: CustomerAccount = None
    fee:Fee = None
    def __init__(self):
       self.fee = Fee()
       print("The bank system is created successfully.")
    def menu(self):
        """

        Entry menu for customer operations

        Returns:

        """
        while True:
            print("Please select the action you need to perform:")
            print("1 Create a customer account")
            print("2 Login customer account")
            print("3 View banking system revenue")
            choice = input();
            if choice == "1":
                self.create()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.show()
            else:
                print("Invalid operation")

    def create(self):
        """

        Create a customer account

        Returns:

        """
        print("Please enter the first name")
        firstName = input()
        print("Please enter the second name")
        lastName = input()
        print("Please enter residence")
        countryOfResidence = input()
        print("Please enter your age")
        age = input()
        print("Please enter your email address")
        email = input()
        print("Please enter your password")
        password = input()
        print("Please enter your account name")
        userName = input()
        userName = self.checkUserName(userName)
        self.save(userName,password)
        account = CustomerAccount(firstName,lastName,countryOfResidence,age,email,password,userName,self.fee,self.customerAccount)
        self.customerAccount.append(account)

    def login(self):
        """

        Log in by username and password

        Returns:

        """
        print("Please enter your account name")
        userName = input()
        print("Please enter your password")
        password = input()
        account: CustomerAccount = None
        for i in range(len(self.customerAccount)):
            if self.customerAccount[i].login(userName,password) != None:
                account = self.customerAccount[i]
                break
        if account != None:
            account.menu()
        else:
            print("The account password does not match")

    def show(self):
        """

        Print receipts from bank accounts

        Returns:

        """
        print("Current income: ",self.fee.money)

    def checkUserName(self,userName):
        """

        Check whether the current user name is already in use

        Args:
            userName(str): User name

        Returns:

        """
        while True:
            for i in range(len(self.customerAccount)):
                if self.customerAccount[i].userName == userName:
                    print("The user name is the same. Please select another user name")
                    print("Please enter a new account name")
                    userName = input()
                    break
            return userName

    def encryption(self,password:str):
        """

        Encrypt customer passwords

        Args:
            password(str):

        Returns:

        """
        afterEncryption = ""
        for i in range(len(password)):
            afterEncryption += chr(ord(password[i]) + 2);
        lt = list(afterEncryption)
        for i in range(3):
            n= len(lt)-1;
            lt.insert(0,lt.pop())
        return "".join(lt)

    def save(self,username,password):
        """

        Write the user name, password, and encrypted password to the file

        Args:
            username(str):
            password(str):

        Returns:

        """
        file = open("password.txt", "a", encoding="UTF-8")
        file.write(username)
        file.write(" ")
        file.write(password)
        file.write(" ")
        file.write(self.encryption(password))
        file.write("\n")
        file.flush()
        file.close()
