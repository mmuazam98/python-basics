class customer:
    def __init__(self, name, address, pincode):
        self.name = name
        self.address = address
        self.pincode = pincode

    def showName(self):
        return self.name + ' ' + self.address + ' ' + self.pincode


s = []
for i in range(10):
    s[i] = customer(i, i, i)
    print(s[i].showName())
