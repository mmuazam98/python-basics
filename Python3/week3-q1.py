name1 = input("Enter your name: ")
a = int(input('Enter address pincode: '))
name2 = input("Enter your name: ")
b = int(input('Enter address pincode: '))
name2 = input("Enter your name: ")
c = int(input('Enter address pincode: '))

smallest = 0

if a < b and a < c :
    smallest = a
if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c
if smallest == a:
    name = name1
if smallest == b:
    name = name2
if smallest == c:
    name = name3
    
print ('Customer {0} lives nearby'.format(name))