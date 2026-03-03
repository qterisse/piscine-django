from beverages import *
import random

class CoffeeMachine:
    HEALTH = 3

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.price = 0.90
            self.name = "empty cup"
            self.description = "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
            self.message = "This coffee machine has to be repaired."
        
        def __str__(self):
            return self.message

    def __init__(self):
        self.hp = self.HEALTH
    
    def repair(self):
        self.hp = self.HEALTH
    
    def serve(self, beverage_class):
        if (self.hp <= 0):
            raise self.BrokenMachineException()

        beverage = random.choice([beverage_class(), self.EmptyCup()])
        self.hp -= 1
        return beverage


if __name__ == "__main__":
    machine = CoffeeMachine()
    beverages = [Coffee, Tea, Cappuccino, Chocolate]

    def serve_clients():
        for n in range(CoffeeMachine.HEALTH + 1):
            try:
                print(machine.serve(beverages[n % len(beverages)]))
            except Exception as e:
                print(e)
            print()
    
    serve_clients()
    machine.repair()
    serve_clients()


