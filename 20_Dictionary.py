#list
numbers = [1,5,9,6,70]
words = ['red','green','blue']
some_list = [1,8,5,True, False,[1,5,8]]

#cortege
cortege1 = (1,5,9,6,70)
cortege2 = ('red','green','blue')
cortege3 = (1,8,5,True, False,[1,5,8])

#dictionary - dic
student = {
    #key : value
    #key - string, number
    #value - anything type
    'name':'Stas',
    'lastname':'Bondar',
    'rating':11.2,
    'group' : 'PV411',
    'birthday':'25.01.2007'
}
print(student)
print(student['name'])
print(student['lastname'])
print(f"Name : {student['name']}. Birthday {student['birthday']}")

#get all keys()
for key in student.keys():
    print(f"Key : {key}  --->  Value : {student[key]} ")


#get all values()
for value in student.values():
    print(f" {value}")


#get all key and value
for key, value in student.items():
    print(f" {key}  --->  {value} ")

print(student.keys())
print(student.values())
print(student.items())

#delete element from the dic
print("--------------- Delete by key ---------------")
print(student)
del student['rating']
print(student)
#delete last element
student.popitem()
print(student)
student.pop('lastname')
print(student)

#add new element
student['email'] = 'stas@gmail.com'
print(student)
print(student['email'])
student['email'] = 'olena@gmail.com'
print(student)

students = [
    { 'name':'Stas1',
     'lastname':'Bondar',
     'rating':11.2,
     'group' : 'PV411',
     'birthday':'25.01.2007'},
    { 'name':'Stas2','lastname':'Bondar','rating':11.2,'group' : 'PV411','birthday':'25.01.2007'},
    { 'name':'Stas3','lastname':'Bondar','rating':11.2,'group' : 'PV411','birthday':'25.01.2007'},
    { 'name':'Stas4','lastname':'Bondar','rating':11.2,'group' : 'PV411','birthday':'25.01.2007','marks':[11,12,10,9,3]},
    { 'name':'Stas5','lastname':'Bondar','rating':11.2,'group' : 'PV411','birthday':'25.01.2007'},
]

print(students[3])
print(students[3]['lastname'])
print(students[3]['marks'][-1])

for mark in students[3]['marks']:
    print(mark, end=" ")
print()


import json
student = {
    'name':'Stas',
    'lastname':'Bondar',
    'rating':11.2,
    'group' : 'PV411',
    'birthday':'25.01.2007'
}
# with open('student.txt','w') as file:
#     file.write(str(student))

print(type(student))
print(student)

byte_obj = json.dumps(student)
print(type(byte_obj))
print(byte_obj)
with open('student.txt','w') as file:
    file.write(byte_obj)

read_obj = json.loads(byte_obj)
print(type(read_obj))
print(read_obj)
print(read_obj['name'])

with open('student.txt') as file :
    info = file.read()
    print(info)
    info = json.loads(info)
    print(info['name'])
