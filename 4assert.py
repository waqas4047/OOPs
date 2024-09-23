class Item:

    def __init__(self, name: str, price: int, quantity=0):

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # * to validate that the arguments
        assert price >= 0, f"the price is {price} is less than zero"
        # with the help of asserrtion we can validate our data here if price is in negative value it will print
        # the assertion error to us
        assert quantity >= 0, f"the quantity {quantity} should be grater than zero"

    def calculate(self):
        print(self.price * self.quantity)


item1 = Item("phone", 2000, 3)
item2 = Item("laptop", 50000, 4)

item1.calculate()
item2.calculate()
