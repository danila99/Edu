# version code 988
# Please fill out this stencil and submit using the provided submission script.
import random
from GF2 import one
from vec import Vec
from vecutil import list2vec
import independence

## Problem 1
def randGF2(): 
    return random.randint(0, 1) * one

def rand_vec_GF2(): 
    return list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s, t):
    while(True):
        new_u = rand_vec_GF2()
        ua = a0 * new_u
        ub = b0 * new_u
        if ua == s and ub == t:
            return new_u

                
## Problem 2
# Give each vector as a Vec instance

secret_a0 = a0
secret_b0 = b0
secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: one, 4: 0, 5: one})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: 0, 4: 0, 5: 0})
secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: one, 4: 0, 5: one})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: one, 5: one})
secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: 0, 4: one, 5: 0})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: 0, 4: one, 5: one})
secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: 0, 4: one, 5: one})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: one, 4: one, 5: one})
