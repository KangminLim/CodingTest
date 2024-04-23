def getArea(arr,i):
    return (arr[i] + arr[i+1]) / 2

def parseRange(arr,st,en):
    if en<=0:
        en = len(arr)-1+en
    return (st,en)


def solution(k, ranges):
    answer = []
    lst = [k]
    # collatz 1로 만들기
    while k > 1:
        if k%2 ==0:
            k//=2
        else:
            k = k*3+1
        lst.append(k)
        
    # 2. 넓이 누적합 구하기
    areas = [0] # areas[1] : [0~1] 구간 넓이
    
    for i in range(len(lst)-1):
        areas.append(areas[i] + getArea(lst,i))
    
    # 3. range 처리
    for rng in ranges:
        st, en = parseRange(lst,rng[0],rng[1]) # [st~en] 구간
        
        if st > en:
            answer.append(-1)
        else:
            answer.append(areas[en]-areas[st])
    
    return answer
        
    