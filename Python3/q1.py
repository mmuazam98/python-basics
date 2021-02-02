import math
price=24.95
discount=.60
charges=.75
firstShipping=3.00
units=60
totalDiscount=price*discount*units
shipping=charges*59+firstShipping
result=totalDiscount+shipping
print('The total cost for 60 copies:%.2f'%result)