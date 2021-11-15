tbl <- read.table(file.choose(),header=TRUE,sep=",")
population <- tbl["POPESTIMATE2009"]
print(summary(population[-1:-5,]))

# Output
    Min.  1st Qu.   Median     Mean     3rd Qu.   Max. 
  544300  1734000  4141000     5980000  6613000   36960000

