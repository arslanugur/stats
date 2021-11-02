# https://www.hackerrank.com/challenges/s10-mcq-7/problem

#The Regression Line of y on x is 3x + 4y + 8 = 0
#The Regression Line of x on y is 4x + 3y + 7 = 0
#What's the value of Pearson Correlation Coefficient?

#regression X:

3x + 4y + 8 = 0
- 4y = 3x + 8
-y = 3x/4 + 8/4
-y = 3x/4 + 4 #(reverse signal)
y = -3x/4 - 4
bx = -3/4

#regression Y:
4x + 3y + 7 = 0
-4y = 3y + 7
-x = 3x/4 + 7/4 #(reverse signal)
y =  -3x/4 - 7/4
by = -3/4
r² = bx * by
r² = -3/4 * -3/4
r² = 9/16
r +/- 3/4
if bx = by
  r = -3/4

print ("Result is: {}".format("-3/4"))

###########################################################################

#Rewriting both lines in the form of y = mx + c
y = (-3/4) * x - 2
x = (-3/4) * y + (-7 / 4)

c1 = -3 / 4
c2 = -3 / 4

#Let x_std be the standard deviation of x, and let y_std be the standard deviation of y

p = c1(x_std / y_std)
p = c2(y_std / x_std)

#Multiplying both questions:
p^2 = c1 * c2
p^2 = (-3 / 4) * (-3 / 4)
p^2 = 9 / 16
p = +/-(3 / 4)

Since x_std and y_std have to be positive. So p shares the same sign as c1 or c2. Thus, -3/4

>>> -3/4

