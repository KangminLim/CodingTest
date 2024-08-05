def divisor(num):
    if num == 1:
        return 0
    else:
        mdiv = 1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                if (num//i) <= 10000000:
                    return num//i
                mdiv = i
    return mdiv
def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        answer.append(divisor(i))
    return answer
        