"""Circle

Provides functions to calculate circumference and area for a circle.

"""
import math
from shapes.shapesmod import Shape

class Circle(Shape):
  def __init__(self,radius,units="m"):
    super().__init__("circle",units)
    self.radius = radius
  
  def perimeter(self):
    """Calculates the circumference given the radius.

    Parameters:
    ----------
    r

    Returns:
    ----------
    circumference
    """
    return 2 * math.pi * self.radius

  def area(self):
    """Calculates the area given the radius.

    Parameters:
    ----------
    r

    Returns:
    ----------
    area
    """
    return math.pi * self.radius ** 2