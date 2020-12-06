from shapes.circle import Circle 
from shapes.square import Square

def main():
  shapes = []
  shapes.append(Circle(3))
  shapes.append(Square(3))

  for shape in shapes:
    print(shape.get_info())

if __name__ == "__main__":
  main()