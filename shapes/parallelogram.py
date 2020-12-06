"""Parallelogram

Provides functions to calculate perimeter and area for a parallelogram.

"""
from shapes.shapesmod import Shape

class Parallelogram(Shape):
  def __init__(self,length,width,height,units="m"):
    super().__init__("parallelogram",units)
    self.sidelength = length
    self.width = width
    self.height = height

  def perimeter(self):
    """Calculates the perimeter given the base length and side length.
  
    Parameters:
    ----------
    l,sl

    Returns:
  ----------
    perimeter
    """
    return (self.sidelength+self.width)*2

  def area(self):
    """Calculates the area given the width and height.
  
    Parameters:
    ----------
    l,h

    Returns:
    ----------
    area
    """
    return self.width*self.height