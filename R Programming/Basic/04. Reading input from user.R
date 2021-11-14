# readline() lets the user enter a one-line string at the terminal.
# prompt is printed in front of the user’s input
# as.integer converts the string into integer
readinteger <- function()
{ 
  n <- readline(prompt="Enter an integer: ")
  if(!grepl("^[0-9]+$",n))  # used to handle if user enters string or no value
  {
    return(readinteger())
  }
  
  return(as.integer(n))
}

print(readinteger())


# Output
Enter an integer: 31r132weq
Enter an integer: 5
[1] 5


