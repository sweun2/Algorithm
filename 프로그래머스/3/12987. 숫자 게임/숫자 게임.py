def solution(A, B):
    A.sort()
    B.sort()
    n = len(A)
    
    index_A = n - 1
    index_B = n - 1
    
    while index_A >=0 and index_B>=0:
        if A[index_A] < B[index_B]:
            index_A -= 1
            index_B -= 1
        else:
            index_A -=1
    
    return (n - index_B) - 1