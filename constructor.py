class Calculate:
    def __init__(self, digit1, digit2):
        self.num1 = digit1
        self.num2 = digit2

    def add(self):
        return self.num1 + self.num2  # accessing instence variable using self


item1 = Calculate(22, 44)
print(item1.add())
