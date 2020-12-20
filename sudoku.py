from gurobipy import *

n = 3

def read_sudoku(filename):
    sudoku = []
    with open(filename, "r") as file:
        for line in file:
            sudoku.append(line[:-1].split(" "))
    return sudoku

def print_sudoku(sudoku):
    for line in sudoku:
        for cell in line:
            print(cell, end = " ")
        print()

def max_index(x):
    return x.index(max(x)) + 1

def check_sudoku(sudoku, solution):
    for i in range(n**2):
        for j in range(n**2):
            if sudoku[i][j] != "x" and int(sudoku[i][j]) != solution[i][j]:
                return False
    return True

def solve_sudoku(filename):
    sudoku = read_sudoku(filename)

    model = Model("Sudoku solver")

    q = model.addVars(n**2**n, lb = 0, ub = 1, vtype = GRB.INTEGER)

    model.addConstrs((quicksum(q[i*n**2**2+j*n**2+k] for k in range(n**2)) == 1 for j in range(n**2) for i in range(n**2)), name = "cell")
    model.addConstrs((quicksum(q[i*n**2**2+j*n**2+k] for j in range(n**2)) == 1 for k in range(n**2) for i in range(n**2)), name = "row")
    model.addConstrs((quicksum(q[i*n**2**2+j*n**2+k] for i in range(n**2)) == 1 for k in range(n**2) for j in range(n**2)), name = "column")
    model.addConstrs((quicksum(quicksum(q[i*n**2**2+j*n**2+k] for j in range(n*m,n*(m+1))) for i in range(n*l,n*(l+1))) == 1 for k in range(n**2) for m in range(n) for l in range(n)), name = "box")
    for i in range(n**2):
        for j in range(n**2):
            if sudoku[i][j] != "x":
                model.addConstr(q[i*n**2**2+j*n**2+int(sudoku[i][j])-1] == 1, name = "clues")

    model.Params.OutputFlag = 0
    model.optimize()

    solution = [[max_index([q[i*n**2**2+j*n**2+k].x for k in range(n**2)]) for j in range(n**2)] for i in range(n**2)] 
    if check_sudoku(sudoku, solution):
        return solution
    else:
        print("No solutions exist")

def solve_kokonotsu(filename):
    sudoku = read_sudoku(filename)

    model = Model("Sudoku solver")

    q = model.addVars(n**2**n, lb = 0, ub = 1, vtype = GRB.INTEGER)

    model.addConstrs((quicksum(q[i*n**2**2+j*n**2+k] for k in range(n**2)) == 1 for j in range(n**2) for i in range(n**2)), name = "cell")
    model.addConstrs((quicksum(q[i*n**2**2+j*n**2+k] for j in range(n**2)) == 1 for k in range(n**2) for i in range(n**2)), name = "row")
    model.addConstrs((quicksum(q[i*n**2**2+j*n**2+k] for i in range(n**2)) == 1 for k in range(n**2) for j in range(n**2)), name = "column")
    model.addConstrs((quicksum(quicksum(q[i*n**2**2+j*n**2+k] for j in range(n*m,n*(m+1))) for i in range(n*l,n*(l+1))) == 1 for k in range(n**2) for m in range(n) for l in range(n)), name = "box")
    for i in range(n**2):
        for j in range(n**2):
            if sudoku[i][j] != "x":
                model.addConstr(q[i*n**2**2+j*n**2+int(sudoku[i][j])-1] == 1, name = "clues")
    model.addConstrs((quicksum(q[i*n**2**2+i*n**2+k] for i in range(n**2)) == 1 for k in range(n**2)), name = "diag1")
    model.addConstrs((quicksum(q[i*n**2**2+(n**2-1-i)*n**2+k] for i in range(n**2)) == 1 for k in range(n**2)), name = "diag2")

    model.Params.OutputFlag = 0
    model.optimize()

    solution = [[max_index([q[i*n**2**2+j*n**2+k].x for k in range(n**2)]) for j in range(n**2)] for i in range(n**2)] 
    if check_sudoku(sudoku, solution):
        return solution
    else:
        print("No solutions exist")

def solve_knight(filename):
    sudoku = read_sudoku(filename)

    model = Model("Sudoku solver")

    q = model.addVars(n**2**n, lb = 0, ub = 1, vtype = GRB.INTEGER)

    model.addConstrs((quicksum(q[i*n**2**2+j*n**2+k] for k in range(n**2)) == 1 for j in range(n**2) for i in range(n**2)), name = "cell")
    model.addConstrs((quicksum(q[i*n**2**2+j*n**2+k] for j in range(n**2)) == 1 for k in range(n**2) for i in range(n**2)), name = "row")
    model.addConstrs((quicksum(q[i*n**2**2+j*n**2+k] for i in range(n**2)) == 1 for k in range(n**2) for j in range(n**2)), name = "column")
    model.addConstrs((quicksum(quicksum(q[i*n**2**2+j*n**2+k] for j in range(n*m,n*(m+1))) for i in range(n*l,n*(l+1))) == 1 for k in range(n**2) for m in range(n) for l in range(n)), name = "box")
    for i in range(n**2):
        for j in range(n**2):
            if sudoku[i][j] != "x":
                model.addConstr(q[i*n**2**2+j*n**2+int(sudoku[i][j])-1] == 1, name = "clues")

    model.Params.OutputFlag = 0
    model.optimize()

    solution = [[max_index([q[i*n**2**2+j*n**2+k].x for k in range(n**2)]) for j in range(n**2)] for i in range(n**2)] 
    if check_sudoku(sudoku, solution):
        return solution
    else:
        print("No solutions exist")

if __name__ == "__main__":
    #solution = solve_sudoku("17.su")
    solution = solve_kokonotsu("kok.su")
    print_sudoku(solution)
