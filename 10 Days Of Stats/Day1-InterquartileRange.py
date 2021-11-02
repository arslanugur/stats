#https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Define functions
def median(size, values):
    if size % 2 == 0:
        median = (values[int(size/2)-1] + values[int(size/2)]) / 2
    else:
        median = float(values[int(size/2)])
    return median

# Set the data
size = int(input())
elements = list(map(int, input().split()))
frequencies = list(map(int, input().split()))

new_data = []
for i in range(len(elements)):
    for j in range(frequencies[i]):
        new_data.append(elements[i])
new_data = sorted(new_data)

# Verify that the total data is even or odd
size = int(len(new_data))
if size % 2 == 0:
    data_low = new_data[0:int(size/2)]
    data_high = new_data[int(size/2):size]
else:
    data_low = new_data[0:int(size/2)]
    data_high = new_data[int(size/2)+1:size]

# Get the final result and print on the screen
low = median(len(data_low), data_low)
high = median(len(data_high), data_high)
print(high - low)
  
  
################ SECOND WAY ###############

def median(arr):
    if len(arr) % 2 == 0:
        temp = arr[(len(arr) // 2) - 1]
        return (temp + arr[(len(arr) // 2)]) / 2
    return arr[(len(arr) // 2)]


n = int(input())
temp = [int(e) for e in input().split()]
f = [int(e) for e in input().split()]
x = []
for i in range(n):
    x += ([temp[i]] * f[i])
x = sorted(x)
n = sum(f)
q = round((median(x[:(n // 2)])), 1)
if n % 2 == 0:
    q -= round(median(x[(n // 2):]), 1)
else:
    global q3
    q -= round(median(x[(n // 2) + 1:]), 1)
print(round(float(-q), 1))def median(arr):
    if len(arr) % 2 == 0:
        temp = arr[(len(arr) // 2) - 1]
        return (temp + arr[(len(arr) // 2)]) / 2
    return arr[(len(arr) // 2)]


n = int(input())
temp = [int(e) for e in input().split()]
f = [int(e) for e in input().split()]
x = []
for i in range(n):
    x += ([temp[i]] * f[i])
x = sorted(x)
n = sum(f)
q = round((median(x[:(n // 2)])), 1)
if n % 2 == 0:
    q -= round(median(x[(n // 2):]), 1)
else:
    global q3
    q -= round(median(x[(n // 2) + 1:]), 1)
print(round(float(-q), 1))

