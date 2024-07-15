
def solution(numbers, target):
    answer = 0
    def backtracking(sm, n):
        nonlocal answer
        if n == len(numbers):
            if sm == target:
                answer += 1
            return
        backtracking(sm + numbers[n],n+1)
        backtracking(sm - numbers[n],n+1)

    backtracking(0,0)

    return answer
