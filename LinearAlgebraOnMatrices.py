import sympy as sp #This is pivotal for matrix operations

# Inputting matrix
matrix = []
print("Enter each entry for the 4x4 matrix")
for i in range(4):
    while True:
        row = input(f"Enter 4 values for row {i+1}, separated by space: ").split()
        if len(row)!=4:
            print("There must be exactly 4 values")
            continue
        try:
            row = [sp.sympify(x) for x in row]
            matrix.append(row)
            break
        except:
            print("Invalid input. Please try again.")

A = sp.Matrix(matrix)

print("\nMatrix entered:  \n")
sp.pprint(A) 


#Declaring variables used for each task
B = sp.Matrix([0,0])
steady_1 = None
steady_2 = None


# Picking task to perform
while True:
    print("\nPick any task: \n1. An eigenvalue of 1 exists for the given matrix\n2. Finding steady state vector \n3. Revising matrix, then comparing steady state vectors \n4. Finding second largest eigenvalue")
    i = input("\nEnter 1, 2, 3, 4, or Q to exit: ")
    if i.lower() == "q":
        break
    if i not in {"1","2","3","4"}:
        print ("Invalid input, try again")
        continue
    
    "\n"
    # Task 1
    if i == "1":
        eigenval_list = list(A.eigenvals().keys())
        rounded = [round(float(x),3) for x in eigenval_list]
        if 1 in rounded:
            print ("Matrix A contains an eigenvalue of 1")
        else:
            print ("Matrix A does not contain an eigenvalue of 1")

    # Task 2
    elif i == "2":
        A = A.applyfunc(sp.nsimplify)
        B = A-sp.eye(4)
        S = B.nullspace()
        if not S:
            print ("\nThere is no steady state vector for this matrix")
        else:
            v=S[0]
            steady_1 = v/sum(v)
            print("\nSteady state vector is: ")
            sp.pprint(steady_1)
        
    # Task 3
    elif i == "3":
        while True:
            i = input("Pick row number to change: ")
            if i not in {"1","2","3","4"}:
                print ("Invalid row, try again")
                continue
            break
        while True:
            j = input("Pick column number: ")
            if j not in {"1","2","3","4"}:
                print ("Invalid column, try again")
                continue
            break
        while True:
            k = input("Type the changed value for that row and column: ")
            try:
                k=float(k)
                if k>=0:
                    break
                else:
                    print("Invalid input, try again")
            except (ValueError):
                print("Invalid input, try again")
        row = int(i)-1
        col = int(j)-1
        val = float(k)
        diff = val-A[row,col]
        C=A
        C[row,col] = val
        if diff>=0:
            C[col,col]-=diff
        else:
            C[col,col]+=diff
        C = C.applyfunc(sp.nsimplify)
        B = C-sp.eye(4)
        S = B.nullspace()
        if not S:
            print ("\nThere is no steady state vector for this matrix")
        else:
            v=S[0]
            steady_2 = v/sum(v)
            print("\nNew steady state vector is: ")
            sp.pprint(steady_2)
            
    #Task 4 
    elif i == "4":
        eigenval_list = list(A.eigenvals().keys())
        sorted_list = sorted(eigenval_list, reverse=True)
        print("\nThe second largest eigenvalue is " + str(sorted_list[1]))
        
  