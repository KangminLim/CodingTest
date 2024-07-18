from collections import Counter
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1_counter = Counter(list(str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()))
    str2_counter = Counter(list(str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()))
    
    len_inter = sum((str1_counter & str2_counter).values())
    len_union = sum((str1_counter | str2_counter).values())
    return 65536 if len_union == 0 and len_inter == 0 else int(len_inter/len_union*65536)