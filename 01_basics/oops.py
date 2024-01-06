# class is a template to make an object ( remember the example of ticket resrevation in employee by Harry )

# class = a blank railway reservation form
# object = filled railway reservation form (different people made different form by filling up their personal details)

class Employee:
    def __init__(self,name,salary): #method 1
        self.name = name
        self.salary = salary
    
    def getSalary(self): #method 2
        print(self.salary)

tamal = Employee("tamal","3455")
print(tamal.name)
print(tamal.salary)
tamal.getSalary()
