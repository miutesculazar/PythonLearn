import math


class Coffee:

    def __init__(self, coffee_spoons=0, sugar=0, water=0):
        self.coffee_spoons = coffee_spoons
        self.sugar = sugar
        self.water = water

    def prepare_coffee(self):
        catitate_totala_cafea = self.coffee_spoons + self.sugar + self.water
        return catitate_totala_cafea

    def prepare_time_coffee(self):
        time_to_prepare = math.cos(self.water * math.pi) + math.sin(math.pi * self.sugar) + (math.pi * self.sugar)
        print(time_to_prepare)
