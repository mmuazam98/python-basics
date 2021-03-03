class customer:
    def __init__(self):
        self.names = ["Muazam","Hazik","Mutafiq","Arsh","Azmat","Suvo","Yash"]
        self.addresses = ["Srinagar","Ganderbal","Shalimar","Budgam","Patan","Jammmu","Lal Chowk"]
        self.pincodes = [190001,190001,190004,190004,190001,190004,603203]
    def find(self):
        name = input("Enter a name: ")
        index = self.names.index(name)
        pincode = self.pincodes[index]
        i=0
        c=0
        print("Customers who live nearby:")
        while i<len(self.names):
            if(self.pincodes[i]==pincode and self.names[i]!=name):
                print(self.names[i])
                c=c+1
            i=i+1
            if(c==0 and i==len(self.names)):
                print("No one is living nearby")
        
        

ob = customer()
ob.find()