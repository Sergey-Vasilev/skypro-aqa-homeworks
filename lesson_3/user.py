

class User:
   
   def __init__(self, first_name, list_name):
      self.first_name = first_name
      self.list_name = list_name

   def sayF(self):
      print("Мое имя:", self.first_name)

   def sayL(self):
      print("Моя фамилия:", self.list_name)

   def sayFull_name(self):
      print("Мое имя и фамилия:", self.first_name, self.list_name)



