agecount <- function(age = NULL) {
    ## Check that "age" is non-NULL; else throw error
    if (is.na(age))
        stop("age is empty")  
    
    ## Read "homicides.txt" data file
    data <- tolower(readLines("homicides.txt"))
    data <- sapply(data, extract)
    
    ## Return integer containing count of homicides for that age
    length(grep(sprintf(" %d ", age), data))
}

extract <- function(d) {
    r <- regexpr(" \\d+ years old", d)
    substr(d, r[1], r[1] + attr(r, "match.length") - 1)
}