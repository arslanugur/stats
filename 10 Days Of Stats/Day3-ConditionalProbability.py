# https://www.hackerrank.com/challenges/s10-mcq-4/problem

#TASK
#Suppose a family has 2 children, one of which is a boy.
#What is the probability that both children are boys?

#first children is boy and second is boy
#first children is boy and second is girl
#first children is girl and second is girl
#It is three different possibilities
# >>> 1/3

import itertools
from fractions import Fraction

# Sample space
SAMPLE_SPACE = list(itertools.product(("b", "g"), ("b", "g")))

# Event b at least one boy [A]
EVENT_B = []
for i in SAMPLE_SPACE:
    if i[0] == "b" or i[1] == "g":
        EVENT_B.append(i)

# Event 2b two boys [B]
EVENT_2B = []
for i in SAMPLE_SPACE:
    if i[0] == "b" and i[1] == "b":
        EVENT_2B.append(i)

# Conditional probability -> p(2b | b) = p (b | 2b) * p (2b) / p(b)
# Where -> p (b) = p(b|2b)* p(b) + p(b|2b')*p(b')

# For p(b|2b)
PB_2B = []
for i in EVENT_2B:
    PB_2B.append(i)

PROB_PB_2B = Fraction(len(PB_2B), len(EVENT_2B))

# For p(2b)
PROB_2B = Fraction(len(EVENT_2B), len(SAMPLE_SPACE))

# For p(b)
PROB_B = Fraction(len(EVENT_B), len(SAMPLE_SPACE))

# Solving for p(2b | b) = p (b | 2b) * p (2b) / p(b)
print(PROB_PB_2B*PROB_2B/PROB_B)

