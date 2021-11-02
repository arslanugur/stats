# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

# Question: The final grades for a Physics exam taken by a large group of
# students have a mean of mi = 70 and a standard deviation of sigma = 10.
# If we can approximate the distribution of these grades by a normal
# distribution, what percentage of the students:
# 1. Scored higher than 80 (i.e., have a grade > 80)?
# 2. Passed the test (i.e., have a grade >= 60)?
# 3. Failed the test (i.e., have a grade < 60)?

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
val_first_question = float(input())
val_sec_third_question = float(input())

# Gets the result and show on the screen
print (round(100 - (cumulative(mean, std, val_first_question) * 100), 2))
print (round(100 - (cumulative(mean, std, val_sec_third_question) * 100), 2))
print (round(cumulative(mean, std, val_sec_third_question) * 100, 2))

#################

import math

MU, SD = list(map(float, input().rstrip().split()))
X_1 = float(input())
X_2 = float(input())

def normal_distribution(X, MU, SD):
    '''Function to calculate the normal distribution'''
    return 1/2*(1+math.erf((X-MU)/(SD*math.sqrt(2))))

# grade >80
print(round((1-normal_distribution(X_1, MU, SD))*100, 2))

# grade >= 60
print(round((1-normal_distribution(X_2, MU, SD))*100, 2))

# grade <60
print(round((normal_distribution(X_2, MU, SD))*100, 2))

##############

import math

avg, sigma = [70, 10]

def cdf(u, d, x):
    return (math.erf((x - u) / (d * math.sqrt(2))) + 1) / 2
# cdf = lambda x: 0.5 * (1 + math.erf((x - avg) / (sigma * (2 ** 0.5))))

print(100 * round((cdf(avg, sigma, 100) - cdf(avg, sigma, 80)), 4))
print(100 * round((cdf(avg, sigma, 100) - cdf(avg, sigma, 60)), 4))
print(100 * round((cdf(avg, sigma, 60) - cdf(avg, sigma, 0)), 4))

