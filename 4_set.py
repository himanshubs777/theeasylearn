destination = {'gujrat' ,'rajsthan','mumbai','manali','gujrat','rajsthan','kasmir'}
print(destination)

list_color = ['red','pink','orange','red','pink','yellow','white']
print(set(list_color))

destination.add('goa')
destination.remove('mumbai')
print(destination)

# union, intersection , diffrence

set1 = {10,20,40,50,30,25,66,88,99}
set2 = {20,10,33,44,40,25,66,70,32}

union = set1.union(set2)
intersection = set1.intersection(set2)
diffrence = set1.difference(set2)

print("union:",union)
print("intersection",intersection)
print("diffrence",diffrence)
