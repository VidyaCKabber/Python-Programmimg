import numpy as np 

print("Enter first matrix number of rows and cols to perform Addition and Subtraction")

row_1 = int(input("Enter first matrix number of rows "))
col_1 = int(input("Enter first matrix number of cols "))

print("Number of cols of first matrix and ross must be same to perform Matrix multiplication ")
row_2 = int(input("Enter second matrix number of rows "))

if(col_1 == row_2):
    col_2= int(input("Enter second matrix number of cols "))
    print("Enter first matrix elements in single line (separated by sapce) ")
    fm_entries = list(map(float,input().split()))
    fm_matrix = np.array(fm_entries).reshape(row_1,col_1)

    print("Enter second matrix elements in single line (separated by space) ")
    sm_entries = list(map(float,input().split()))
    sm_matrix = np.array(sm_entries).reshape(row_2,col_2)

    #Multifly Add both the matrices
    print("Multiplication of\n",fm_matrix,"\n*s\n",sm_matrix, "\n=\n",fm_matrix.dot(sm_matrix))

else:
    print("Number of cols of first matrix and ross must be same to perform Matrix multiplication ")



