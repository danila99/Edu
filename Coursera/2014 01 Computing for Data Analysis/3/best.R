best <- function(state, outcome) {
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

    ## filter by state
    data <- subset(data, State == state)
    death = as.numeric(data[, index])
    
    ## Return hospital name in that state with lowest 30-day death rate
    data$Hospital.Name[death == min(death, na.rm=TRUE) & !is.na(death)]
}