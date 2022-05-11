# Conditional Execution
#3.1
hrs = float(input("Enter Hours:"))
rate=float(input("Enter rate:"))
if hrs <=40:
    total = hrs * rate
    print(total)
else:
    print(40*rate +(hrs-40)*1.5*rate)
    
#3.2
score = float(input("Enter Score: "))
if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")
