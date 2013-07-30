#!/usr/bin/env Rscript

stdin <- file('stdin', open='r')
while ( length(line <- readLines(stdin, n=1, warn=FALSE)) > 0 ) {
    line <- gsub('(^\\s+|\\s+$)', '', line)
    keys <- unlist(strsplit(line, split='\\s+'))
    value <- 1
    lapply(keys, FUN=function(key,value) cat(paste(key,'\t',value,'\n',sep='')), value=value)
}
close(stdin)
