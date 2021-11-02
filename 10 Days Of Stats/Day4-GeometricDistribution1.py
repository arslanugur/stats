# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

#1st way
# Set data
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = q ** (n - 1) * p
print(round(result, 3))

#2nd way
def geometric(n, p, q):
    answer = q ** (n - 1)
    answer *= p
    return answer


p = [int(e) for e in input().split()]
p = p[0] / p[1]
n = int(input())
print(round(geometric(n, p, 1 - p), 3))

#3rd way
A, B = map(int, input().strip().split(' '))
C = int(input())

P = float(A/B)

RES = (1-P) ** (C-1) * P

print(round(RES, 3))

