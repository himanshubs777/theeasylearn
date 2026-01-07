'''
create a list to store your favorite destinations in india
create list & store 10 different type of values in it
create a list and all methods of list
print complete list
print first element
print elements from index 2 to 5
print last element
print elements in starting to index 2 
print list two times
print concatenated  list

all functions of list
append
extend
insert
remove
pop
clear
sort
reverse
'''
# list of favorite destinations in india
list1 = ["gujrat","rajsthan","leh-ladakh","manali","goa","kerla","mumbai"]
# list of 10 different type of values
list2 = [1, "hello", 3.14, True, False, [1,2,3], {"name": "himanshu"}, (4,5), None, "india"]

#methods of list

#print complete list
print("complete list:",list1)

#print first element
print("first element:",list1[0])

#print elements from index 2 to 5
print("element 2 to 5",list1[2:7])

#print last element
print("print last :",list1[-1])

#print element starting in index 2
print("start index 2:",list1[2:])

#print list two times
print("two times:",list1 * 2)

# print concatenated  list
print("concatenated list:", list1 + list2)

#function of list
list = ["0",0,"hello",True,False,"byy",10,20 ]
list.append("hi,hello")
print("append:",list)
list.extend(["one","two","three"])
print("extend",list)
list.insert(2,"hello")
print("insert",list)
list.remove("byy")
print("remove",list)
list.pop(5)
print("pop",list)
list.clear()
print("clear",list)
# print(list1)
list3 = [3,4,6,2,1,7,9,0]
list3.sort()
print("sort",list3)
list3.reverse()
print("reverseprint",list3)