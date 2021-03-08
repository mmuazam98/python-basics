print("Enter hourly wage:")
wage = int(input())
print("Enter hours you've worked in the past week:")
hours=int(input())

if hours > 40:
    extra=hours-40
    income=wage*40+extra*wage*1.5
    print("Total wage earned : Rs.%.2f"%income)
else:
    print("Total wage earned : Rs.",wage*hours)    
