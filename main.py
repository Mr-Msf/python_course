import circle
import square
import rectangle
import parallelogam
import triangle
import trapezoid

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
  print("For a parallelogam with l = {0} and h = {1}:".format(l,h))
  print("The perimeter is {0}.".format(parallelogam.perimeter(l,h)))
  print("The area is {0}.".format(parallelogam.area(l,h)))
  print("-------")






if __name__ == "__main__":
  scircle()
  ssquare()
  srectangle()
  sparallelogram()