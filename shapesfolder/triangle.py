"""Triangle

Provides functions to calculate perimeter and area for a triangle.

"""

def perimeter(l,s1,s2):
  """Calculates the perimeter given the base length, 1st side length, and 2nd side length.
  
  Parameters:
  ----------
  l,s1,s2

  Returns:
  ----------
  perimeter
  """
  return l+s1+s2

def area(bl,h):
  """Calculates the area given the base length and height.
  
  Parameters:
  ----------
  bl,h

  Returns:
  ----------
  area
  """
  return bl*h/2