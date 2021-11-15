tbl <- read.table(file.choose(),header=TRUE,sep=',')
population <- tbl[c("NAME","POPESTIMATE2009","NPOPCHG_2009")]
smallest.state.pop <- min(population$POPESTIMATE2009)
print(population[population$POPESTIMATE2009==smallest.state.pop,])

# Output:
NAME POPESTIMATE2009 NPOPCHG_2009
56 Wyoming          544270        11289

