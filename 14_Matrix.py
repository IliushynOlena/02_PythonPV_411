
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
#get rows
for row in matrix:
    print(row)
#get elements
for row in matrix:
    for elem in row:
        print(f" {elem}\t",end="")

    print()

print(matrix[0])
print(matrix[1])
print(matrix[2])

print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])

#get element by index
for i in range(len(matrix)):#0 1 2
    for j in range(len(matrix[i])):#0 1 2
        print(matrix[i][j],end=" ")
    print()
#for i in range(3) - 0 1 2
#for j in range(5) : 0 1 2 3 4
matrix2 = [[ j for j in range(5)] for i in range(3)]
print(matrix2)


import random
matrix_random = []
row = 5
col = 6
# for i in range(row):
#     list=[]
#     for j in range(col):
#         list.append(random.randint(20,50))
#     matrix_random.append(list)
#1.for j in range(col) --> 0 1 2 3 4 5 
#2. random.randint(20,50)
for i in range(row):
    matrix_random.append( [random.randint(20,50) for j in range(col)] )

for row in matrix_random:
    print(row)

#summa = sum(matrix_random) #error
summa= 0
for row in matrix_random:
    summa += sum(row)
    print(f"Summa elments in row {sum(row)}")
print(f"Total summa = {summa}")

print()

summa_col_total = 0
summa_col = 0
row = 5
for i in range(col):#i = 0
    summa_col = 0
    for j in range(row):#j = 0 1 2 3 4
        summa_col_total+= matrix_random [j][i]
        summa_col+= matrix_random [j][i]
    print(f"Summa elments in cols {summa_col}")
print(f"Summa elments in cols {summa_col_total}")