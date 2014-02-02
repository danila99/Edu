corr <- function(directory, threshold = 0) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files
    
    ## 'threshold' is a numeric vector of length 1 indicating the
    ## number of completely observed observations (on all
    ## variables) required to compute the correlation between
    ## nitrate and sulfate; the default is 0
    
    ## Return a numeric vector of correlations
    id <- 1:length(list.files(directory))
    c <- complete(directory, id)
    filtered <- c[(c$nobs > threshold),"id"]
    sapply(filtered, cordata, directory) 
}

cordata <- function(index, directory) {
    d <- na.omit(getmonitor(index, directory))
    cor(d$sulfate, d$nitrate)
}