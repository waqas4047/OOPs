class Item:

    discount = 3.7

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

print(Item.discount)  # it will directly acces this discount attribute
print(item1.discount)
# it will first see it in the  instence level mean it will see first this attrubute in the
# item1.dicount=3.7 like above we assign values to the instanse self.name=name  thsi is assignment of
# attributes to instence when if this attrbute is not found there then it will go to class level
print(item2.discount)
