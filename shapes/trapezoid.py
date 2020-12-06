"""Trapezoid

Provides functions to calculate perimeter and area for a trapezoid.

"""

from shapes.shapesmod import Shape

class Trapezoid(Shape):
  def __init__(self,sidelength1,sidelength2,baselength1,baselength2,height,units="m"):
    super().__init__("trapezoid",units)
    self.sidelength1 = sidelength1
    self.sidelength2 = sidelength2
    self.baselength1 = baselength1
    self.baselength2 = baselength2
    self.height = height

  def perimeter(self):
    """Calculates the perimeter given the bottom length, top length, 1st side length, and 2nd side length.
  
    Parameters:
    ----------
    bl1,bl2,s1,s1

    Returns:
    ----------
    perimeter
    """
    return self.sidelength1 + self.sidelength2 + self.baselength1 + self.baselength2

  def area(self):
    """Calculates the area given the bottom length, top length, and height.
  
    Parameters:
    ----------
    bl1,bl2,h

    Returns:
    ----------
    area
    """
    return (self.baselength1 + self.baselength2)*self.height/2