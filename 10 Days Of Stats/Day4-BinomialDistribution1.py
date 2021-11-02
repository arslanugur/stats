# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

#1st way
# Define functions
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

def binomial(x, n, p):
    f = factorial(n) / (factorial(n - x) * factorial(x))
    return (f * p**x * (1.0 - p)**(n-x))

# Set data
values = list(map(float, input().split()))
p = values[0] / (values[0] + values[1])
n = 6

# Get binomial result
result = binomial(3,n,p) + binomial(4,n,p) + binomial(5,n,p) + binomial(6,n,p)
print(round(result, 3))

#2nd way
def factorial(N):
    '''Function to calculate N factorial'''
    if N == 0:
        return 1
    else:
        return N * factorial(N - 1)

def combination(N, X):
    '''Function to calculate the combination of N and X'''
    result = factorial(N) / (factorial(N - X) * factorial(X))
    return result

def binomial(X, N, P):
    '''Function to determine the binomial of X, N, and P'''
    Q = 1 - P
    result = combination(N, X) * (P**X) * (Q**(N - X))
    return result

if __name__ == '__main__':
    L, R = list(map(float, input().split()))
    ODDS = L / R
    TOTAL = list()
    for i in range(3, 7):
        TOTAL.append(binomial(i, 6, ODDS / (1 + ODDS)))
    print(round(sum(TOTAL), 3))
    
 #3rd way
from math import factorial

def c(n, x):
    return (factorial(n) / (factorial(x) * factorial(n - x)))

def binomial(n, x, p, q):
    answer = c(n, x)
    answer *= (p ** x)
    answer *= (q ** (n - x))
    return answer

s = [float(e) for e in input().split()]
p = s[0] / (s[0] + s[1])
q = s[1] / (s[0] + s[1])

prob = 0
for i in range(3, 7):
    prob += binomial(6, i, p, q)

print(round(prob, 3))

