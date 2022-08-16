from typing import List

"""
class Employee:
    def __init__(self, name, salary, bonus):
        self.__name = name
        self.__salary = salary
        self.__bonus = bonus

    @property
    def get_salary(self):
        return self.__salary

    @property
    def get_name(self):
        return self.__name

    @property
    def get_bonus(self):
        return self.__bonus

    def set_salary(self, salary):
        self.__salary = salary if salary > 0 else 0

    def set_bonus(self, bonus):
        self.__bonus = bonus if bonus > 0 else 0

    def __str__(self):
        return f'Name:{self.__name} Salary = {self.__salary} Bonus = {self.__bonus}'

    def to_pay(self):
        return self.__salary + self.__bonus

VovaWorker = Employee(name='Vova', salary=1050, bonus=120)
LinaWorker = Employee(name='Lina', salary=4200, bonus=520)
RazorWorker = Employee(name='Razor', salary=2200, bonus=1800)

class SalesPerson(Employee):

    def __init__(self, name, salary, percentage_of_productivity, sales_plan_execution):
        super().__init__(name, salary, 0)
        self.__percentage_of_productivity = percentage_of_productivity
        self.__sales_plan_execution = sales_plan_execution

    def set_bonus(self, bonus):
        if self.__sales_plan_execution > 100:
            self.__bonus = bonus * 2
        elif self.__sales_plan_execution > 200:
            self.__bonus = bonus * 3
        else:
            self.__bonus = bonus

customer1 = SalesPerson(name='New Customer', salary=1000, percentage_of_productivity=50, sales_plan_execution=100)
customer2 = SalesPerson(name='Old Customer', salary=1000, percentage_of_productivity=50, sales_plan_execution=200)
customer3 = SalesPerson(name='New Customer', salary=1000, percentage_of_productivity=50, sales_plan_execution=300)

customer1.set_bonus(100)
customer2.set_bonus(200)
customer3.set_bonus(300)

print(customer1.to_pay())
print(customer2.to_pay())
print(customer3.to_pay())

print(customer1.get_bonus)
print(customer2.get_bonus)
print(customer3.get_bonus)

print(customer1.get_name)
print(customer2.get_name)
print(customer3.get_name)

customer3.set_salary(1000)
print(customer3.get_salary)

class Manager(Employee):

    def __init__(self, name, salary, client_amount):
        super().__init__(name, salary, 0)
        self.__client_amount = client_amount

    def set_bonus(self, bonus):
        if self.__client_amount > 100:
            self.__bonus = bonus + 500
        elif self.__client_amount > 150:
            self.__bonus = bonus + 1000
        else:
            self.__bonus = bonus

newManager = Manager(name='New Manager# 1', salary=1000, client_amount=100)
oldManager = Manager(name='Old Manager# 2', salary=1000, client_amount=200)

class Company:
    def __init__(self, employees: List[Employee]):
        self.__employees = employees

    def give_everyone_bonus(self, company_bonus):
        for employee in self.__employees:
            employee.set_bonus(company_bonus)

    def total_to_pay(self):
        total = 0
        for employee in self.__employees:
            total += employee.to_pay()
        return total

    def name_max_salary(self):
        max_salary = 0
        max_name = ''
        for employee in self.__employees:
            if employee.to_pay() > max_salary:
                max_salary = employee.to_pay()
                max_name = employee.get_name
        return max_name

    def print_employees(self):
        for employee in self.__employees:
            print(employee)

new_company = Company([VovaWorker, LinaWorker, RazorWorker, customer1, customer2, customer3, newManager, oldManager])
new_company.name_max_salary()
new_company.give_everyone_bonus(100)
new_company.print_employees()
"""


class Sphere(object):
   p=3.14159265359
   def __init__(self, radius=1, x=0, y=0, z=0):
      self.radius=radius; self.x=x; self.y=y; self.z=z

   def get_radius(self):
      return self.radius

   def get_volume(self):
      return(4.0/3.0*(self.p*(self.radius**3)))

   def get_square(self):
      return(4*(self.p*(self.radius**2)))

   def get_center(self):
      return(self.x, self.y, self.z)

   def set_radius(self, r):
      self.radius=r

   def set_center(self,x1,y1,z1):
      self.x=x1; self.y=y1; self.z=z1

   def is_point_inside(self,x,y,z):
      if ((self.x-x)**2+(self.y-y)**2+(self.z-z)**2)<=self.radius**2:
         return True
      else:
         return False

s1 = Sphere()
print(s1.get_center(), '== (0, 0, 0)')
print(s1.get_radius(), '== 1')
print(s1.get_volume(), '== 4.18879020479')
print(s1.get_square(), '== 12.5663706144')
print(s1.is_point_inside(0, 0.99, 0), '== True')
print(s1.is_point_inside(0.99, 0, 0), '== True')
print(s1.is_point_inside(0, 0, 0.99), '== True')
s1.set_radius(2)
s1.set_center(1, 3, 2)
print(s1.is_point_inside(0, 0.99, 0), '== True')
print(s1.is_point_inside(0.99, 0, 0), '== False')
print(s1.is_point_inside(0, 0, 0.99), '== False')
print(s1.get_center(), '== (1, 3, 2)')
print(s1.get_radius(), '== 2')

