def solution(numbers, hand):
    # phone = [['1','2','3'],['4','5','6'],['7','8','9'],['#','0','#']]
    phone_dict = {
        1:(0,0),
        2:(0,1),
        3:(0,2),
        4:(1,0),
        5:(1,1),
        6:(1,2),
        7:(2,0),
        8:(2,1),
        9:(2,2),
        '*':(3,0),
        0:(3,1),
        '#':(3,2)
    }
    answer = []
    left = phone_dict['*']
    right = phone_dict['#']
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer.append('L')
            left = phone_dict[number]
        elif number == 3 or number == 6 or number == 9:
            answer.append('R')
            right = phone_dict[number]
        else:
            left_distance = abs(phone_dict[number][0]-left[0]) + abs(phone_dict[number][1]-left[1])
            right_distance = abs(phone_dict[number][0]-right[0]) + abs(phone_dict[number][1]-right[1])
            
            if left_distance > right_distance:
                right = phone_dict[number]
                answer.append('R')
            
            elif left_distance < right_distance:
                left = phone_dict[number]
                answer.append('L')
            
            else:
                if hand == 'left':
                    left = phone_dict[number]
                    answer.append('L')
                else:
                    right = phone_dict[number]
                    answer.append('R')
            
    return ''.join(answer)