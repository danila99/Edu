complete <- function(directory, id) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files
    
    ## 'id' is an integer vector indicating the monitor ID numbers
    ## to be used
    
    ## Return a data frame of the form:
    ## id nobs
    ## 1  117
    ## 2  1041
    ## ...
    ## where 'id' is the monitor ID number and 'nobs' is the
    ## number of complete cases

    d <- lapply(id, getmonitor, directory)
    dcomplete <- sapply(d,  function(df) length(na.omit(df)[,1]))
    data.frame("id"=id, "nobs"=dcomplete)
}
