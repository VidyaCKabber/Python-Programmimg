import numpy as np 

print("Enter first matrix number of rows and cols to perform Addition and Subtraction")

row_1 = int(input("Enter first matrix number of rows "))
col_1 = int(input("Enter first matrix number of cols "))

print("Number of rows and cols must be same to perform Addition and Subtraction ")
row_2 = int(input("Enter second matrix number of rows "))

if(row_1 == row_2):
    col_2= int(input("Enter second matrix number of cols "))
    if(col_2 == col_1):
        print("Enter first matrix elements in single line (separated by sapce) ")
        fm_entries = list(map(float,input().split()))
        fm_matrix = np.array(fm_entries).reshape(row_1,col_1)

        print("Enter second matrix elements in single line (separated by space) ")
        sm_entries = list(map(float,input().split()))
        sm_matrix = np.array(sm_entries).reshape(row_2,col_2)

        #Add both the matrices
        print("Addition of\n",fm_matrix,"\n+\n",sm_matrix, "\n=\n",np.add(fm_matrix,sm_matrix))

        #Subtract both the matrices
        print("Substraction of\n",fm_matrix,"\n-\n",sm_matrix, "\n=\n",np.subtract(fm_matrix,sm_matrix))

    else:
        print("Number of cols of both the matrices must be same to perform Addition and Substraction ")
    
else:
    print("Number of rows of both the matrices must be same to perform Addition and Substraction ")



