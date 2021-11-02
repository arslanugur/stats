# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

# Pearson correlation coefficient
# Reference: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

# Question: Given two n-element data sets, X and Y, calculate the value of
# the Pearson correlation coefficient.

# import libraries
import statistics as st

# define function to Pearson correlation coefficient
def correlation_coefficient(n, dt_x, dt_y):
    mean_x = st.mean(dt_x)
    mean_y = st.mean(dt_y)
    std_x = st.pstdev(dt_x)
    std_y = st.pstdev(dt_y)
    c = 0
    for i in range(n):
        c = c + (dt_x[i] - mean_x) * (dt_y[i] - mean_y)
    return c / (n * std_x * std_y)

# Set data
n = int(float(input()))
data_set_x = list(map(float, input().split()))
data_set_y = list(map(float, input().split()))

# Gets the result and show on the screen
print (round(correlation_coefficient(n, data_set_x, data_set_y), 3))

#####################

def mean(arr):
    return float(sum(arr) / len(arr))


def sd(x):
    mu = mean(x)
    temp = round(float(sum([(e - mu) ** 2 for e in x])), 1)
    temp = temp / len(x)
    return round(temp ** 0.5, 1)


n = int(input())
x = [float(e) for e in input().split()]
y = [float(e) for e in input().split()]
mux = round(mean(x), 3)
muy = round(mean(y), 3)
sigx = round(sd(x), 3)
sigy = round(sd(y), 3)
rho = 0
for i in range(n):
    rho += ((x[i] - mux) * (y[i] - muy))
rho /= (n * sigx * sigy)

print(round(rho, 3))

#################

def std(x):
    return (sum([(i-(sum(x))/len(x))**2 for i in x])/len(x))**0.5

N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

X_M = sum(X)/len(X)
Y_M = sum(Y)/len(Y)

X_S = std(X)
Y_S = std(Y)

print(round(sum([(i-X_M)*(j-Y_M) for i, j in zip(X, Y)])/(N*X_S*Y_S), 3))

