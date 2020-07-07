class professional:
   
   def __init__(self,category,name):
      self.category = category
      self.name = name
      self.scheduled = []

   def toString(self):
      return "%s %s" %(self.category, self.name)