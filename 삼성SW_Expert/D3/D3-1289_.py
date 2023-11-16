T = int(input())

for t in range(1,T+1):
    memory = list(input())
    num = 0
    reset = [0] * len(memory)
    for i in range(len(memory)):
        if int(memory[i]) != reset[i]:
            for j in range(i,len(memory)):
                reset[j] = int(memory[i])
            num += 1
    print('#{} {}'.format(t, num))