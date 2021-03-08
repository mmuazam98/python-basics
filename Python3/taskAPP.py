# create a class student, accept 5 marks, find average of these marks and print average in main
class student:
    def __init__(self, m1, m2, m3, m4, m5):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def showAvg(self):
        return (self.m1+self.m2+self.m3+self.m4+self.m5)/5


s1 = student(100, 99, 98, 100, 99)
print("Average marks:", s1.showAvg())
