class HotBeverage:
    
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
        self.description = "Just some hot water in a cup."
    
    def description(self):
        return self.description
    
    def __str__(self):
        return f"name : {self.name}\nprice : {round(self.price, 2)}\ndescription : {self.description}"

class Coffee(HotBeverage):

    def __init__(self):
        self.price = 0.40
        self.name = "coffee"
        self.description = "A coffee, to stay awake."

class Tea(HotBeverage):

    def __init__(self):
        self.price = 0.30
        self.name = "tea"
        self.description = "Just some hot water in a cup."

class Chocolate(HotBeverage):

    def __init__(self):
        self.price = 0.50
        self.name = "chocolate"
        self.description = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):

    def __init__(self):
        self.price = 0.45
        self.name = "cappuccino"
        self.description = "Un po' di Italia nella sua tazza!"


if __name__ == "__main__":
    hotbeverage = HotBeverage()
    tea = Tea()
    coffee = Coffee()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    for beverage in [hotbeverage, tea, coffee, chocolate, cappuccino]:
        print(beverage, end="\n\n")
