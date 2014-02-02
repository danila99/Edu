rankall <- function(outcome, num = "best") {
    ## Read outcome data
    data <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
    
    ## Check that state and outcome are valid
    if (!any(data$State == state))
        stop("invalid state")
    
    ## For each state, find the hospital of the given rank
    states <- unique(data$State)
    states <- states[order(states)]
    
    ## Return a data frame with the hospital names and the
    ## (abbreviated) state name
    data.frame("hospital"=sapply(states, rankhospital, outcome, num), "state"=states)
}