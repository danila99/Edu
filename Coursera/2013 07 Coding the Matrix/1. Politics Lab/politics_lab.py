voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    d = {}
    for str in voting_data:
        str_arr = str.split()
        d[str_arr[0]] = [int(i) for i in str_arr[3:]]
    
    return d
    
def create_voting_dict_filtered(party):
    party = party.upper()
    assert party in ['R', 'D']
    d = {}
    for str in voting_data:
        str_arr = str.split()
        if str_arr[1] == party:
            d[str_arr[0]] = [int(i) for i in str_arr[3:]]
    
    return d
    
## Task 2

def dict_compare(d1, d2):
    assert len(d1) == len(d2)
    return sum(d1[i] * d2[i] for i in range(len(d1)))

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    v_a = voting_dict[sen_a]
    v_b = voting_dict[sen_b]
    assert len(v_a) == len(v_b)

    return dict_compare(v_a, v_b)


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    assert len(voting_dict) > 0
    
    d = {sen_b:policy_compare(sen, sen_b, voting_dict) for sen_b in voting_dict.keys() if sen != sen_b}
    max = None
    sen_name = ''
    
    for k in d.keys():
        if max == None or d[k] > max:
            max = d[k]
            sen_name = k
            
    return sen_name
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    assert len(voting_dict) > 0
    
    d = {sen_b:policy_compare(sen, sen_b, voting_dict) for sen_b in voting_dict.keys() if sen != sen_b}
    min = None
    sen_name = ''
    
    for k in d.keys():
        if min == None or d[k] < min:
            min = d[k]
            sen_name = k
            
    return sen_name
    
    

## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    
    numbers = [policy_compare(sen, s, voting_dict) for s in sen_set]
    return sum(numbers) / len(numbers)

    
def find_average_d(voting_dict):
    dem = create_voting_dict_filtered('d')
    d = {sen:find_average_similarity(sen, dem, voting_dict) for sen in dem}
    
    max = None
    sen_name = ''
    
    for k in d.keys():
        if max == None or d[k] > max:
            max = d[k]
            sen_name = k

    return sen_name
    
most_average_Democrat = find_average_d(create_voting_dict())

# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    len_start = len(sen_set)
    average = voting_dict[sen_set.pop()]
    while len(sen_set) > 0:
        curr = voting_dict[sen_set.pop()]
        average = [average[i] + curr[i] for i in range(len(average))]
    
    average = [average[i] / len_start for i in range(len(average))]
    return average

average_Democrat_record = [-0.16279069767441862, -0.23255813953488372, 1.0, 0.8372093023255814, 0.9767441860465116, -0.13953488372093023, -0.9534883720930233, 0.813953488372093, 0.9767441860465116, 0.9767441860465116, 0.9069767441860465, 0.7674418604651163, 0.6744186046511628, 0.9767441860465116, -0.5116279069767442, 0.9302325581395349, 0.9534883720930233, 0.9767441860465116, -0.3953488372093023, 0.9767441860465116, 1.0, 1.0, 1.0, 0.9534883720930233, -0.4883720930232558, 1.0, -0.32558139534883723, -0.06976744186046512, 0.9767441860465116, 0.8604651162790697, 0.9767441860465116, 0.9767441860465116, 1.0, 1.0, 0.9767441860465116, -0.3488372093023256, 0.9767441860465116, -0.4883720930232558, 0.23255813953488372, 0.8837209302325582, 0.4418604651162791, 0.9069767441860465, -0.9069767441860465, 1.0, 0.9069767441860465, -0.3023255813953488]


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    d = voting_dict
    rivals = ()
    lowest_similarity = None
    for sen in d.keys():
        rival_candidate = least_similar(sen, d)
        similarity = policy_compare(sen, rival_candidate, d)
        if lowest_similarity == None or lowest_similarity > similarity:
            lowest_similarity = similarity
            rivals = (sen, rival_candidate)

    return rivals
