
class Employee:
  c = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.c += 1

  def displayCount(self):
    print(Employee.c)

  def displayEmployee(self):
    print(self.name, self.salary)

e1 = Employee('pan', 20000)
e2 = Employee('man', 50000)
e1.displayEmployee()
e2.displayEmployee()
Employee.c
e1.displayCount()
