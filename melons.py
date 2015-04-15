"""This file should have our melon-type classes in it."""

class Melon(object):
    def get_base_price(self):
        return 5.00


class WatermelonOrder(Melon):
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

class CantaloupeOrder(Melon):
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

class CasabaOrder(Melon):
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

class SharlynOrder(Melon):
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

class SantaClausOrder(Melon):
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

class ChristmasOrder(Melon):
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

class HornedMelonOrder(Melon):
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

class XiguaOrder(Melon):
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

class OgenOrder(Melon):
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