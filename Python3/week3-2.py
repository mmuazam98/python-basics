class tax:
    def __init__(self,income):
        self.inc=income
    
    def calctax(self):
        x= self.inc-1.5
        if(x<10):
            print("Income Tax= ",0.06*self.inc)
        elif( x in range(10,16)):
            print("Income tax= ",0.08*self.inc)
        else:
            print("Income tax= ",0.1*self.inc)

list=[tax(20),tax(11),tax(15)]
for i in list:
    i.calctax()
