# Question: A large elevator can transport a maximum of 9800 pounds. Suppose a
# load of cargo containing 49 boxes must be transported via the elevator.
# The box weight of this type of cargo follows a distribution with a mean
# of u = 205 pounds and a standard deviation of a = 15 pounds. Based on this
# information, what is the probability that all 49 boxes can be safely loaded
# into the freight elevator and transported?

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

new_mean = mean * n
new_std = math.sqrt(n) * std

# Gets the result and show on the screen
print (round(cumulative(new_mean, new_std, max_weight),4))

########
import math

def cdf(mean, sigma, x):
    res = (math.erf((x - mean) / (variance * math.sqrt(2))) + 1) / 2
    res = round(res, 4)
    return res


max_n = 9800
mean = 205
variance = 15
n = 49

mean = mean * n
variance = variance * math.sqrt(n)

print(round(cdf(mean, variance, max_n), 4))

########

import math

H = int(input())
B = int(input())
C = int(input())
INPUT = math.sqrt(B) * int(input())

print(round(0.5 * (1 + math.erf((H - (B * C)) / (INPUT * math.sqrt(2)))), 4))

