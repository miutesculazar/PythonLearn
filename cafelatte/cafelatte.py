from coffee.coffee import Coffee
import math


class Cafelatte(Coffee):

    def __init__(self, coffee_spoons=0, sugar=0, water=0, milk=0):
        super().__init__(self, coffee_spoons, sugar, water)
        self.milk = milk
        self.given_energy = 0

    def prepare_coffee(self):
        return super(self.prepare_coffee()) + self.milk

    def prepare_time_coffee(self):
        time_to_prepare = math.cos(self.water * math.pi) + math.sin(math.pi * self.sugar) + (math.pi * self.sugar) + self.milk

    def energy(self):
        self.given_energy = self.milk
        return self.given_energy
