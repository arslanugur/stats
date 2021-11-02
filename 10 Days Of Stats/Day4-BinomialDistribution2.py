# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

# 1st way
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
p = (values[0] / 100)
n = int(values[1])

# First rule: No more than 2 rejects
no_more_than_2_rejects = 0
for i in range(n):
    if i < 3:
        no_more_than_2_rejects = no_more_than_2_rejects + binomial(i, n, p)
print(round(no_more_than_2_rejects, 3))

# Second rule: At least 2 rejects
at_least_2_rejects = 0
for i in range(n):
    if i > 1:
        at_least_2_rejects = at_least_2_rejects + binomial(i, n, p)
print(round(at_least_2_rejects, 3))

#2nd way
import math

P = 0.12
ANS_1 = 0

for i in range(0, 3):
    ANS_1 += math.factorial(10)/math.factorial(i)/math.factorial(10-i) * P**i * (1-P)**(10-i)
    if i == 1:
        ANS_2 = 1 - ANS_1

print(round(ANS_1, 3))
print(round(ANS_2, 3))

#3rd way
from math import factorial

def c(n, x):
    return (factorial(n) / (factorial(x) * factorial(n - x)))

def binomial(n, x, p, q):
    answer = c(n, x)
    answer *= (p ** x)
    answer *= (q ** (n - x))
    return answer

p, n = [int(e) for e in input().split()]
p = p / 100
probability = 0

for i in range(0, 3):
    probability += binomial(10, i, p, 1 - p)

print(round(probability, 3))
probability = 0
for i in range(2, 11):
    probability += binomial(10, i, p, 1 - p)

print(round(probability, 3))

