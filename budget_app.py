class Budget:

    """
    A budget class to create objects of budget categories that can allow deposit, withdrawal, transfer between
    categories, as well as give a final balance for the category
    """

    def __init__(self, name):
        self.name = name
        self.categories = []   # to tell you the transactions that took place in your budget
        self.budget_amt = 0


    def deposit(self, deposit_amount, description):
        """
        A deposit method to accept deposit amount and what the deposit is for.
        It will cause the budget_amt to increase by the deposited amount
        """
        self.categories.append({'amount': deposit_amount, 'description': description})
        self.budget_amt += deposit_amount

    def withdrawal(self, withdrawal_amount, description):
        """
        A withdrawal method will cause the specified withdrawal amount to be deducted from the budgeted amount.

        """
        if self.check_funds(withdrawal_amount):
            self.categories.append({'amount': -withdrawal_amount, 'description': description})
            self.budget_amt -= withdrawal_amount
            return True
        return False

    def transfer(self, transfer_amount, category):
        """
        The transfer method receives the amount it wants to transfer from the category food.transfer(...)
        and transfers it to the category it wants to send it to .transfer(transfer_amount, 'clothing')
        """

        if self.check_funds(transfer_amount):
            self.withdrawal(transfer_amount, 'Transfer to '+category.name)
            category.deposit(transfer_amount, 'Transfer from '+self.name)
            self.budget_amt -= transfer_amount
            return True
        return False


    def get_balance(self):
        """
        The check_balance method would give the final balance from all the transaction made on a particular category
        which is gotten from the final money from the budgeted amount
        """
        return self.budget_amt

    def check_funds(self, amount):
        """
        The check_funds method is used to check if the available budget amount is enough to accomodate the requested
        amount
        """
        if self.get_balance() >= amount:
            return True
        return False


    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ''
        for item in self.categories:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
        output = title + items + "Total: " + str(self.budget_amt)
        return output


if __name__ == '__main__':
    food = Budget('food')
    clothing = Budget('clothing')
    print(food.budget_amt)
    print(clothing.budget_amt)
    food.deposit(3500, 'initial deposit')
    food.withdrawal(700, 'Provisions')
    print(food.get_balance())
    food.transfer(1200, clothing)
    print(food)
    print(clothing)
