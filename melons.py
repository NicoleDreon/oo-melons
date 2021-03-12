"""Classes for melon orders."""


# class DomesticMelonOrder():
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder():
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code

# thought process:

class AbstractMelonOrder:
    def __init__(self, species, qty, shipped, order_type):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = None

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, AbstractMelonOrder):
        self.order_type = "domestic"
        self.tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, AbstractMelonOrder):
        self.order_type = "international"
        self.tax = 0.17
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    
    

        # if self.order_type = "international":
        #     self.order_type = ""
        # self.tax = 0

# we'll be pulling the attributes from the super class, InternationalMelon
# using the super(). ...
# can we do an else statement like 
# if self.order_type = "international":
#     self.tax = 0.17
# else:
#     self.tax = 0.08 