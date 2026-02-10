hrs = input("Enter Hours:")
h = float(hrs)
rt = input ("Enter Rate per Hour:")
r = float(rt)
 
if h<=40:
    pay = h * r 
    print(pay)
    
else:
    reg = r * 40
    otp = (h-40) * 1.5 * r
    pay = reg + otp
    print(pay) 




