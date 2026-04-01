class Employee :
    def __init__(self , name , bas_salary):
        self.name = name
        self.salary = bas_salary
        
class Manager(Employee) :
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus
    def calulate_pay(self) :
        plus_bonus =  self.salary+ self.bonus
        print(plus_bonus)
class Developer(Employee) :
    def __init__(self, name, bas_salary, programming_language):
        super().__init__(name, bas_salary)
        self.programming_language = programming_language
    def write_code(self) :
        print(f"{self.name} is writing conde in {self.programming_language}")
        
manager = Manager("Reach" ,7000, 4000)
manager.calulate_pay()

developer = Developer("Virak" , 100, "Python")
developer.write_code()
print(f"Develope's Salary is :{developer.salary}")
    
    