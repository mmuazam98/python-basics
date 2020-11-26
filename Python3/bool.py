a = True
b = False

if a and b:
    print("Both true")

if a or b:
    print("one is true")

if not b:
    print("opposite")

if a is b:
    print("Same")
elif a is not b:
    print("Different")

x = ('cats','dogs','birds')
y = 'cats'
z = 'sheeps'
if y in x:
    print("present")
if z not in x:
    print("Absent")