import sympy as sp #This is pivotal for matrix operations

# Inputting matrix
matrix = []
print("Enter each entry for the 4x4 matrix")
for i in range(4):
    while True:
        row = input(f"Enter 4 values for row {i+1}, seperated by space: ").split()
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

print("\nMatrix entered: ")
sp.pprint(A) 


B = sp.Matrix([0,0])


# Picking task to perform
"\n"
print("Pick any task: \n1. An eigenvalue of 1 exists for the given matrix\n2. Finding steady state vector \n3. Revising matrix, then comparing steady state vectors \n4. Finding second largest eigenvalue")
while True:
   i = input("\nEnter 1, 2, 3, or 4: ")
   if i not in {"1","2","3","4"}:
       print ("Invalid input, try again")
       continue
   break

"\n"
# Task 1
if i == "1":
    if 1 in A.eigenvals():
        print ("Matrix A contains an eigenvalue of 0")
    else:
        print ("Matrix A does not contain an eigenvalue of 0")

# Task 2
if i == "2":
    A = A.applyfunc(sp.nsimplify)
    B = A-sp.eye(4)
    S = B.nullspace()
    sp.pprint(S[0])
    #To be continued

