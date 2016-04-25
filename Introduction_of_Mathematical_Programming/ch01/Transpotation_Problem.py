# 1.1.3 Transpotation Problem

import pulp

N = 2
M = 3

# each total product
A = [90, 80]

# each order for a company
B = [70, 40, 60]

# each transfer cost
Cost = [[4, 7, 12],
        [11, 6, 3]]

prog = pulp.LpProblem('Transpotation Problem', pulp.LpMinimize)

x = pulp.LpVariable.dicts('X', (range(N), range(M)), 0, None, pulp.LpInteger)

str_x = [[x[i][j] for j in range(M)] for i in range(N)]

prog += pulp.lpDot(Cost, str_x)

for i in range(N):
    prog += pulp.lpDot([1 for j in range(M)], [x[i][j] for j in range(M)]) == A[i]

for i in range(M):
    prog += pulp.lpDot([1 for j in range(N)], [x[j][i] for j in range(N)]) == B[i]

prog.solve()

print(prog)
for i in range(N):
    for j in range(M):
        print(x[i][j].varValue)
