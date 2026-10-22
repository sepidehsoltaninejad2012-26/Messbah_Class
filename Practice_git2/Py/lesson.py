class Lesson:
    def __init__(self, code, name, teacher):
        self.code = code
        self.name = name
        self.teacher = teacher

    def __repr__(self):
      return f"name : {self.name}, teacher : {self.teacher}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(value,string):
            raise TypeError("name must be string")
        self.__name = name

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        if not isinstance(value,int):
            raise TypeError("code must be integer")
        self.__code = code

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        self.__teacher = teacher

lesson1 = Lesson(12345, "python", "Ahmad")
print(lesson1)
