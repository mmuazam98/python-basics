import datetime

date = datetime.date.today()
rate1 = input("How would you rate our Delivery Service (On a scale of 1 to 5): ")
rate2 = input("How would you rate our Customer Service (On a scale of 1 to 5): ")

sum = float(rate1) + float(rate2)
print("Date            Total Score")
print("---------------------------")
print (date,"    ",sum)