"""Circle

Provides functions to calculate circumference and area for a circle.

"""
import math

def circumference(r):
  return 2*math.pi*r

def area(r):
  """Calculates the area given the radius.
  
  Parameters:
  ----------
  r

  Returns:
  ----------
  area
  """
  return math.pi*r**2