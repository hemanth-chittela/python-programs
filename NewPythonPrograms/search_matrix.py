matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
Flag=False
Target=20
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]==Target:
            Flag=True
            break
if Flag:
    print("True")
else:
    print("False")