
class Length:

  def __init__(self, c, m):
    self.c = c
    self.m = m
    self._g = m
    self.__cc = 10

  def __str__(self):
    return ('Length (%d cm, %d mm)' % (self.c, self.m))

  def __add__(self,other):
    return (Length(self.c + other.c, self.m + other.m))

l1 = Length(2,6)
l2 = Length(5,3)
print(l1 + l2)
pointer = Length(5,5)
print(pointer._g)
print(pointer._Length__cc)