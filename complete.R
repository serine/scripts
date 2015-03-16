#!/usr/bin/env Rscript

complete <- function(directory, id=1:332) {
	all.files <- list.files(directory, pattern="*.csv", full.names=TRUE)
	
	x <- NULL
	y <- NULL

	for (i in id) {
		id.format <- formatC(i, width=3, flag=0)
		file.of.int <- grep(id.format, all.files)
		file.in <- all.files[file.of.int]
	        read.in.file <- read.csv(file.in)
	        file.id <- read.in.file[4]
	        adj.col <- read.in.file[2:3]
	        adj.col.na.rm <- na.omit(adj.col)
                #print(paste(i, nrow(adj.col.na.rm)))
		x <- c(x, i)
		y <- c(y, nrow(adj.col.na.rm))
                #df <- data.frame(x,y)
	}
	df <- data.frame(x, y)
	colnames(df) <- c('id', 'nobs')
	print(df)

}

#complete('specdata', 30:25)
