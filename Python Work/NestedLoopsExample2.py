#Mary Kate Sheehan
#10/16/2023
#Array Example, index of the elements of an array

#3 columns, 3 rows
#     0    1     2
# 0   11   22    33
# 1   44   55    66
# 2   77   88    99


#to design or do operations on array
#nested loop:
    #outer loop: rows
    #inner loop: columns


for row in range(3):
    for column in range(3):
        print("(",row,",",column,")", end = "...")
