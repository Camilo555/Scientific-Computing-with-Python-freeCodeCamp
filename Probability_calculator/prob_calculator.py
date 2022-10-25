from copy import deepcopy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      self.contents += value * [key]  

  def draw(self,n):
    draw_list =[]
    if n>=len(self.contents):
      return self.contents
    else:
      for i in range(n):
        ran = random.choice(self.contents)
        draw_list.append(ran)
        self.contents.remove(ran)

      return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    hat_copy = deepcopy(hat)
    
    exp_balls = []
    for key, value in expected_balls.items():
      for i in range(value):
        exp_balls.append(key)

    contents = hat_copy.draw(num_balls_drawn)

    check = all(item in contents for item in exp_balls)

    if check is True:
      M += 1
  
  return M/num_experiments