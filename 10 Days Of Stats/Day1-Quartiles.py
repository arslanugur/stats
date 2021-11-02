#https://www.hackerrank.com/challenges/s10-quartiles/problem

def median(arr):
    if len(arr) % 2 == 0:
        temp = arr[(len(arr) // 2) - 1]
        return (temp + arr[(len(arr) // 2)]) / 2
    return arr[(len(arr) // 2)]


n = int(input())
x = [int(e) for e in input().split()]
x = sorted(x)
print(int(median(x[:(n // 2)])))
print(int(median(x)))
if n % 2 == 0:
    print(int(median(x[(n // 2):])))
else:
    print(int(median(x[(n // 2) + 1:])))
    
   
  
############# SECOND WAY ################  
  # Define functions
def median(size, values):
    if size % 2 == 0:
        median = (values[int(size/2)-1] + values[int(size/2)]) / 2
    else:
        median = values[int(size/2)]
    return int(median)

# Set the data
size = int(input())
numbers = sorted(list(map(int, input().split())))

# Verify that the total data is even or odd
if size % 2 == 0:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2):size]
else:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2)+1:size]

# Get the final result and print on the screen
print (median(len(data_low), data_low))
print (median(size, numbers))
print (median(len(data_high), data_high))

