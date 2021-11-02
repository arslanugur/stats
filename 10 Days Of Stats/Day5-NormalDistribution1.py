# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problemimport math

# Question: In a certain plant, the time taken to assemble a car is a random
# variable, X, having a normal distribution with a mean of 20 hours and a
# standard deviation of 2 hours. What is the probability that a car can be
# assembled at this plant in:
# 1. Less than 19.5 hours?
# 2. Between 20 and 22 hours?

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
less_period = float(input())
between_period = list(map(float, input().split()))

# Gets the result and show on the screen
print (round(cumulative(mean, std, less_period),3))
print (round(cumulative(mean, std, between_period[1]) - cumulative(mean, std, between_period[0]), 3))

################


MU = 20
SD = 2

def normal_cdf(X, MU, SD):
    '''Function to calculate the Cumulative Distribution Function'''
    return 1/2*(1+math.erf((X-MU)/(SD*math.sqrt(2))))

RESULT_1 = normal_cdf(19.5, MU, SD)
RESULT_2 = normal_cdf(22, MU, SD) - normal_cdf(20, MU, SD)

print(round(RESULT_1, 3))
print(round(RESULT_2, 3))

# .erf() -> https://docs.python.org/3.5/library/math.html#math.erf

##############

import math


avg, sigma = [float(e) for e in input().split()]
cdf = lambda x: 0.5 * (1 + math.erf((x - avg) / (sigma * (2 ** 0.5))))


# def normal(x, avg, sigma):
#     answer = 1 / (sigma * math.sqrt(2 * math.pi))
#     exponent = (x - avg) ** 2
#     exponent /= (2 * (sigma ** 2))
#     answer *= (math.e ** (-exponent))
#     return answer


temp1 = float(input())
print(round(cdf(temp1), 3))

temp1 = [float(e) for e in input().split()]
print(round(cdf(temp1[1]) - cdf(temp1[0]), 3))

