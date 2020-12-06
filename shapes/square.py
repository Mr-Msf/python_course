"""Square

Provides functions to calculate perimeter and area for a square.

"""

from shapes.shapesmod import Shape
class Square(Shape):
  def __init__(self,length,units="m"):
    super().__init__("square",units)
    self.length = length
  
  def perimeter(self):
    """Calculates the perimeter given the length.

    Parameters:
    ----------
    l

    Returns:
    ----------
    perimeter
    """
    return self.length*4

  def area(self):
    """Calculates the area given the length.
  
    Parameters:
    ----------
    l

    Returns:
    ----------
    area
    """
    return self.length**2