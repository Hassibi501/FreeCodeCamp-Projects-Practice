
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
            self.withdraw(amount, f"Transfer to {other_category.name}")
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
        results = f"{self.name:*^30}\n"
        
        for item in self.ledger:
            results += f"{item["description"][:23]:<23}{item["amount"]:>7.2f}\n"
        
        results += f"Total: {self.get_balance():0.2f}"
        

        return results
        

def create_spend_chart(categories):
    
    total_withdraw_amount = 0
    current_withdraw_amount = 0
    lst = []
    dic = {}
    for category in categories:
        print(f"{category.name}: {category.ledger}")
        for item in range(len(category.ledger)):
            #print(category.ledger[item["amount"]]) why cant i do this?
            print(category.ledger[item])

            dic = category.ledger[item]
            if dic["amount"] < 0:
                total_withdraw_amount += dic["amount"]
                current_withdraw_amount += dic["amount"]
        if current_withdraw_amount != 0:
            lst.append(round(current_withdraw_amount, 2))
        current_withdraw_amount = 0
    print(lst) 
    print(round(total_withdraw_amount, 2))
    
    

# food = Category("Food")

# food.deposit(500, "beef for my favoirte restruant that i work in right now")

# food.withdraw(40.87, "chicken")

# car =  Category("Car")

# car.deposit(500, "engine part")

# car.transfer(400, food)

# food.transfer(70, car)

# print(food)

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
car =  Category("Car")

car.deposit(500, "engine part")

car.transfer(400, food)
#print(food)

create_spend_chart([food, clothing, car])