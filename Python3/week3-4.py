class Bank:
    def __init__(self,acc_id,name,bal):
        self.acc_id=acc_id
        self.name=name
        self.bal=bal
    
    def show(self):
        print("Account id= ",self.acc_id)
        print("Name= ",self.name)
        print("Balance= ",self.bal)

class Saving(Bank):
    def __init__(self,acc_type,acc_id,name,bal,credit,debit):
        self.acc_type=acc_type
        self.credit=credit
        self.debit=debit
        Bank.__init__(self, acc_id, name, bal)
    
    def score(self):
        total= 1*(self.credit/2000) - 1*(self.debit/2000) + 1*(self.bal/10000)
        self.show()
        print("total score of savings account= ",total,"\n")
        
    

class Current(Bank):
    def __init__(self,acc_type,acc_id,name,bal,credit,overdue):
        self.acc_type=acc_type
        self.credit=credit
        self.overdue=overdue
        Bank.__init__(self, acc_id, name, bal)
    
    def score(self):
        total= 1*(self.credit/2000) - 1*(self.overdue/25000) + 1*(self.bal/10000)
        self.show()
        print("total score of current account= ",total,"\n")
        
        
class Loan(Bank):
    def __init__(self,acc_type,acc_id,name,bal,time_pay,penalty_pay):
        self.acc_type=acc_type
        self.time_pay=time_pay
        self.penalty_pay=penalty_pay
        Bank.__init__(self, acc_id, name, bal)
    
    def score(self):
        total= 1*self.time_pay - 1*self.penalty_pay
        self.show()
        print("total score of loan account= ",total,"\n")
        
obj1= Saving("saving",44,"Anurag",50000,20000,10000)
obj2= Current("current",40,"Rishy",50000,20000,10000)
obj3= Loan("loan",39,"Aniket",50000,5,3)

obj1.score()
obj2.score()
obj3.score()