'''
create tuple to store all states name of india 
display tuple 
display 1st five items 
display 2nd and 3rd and 4th item 
display all items from 7th position onwards 
try to remove 3rd item see what happens 
'''

states = ("andhra pradesh", "arunachal pradesh", "assam", "bihar", "chhattisgarh", "goa", "gujarat", "haryana", "himachal pradesh", "jammu and kashmir", "jharkhand", "karnataka", "kerala", "madhya pradesh", "maharashtra", "manipur", "meghalaya", "mizoram", "nagaland", "odisha")
# display tuple
print("complete tuple:",states)
# display 1st five items
print("first five items:",states[0:5])
# display 2nd and 3rd and 4th item
print("2nd,3rd,4th item:",states[1:4])
# display all items from 7th position onwards
print("items from 7th position onwards:",states[6:])
# try to remove 3rd item see what happens
states.remove("assam") 
print(states)