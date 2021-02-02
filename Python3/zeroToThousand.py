def add(n):
    sum = 0
    while (n != 0):  
        sum = sum + (n % 10) 
        n = n//10
    print("Sum of digits:",sum)

num=int(input("Enter a number between 0 and 1000: "))
while(num>1000):
    print("Entered number should be between 0 and 1000.\n")
    num=int(input("Enter a number between 0 and 1000: "))
add(num)


    

