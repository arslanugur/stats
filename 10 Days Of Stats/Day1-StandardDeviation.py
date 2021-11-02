#https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# Import library
import math

# Define functionts
def mean(data):
    return sum(data) / len(data)

def stddev(data, size):
    sum = 0
    for i in range(size):
        sum = sum + (data[i] - mean(data)) ** 2
    return math.sqrt(sum / size)

# Set data
size = int(input())
numbers = list(map(int, input().split()))

# Get standard deviation
print(round(stddev(numbers, size), 1))

################# SECOND WAY #######################

def mean(arr):
    return float(sum(arr) / len(arr))


def sd(x):
    mu = mean(x)
    temp = round(float(sum([(e - mu) ** 2 for e in x])), 1)
    temp = temp / len(x)
    return round(temp ** 0.5, 1)


n = int(input())
x = [int(e) for e in input().split()]
print(sd(x))

