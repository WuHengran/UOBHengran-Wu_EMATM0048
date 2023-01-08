"""
The Wallet class and subclasses that is responsible for recording the wallet balance, the
basic operation of wallet transfer.

@Author Hengran Wu
"""
from Transaction import Transaction
from Fee import Fee

class Wallet:
    id = 0
    balance: int = 0
    lastTransaction: Transaction = None
    fee: Fee = None

    def __init__(self,id,balance,fee):
        """
        Initialization function
        Args:
            id (int): Wallet id
            balance (float): Balance of wallet
            fee (Fee): Used to deal with tax rates in transactions

        """
        self.id = id
        self.balance = balance
        self.fee = fee
    def transaction(self,amount,lastTransaction):
        """
        Calculate the balance, deduct taxes, and update the last transaction

        Args:
            amount (float): Amount of transaction
            lastTransaction (Transaction):  Record the last transaction

        Returns:
            Trade success or failure

        """
        if amount > 0:
            amount = self.fee.count(amount,lastTransaction.type)
        self.balance += amount
        self.lastTransaction = lastTransaction
        print("Successful transaction")
        print("Current wallet income：",amount)
        return True

    def prepares(self,amount,transactionType):
        """
        Encapsulate the Transaction type and amount as the Transaction class

        Args:
            amount(float): Transaction amount
            transactionType(Transaction): Transaction type

        Returns:
             Trade success or failure

        """
        transaction = Transaction(transactionType, amount)
        return self.transaction(amount, transaction)

    def examine(self,amount):
        """
        Check whether the current amount can complete the transaction

        Args:
            amount(float): Transaction amount

        Returns:
            Whether the transaction can be completed

        """
        if(self.balance+amount >= 0):
            return True
        else:
            print("The current balance is insufficient to complete the transaction")
            return False

    def transactions(self, amount, transactionType):
        """


        Args:
            amount(float): Transaction amount
            transactionType(str): Transaction type

        Returns:

        """
        pass

    def check(self, transactionType):
        """
        Check whether the transaction type is legitimate

        Args:
            transactionType(str): Transaction type

        Returns:

        """
        pass

    def show(self):
        """
        Print wallet information

        Returns:

        """
        print("id: ",self.id)
        print("balance",self.balance)
        if(self.lastTransaction != None):
            self.lastTransaction.show()


class DailyUseWallet(Wallet):
    type = "DailyUseWallet"
    capabilities = ("Withdraw","Deposit","Transfer to wallets","Transfer to other customers")

    def __init__(self, id, balance,fee):
        """

        Args:
            id (int): Wallet id
            balance (float): Balance of wallet
            fee (Fee): Used to deal with tax rates in transactions

        """
        super().__init__(id, balance,fee)

    def transactions(self,amount,transactionType):
        """

        Judge whether the transaction type is legitimate, whether the wallet balance
        can complete the transaction, and calculate the transaction information if
        the transaction is legitimate

        Args:
            amount(float): Transaction amount
            transactionType(str): Transaction type

        Returns:
             Trade success or failure
        """
        if(self.capabilities.__contains__(transactionType)):
            if super().examine(amount):
                return super().prepares(amount,transactionType)
        else:
            print("The wallet does not support the current operation")

    def check(self,transactionType):
        """

        Args:
            transactionType(str): Transaction type

        Returns:
            Whether the transaction can be completed
        """
        if (self.capabilities.__contains__(transactionType)):
            return True
        else:
            return False

    def show(self):
        """

        Print wallet information

        Returns:

        """
        super().show()
        print("type: DailyUseWallet")


class SavingWallet(Wallet):
    type = "SavingWallet"
    capabilities = ("Withdraw","Deposit")

    def __init__(self, id, balance,fee):
        """

        Args:
            id (int): Wallet id
            balance (float): Balance of wallet
            fee (Fee): Used to deal with tax rates in transactions
        """
        super().__init__(id, balance,fee)

    def transactions(self, amount, transactionType):
        """

        Judge whether the transaction type is legitimate, whether the wallet balance
        can complete the transaction, and calculate the transaction information if
        the transaction is legitimate

        Args:
            amount(float): Transaction amount
            transactionType(str): Transaction type

        Returns:
             Trade success or failure
        """
        if (self.capabilities.__contains__(transactionType)):
            if super().examine(amount):
                return super().prepares(amount, transactionType)
        else:
            print("The wallet does not support the current operation")

    def check(self, transactionType):
        """

        Args:
            transactionType(str): Transaction type

        Returns:
            Whether the transaction can be completed

        """
        if (self.capabilities.__contains__(transactionType)):
            return True
        else:
            return False

    def show(self):
        """

        Print wallet information

        Returns:

        """
        super().show()
        print("type: ",self.type)


class HolidaysWallet(Wallet):
    type = "HolidaysWallet"
    capabilities = ("Withdraw","Deposit","Transfer to wallets")

    def __init__(self, id, balance,fee):
        """

        Args:
            id (int): Wallet id
            balance (float): Balance of wallet
            fee (Fee): Used to deal with tax rates in transactions
        """
        super().__init__(id, balance,fee)

    def transactions(self, amount, transactionType):
        """

        Judge whether the transaction type is legitimate, whether the wallet balance
        can complete the transaction, and calculate the transaction information if
        the transaction is legitimate

        Args:
            amount(float): Transaction amount
            transactionType(str): Transaction type

        Returns:
             Trade success or failure

        """
        if (self.capabilities.__contains__(transactionType)):
            if super().examine(amount):
                return super().prepares(amount, transactionType)
        else:
            print("The wallet does not support the current operation")

    def check(self, transactionType):
        """
        Args:
            transactionType(str): Transaction type

        Returns:
            Whether the transaction can be completed
        Args:
            transactionType:

        Returns:

        """
        if (self.capabilities.__contains__(transactionType)):
            return True
        else:
            return False

    def show(self):
        """

        Print wallet information

        Returns:

        """
        super().show()
        print("type: ",self.type)


class MortgageWallet(Wallet):
    type = "MortgageWallet"
    capabilities = ("Deposit")

    def __init__(self, id, balance,fee):
        """

        Args:
            id (int): Wallet id
            balance (float): Balance of wallet
            fee (Fee): Used to deal with tax rates in transactions
        """
        super().__init__(id, balance,fee)

    def transactions(self, amount, transactionType):
        """

        Judge whether the transaction type is legitimate, whether the wallet balance
        can complete the transaction, and calculate the transaction information if
        the transaction is legitimate

        Args:
            amount(float): Transaction amount
            transactionType(str): Transaction type

        Returns:
             Trade success or failure

        """
        if (self.capabilities.__contains__(transactionType)):
            if super().examine(amount):
                return super().prepares(amount, transactionType)
        else:
            print("The wallet does not support the current operation")

    def check(self, transactionType):
        """

        Args:
            transactionType:

        Returns:

        """
        if (self.capabilities.__contains__(transactionType)):
            return True
        else:
            return False

    def show(self):
        """

        Print wallet information

        Returns:

        """
        super().show()
        print("type: ",self.type)
