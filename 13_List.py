#1
category = ["Drama","Comedy","Fantasy"]
#2
courses = list(("Python","SQL","HTML","C++","C#"))

print(category)
print(courses)

#empty list
studentsScore = []
marks = list()
print(studentsScore)
print(marks)

myList = ["Math", 145, 1.33, True, False, [1,5,8,9],["Good","Bad",3.36]]
print(myList)

customers = ["Bob","Anna","Sophia","Jack","Bob","Jack"]
print(customers)

letters = list("alsfjsldkgjs")
print(letters)

#newList = [expession for item in sequence]
#for i in range(6) # 0 1 2 3 4 5 
numbers = [ i for i in range(6)]
print(numbers)

numbers = [i + 10  for i in range(6)]
print(numbers)

numbers = [ i*i for i in range(6)]
print(numbers)

import random
#for i in range(10) --> 0 1 2 3 4 5 6 7 8 9 - count iteration
list_numbers = [random.randint(20,50)    for i in range(10)]
print(list_numbers)

for num in list_numbers:
    print(num, end=" ")
print()

dob = 1
for index in range(len(list_numbers)):
    if index%3 == 0:
        dob *= list_numbers[index]
        print(list_numbers[index])
#for i in "example" ---> e x a m p le 
list_1 = [i for i in "example"]
print(list_1)
list_2 = [i+"*" for i in "example"]
print(list_2)
list_3 = [i*"*" for i in range(1,10)]
print(list_3)

list_4= [i for i in "language"]
print(list_4)
#"_" - сепаратор - символ для обєднання елементів
# .join(list_3) - обєднує всі елементи списку в одну стрінгу
print("_".join(list_4))

line = "blue red green gray white black pink red green purple red green gray white black pink"
list_colors = line.split(' ')
print(list_colors)
for word in list_colors:
    print(word)

#newList = [expession for item in sequence if condition ]
#for i in range(1,11) # 1 2 3 4 5 6 7 8 9 10
list_5 = [i*i for i in range(1,11) if i%2== 0]
print(list_5)

customers = ["Bob","Anna","Sophia","Jack","Bob","Jack"]
#for i in customers = "Bob","Anna","Sophia","Jack","Bob","Jack"
list_6 = [name   for name in customers if name!= "Bob" and name != "Jack"]
print(list_6)

#for x in range(1,4) = 1 2 3 
#for y in range(1,4) = 2 3 4
#x= 1  1*2  1*3 1*4 
#x = 2 2*2 2*3 2*4
#x = 3 3*2 3*3 3*4
# for i in range(1,4):
#     for j in range(2,5):
#         print(i*j)
list_7 = [x*y  for x in range(1,4)  for y in range(2,5)]
print(list_7)

list_8 = [[x*y  for x in range(1,4)]  for y in range(2,5)]
print(list_8)


myList = ["Math",2365,5.13,"Yellow",True, False,[1,45,23,14]]
print(myList)
print(myList[0])
print(myList[2])
print(myList[len(myList)-1])
print(myList[-1])
#зріз = [start : stop : step]
print(myList[1:3])
print(myList[-4:-2])
print(myList[1:-1])
#reverse 
print(myList[::-1])
print(myList[4::-1])
print(myList[-4::-1])

category = ["Drama", "Comedy", "Fantasy","Cartoon","Horor","History","Science"]
print(category)
category[0] = "Action"
print(category)
category[::2] = ["New name1","New name2","New name3","New name4"]
print(category)

userLogs = ["admin","student","teacher","hr","user"]
prices = [100,200,30,400,50]
print(len(userLogs))
print(len(prices))

print(sorted(userLogs))
print(sorted(prices))

print(min(userLogs))
print(min(prices))

print(max(userLogs))
print(max(prices))

#print(sum(userLogs))  # errors ---> work with nubers
print(sum(prices))

#operator + 
category1 = ["Drama", "Comedy", "Fantasy"]
category2 = ["Cartoon","Horor","History","Science"]
print(category1+ category2)
print(category1*2)
#start = 0; 
for film in category1[1:5:1]:
    print(film)
#range(size) -> size = 3 => range(3) => start = 0; end= 2;step = 1 ---> 0 1 2
# category1[0]
# category1[1]
# category1[2]
# category1[3]
#range(3) ---> 0 1 2
#range(1,5,1)
#range(1,3)
for index in range(1,len(category1),1):
    print(category1[index])

print("Methods list : ")
print(category1)
#add new element in the end
category1.append("Fantasy")
print(category1)

#add range of elements in the end
category1.extend(category2)
print(category1)

#insert - add new element on the index
category1.insert(1,"Novel")
print(category1)

#remove - delete first element on value
category1.remove("Fantasy")
print(category1)

#pop - delete element on the index
category1.pop(0)
print(category1)

#pop - delete last element 
category1.pop()
print(category1)

#delete all element
category1.clear()
print(category1)


category1 = ["Drama", "Comedy", "Comedy","Comedy","Fantasy"]
#find element 
print(category1.index("Comedy"))
#print(category1.index("Comedyyyy"))

print(category1.count("Comedy"))

category1.sort()
print(category1)
#or 
category1.sort(reverse=False)
print(category1)

category1.sort(reverse=True)
print(category1)

customers = ["Anna","Bob","Sophia","Jack","Bob","Jack"]
for name in customers:
    if name == "Bob":
        print("Bob is a customer")

print( "Bob" in customers)
print( "Olena" in customers)
if "Bob" in customers:
    print("Bob is customer")
else:
    print("Error")


numbers = [1,2,3,4,5]
# numbers_clone = numbers
# print(numbers)
# print(numbers_clone)

# numbers_clone[0] = 45
# numbers_clone[2] =94
# numbers_clone[-1] = 11

# print(numbers)
# print(numbers_clone)

#1 method copy
# numbers_clone_1 = numbers.copy()
# print(numbers)
# print(numbers_clone_1)
# numbers_clone_1[0]= 144
# print(numbers)
# print(numbers_clone_1)

#use list constructor
# numbers_clone_1 = list(numbers)
# print(numbers)
# print(numbers_clone_1)
# numbers_clone_1[0]= 144
# print(numbers)
# print(numbers_clone_1)

#3 user slice 
numbers_clone_1 = numbers[:]
print(numbers)
print(numbers_clone_1)
numbers_clone_1[0]= 144
print(numbers)
print(numbers_clone_1)