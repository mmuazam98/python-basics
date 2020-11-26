x = (1, '2',3.0, [4],5)
y = [1, '2',3.0, [4],5]
print(type(x))
print(type(x[3]))

print(id(x)) #generates unique id
print(id(y))


if isinstance(x,tuple):
    print("tuple")
elif isinstance(x,list):
    print("list") 
else:
    print("non")