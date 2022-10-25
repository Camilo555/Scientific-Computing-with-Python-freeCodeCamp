class Rectangle:
  def __init__(self, Width, Height):
    self.width = int(Width)
    self.height = int(Height)

  def __str__(self):
    out = str(self.__class__.__name__) + f"(width={self.width}, height={self.height})"
    return out

  def set_width(self, new_width):
    self.width = int(new_width)

  def set_height(self, new_height):
    self.height = int(new_height)
  
  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
    else:
      s = ''
      for i in range(self.height):
        s += '*'*self.width+'\n'
      return s
      
  def get_amount_inside(self, shape):
    out = (self.width // shape.width)*(self.height // shape.height)
    return out
    
class Square(Rectangle):
  def __init__(self, Side):
    self.width = int(Side)
    self.height = int(Side)
    
  def __str__(self):
    out = str(self.__class__.__name__) + f"(side={self.width})"
    return out
    
  def set_side(self,new_side):
    self.width = int(new_side)
    self.height = int(new_side)
  
