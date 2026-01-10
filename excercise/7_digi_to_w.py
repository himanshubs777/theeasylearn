#write a program to convert given 3 digit amount into words
# input : 175 output : one hundred seventy five  

number = int(input("Enter the number 3 digit:"))

first = number // 100
second = (number // 10) % 10
last = number % 10
# print(second)

words1 = [' ','one hundread','two hundread','three hundread','four hundread','five hundread','six hundread','seven hundread','eight hundread','nine hundread']
words2 = [' ','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
words3 = ['Zero','one','two','three','four','five','six','seven','eight','nine']

print(words1[first],words2[second],words3[last])