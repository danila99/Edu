count <- function(cause = NULL) {
    ## Check that "cause" is non-NULL; else throw error
    if (is.na(cause))
        stop("cause is empty")    
    
    ## Check that specific "cause" is allowed; else throw error
    validCauses <- c("asphyxiation", "blunt force", "other", "shooting", "stabbing", "unknown")
    if (!any(validCauses == cause))
        stop("invalid cause")
    
    ## Read "homicides.txt" data file
    data <- tolower(readLines("homicides.txt"))
    data <- sapply(data, function(d) {substr(d, regexpr("cause:", d)[1], stop=nchar(d))} )
    data <- sapply(data, function(d) {substr(d, 1, stop=regexpr("<", d)[1] - 1)} )
    
    ## Extract causes of death
    ## Return integer containing count of homicides for that cause
    length(grep(cause, data))
}