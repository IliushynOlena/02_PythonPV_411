# завдання 1

import random
line = [random.randint(-10, 10) for i in range(5)]
suma1 = 0
suma2 = 0
suma3 = 0
for i in line:
    if i < 0:
        suma1 += i
    if i % 2 == 0:
        suma2 += i
    if i % 2 != 0:
        suma3 += i

print("Сума відємних чисел:", suma1)
print("Сума парних чисел:", suma2)
print("Сума не парних чисел:", suma3)


suma4 = 1
for index in range(len(line)):#0 1 2 3 4 5 6 7 8 9
    if index % 3 == 0:
        suma4 *= line[index]
print("добуток елементів з індексами кратними 3:", suma4)

numbers=[]
#numbers= 5  9  8  7  -5  4  12  6 -3  9
#index    0  1  2  3   4  5   6  7  8  9 
max = max(numbers) #12
min = min(numbers) #-5
max_index= numbers.index(max)#6  2
min_index= numbers.index(min)#4   6








print(line)
max_elem = (max(line))
min_element = (min(line))
max_index = line.index(max_elem)
min_index = line.index(min_element)
print(f"Max element {max_elem} in index  {max_index}")
print(f"Min element {min_element} in index  {min_index}")
if min_index > max_index:
    min_index, max_index = max_index, min_index
print(f"Max  index  {max_index}")
print(f"Min  index  {min_index}")
dob= 1
for index in range(min_index+1,max_index):
    dob *= line[index]

print("добуток елементів між мінімальним і максимальним елементом:", dob)
suma6 = 0
first_pos = 0
last_pos = 0
index_first_pos = 0
index_last_pos = 0
for index in range(len(line)):
    if line[index] > 0:
        index_first_pos = index
        break

for index in range(len(line)):
    if line[index] > 0:
        index_first_pos = index
        break


print("сума елементів, що знаходяться між першим та останнім додатними елементами:", suma6)

# завдання 2

list1 = []
list2 = []
list3 = []
list4 = []
for i in line:
    if i % 2 == 0:
        list1.append(i)
print(list1)
for i in line:
    if i % 2 != 0:
        list2.append(i)
print(list2)
for i in line:
    if i < 0:
        list3.append(i)
print(list3)
for i in line:
    if i >= 0:
        list4.append(i)
print(list4)

list_4 = [i for i in range(1,11) if i%2== 0]
print(list_4)

#for i in range(1,11) # 1 2 3 4 5 6 7 8 9 10
list_4 = [i for i in range(1,11) if i%2== 1]
print(list_4)

#for i in range(1,11) # 1 2 3 4 5 6 7 8 9 10
list_4 = [i for i in range(1,11) if i > 0]
print(list_4)

#for i in range(1,11) # 1 2 3 4 5 6 7 8 9 10
list_4 = [i for i in range(1,11) if i < 0]
print(list_4)

# завдання 3

line_a = [random.randint(-100, 101) for i in range(10)]
line_b = [random.randint(-100, 101) for i in range(10)]
line_c = []
line_c.extend(line_a)
line_c.extend(line_b)
print(line_c)