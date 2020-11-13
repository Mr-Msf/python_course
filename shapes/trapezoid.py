"""Trapezoid

Provides functions to calculate perimeter and area for a trapezoid.

"""

def perimeter(bl1,bl2,s1,s2):
  """Calculates the perimeter given the bottom length, top length, 1st side length, and 2nd side length.
  
  Parameters:
  ----------
  bl1,bl2,s1,s1

  Returns:
  ----------
  perimeter
  """
  return bl1+bl2+s1+s2

def area(bl1,bl2,h):
  """Calculates the area given the bottom length, top length, and height.
  
  Parameters:
  ----------
  bl1,bl2,h

  Returns:
  ----------
  area
  """
  return (bl1+bl2)*h/2