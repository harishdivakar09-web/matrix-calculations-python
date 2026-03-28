import numpy as np
import sympy as sp

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

A_np = np.array(matrix, dtype=object)
A_sp = sp.Matrix(matrix)

print("\nMatrix entered: ")
sp.pprint(A_sp)
