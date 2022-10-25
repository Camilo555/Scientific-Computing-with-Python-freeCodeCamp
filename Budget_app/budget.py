class Category:
  def __init__(self,Categ):
      self.name = Categ
      self.ledger = []

  def __str__(self):
      title = f"{self.name:*^30}\n"
      elements = ''
      tot = 0
      for elem in self.ledger:
          elements += f"{elem['description'][0:23]:23}" + f"{elem['amount']:>7.2f}" + '\n'
          tot += elem['amount']
        
      out = title + elements + "Total: " + str(tot)
      return out

  def deposit(self,amount, description=''):
      self.ledger.append({'amount': float(amount), 'description': description})
      return None
    
  def withdraw(self,amount, description=''):
      if self.check_funds(float(amount)):
          self.ledger.append({'amount': float(-amount), 'description': description})
          return True
      else:
          return False

  def get_balance(self):
      bal = 0
      for element in self.ledger:
        bal += element['amount']
      return bal

  def transfer(self,amount, category):
      if self.check_funds(amount):
        self.ledger.append({'amount': float(-amount), 'description': f'Transfer to {category.name}'})
        category.deposit(float(amount),description = f"Transfer from {self.name}")
        return True
      else:
        return False

  def check_funds(self,amount):
    if self.get_balance()>=amount:
        return True
    return False
    
  def get_withdrawls(self):
      lis = []
      for elem in self.ledger:
          if elem['amount']<0:
              lis.append(elem['amount'])
      lis_tot = sum(lis)
      return lis_tot
    



def truncate(n):
  mult = 10
  return int(n*mult)/mult

def create_spend_chart(categories):

  res = "Percentage spent by category\n"
  l = 100
  names = []
  total = 0
  breakdown = []

  for category in categories:
    total+= category.get_withdrawls()
    breakdown.append(category.get_withdrawls())
    names.append(category.name)
  tot = list(map(lambda s: truncate(s/total), breakdown))

  while l>=0:
      cat_sp = ' '
      for i in tot:
        if i * 100>= l:
            cat_sp += "o  "
        else:
            cat_sp += "   "
      res+= str(l).rjust(3) + '|' + cat_sp + ('\n')
      l-=10
    
  dashes = '-' + '---'*len(categories)
  maxi = max(names, key=len)
  x = ''

  for c in range(len(maxi)):
      name_str = '     '
      for name in names:
          if c>= len(name):
            name_str += "   "
          else:
            name_str += name[c] + '  '
      if (c != len(maxi)-1):
        name_str += '\n'
        
      x +=name_str
    
  res += dashes.rjust(len(dashes)+4) + '\n' + x 
  return res