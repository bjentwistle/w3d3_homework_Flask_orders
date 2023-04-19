# new class of Order to create our toy shop list 
class Order():

    def __init__(self, customer_name, toy_description, price, in_stock):
        self.customer_name = customer_name
        self.toy_description = toy_description
        self.price = price
        self.in_stock = in_stock # should be a boolean, has the toy is in stock, True or False.

