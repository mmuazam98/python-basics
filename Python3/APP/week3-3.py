class bank:
    def __init__(self):
        self.balance = int(input("Enter balance:"))


class customer(bank):
    def viewBalance(self):
        return self.balance


class savings(bank):
    def transaction(self, amount):
        self.balance = self.balance - amount
        return self.balance


s = customer()
print(s.viewBalance())
d = savings()
print(d.transaction(1000))
