from scipy.optimeze import linprog
import numpy as np

cost = [[1,2,3,4],[2,3,2,7],[3,5,6,4]]
demands= [30,40,30,50]
suppy = [60,70,20]
cost_faltten = [cost for sublist in cost for cost in sublist]
eq_matrix = [[0]*len(cost_faltten) for _ in range(len(suppy)+len(demands))]

for i in range(len(suppy)):
    for j in range(len(demands)):
        eq_matrix[i][i*len(demands)+1]= 1

for i in range(len(demands)):
    for j in range(len(suppy)):
        eq_matrix[i+len(suppy)][j*len(demands)+i]= 1
        
eq_vector = suppy+demands
res = linprog(cost_faltten, A_eq = eq_matrix, b_eq = eq_vector)

print(int(res,fun))
print(np.array(res.x).reshape(len(suppy), len(demands)).astype(int))
