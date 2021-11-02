# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

# Spearman's Rank Correlation Coefficient
# Reference: https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient
# Quiz: Given two n-element data sets, X and Y, calculate the value of
# Spearman's rank correlation coefficient.

# Define functions
def rank(dt):
    rank = {}
    sort = sorted(dt)
    for i in range(len(dt)):
        for j in range(len(sort)):
            if dt[i] == sort[j]:
                rank[dt[i]] = j + 1
    return rank

def spearman(x, y, rx, ry, n):
    diff_rank = 0
    for i in range(n):
        if rx[x[i]] != ry[y[i]]:
            diff_rank = diff_rank + ((rx[x[i]] - ry[y[i]]) ** 2)
    return (6 * diff_rank) / (n ** 3 - n)

# Set data
n = int(float(input()))
data_set_x = list(map(float, input().split()))
data_set_y = list(map(float, input().split()))

# Get rank
rank_x = rank(data_set_x)
rank_y = rank(data_set_y)

# Gets the result and show on the screen
s = spearman(data_set_x, data_set_y, rank_x, rank_y, n)
print(round(1 - s, 3))

##############

n = int(input())
x = [float(e) for e in input().split()]
y = [float(e) for e in input().split()]


rank_x = dict((x1, i + 1) for i, x1 in enumerate(sorted(set(x))))
rank_y = dict((x1, i + 1) for i, x1 in enumerate(sorted(set(y))))

x_rank = [rank_x[e] for e in x]
y_rank = [rank_y[e] for e in y]

d = [(x_rank[i] - y_rank[i]) ** 2 for i in range(n)]
rxy = 1 - ((6) * sum(d)) / (n * (n * n - 1))

print(round(rxy, 3))

###############

N = int(input())
X = list(map(float, input().strip().split()))
Y = list(map(float, input().strip().split()))

X_COPY = X.copy()

Y_COPY = Y.copy()

X_COPY.sort()

XD = dict(zip(X_COPY, range(1, N+1)))

Y_COPY.sort()

YD = dict(zip(Y_COPY, range(1, N+1)))

RX = [XD[i] for i in X]

RY = [YD[i] for i in Y]

print(round(1-(6*sum([(RX-RY)**2 for RX, RY in zip(RX, RY)]))/((N**3)-N), 3))

