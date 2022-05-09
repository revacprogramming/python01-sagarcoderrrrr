# Conditional Execution

hrs = float(input("Enter Hours:"))
rate=float(input("Enter rate:"))
if hrs <=40:
    total = hrs * rate
    print(total)
else:
    print(40*rate +(hrs-40)*1.5*rate)
    
