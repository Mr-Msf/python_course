import circle

def main():
  r = 3
  print("For a circle with r = {0}:".format(r))
  print("The circumference is {0}.".format(circle.circumference(r)))
  print("The area is {0}.".format(circle.area(r)))

if __name__ == "__main__":
  main()