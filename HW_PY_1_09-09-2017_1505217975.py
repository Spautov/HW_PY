from pprint import pprint
import random

def create_matrix(m=1, n=1, init_val=0):
    return [[init_val for _ in range(n)] for _ in range(m)]

def randomize_matrix(mat):
    for l in mat:
        for i in range(len(l)):
            l[i] = random.randint(10, 20)
    return mat

def swap_lines(mat, l1, l2):
    mat[l1], mat[l2] = mat[l2], mat[l1]
    return mat

def swap_columns(mat, col1, col2):
    for arr in mat:
        arr[col1], arr[col2] = arr[col2], arr[col1]


if __name__ == '__main__':
    mat = create_matrix(5,5)
    pprint(mat)
    rand_mat = randomize_matrix(mat)
    pprint('-'*20)
    pprint(mat)
    swap_lines(rand_mat, 1, 4)
    pprint('-'*20)
    pprint(rand_mat)
    swap_columns(rand_mat,0,4)
    pprint('-'*20)
    pprint(rand_mat)

