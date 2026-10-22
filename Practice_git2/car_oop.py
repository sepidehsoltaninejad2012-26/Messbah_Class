class Car:
#construction
    def __init__(self):
        print("ساخته شد")
        self.name = None
        self.color = None
        self.plate = None


    def save(self):
        print(f"SAVED : {self.name} {self.color} {self.plate}")

    def change_plate(self, plate):
        return f"{self.plate}"
