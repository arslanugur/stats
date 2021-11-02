# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem

# Import library
from sklearn import linear_model

# Set data
m, n = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(n):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < m:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

# Get the parameters X for discovery the Y
q = int(input())
new_X = []
for i in range(q):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

# Gets the result and show on the screen
result = model.predict(new_X)
for i in range(len(result)):
    print(round(result[i],2))
    
##############################################################################

import numpy
from numpy.linalg import inv

m, n = [int(e) for e in input().split()]
X = []
Y = []
for i in range(n):
    temp = [1]
    temp1 = [float(e) for e in input().split()]
    X.append(temp + temp1[:m])
    Y.append(temp1[m])
X = numpy.array(X)
Y = numpy.reshape(numpy.array(Y), (n, 1))

B = inv(numpy.matmul(X.transpose(), X))
B = numpy.matmul(B, X.transpose())
B = numpy.matmul(B, Y)

q = int(input())
X1 = []
for i in range(q):
    X1.append([1] + [float(e) for e in input().split()])

X1 = numpy.array(X1)
answer = numpy.matmul(X1, B)

for e in answer:
    print(round(e[0], 2))
    
##############################################################################

from sklearn import linear_model

M, N = list(map(int, input().strip().split()))
X = [0]*N
Y = [0]*N

for i in range(N):
    inp = list(map(float, input().strip().split()))
    X[i] = inp[:-1]
    Y[i] = inp[-1]

LM = linear_model.LinearRegression()
LM.fit(X, Y)
A = LM.intercept_
B = LM.coef_

Q = int(input())

for i in range(Q):
    f = list(map(float, input().strip().split()))
    Y = A + sum([B[j] * f[j] for j in range(M)])
    print(round(Y, 2))
    
    
