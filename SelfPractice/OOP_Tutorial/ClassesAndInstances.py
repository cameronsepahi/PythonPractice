#Ex) Application for company with employeees 

class Employee:
    #class variables
    num_of_emps = 0
    raise_amount = 1.04
    
    #pass -> statement that lets you leave a class empty without returning error

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '_@company.com'

        #since constructor runs everytime we create new instances (or new employees) we can increment class var in this constructor
        Employee.num_of_emps += 1

        #instantiating method (funcs inside classes) -> always has self as input
    def fullname(self):
        return print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    #creating class methods using @classmethod decorator, which can modify a method by receiving the class as first argument instead of method
    #Useful if you want to change all the instances' values of the class, instead of individual methods
    @classmethod 
    def set_raise_amt(cls, amount):
        cls.riase_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


#Instance variables (instantiating objects with attributes defined in class)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#Printing specific attribute of object
# print(emp_1.email)
# print(emp_2.email)

#Printing formatted attributes of objects defined in fullname method
# print(Employee.fullname(emp_1))
# print(Employee.fullname(emp_2))

#Applying apply_raise method to objects
# emp_1.apply_raise()
# print(emp_1.pay)

#Checking all defined attributes (not including methods) of object
# print(emp_1.__dict__)

#Changing value of class variable
# Employee.raise_amount = 1.05

#Changing value of individual object class var (which is further defined in a method)
# emp_1.raise_amount = 1.05

#Call class var that shows number of employees based on the number of instances/employees you created
# print(Employee.num_of_emps)

#Given unorganized values, organize them and then add them as instances by using from_string constructor
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Cameron-Sepahi-100000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)



