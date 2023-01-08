"""

Record the last transaction information, including the type and amount of the transaction

@Author Hengran Wu
"""
class Transaction:
    type = None
    amount = None
    def __init__(self,type,amount):
        """

        Args:
            type(str): Transaction type
            amount(float): Transaction amount
        """
        self.type = type
        self.amount = amount
    def update(self,type,amount):
        """

        Args:
            type(str): Transaction type
            amount(float): Transaction amount

        Returns:

        """
        self.type = type
        self.amount = amount
    def show(self):
        """

        Print information about the last transaction

        Returns:

        """
        print("last transaction type: ",self.type)
        print("last transaction amount: ",self.amount)