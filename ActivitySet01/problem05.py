# Functions
def computepay(h, r):
    if h<=40:
        total = h*r
    else:
        total=r*40 + r*(h-40)*1.5
    return total
    

h = float(input("Enter Hours:"))
r=float(input("rate"))
p = computepay(h, r)
print("Pay", p)