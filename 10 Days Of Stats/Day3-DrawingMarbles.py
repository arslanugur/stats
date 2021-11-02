# A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from
# the bag, at random, without replacement. If the first marble is red, what is
# the probability that the second marble is blue?

# First marble is red, left six marbles in the bag, whose the four are blue,
# then 4/6 or 2/3

from itertools import permutations
from fractions import Fraction

# 1 for Red Marbles
# 0 for Blue Marbles
RED_MARBLES = [1, 1, 1]
BLUE_MARBLES = [0, 0, 0, 0]

# All combinations, excluded first blue
FIRST_DRAW = list(filter(lambda m: m[0] == 1, permutations(RED_MARBLES + BLUE_MARBLES, 2)))

# All combinations with second blue
MARBLES_REMAINING = list(filter(lambda m: m[1] == 0, FIRST_DRAW))

# Result is 2/3
print(Fraction(len(MARBLES_REMAINING), len(FIRST_DRAW)))

