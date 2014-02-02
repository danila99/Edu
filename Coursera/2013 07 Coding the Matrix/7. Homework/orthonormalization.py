from orthogonalization import orthogonalize
from orthogonalization import aug_orthogonalize
import matutil
from math import sqrt
from vec import Vec

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    l = orthogonalize(L)
    norms = [sqrt(x*x) for x in l]
    return [l/n for n,l in zip(norms, l)]
    
def adjust(v, multipliers):
    assert len(v.f.keys()) == len(multipliers)
    
    new_v = Vec(v.D, v.f)
    for i in range(len(v.f.keys())):
        new_v[i] *= multipliers[i]

    return new_v

def mat2list(M):
    return list(matutil.mat2coldict(M).values())
    
def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    Q, R = aug_orthogonalize(L)

    Q_mat = matutil.coldict2mat(Q)
    Q_norm_mat = matutil.coldict2mat(orthonormalize(Q))
    R_mat = matutil.coldict2mat(R)
    R_norm_mat = (Q_mat.transpose() * Q_norm_mat) * R_mat
    
    return mat2list(Q_norm_mat), mat2list(R_norm_mat)
    
