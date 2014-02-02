rankhospital <- function(state, outcome, num = "best") {
    index = 11
    validOutcomes <- c("heart attack", "heart failure", "pneumonia")
    if (!any(validOutcomes == outcome))
        stop("invalid outcome")
    else if (outcome == "heart failure")
        index = 17
    else if (outcome == "pneumonia")
        index = 23
    
    ## Read outcome data
    data <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
    
    if (!any(data$State == state))
        stop("invalid state")
    
    
    data <- subset(data, State == state) # filter by state
    data[, index] <- as.numeric(data[, index]) # convert rates to numeric
    data <- data[complete.cases(data[, index]), ] # removing NAs
    data <- data[ order(data[,index], data$Hospital.Name), ] # sort
    
    ## Return hospital name in that state with the given rank 30-day death rate
    if(is.numeric(num) & num <= nrow(data))
        data$Hospital.Name[num]
    else if (num == "best")
        data$Hospital.Name[1]
    else if (num == "worst")
        data$Hospital.Name[nrow(data)]
    else
        NA
}