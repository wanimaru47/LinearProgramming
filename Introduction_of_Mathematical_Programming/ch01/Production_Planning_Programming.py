# 1.1.1 Production Planning Problem (P.1)

import pulp

prog = pulp.LpProblem('test', pulp.LpMaximize)

A = [[5, 0, 6],
     [0, 2, 8],
     [7, 0, 15],
     [3, 11, 0]]
b = [80, 50, 100, 70]
c = [70, 120, 30]

x = pulp.LpVariable.dicts('X', range(3), 0, 100, pulp.LpInteger)

prog += pulp.lpDot(c, [x[i] for i in range(3)])

for row in range(4):
    prog += pulp.lpDot(A[row], [x[i] for i in range(3)]) <= b[row]

for i in range(3):
    prog += x[i] >= 0

print(prog)
prog.solve();

for i in range(3):
    print(x[i].varValue)
