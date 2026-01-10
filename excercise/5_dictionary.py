'''
create dictionary to store 20 different detail about your ownself 
print dictionary
print name, age, gender, dob 
add key value pair pincode into dictionary 
add key value pair to store your 5 favourite touriest destination 
print all the favourite touriest destination 

use update method to add new key value pair in dictionary
use update method to change existing key value pair in dictionary
use pop method to remove dob 
use popitem item method to remove last item 

display all keys
display all values 

copy dictionary to another dictionary using copy function 
clear newly create dictionary. 
'''
#20 different detail about yourself
student = {
    "name" : "himanshu sarvaiya",
    "age" : 20,
    "gender" : "male",
    "dob" : "08-06-2006",
    "address" : "sarita society",
    "phone" : "1212131314",
    "email" : "himanshusarvaiya77@gamil.com",
    "education" : "BCA",
    "occupation" : "student",
    "hobbies" : "editing",
    "skills" : "python",
    "languages" : ["english", "hindi", "gujarati"],
    "interests" : ["technology", "science", "travel"],
    "goals" : ["learn new skills", "build projects", "Data science"],
    "achievements" : "none",
    "family" : {"father": "b", "mother": "d"},
    "friends" : ["bhavdip", "jatin", "rohit"],
    "favorite_food" : "pizza",
    "favorite_color" : "blue",
    "favorite_movie" : "fast and fruious"
}

# print dictionary
print(student)
# print name, age, gender, dob 
print(student["name"])
print(student["age"])
print(student["gender"])
print(student["dob"])
# add key value pair pincode into dictionary
# use update method to add new key value pair in dictionary
student.update({'pincode':3633300})
print(student['pincode'])
# add key value pair to store your 5 favourite touriest destination 
student.update({'favourite_tourist_destination': ['paris', 'london', 'new york', 'tokyo', 'sydney']})
# print all the favourite touriest destination
print(student['favourite_tourist_destination'])
# use update method to change existing key value pair in dictionary
student.update({'favourite_tourist_destination': ['paris', 'london', 'new york', 'tokyo', 'america']})
print(student['favourite_tourist_destination'])

# use pop method to remove dob 
student.pop('dob')
print(student)

# use popitem item method to remove last item 
student.popitem()
print(student)

# display all keys
print(student.keys())

#display all value

print(student.values())

# copy dictionary to another dictionary using copy function 
std = student.copy()
print(std)
# clear newly create dictionary. 
std.clear()

