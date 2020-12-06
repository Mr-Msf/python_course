from shapes.circle import Circle 
from shapes.square import Square
from shapes.rectangle import Rectangle
from shapes.parallelogram import Parallelogram
from shapes.triangle import Triangle
from shapes.trapezoid import Trapezoid

def main():
  shapes = []
  shapes.append(Circle(3))
  shapes.append(Square(3))
  shapes.append(Rectangle(3,4))
  shapes.append(Parallelogram(3,4,5))
  shapes.append(Triangle(3,4,5,6))
  shapes.append(Trapezoid(3,4,5,6,7))

  for shape in shapes:
    print(shape.get_info())

if __name__ == "__main__":
  main()