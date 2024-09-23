name = input("Enter you user name : ")
paswd = int(input("Enter you password : "))


class user:
    def __init__(self, name: str, paswd: int):
        self.name = name
        self.paswd = paswd

    def greeting(self):
        print(f"hello Mr {self.name} your password is {self.paswd}")


u = user(name, paswd)

u.greeting()
