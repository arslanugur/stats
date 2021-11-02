# https://www.hackerrank.com/challenges/s10-mcq-3/problem

import itertools
from fractions import Fraction
from collections import Counter

# Let r = 1 and black = 0
# Bag X
X = list(Counter({1:4, 0:3}).elements())

# Bag Y 
Y = list(Counter({1:5, 0:4}).elements())

# Bag z
Z = list(Counter({1:4, 0:4}).elements())

# Sample space / total number of outcomes
TOTAL_SAMPLES = list(itertools.product(X, Y, Z))

# Total number of outcomes
TOTAL_SAMPLES_SIZE = len(TOTAL_SAMPLES)

# Total number of favourable outcomes
FAVOURABLE_OUTCOMES_SIZE = sum([sum(i) == 2 for i in list(itertools.product(X, Y, Z))])

# Probability as a fraction
print(Fraction(FAVOURABLE_OUTCOMES_SIZE,TOTAL_SAMPLES_SIZE))

# >>> 17/42

############# SECOND WAY ###############

# Set data
x = {"Red":4/7, "Black":3/7}
y = {"Red":5/9, "Black":4/9}
z = {"Red":4/8, "Black":4/8}

# Get possibilities
first_possibility = x["Red"] * y["Red"] * z["Black"]
second_possibility = x["Red"] * y["Black"] * z["Red"]
third_possibility = x["Black"] * y["Red"] * z["Red"]

# Get probability
print(first_possibility + second_possibility + third_possibility)

