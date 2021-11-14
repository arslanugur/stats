# General syntax: while(condition){code}
# Sys.sleep is used to suspend the operation for a given amount of time

countdown <- function(from)
{
  print(from)
  while(from!=0)
  {
    Sys.sleep(1)
    from <- from - 1
    print(from)
  }
}

countdown(5)

# Output:
[1] 5
[1] 4
[1] 3
[1] 2
[1] 1
[1] 0


