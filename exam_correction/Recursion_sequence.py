def recursive_sequence(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return recursive_sequence(3*n)+recursive_sequence(2*n+1)
recursive_sequence(10)