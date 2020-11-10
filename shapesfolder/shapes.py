from shapesfolder import circle
from shapesfolder import square
from shapesfolder import rectangle
from shapesfolder import parallelogram
from shapesfolder import triangle
from shapesfolder import trapezoid

def scircle():
  r = 3
  print("For a circle with r = {0}:".format(r))
  print("The circumference is {0}.".format(circle.circumference(r)))
  print("The area is {0}.".format(circle.area(r)))
  print("-------")

def ssquare():
  l = 3
  print("For a square with l = {0}:".format(l))
  print("The perimeter is {0}.".format(square.perimeter(l)))
  print("The area is {0}.".format(square.area(l)))
  print("-------")

def srectangle():
  l = 3
  w = 4
  print("For a rectangle with l = {0} and w = {1}:".format(l,w))
  print("The perimeter is {0}.".format(rectangle.perimeter(l,w)))
  print("The area is {0}.".format(rectangle.area(l,w)))
  print("-------")

def sparallelogram():
  l = 3
  h = 4
  sl = 3
  print("For a parallelogram with l = {0}, h = {1}, and sl = {2}:".format(l,h,sl))
  print("The perimeter is {0}.".format(parallelogram.perimeter(l,sl)))
  print("The area is {0}.".format(parallelogram.area(l,h)))
  print("-------")

def striangle():
  bl = 3
  h = 2
  s1 = 3
  s2 = 3
  print("For a triangle with bl = {0}, h = {1}, s1 = {2}, and s2 = {3}:".format(bl,h,s1,s2))
  print("The perimeter is {0}.".format(triangle.perimeter(bl,s1,s2)))
  print("The area is {0}.".format(triangle.area(bl,h)))
  print("-------")

def strapezoid():
  bl1 = 3
  bl2 = 2
  h = 2
  s1 = 3
  s2 = 3
  print("For a trapezoid with bl1 = {0}, bl2 = {1}, h = {2}, s1 = {3}, and s2 = {4}:".format(bl1,bl2,h,s1,s2))
  print("The perimeter is {0}.".format(trapezoid.perimeter(bl1,bl2,s1,s2)))
  print("The area is {0}.".format(trapezoid.area(bl1,bl2,h)))
  print("-------")

def sshapes():
  scircle()
  ssquare()
  srectangle()
  sparallelogram()
  striangle()
  strapezoid()