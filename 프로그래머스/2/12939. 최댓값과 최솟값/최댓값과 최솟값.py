def solution(s):
    answer = ''
    s = s.split(' ')
    mx = int(-1e9)
    mn = int(1e9)
    for ch in s:
        mx = max(int(ch),int(mx))
        mn = min(int(ch),int(mn))
    answer = str(mn) + ' ' + str(mx)
    return answer