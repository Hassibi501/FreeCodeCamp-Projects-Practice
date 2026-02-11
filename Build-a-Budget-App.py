
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if True:
            self.ledger.append({"amount": amount * -1, "description": description})
        else:
            return False

    def get_balance(self):
        balance = 0
        for money in self.ledger:
            balance += money["amount"]
        return balance

    def transfer(self, amount, other_category):
        if True:
            self.withdraw(amount, f"Transfer to {other_category.name}`")
            other_category.deposit(amount, f"Transfer from {self.name}")
        else:
            return False
        
    def check_funds(self):
        
        withdraw_amounts = 0
        for money in self.ledger:
            if money["amount"] < 0:
                withdraw_amounts += money["amount"]
        return withdraw_amounts
        
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

food.withdraw(100, "chicken")

food.withdraw(50)

car =  Category("Car")

car.deposit(500, "engine part")

car.transfer(400, food)

#print(food)

