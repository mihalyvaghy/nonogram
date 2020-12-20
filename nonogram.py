from gurobipy import *
import csv

def read_nonogram(filename):
    with open(filename, "r") as file:
        data = list(csv.reader(file))
    return [data[1:1+int(data[0][0])], data[1+int(data[0][0]):]]

def print_nonogram(nonogram):
    pass

def solve_nonogram(filename):
    nonogram = read_nonogram(filename)

    model = Model("Nonogram solver")

    print(sum([len(nonogram[i][j]) for i in range(2) for j in range(len(nonogram[i]))]))

if __name__ == "__main__":
    solution = solve_nonogram("small.no")
    print_nonogram(solution)
