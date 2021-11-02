# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

n = [float(e) for e in input().split()]
print(round((160 + 40 * (n[0] + n[0] ** 2)), 3))
print(round((128 + 40 * (n[1] + n[1] ** 2)), 3))

###############

AVERAGE_X, AVERAGE_Y = [float(num) for num in input().split(" ")]

# Cost
COST_X = 160 + 40*(AVERAGE_X + AVERAGE_X**2)
COST_Y = 128 + 40*(AVERAGE_Y + AVERAGE_Y**2)

print(round(COST_X, 3))
print(round(COST_Y, 3))

