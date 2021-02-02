print("Enter numbers:\n")
arr = []
def insert(): 
    c = 1
    while(c==1):   
        el = int(input())
        if el>0:
            arr.append(el)
        else:
            arr.append(el)
            c=0
insert()
max=arr[0]
for i in arr:
    if i > max: max = i
count =0
for i in arr:
    if i == max: count=count+1
print("Largest number:",max)
print("Count:",count)


