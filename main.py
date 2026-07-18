import numpy as np
from numpy import linalg as LA
np.set_printoptions(precision=3, suppress=False)
print("Enter 4x4 matrix")
A = np.zeros((4,4))
I = np.eye(4)

#Input
for i in range(4):
    while True:
         row = input(f"Enter 4 numbers for row {i+1}, separated by spaces\n ").strip().split()
         if len(row)!=4:
             print("You must enter four numbers\n")
             continue
         
         try:
             A[i] = [float(x) for x in row]
             break
         
         except:
             print("This is not a valid integer\n")

print("This is your 4x4 matrix\n")
print(A)
A = np.array([
    [0.5, 0.2, 0.1, 0.3],
    [0.2, 0.5, 0.2, 0.2],
    [0.2, 0.2, 0.6, 0.1],
    [0.1, 0.1, 0.1, 0.4]
])


     
    
    

while True:
    
    def escape_task():
     a = input("Press R to return, or Q to exit: ").strip().lower()
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
        finally:
            escape_task()
            
    if i == "3":
        C = A.__deepcopy__()
        num = input("\nChoose row number and column number to replace with: ").strip().split()
        replace = input("\nType the number you want to replace the matrix with: ").strip().split()
        current = C[num[0]][num[1]]
        difference = abs(replace-current)
        if current>replace:
            
        
       
        
         
        
    


        
    
        

       