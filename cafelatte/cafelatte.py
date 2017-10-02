from coffee.coffee import Coffee

class Cafelatte(Coffee):

    def __init__(self, coffee_spoons=0, sugar=0, water=0, lapte=0):
        Coffee.__init__(self, coffee_spoons, sugar, water)
        self.lapte = lapte

    def prepare_coffee(self):