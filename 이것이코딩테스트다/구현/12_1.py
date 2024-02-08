#럭키스트레이트(18406)
N = list(input())
left = N[:len(N)//2]
right = N[len(N)//2:]
left_sum, right_sum = 0, 0
for i in range(len(left)):
    left_sum += int(left[i])
    right_sum += int(right[i])

if left_sum != 0 and right_sum !=0 and left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")