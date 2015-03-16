#!/usr/bin/env Rscript

corr <- function(directory, threshold = 0) {
	
	data.array <- NULL

	files.in <- list.files(directory, pattern="*.csv", full.names=TRUE)

	for (i in files.in) {
		file.in <- read.csv(i)
		file.id <- file.in[1,4]
	        adj.col <- file.in[2:3]
	        adj.col.na.rm <- na.omit(adj.col)
                nobs <- nrow(adj.col.na.rm)
                #print(paste(file.id, nrow(adj.col.na.rm)))
		if (nobs > threshold){
			x <- adj.col.na.rm[[1]]
			y <- adj.col.na.rm[[2]]
			cr <- cor(x,y)
			data.array <- c(data.array, cr)
		}
		else {
			if (is.null(data.array)) {
			        data.array <- c(0)
			}
		}
	}
		
	print(data.array)
}

#corr('specdata/', 5000)
