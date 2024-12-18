'''
line = "Hello world. Have a nice day!!!!"#25

num = 10
print(line)
print(line[0])
print(line[1])
print(line[2])
print(line[3])
print(line[4])
print(line[5])
i = 0
end = 10
while i <= end:
    print(line[i], end=" ")
    i += 1
print()



for letter in line:
    print(letter, end=" ")

print("Continue.....")
print()
for letter in line[0:18:1]:#start = 0. end = 9. step = 1
    print(letter, end=" ")

print()
for letter in line[0:5]:#start = 0. end = 4. step = 1
    print(letter, end=" ")
print()
for letter in line[5:]:#start = 5. end = 21. step = 1
    print(letter, end=" ")
print()
for letter in line[5: 10]:#start = 0. end = 4. step = 1
    print(letter, end=" ")
print()
for letter in line[:]:#start = 0. end = 21. step = 1
    print(letter, end=" ")
print()
for letter in line[::3]:#start = 0. end = 21. step = 2
    print(letter, end=" ")
print()
#start = 0, end = 10-1, step = 1
for num in range(10):
    print(num, end=" ")

print()
#start = 10, end = 20-1, step = 1
for num in range(10,20):
    print(num, end=" ")
print()
#start = 10, end = 20-1, step = 2
for num in range(10,20,2):
    print(num, end=" ")


print()
while True:
    number = int(input(" 2 + 2 = ? ---> "))
    if number == 4:
        print("Congratulation !!!!!!")
        break
    else:
        print("Error .... Enter again : ")

print("Continue......")


#0.......end
#break
#continue
i = 0
num = int(input("Enter number : "))
while i <= num:
    # if i%3 != 0:
    #     print(i, end=" ")
    i+=1
    if i%3 == 0:
        continue
    print(i, end=" ")

'''
# counter = 0
# number = int(input("Enter number : "))#17 ....17/1 17/2 17/3 17/4....17/17
# for i in range(1, number+1):
#     if number%i == 0:
#         counter+=1

# if counter >2 :
#     print("Prime")
# else:
#     print("Number is simple ")

# flag = True # bool
# number = int(input("Enter number : "))#17 ....17/1 17/2 17/3 17/4....17/17
# for i in range(2, number//2+1):#100 / (1...50)
#     if number%i == 0:
#         flag = False
#         break
# #flag = True   flag = False
# if not flag :# not True-->False.. False--->True
#     print("Prime")
# else:
#     print("Number is simple ")

# if not 5 == 4:# not True-->False.. False--->True
#     print("True")
# else:
#     print("False ")

for i in range(10):#Height
    for j in range(10):#width
        print("*",end=" ")
    print()
print()
for i in range(10):#Height
    for j in range(10):#width
        if(i >= j):
            print("*",end=" ")
    print()
    