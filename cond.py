import numpy as np
#from Matrix.inverse_matrix import inverse
from colors import bcolors
from matrix_utility_fixed import print_matrix


def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row


def condition_number(A):
    # Step 1: Calculate the max norm (infinity norm) of A
    norm_A = norm(A)

    # Step 2: Calculate the inverse of A
    #A_inv = inverse(A)
    A_inv = np.linalg.inv(A)

    # Step 3: Calculate the max norm of the inverse of A
    norm_A_inv = norm(A_inv)

    # Step 4: Compute the condition number
    cond = norm_A * norm_A_inv

    print(bcolors.OKBLUE, "A:", bcolors.ENDC)
    print_matrix(A)

    print(bcolors.OKBLUE, "inverse of A:", bcolors.ENDC)
    print_matrix(A_inv)

    print(bcolors.OKBLUE, "Max Norm of A:", bcolors.ENDC, norm_A, "\n")

    print(bcolors.OKBLUE, "max norm of the inverse of A:", bcolors.ENDC, norm_A_inv)

    #print_matrix(np.dot(A_inv,A))

    return cond


if __name__ == '__main__':
    print("the git link:https://github.com/haikarmi/condition-of-linear-equations_hai.git\n group:Almog Babila-209477678, Hai karmi-207265687, Yagel Batito-318271863, Meril Hasid-324569714\n date :19/02/24 \n student: hai karmi id: 207265687")

    A = np.array([[2,1,0],
                  [3,-1,0],
                  [1,4,-2]])
    cond = condition_number(A)

    print(bcolors.OKGREEN, "\n condition number: ", cond, bcolors.ENDC)

    print("condition number according numpi: ",np.linalg.cond(A,np.inf))


