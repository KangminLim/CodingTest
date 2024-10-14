def solution(n):
    answer = 0
    n_b = bin(n)[2:]
    n_1 = n_b.count('1')
    i = n
    while True:
        i += 1 
        tmp_b = bin(i)[2:]
        tmp_1 = tmp_b.count('1')
        if n_1 == tmp_1:
            break
    return i