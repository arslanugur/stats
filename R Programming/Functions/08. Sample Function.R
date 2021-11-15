print(sample(1:5))
print(sample(1:5, size=5, replace=FALSE))  # Similar as the previous line since replace is false
print(sample(c(2,5,3,1), size=5, replace=TRUE))
print(sample(1:4, size=10, prob=c(1,5,3,2), replace=TRUE))

# Output:
[1] 5 2 3 4 1
[1] 2 1 5 4 3
[1] 3 5 5 5 5
[1] 2 3 3 3 3 3 2 1 4 2


