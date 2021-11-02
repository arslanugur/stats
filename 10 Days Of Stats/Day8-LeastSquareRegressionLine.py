# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

#Linear Regression 

def mean(arr):
    return float(sum(arr) / len(arr))


def sd(x):
    mu = mean(x)
    temp = round(float(sum([(e - mu) ** 2 for e in x])), 1)
    temp = temp / len(x)
    return round(temp ** 0.5, 1)


n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
mux = round(mean(x), 3)
muy = round(mean(y), 3)
sigx = round(sd(x), 3)
sigy = round(sd(y), 3)
rho = 0
for i in range(n):
    rho += ((x[i] - mux) * (y[i] - muy))
rho /= (n * sigx * sigy)


b = rho * (sigy / sigx)
a = muy - (b * mux)

answer = a + b * 80
print(round(answer, 2))

###########################################################################

def mean(X):
    '''To calculate the mean'''
    return sum(X)/len(X)

def lsr(X, Y):
    '''To calculate the Least Square Regression'''
    B = sum([(X[i] - mean(X)) * (Y[i] - mean(Y)) for i in range(len(X))])/sum([(j - mean(X))**2 for j in X])
    A = mean(Y) - (B*mean(X))
    return A+(B*80)

X = []
Y = []

for i in range(5):
    A, B = list(map(int, input().split()))
    X.append(A)
    Y.append(B)

print(round(lsr(X, Y), 3))

###########################################################################

# import library
import statistics as st

# Set data
n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
mean_x = st.mean(x)
mean_y = st.mean(y)
x_squared = sum([x[i] ** 2 for i in range(5)])
xy = sum([x[i]*y[i] for i in range(5)])

# Set the B and A
b = (n * xy - sum(x) * sum(y)) / (n * x_squared - (sum(x) ** 2))
a = mean_y - b * mean_x

# Gets the result and show on the screen
print (round(a + 80 * b, 3))


