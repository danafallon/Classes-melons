"""This file should have our melon-type classes in it."""

class AbstractOrder(object):

    def __init__(self):
        """When users attempt to instantiate from AbstractOrder,
        give them an informational error message.
        """
        raise Exception("Cannot create a melon from this class!")

    def get_base_price(self):
        return 5.00

    def get_price(self, qty):
        base_cost = self.get_base_price()
        if self.price_bump != 0:
            base_cost += self.price_bump
        if self.imported == True:
            base_cost = base_cost * 1.5
        if self.shape == 'square':
            base_cost = base_cost * 2
        
        total_cost = base_cost * qty

        return total_cost


class WatermelonOrder(AbstractOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    price_bump = 0

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total_cost = super(WatermelonOrder, self).get_price(qty)
        if qty > 2:
            total_cost = total_cost * .75
        return total_cost


class CantaloupeOrder(AbstractOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    price_bump = 0

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total_cost = super(CantaloupeOrder, self).get_price(qty)
        if qty > 4:
            total_cost = total_cost * .5
        return total_cost


class CasabaOrder(AbstractOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    price_bump = 1

    def __init__(self):
        pass


class SharlynOrder(AbstractOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    price_bump = 0

    def __init__(self):
        pass


class SantaClausOrder(AbstractOrder):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    price_bump = 0

    def __init__(self):
        pass


class ChristmasOrder(AbstractOrder):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']
    price_bump = 0

    def __init__(self):
        pass


class HornedMelonOrder(AbstractOrder):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    price_bump = 0

    def __init__(self):
        pass


class XiguaOrder(AbstractOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']
    price_bump = 0

    def __init__(self):
        pass


class OgenOrder(AbstractOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    price_bump = 1

    def __init__(self):
        pass