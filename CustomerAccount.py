"""

CustomerAccount is responsible for creating wallets, deleting wallets, viewing wallet details,
transferring money, logging out, and logging out of accounts.

@Author Hengran Wu
"""
from Wallet import *
from Fee import Fee
class CustomerAccount:
    firstName = None
    lastName = None
    countryOfResidence = None
    age = None
    email = None
    password = None
    userName = None
    wallets = []
    staticId = 0
    fee:Fee =None
    customerAccount = []

    def __init__(self, firstName,lastName,countryOfResidence,age,email,password,userName,fee,customerAccount):
        """

        Args:
            firstName(str):
            lastName(str):
            countryOfResidence(str):
            age(str):
            email(str):
            password(str):
            userName(str):
            fee(Fee):
            customerAccount(list):
        """
        self.firstName = firstName
        self.lastName = lastName
        self.countryOfResidence=countryOfResidence
        self.age = age
        self.email = email
        self.password = password
        self.userName = userName
        self.fee = fee
        self.customerAccount = customerAccount
        print("The individual account is created successfully.")


    def show(self):
        """

        Print customer account information

        Returns:

        """
        print("firstName: ", self.firstName)
        print("lastName: ", self.lastName)
        print("countryOfResidence: ", self.countryOfResidence)
        print("age: ", self.age)
        print("email: ", self.email)
        print("password : ", self.password)
        print("userName: ", self.userName)

    def destroy(self):
        """

        Unregister object

        Returns:

        """
        del self

    def menu(self):
        """

        menu

        Returns:

        """
        while True:
            print("Please select the action you need to perform:")
            print("1: Create a wallet")
            print("2: Delete wallet")
            print("3: Show wallet details")
            print("4: Operating wallet")
            print("5: Log out")
            print("6: Delete current account")
            choice = input()
            if choice == "1":
                self.creatWallet()
            elif choice == "2":
                self.deleteWallet()
            elif choice == "3":
                self.showAllWallet()
            elif choice == "4":
                self.operateWallet()
            elif choice == "5":
                return
            elif choice == "6":
                self.deleteAccount()
                return
            else:
                print("Invalid operation")

    def creatWallet(self):
        """

        Create a wallet based on the wallet type

        Returns:

        """
        while True:
            print("The type of wallet you need to create")
            print("1: DailyUseWallet")
            print("2: SavingWallet")
            print("3: HolidaysWallet")
            print("4: MortgageWallet")
            choice = input()
            if choice == "1":
                wallet = DailyUseWallet(self.staticId, 0,self.fee)
            elif choice == "2":
                wallet = SavingWallet(self.staticId, 0,self.fee)
            elif choice == "3":
                wallet = HolidaysWallet(self.staticId, 0,self.fee)
            elif choice == "4":
                wallet = MortgageWallet(self.staticId, 0,self.fee)
            else:
                print("Invalid operation")
                wallet = None
            if wallet != None:
                print("Wallet creation success")
                wallet.show()
                self.staticId += 1
                self.wallets.append(wallet)
                break

    def deleteWallet(self):
        """

        delete a wallet

        Returns:

        """
        print("Please enter the wallet id you want to delete")
        choice = input()
        n = len(self.wallets)
        for i in range(n):
            wallet = self.wallets[i]
            if str(wallet.id) == choice:
                self.wallets.remove(wallet)
                return
        print("The entered wallet id does not exist")

    def showAllWallet(self):
        """

        Print all wallet information

        Returns:

        """
        n = len(self.wallets)
        for i in range(n):
            wallet:Wallet = self.wallets[i]
            wallet.show()

    def operateWallet(self):
        """

        The entry menu for wallet transactions

        Returns:

        """
        print("Please enter the wallet id you want to operate")
        id = input()
        wallet = self.findWallet(id,self.wallets)
        if wallet ==None:
            print("Wallet does not exist")
            return
        print("Please select the action you need to perform:")
        print("1: Withdraw")
        print("2: Deposit")
        print("3: Transfer to wallets")
        print("4: Transfer to other customers")
        choice = input()
        if choice == "1":
            self.withdraw(wallet)
        elif choice == "2":
            self.deposit(wallet)
        elif choice == "3":
            self.transferToWallets(wallet)
        elif choice == "4":
            self.transferToOtherCustomers(wallet)
        else:
            print("Invalid operation")

    def findWallet(self,id:int,wallets):
        """

        Find a wallet by wallet id

        Args:
            id(int): wallet id
            wallets(list): The list of wallets under the current account

        Returns:
            Return wallet if found, otherwise return None

        """
        n = len(wallets)
        for i in range(n):
            wallet = wallets[i]
            if str(wallet.id) == id:
                return wallet
        return None

    def withdraw(self,wallet:Wallet):
        """

        Check whether the current wallet meets the withdrawal conditions, and withdraw money

        Args:
            wallet(Wallet):  The wallet that is currently performing the operation

        Returns:

        """
        print("Please enter the withdrawal amount")
        while True:
            str = input()
            try:
                amount = float(str)
                break
            except ValueError:
                print("Please enter the correct amount")
        wallet = self.check(wallet,"Withdraw",-amount)
        if wallet != None:
            wallet.transactions(-amount,"Withdraw")

    def deposit(self,wallet:Wallet):
        """

        Check whether the current wallet is available for deposit, and if so, complete
        the deposit according to the user's deposit amount

        Args:
            wallet(Wallet):  The wallet that is currently performing the operation

        Returns:

        """
        print("Please enter the deposit amount")
        while True:
            str = input()
            try:
                amount = float(str)
                break
            except ValueError:
                print("Please enter the correct amount")
        wallet.transactions(amount, "Deposit")

    def transferToWallets(self,wallet:Wallet):
        """

        Check whether the current wallet meets the transfer requirements for other wallets.
        If so, check whether the target wallet exists. If so, complete the transfer

        Args:
            wallet(Wallet):  The wallet that is currently performing the operation

        Returns:

        """
        print("Please enter the target wallet id")
        id = input()
        targetWallet:Wallet = self.findWallet(id, self.wallets)
        if targetWallet == None:
            print("The target wallet does not exist")
            return
        if targetWallet.check("Transfer to wallets") == False:
            print("The target wallet does not support the current transaction")
            return
        print("Please enter the transfer amount")
        while True:
            str = input()
            try:
                amount = float(str)
                break
            except ValueError:
                print("Please enter the correct amount")
        wallet = self.check(wallet, "Transfer to wallets", -amount)
        if wallet != None:
            wallet.transactions(-amount, "Transfer to wallets")
            targetWallet.transactions(amount, "Transfer to wallets")



    def transferToOtherCustomers(self,wallet:Wallet):
        """

        Check whether the current wallet meets the transfer requirements for other accounts.
        If so, check whether the target wallet of the target account exists. If so, complete the transfer

        Args:
            wallet(Wallet):  The wallet that is currently performing the operation

        Returns:

        """
        print("Please enter the target account")
        targetUserName = input()
        print("Please enter the target wallet")
        targetId = input()
        targetWallet:Wallet = self.findOtherCustomWallet(targetUserName,targetId)
        if targetWallet == None:
            print("Target account or target wallet does not exist")
            return
        if targetWallet.check("Transfer to other customers") == False:
            print("The target wallet does not support the current transaction")
            return
        print("Please enter the transfer amount")
        while True:
            str = input()
            try:
                amount = float(str)
                break
            except ValueError:
                print("Please enter the correct amount")
        wallet = self.check(wallet, "Transfer to wallets", -amount)
        if wallet != None:
            wallet.transactions(-amount, "Transfer to other customers")
            targetWallet.transactions(amount, "Transfer to other customers")

    def findOtherCustomWallet(self,targetUserName,targetId):
        """

        Check whether the target wallet exists based on the account name and wallet id

        Args:
            targetUserName(str): User name of the target account
            targetId(int): id of the target wallet

        Returns:

        """
        account: CustomerAccount = None
        for i in range(len(self.customerAccount)):
            if self.customerAccount[i].userName == targetUserName:
                account = self.customerAccount[i]
                break
        if account != None:
            for i in range(len(account.wallets)):
                if account.wallets[i].id == int(targetId):
                    return account.wallets[i]
            return None
        else:
            return None

    def login(self,userName,password):
        """

        Search for the matching account in the account list based on the account name and password.
        If yes, the login succeeds

        Args:
            userName(str):
            password(str):

        Returns:
            A successful login returns the customer account, and a failed login returns None

        """
        if(self.userName==userName):
            if(self.password==password):
                return self
        return None

    def deleteAccount(self):
        """

        Removes the current customer from the bank account and unregisters the current customer object

        Returns:

        """
        self.customerAccount.remove(self)
        print("The current customer account has been deleted")
        self.destroy()

    def check(self,wallet: wallets,type,amount):
        """

        If the current wallet cannot meet the current transaction amount, check whether
        there are other wallets that meet the transaction in other wallets of the account
        customer. If there are, switch wallets to complete the transaction according to
        the choice of the customer

        Args:
            wallet(Wallet):  The wallet that is currently performing the operation
            type(str): Transaction type
            amount(float):  Amount of transaction

        Returns:
            Return wallet or None

        """
        if wallet.check(type):
            if wallet.examine(amount):
                return wallet
            else:
                for i in range(len(self.wallets)):
                    preWallet = self.wallets[i]
                    if preWallet == wallet:
                        continue
                    if preWallet.check(type):
                        if preWallet.examine(amount):
                            print("The current wallet amount cannot be paid. Wallet ",preWallet.id, " is detected to meet the payment conditions. Whether to switch to wallet payment")
                            print("Enter 1 to switch wallet, enter 2 to reject")
                            while True:
                                choice = input()
                                if choice == "1":
                                    return preWallet
                                elif choice == "2":
                                    None
                                else:
                                    print("Invalid operation")
        return None
