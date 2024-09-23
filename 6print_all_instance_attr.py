class Item:
    discount = 33
    pay_rate = 6.4

    def __init__(self, name: str, price: int, quantity=0):

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity


# to print all the attribute that belong to a spesific class or instance

item1 = Item("phone", 33, 7)
item2 = Item("jfkd", 4455, 2)
print(Item.__dict__)  # wiil print all the attlribute of class
print(item1.__dict__)  # will print all the attribute of instence 1
print(item2.__dict__)  # will print all the attribute of instence 1
