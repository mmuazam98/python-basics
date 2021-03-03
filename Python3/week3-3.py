class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def show(self):
        print("Name= ",self.name)
        print("Balance= ",self.balance)
    
class Savings(Bank):
    def __init__(self,name,balance):
        Bank.__init__(self, name, balance)
        
    def transaction(self):
       print("Inside Saving")
       self.show()
       return
    
class Current(Bank):
  def __init__(self,name,balance):
        Bank.__init__(self, name, balance)
        
  def transaction(self):
     print("Inside Current")
     self.show()
     return
            
class Loan(Bank):
  def __init__(self,name,balance):
        Bank.__init__(self, name, balance)
        
  def transaction(self):
     print("Inside loan  ")
     self.show()
     return
     
     
obj1=Savings('Muazam',10000)
obj2=Current("Mutafiq",900000)  
obj3=Loan("Azmat",20000)
obj1.transaction()
obj2.transaction()
obj3.transaction()
