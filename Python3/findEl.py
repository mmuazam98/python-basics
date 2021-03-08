class arrF:
    def __init__(self, m):
        self.m = [1, 2, 3, 4, 5, 6, 7]

    def findSum(self, s):
        for x in self.m:
            for y in self.m:
                if (self.m[x]+self.m[y] == s):
                    print(x, y)


ob = arrF(1)
(ob.findSum(3))
