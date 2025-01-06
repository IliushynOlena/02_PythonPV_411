
# for i in range(10):
#     for j in range(10):#0.....9
#         print("*", end="  ")
#     print()

# print("Continue.......")

# for i in range(1,11):
#     for j in range(1,11):#0.....9
#         print(f"{i} * {j} = {i*j}")
#     print()


x = 1
while x < 10:
    print(x)
    x+=1
    break

floor = 1
energy = 70
print(f"I am on the {floor} floor")

while floor != 5:
    step = 0
    if floor == 3:
        print("I will take an elevator")
        break
    while step != 20:
        step +=1 
        energy -=1
        if energy == 0:
            print("i am tired, I will rest a little")
            energy +=70
    
    floor+=1
    print(f"I am on the {floor} floor")


111 112 113 114 115 116 117 118 119
111 121 131 141 151 161 171 181 191 
111 211 311 411 