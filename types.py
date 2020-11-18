# list 
x = [1,2,3]
x[2]=6
for i in x:
    print(i)

# tuple - value can't be changed
x = {1,2,3}
for i in x:
    print(i)

#range - value cant change
x = range(5)
for i in x:
    print(i)

#range - to change a value
x = list(range(5)) 
x[2]=3
for i in x:
    print(i)

# loop between a range range(from,to)
x= range(5,10)

# loop with steps range(from, to, step)
xy = range(5, 50, 5)

print(xy)


x = {'one':1,'two':2}
for id, value in x.items():
    print('id: {}, value: {}'.format(id, value))