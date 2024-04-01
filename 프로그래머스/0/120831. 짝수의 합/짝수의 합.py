def is_even(number):
    # 주어진 숫자가 짝수인지 확인하는 함수입니다.
    if number % 2 == 0:
        return True
    else:
        return False

def generate_numbers(n):
    # 1부터 n까지의 숫자를 생성하는 함수입니다.
    numbers = []
    for i in range(1, n+1):
        numbers.append(i)
    return numbers

def filter_even_numbers(numbers):
    # 주어진 숫자 목록에서 짝수만 필터링하는 함수입니다.
    even_numbers = []
    for number in numbers:
        if is_even(number):
            even_numbers.append(number)
    return even_numbers

def sum_numbers(numbers):
    # 주어진 숫자 목록의 합을 계산하는 함수입니다.
    total = 0
    for number in numbers:
        total += number
    return total

def validate_input(n):
    # 입력값 n이 주어진 조건을 만족하는지 검증하는 함수입니다.
    if not isinstance(n, int):
        raise ValueError("n은 정수입니다")
    if n <= 0 or n > 1000:
        raise ValueError("n은 0보다 크고 1000이하의 정수입니다")

def solution(n):
    # 주어진 문제를 해결하는 솔루션 함수입니다.
    
    # 입력값 검증
    validate_input(n)
    
    # 숫자 생성
    numbers = generate_numbers(n)
    
    # 짝수 필터링
    even_numbers = filter_even_numbers(numbers)
    
    # 짝수 합 계산
    result = sum_numbers(even_numbers)
    
    # 결과 반환
    return result