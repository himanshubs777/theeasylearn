#write a program to convert given minutes into hours and remaining minutes
# input : 150 minutes 
# output : 2 hours and 30 minutes 

time = int(input("Enter the time(min):"))
hours = time // 60
minutes = time % 60

print(hours,"hours",minutes,"minutes")
