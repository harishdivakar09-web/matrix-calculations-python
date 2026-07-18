import numpy as np
from numpy import linalg as LA
np.set_printoptions(precision=3, suppress=False)
print("Enter a column-stochastic 4x4 matrix")
I = np.eye(4)

#Input
while True:
    A = np.zeros((4,4))
    for i in range(4):
        while True:
            row = input(f"Enter 4 numbers for row {i+1}, seperated by spaces\n ").strip().split()
            if len(row)!=4:
                print("You must enter four numbers\n")
                continue
            
            try:
                A[i] = [float(x) for x in row]
                break
            
            except ValueError:
                print("This is not a valid integer\n")
                continue
        
    col_sum = A.sum(axis = 0)
    if np.all(A>=0) and np.allclose(col_sum,1):
        break
        
    print("This is not column-stochastic. Try again\n")
              
    
         
        

         
             

print("This is your matrix: ")
print(A)



     
    
    

while True:
    
    def escape_task():
     a = input("\nPress R to return, or Q to exit: ").strip().lower()
     if a == "r":
         return True
     if a == "q":
         return False
    
     
    print("\nPick any task: \n1. An eigenvalue of 1 exists for the given matrix\n2. Finding steady state vector \n3. Revising matrix, then comparing steady state vectors \n4. Finding second largest eigenvalue")
    i = input("\nEnter 1, 2, 3, 4, or Q to exit: ").strip().lower()
    if i not in ["1","2","3","4","q"]:
        print("\nInvalid, please try again")
        continue
    if i in ["q"]:
        break
    
    if i == "1":
        eigenvalues = LA.eigvals(A).tolist()
        if 1 in eigenvalues:
            print("\nThe matrix has an eigenvalue of 1")
        else:
            print("\nThe matrix does not have an eigenvalue of 1")
        if (escape_task()):
            continue
        else:
            break
    
    if i == "2":
        try:
            B = A - I
            b = np.zeros((4,1))
            B[-1] = np.ones(4)
            b[-1] = 1
            print(LA.solve(B,b))
        except LA.LinAlgError:
            print("\nThis matrix has no steady state vector")
    
        if(escape_task()):
            continue
        else:
            break
            
    if i == "3":
        C = A.copy()
        while True:
            try:
                num = float(input("\nChoose row number and column number to replace with: ").strip().split())
                replace = float(input("\nType the number you want to replace with: ").strip().split())
            except:
                print("Invalid integer, try again")
                continue
            
            current = C[num[0]][num[1]]
            difference = abs(replace-current)
        
                
            
            
            
        
       
        
         
        
    


        
    
        

       