def solution(phone_book):
    
    # for phone in phone_book:
    #     for i in range(len(phone_book)):
    #         if phone == phone_book[i]:
    #             continue
    #         if phone in phone_book[i]:
    #             return False
    # return True
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer