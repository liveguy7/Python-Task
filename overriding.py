
class Parent:

  def __init__(self):
    print('calling parent constructor...')

  def parentMethod(self):
    print('calling parent method...')


class Child(Parent):

  def __init__(self):
    super().__init__()
    print('calling child constructor...')

  def parentMethod(self):
    print("overriden parent method")

c = Child()
c.parentMethod()