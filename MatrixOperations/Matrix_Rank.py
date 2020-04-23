import numpy as np 
print("Enter first matrix number of rows and cols to perform Addition and Subtraction")

row_1 = int(input("Enter first matrix number of rows "))
col_1 = int(input("Enter first matrix number of cols "))

print("Enter first matrix elements in single line (separated by sapce) ")
fm_entries = list(map(float,input().split()))
fm_matrix = np.array(fm_entries).reshape(row_1,col_1)
print(fm_matrix)
print("Rank of entered matrix is : ",np.linalg.matrix_rank(fm_matrix))



	
