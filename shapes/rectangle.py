"""Rectangle

Provides functions to calculate perimeter and area for a rectangle.

"""
from shapes.shapesmod import Shape

class Rectangle(Shape):
  def __init__(self,length,width,units="m"):
    super().__init__("rectangle",units)
    self.length = length
    self.width = width

  def perimeter(self):
    """Calculates the perimeter given the length and width.
  
    Parameters:
    ----------
    l,w

    Returns:
    ----------
    perimeter
    """
    return (self.length+self.width)*2

  def area(self):
    """Calculates the area given the length and width.
  
    Parameters:
    ----------
    l,w

    Returns:
    ----------
    area
    """
    return self.length*self.width