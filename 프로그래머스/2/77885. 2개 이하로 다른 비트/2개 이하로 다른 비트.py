def solution(numbers):
    answer = []
    for num in numbers:
        bnum = list('0' + bin(num)[2:])
        idx = ''.join(bnum).rfind('0')
        bnum[idx] = '1'
        if num % 2 == 1:
            bnum[idx+1] = '0'
        answer.append(int(''.join(bnum),2))
        
                
    return answer