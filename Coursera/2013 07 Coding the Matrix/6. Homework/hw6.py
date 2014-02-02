# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
from vec import Vec
from vecutil import zero_vec
import echelon


## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
                  [0,0,0,1],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3]])
        True        
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
        >>> is_echelon([[2,1,0],[-4,0,0],[0,0,1]])
        False        
    '''
    pos = -1
    for l in A:
        curr_pos = next((x for x in range(len(l)) if l[x] != 0), len(l))
        if (pos == len(l)):
            if (curr_pos != pos):
                return False
        else:
            if (pos != -1 and curr_pos <= pos):
                return False
            else:
                pos = curr_pos
    return True



## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    >>> U_rows = [Vec(D, {'A':one, 'C':one, 'D':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one, 'E':one}), Vec(D,{'E':one})] 
    >>> b_list = [one,0,one,one]
    '''

    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(rowlist))):
        row = rowlist[j]
        c = next((label for label in label_list if row[label] == one), None)
        if(c == None):
            continue; # if there are no nonzero entries in that row, the iteration should do nothing
            
        x[c] = (b[j] - x*row)/row[c]
    return x



## Problem 6
def solve(A, b):
    from matutil import mat2rowdict
    M = echelon.transformation(A)
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    rowlist = [U_rows_dict[i] for i in U_rows_dict]
    print(rowlist)
    print(col_label_list)
    print(M*b)
    return echelon_solve(rowlist,col_label_list, M*b)
    
rowlist = [Vec({'A', 'C', 'B', 'D'},{'A': one, 'C': 0, 'B': one, 'D': one}), Vec({'A', 'C', 'B', 'D'},{'A': 0, 'C': 0, 'B': one, 'D': 0}), Vec({'A', 'C', 'B', 'D'},{'A': 0, 'C': one, 'B': 0, 'D': 0}), Vec({'A', 'C', 'B', 'D'},{'A': 0, 'C': 0, 'B': 0, 'D': one})]  # Provide as a list of Vec instances
label_list = ['A', 'B', 'C', 'D'] # Provide as a list
b = [one, one, 0, 0]         # Provide as a list



## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
closest_vector_1 = [1.6, 3.2]
closest_vector_2 = [0, 1, 0]
closest_vector_3 = [3, 2, 1, -4]



## Problem 10
# Write each vector as a list


project_onto_1 = [2, 0]
projection_orthogonal_1 = [0, 1]

project_onto_2 = [-0.16666666666666666, -0.3333333333333333, 0.16666666666666666]
projection_orthogonal_2 = [1.1666666666666667, 1.3333333333333333, 3.8333333333333335]

project_onto_3 = [1, 1, 4]
projection_orthogonal_3 = [0,0,0]



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1

