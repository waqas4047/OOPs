class Item:
    def caluclute(self, name: str, grade: int):
        # with the help of this str and int wilth arg now name will only take string data and
        #  grade will only take integer data
        if not isinstance(name, str):
            raise TypeError("name should be string")
        if not isinstance(grade, int):
            raise TypeError("grade should be int")
        print(f"Mr : {name} has {grade} grade")


item1 = Item()
item2 = Item()

item1.caluclute(4, 8)  # access teh function of class
item2.caluclute("qaiser", 89)  # access teh function of class
