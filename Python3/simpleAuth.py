password = '123abc'
pwd = ''
auth = False
count = 0
attempts = 5

while pwd!=password:
    if count<attempts:
        pwd = input("Whats the password? ")
        count = count + 1
        if(pwd==password):
            auth = True
    else: 
        break  
if auth:
    print("Authorised")
else:
    print("Account is locked")



