"""Triangle

Provides functions to calculate perimeter and area for a triangle.

"""

from shapes.shapesmod import Shape

class Triangle(Shape):
  def __init__(self,sidelength1,sidelength2,width,height,units="m"):
    super().__init__("triangle",units)
    self.sidelength1 = sidelength1
    self.sidelength2 = sidelength2
    self.width = width
    self.height = height

  def perimeter(self):
    """Calculates the perimeter given the base length, 1st side length, and 2nd side length.
  
    Parameters:
    ----------
    l,s1,s2

    Returns:
    ----------
    perimeter
    """
    return self.width+self.sidelength1+self.sidelength2

  def area(self):
    """Calculates the area given the base length and height.
  
    Parameters:
    ----------
    bl,h

    Returns:
    ----------
    area
    """
    return self.width*self.height/2