#utility functions

readinteger <- function()
{ 
  n <- readline(prompt="Enter an integer: ")
  if(!grepl("^[0-9]+$",n))
  {
    return(readinteger())
  }
  return(as.integer(n))
}

# real program start here
  
num <- round(runif(1) * 10, digits = 0)
guess <- -1

cat("Guess a number between 0 and 10.\n")

while(guess != num)
{ 
  guess <- readinteger()
  if (guess == num)
  {
    cat("Congratulations,", num, "is right.\n")
  }
  else if (guess < num)
  {
    cat("It's bigger!\n")
  }
  else if(guess > num)
  {
    cat("It's smaller!\n")
  }
}

# Output:
Enter an integer: 4
It's smaller!
Enter an integer: 3
It's smaller!
Enter an integer: 2
Congratulations, 2 is right.


