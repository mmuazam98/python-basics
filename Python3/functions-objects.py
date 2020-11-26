# functions in python

def runMe(name):
    print("I am a {} function".format(name))

runMe('runMe()')

def func(n=35):
    return n
x=func()
print(x)


# objects in python

class Hours:

    tired = 'Tired'

    def morning(self):
        print('Fresh')
    def evening(self):
        print(self.tired)

def main():
    feeling = Hours()
    feeling.morning()
    feeling.evening()
if __name__ == "__main__":
    main()