#!/usr/bin/env Rscript

pollutantmean <- function(directory, pollutant, id=1:332) {
	all.files <- list.files(directory, pattern="*.csv", full.names=TRUE)

	data.array <- NULL

	for (i in id) {
		id.format <- formatC(i, width=3, flag=0)
		files.of.int <- grepl(id.format, all.files)
		file.in <- all.files[files.of.int]
	        read.in.file <- read.csv(file.in)
	        data <- read.in.file[pollutant]
	        data.na.rm <- na.omit(data)
		col.data <- data.na.rm[,1]
		data.array <- c(data.array, col.data)
	}
	data.mean <- mean(data.array)
	print(mean(data.array))
}

#pollutantmean('~/uni_work/specdata', 'sulfate', 1:10)
