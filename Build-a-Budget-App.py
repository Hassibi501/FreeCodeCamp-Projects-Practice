
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
        else:
            # print("Withdraw Amount is greater than balance")
            return False

    def get_balance(self):
        balance = 0
        for money in self.ledger:
            balance += money["amount"]
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {other_category.name}`")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            # print("transfer Amount is greater than balance")
            return False
        
    def check_funds(self, amount):
        
        # withdraw_amounts = 0
        # for money in self.ledger:
        #     if money["amount"] < 0:
        #         withdraw_amounts += money["amount"]
        # return withdraw_amounts
        
        if self.get_balance() < amount:
            # print(self.get_balance())
            # print("false")
            return False
        else:
            # print(self.get_balance())
            # print("true")
            return True
        
    def __str__(self):
        results = "transtions\n"
        
        for money in self.ledger:
            results += f"Amount: {money["amount"]}  description: {money["description"]}\n"

        results += str(self.get_balance())
        return results
        

def create_spend_chart(categories):
    pass

food = Category("Food")

food.deposit(500, "beef")

food.withdraw(500, "chicken")

car =  Category("Car")

car.deposit(500, "engine part")

car.transfer(400, food)

food.withdraw(401)

car.transfer(200, food)

print(food)