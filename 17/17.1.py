class Employee:

    __name = None
    __age = None
    __salary = None

    def __init__(self, name:str,age:int, salary:int):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getSalary(self):
        return self.__salary

    def setName(self,name):
        self.__name = name
    def setAge(self, age: int):
        self.__age = age
    def setSalary(self, salary: int):
        self.__salary = salary


empl = Employee('Mark',19,100000)
