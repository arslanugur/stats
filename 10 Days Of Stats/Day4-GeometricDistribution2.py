# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

#1nd way
def geometric(n, p, q):
    answer = q ** (n - 1)
    answer *= p
    return answer


p = [int(e) for e in input().split()]
p = p[0] / p[1]
n = int(input())

probability = 0
for i in range(1, n + 1):
    probability += geometric(i, p, 1 - p)

print(round(probability, 3))

#2nd way
# Set data
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = 0
for i in range(n + 1):
    if i > 0:
        result = result + (q ** (i - 1) * p)

# Show the final result
print(round(result, 3))

#3rd way
def geometric_prob(P, X):
    '''Function to calculate the geometric probability'''
    G = (1-P)**(X-1) * P
    return G

NUMBERATOR, DENOMINATOR = map(float, input().split())
X = int(input())
P = NUMBERATOR/DENOMINATOR
G = 0

for i in range(1, 6): # i = 1, 2, 3, 4, 5
    G += geometric_prob(P, i)

print("%.3f" %G)

