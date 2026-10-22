class Lesson:
    def __init__(self, name, family, code, unit, duration):
        self.code = code
        self.name = name
        self.family = family
        self.duration = duration
        self.unit = unit

    def  __repr__(self):
        return f"{self.name} {self.family} {self.code} {self.unit} {self.duration}"

    def save(self):
        print(f" SAVED: {self.name} {self.family} {self.code} {self.unit} {self.duration}")

    def Edit(self, code, unit, duration):
        return f" {self.code} {self.unit} {self.duration}"
