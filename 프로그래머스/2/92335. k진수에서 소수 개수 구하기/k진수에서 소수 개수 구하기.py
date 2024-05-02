def solution(n, k):
    answer = 0
    new_n=change_num(n,k)
    nums = new_n.split('0')
    for num in nums:
        if num and is_prime_num(int(num)):
            answer += 1 
    return answer

def is_prime_num(n):
    if n <= 1:
        return False
    for i in range(2,int(n**(0.5)+1)):
        if n%i == 0:
            return False
    return True

def change_num(n,k):
    tmp = ''
    tmp_n = n
    while tmp_n >= 1:
        div,mod = divmod(tmp_n,k)
        tmp += str(mod) 
        tmp_n = div
    tmp=tmp[::-1]
    return tmp