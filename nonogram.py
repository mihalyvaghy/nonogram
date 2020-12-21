from gurobipy import *
import csv

def read_nonogram(filename):
    with open(filename, "r") as file:
        data = list(csv.reader(file))
    s = {"c": data[1:1+int(data[0][0])], "r": data[1+int(data[0][0]):]}
    for key in s:
        for j in range(len(s[key])):
            for k in range(len(s[key][j])):
                s[key][j][k] = int(s[key][j][k])
    return s

def print_nonogram(s):
    pass

def compute_sizes(s):
    return {key: [len(clusters) for clusters in s[key]] for key in s}

def compute_bounds(s):
    e = {}
    l = {}
    for key in s:
        e[key] = [[sum(s[key][j][:k])+k for k in range(len(s[key][j]))] for j in range(len(s[key]))]
    l["c"] = [[len(s["r"])-(sum(s["c"][j][k:])+len(s["c"][j])-(k+1)) for k in range(len(s["c"][j]))] for j in range(len(s["c"]))]
    l["r"] = [[len(s["c"])-(sum(s["r"][j][k:])+len(s["r"][j])-(k+1)) for k in range(len(s["r"][j]))] for j in range(len(s["r"]))]
    return e, l

def solve_nonogram(filename):
    s = read_nonogram(filename)

    k = compute_sizes(s)
    e, l = compute_bounds(s)

    model = Model("Nonogram solver")

    x = [[model.addVars(l["c"][i][t]-e["c"][i][t]+1, vtype=GRB.BINARY) for t in range(k["c"][i])] for i in range(len(k["c"]))]
    y = [[model.addVars(l["r"][i][t]-e["r"][i][t]+1, vtype=GRB.BINARY) for t in range(k["r"][i])] for i in range(len(k["r"]))]
    z = [model.addVars(len(k["c"]), vtype=GRB.BINARY) for _ in range(len(k["r"]))]

    for row in y:
        for cluster in row:
            model.addConstr(quicksum(list(cluster.values())) == 1)

    for column in x:
        for cluster in column:
            model.addConstr(quicksum(list(cluster.values())) == 1)

    for i in range(len(y)):
        for t in range(len(y[i])-1):
            for j in range(1,len(y[i][t])):
                model.addConstr(y[i][t][j] <= quicksum(y[i][t+1][jp] for jp in range(j,len(y[i][t+1]))))

    for i in range(len(x)):
        for t in range(len(x[i])-1):
            for j in range(1,len(x[i][t])):
                model.addConstr(x[i][t][j] <= quicksum(x[i][t+1][jp] for jp in range(j,len(x[i][t+1]))))


if __name__ == "__main__":
    solution = solve_nonogram("small.no")
    print_nonogram(solution)
