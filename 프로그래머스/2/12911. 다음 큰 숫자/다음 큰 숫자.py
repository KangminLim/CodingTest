def solution(n):
    answer = 0
    n_one = bin(n).count('1')
    temp = n
    while True:
        temp += 1
        t_one = bin(temp).count('1')
        if n_one == t_one:
            return temp
 