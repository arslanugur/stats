# Note: the following code will plot the color of the bar chart according to the value in the database

testscores <- c(96, 71, 85, 92, 82, 78, 72, 81, 68, 61, 78, 86, 90)
testcolors <- ifelse(testscores >= 80, "blue", "red")
barplot(testscores, col=testcolors)

# Output: <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoMAAAKCCAIAAAF...

