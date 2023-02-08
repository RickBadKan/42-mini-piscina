#!/usr/bin/env python3
import random
from beverages import *


class CoffeeMachine:
    def __init__(self):
        self.status = True
        self.broken_counter = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(price=0.90, name="empty cup")

        # Override
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            self.message = message
            super().__init__(self.message)

    def repair(self):
        self.status = True
        self.broken_counter = 0

    def serve(self, beverage):
        if self.broken_counter == 10:
            self.status = False
            raise self.BrokenMachineException()

        self.broken_counter += 1

        return random.choice((beverage, self.EmptyCup()))


if __name__ == '__main__':
    machine = CoffeeMachine()

    drinks = (Chocolate(), Tea(), Cappuccino(), Coffee())

    retrys = 2

    while retrys > 0:
        try:
            while machine.status:
                print(f'{machine.serve(random.choice(drinks))}\n')

        except CoffeeMachine.BrokenMachineException as e:
            print(f'{e}\n\n')
            machine.repair()

        finally:
            retrys -= 1
