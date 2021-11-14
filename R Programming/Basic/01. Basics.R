a <- 32
A <- a * 2  # R is case sensitive
print(a)
print(A)
cat(A, "\n")  # "64" is concatenated with "\n"
if(A>a)  # true, 64 > 32
{
  cat(A, ">", a, "\n")
}

# Output
[1] 32
[1] 64
64
64 > 32

