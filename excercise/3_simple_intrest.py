#write a program to calculate simple interest
#formula = (P * R * T) / 100 
#p=principal amount
#r=rate of interest
#t=time

p = 0
r = 0
t = 0

p = input("Enter the principal :")
r = input("Enter the rate :")
t = input("Enter the time :")

p = float(p)
r = float(r)    
t = float(t)

si = (p * r * t) / 100

print("simple interest is :", si)