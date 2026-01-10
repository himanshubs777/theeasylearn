#write a program to convert given grams into kg and remaining grams
# input : 2500 grams
# output : 2 kg and 500 grams 

weight = int(input("Enter the weight(in grams):"))

kg = weight // 1000
gm = weight % 1000

print(kg,"kg",gm,"grams")