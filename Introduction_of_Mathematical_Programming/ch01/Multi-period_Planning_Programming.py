import pulp

# N: product variety
N = 2
# T: month
T = 3

# the number of row materials per product
A = [[2, 7],
     [5, 3]]

# The shipment at each month
B = [[30, 20],
     [60, 50],
     [80, 90]]

# The number of abailable materials at each month
C = [[920, 790],
     [750, 600],
     [500, 400]]

# Production Cost and Inventory Cost
D = [[75, 50],
     [8, 7]]

# arrange Inventory Plan
E1 = [[1 for t in range(T - 1)] + [0] for n in range(N)]
E2 = [[0] + [1 for t in range(T - 1)] for n in range(N)]

prog = pulp.LpProblem('Multi-period Planning Problem', pulp.LpMinimize);

x = pulp.LpVariable.dicts('X', (range(N), range(T)), 0, None, pulp.LpInteger)
y = pulp.LpVariable.dicts('Y', (range(N), range(T)), 0, None, pulp.LpInteger)

tmp_x = [[x[row][i] for i in range(T)] for row in range(N)]
tmp_y = [[y[row][i] for i in range(T)] for row in range(N)]

prog += pulp.lpDot(D[0], tmp_x) + pulp.lpDot(D[1], tmp_y)

for row_t in range(T):
    for row_i in range(N):
        prog += pulp.lpDot(A[row_i], [x[i][row_t] for i in range(N)]) <= C[row_t][row_i]

for row_t in range(T):
    for row_i in range(N):
        prog += x[row_i][row_t] + E2[row_i][row_t] * y[row_i][(T + row_t - 1) % T] - E1[row_i][row_t] * y[row_i][row_t] == B[row_t][row_i]

print(prog)

prog.solve()

for t in range(T):
    for n in range(N):
        print(x[n][t].varValue)

for t in range(T):
    for n in range(N):
        print(y[n][t].varValue)
