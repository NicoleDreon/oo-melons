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

# refactored code above using multiple inheritance and abstract class
# thought process:

class AbstractMelonOrder:
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas Melon":
            base_price *= 1.5 
            
        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total = total + 3
      
        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order with no tax and inspection."""
    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0)

        self.passed_inspection = False


    def mark_inspection(self):
        self.passed_inspection = True