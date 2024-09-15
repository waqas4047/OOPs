class Calculate:
    def __init__(self):
        self.num1 = 22
        self.num2 = 44

    def add(self):
        return self.num1 + self.num2  # accessing instence variable using self


item = Calculate()
print(item.add())
