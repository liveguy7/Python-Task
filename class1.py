
class Employee:
  c = 0

  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
    print("Employee Constructor")

  def employeeMethod(self):
    print("Parent Method")

class Worker(Employee):
  def __init__(self):
    super().__init__('lna', 56434)
    print("Child Constructor")

  def employeeMethod(self):
    print("Worker has a question....")


emp1 = Employee('pan', 20000)
wrk1 = Worker()
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__module__)
