def f1(f):
    def f2():
      print("hello world")
      f()
      print("helli")
    return f2
@f1
def f3():
    print('Bye world')

# x = f1()
# x()
f3()