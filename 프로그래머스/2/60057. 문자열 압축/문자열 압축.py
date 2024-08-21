def solution(s):
    answer = len(s)
    # 1개 단위부터 압축 늘려가기
    for step in range(1,len(s)//2+1):
        compressed = ''
        prev = s[0:step] 
        cnt = 1
        # 단위 크기만큼 증가시키면서 이전 문자열과 비교하기
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                if cnt >= 2:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                prev = s[j:j+step]
                cnt = 1
        # 남은 문자열 처리 
        if cnt >= 2:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        answer = min(answer,len(compressed))
        
    return answer