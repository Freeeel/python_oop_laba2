class Employee:
    __name = None

    def __init__(self, name, surname):
        self.__name = name

emp1 = Employee('john')
emp2 = emp1

print(emp1 == emp2)
#True