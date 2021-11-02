# https://www.hackerrank.com/challenges/s10-mcq-5/problem

"""
First card = 13/52
Second card of the same suit = 12/51 (without replacement)
There are 4 suits, so answer is (13/52) * (12/51) * 4 = 12/51
>>> 12/51
"""

# Initially there is the possibility of 13/52, however after removing a card,
# the probability of the card being of the same suit falls to 12/51
print (12/51)

