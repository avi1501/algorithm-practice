def knapsack(n, price , weight, capacity):
    matrix = [[-1]*(capacity+1) for i in range(n+1)]

    for i in range(n+1):
        matrix[i][0] = 0
    for i in range(capacity+1):
        matrix[0][i] = 0

    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if weight[i-1] <= j:
                matrix[i][j] = max(matrix[i-1][j],price[i-1]+matrix[i-1][j-weight[i-1]])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[n][capacity]

price = [60, 100, 120,300]
weight = [10,20,30,40]
capacity = 80
n = len(price)


# ar = """57 95 13 29 1 99 34 77 61 23 24 70 73 88 33 61 43 5 41 63 8 67 20 72 98 59 46 58 64 94 97 70 46 81 42 7 1 52 20 54 81 3 73 78 81 11 41 45 18 94 24 82 9 19 59 48 2 72"""
# wt = """83 84 85 76 13 87 2 23 33 82 79 100 88 85 91 78 83 44 4 50 11 68 90 88 73 83 46 16 7 35 76 31 40 49 65 2 18 47 55 38 75 58 86 77 96 94 82 92 10 86 54 49 65 44 77 22 81 52"""

# capacity = 41
# price = list(map(int,ar.split(" ")))
# weight = list(map(int,wt.split(" ")))
# n = len(price)

print(knapsack(n, price, weight, capacity))