class professional:
   
   def __init__(self,category,name):
      self.category = category
      self.name = name

   def toString(self):
      return "%s %s" %(self.category, self.name)