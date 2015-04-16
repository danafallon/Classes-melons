"""This file should have our melon-type classes in it."""

class AbstractOrder(object):

    def __init__(self):
        """When users attempt to instantiate from AbstractOrder,
        give them an informational error message.
        """
        raise Exception("Cannot create a melon from this class!")

    def get_base_price(self):
        return 5.00

    # def get_price(self, qty):
    #     raise AttributeError("Can't get price of non-existent melon")


class WatermelonOrder(AbstractOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_cost = self.get_base_price()
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2
        
        total_cost = base_cost * qty

        if qty > 2:
            total_cost = total_cost * .75

        return total_cost

class CantaloupeOrder(AbstractOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_cost = self.get_base_price()
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2

        total_cost = base_cost * qty

        if qty > 4:
            total_cost = total_cost * .5

        return total_cost

class CasabaOrder(AbstractOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_cost = self.get_base_price()
        base_cost += 1
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2
        
        total_cost = base_cost * qty

        return total_cost

class SharlynOrder(AbstractOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_cost = self.get_base_price()
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2
        
        total_cost = base_cost * qty

        return total_cost

class SantaClausOrder(AbstractOrder):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_cost = self.get_base_price()
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2
        
        total_cost = base_cost * qty

        return total_cost

class ChristmasOrder(AbstractOrder):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_cost = self.get_base_price()
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2
        
        total_cost = base_cost * qty

        return total_cost

class HornedMelonOrder(AbstractOrder):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_cost = self.get_base_price()
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2
        
        total_cost = base_cost * qty

        return total_cost

class XiguaOrder(AbstractOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_cost = self.get_base_price()
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2
        
        total_cost = base_cost * qty

        return total_cost

class OgenOrder(AbstractOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_cost = self.get_base_price()
        base_cost += 1
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2
        
        total_cost = base_cost * qty

        return total_cost