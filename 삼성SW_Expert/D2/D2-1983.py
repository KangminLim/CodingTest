T = int(input())
grades=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for tc in range(1,T+1):
    N, K =map(int,input().split())
    total_list = []
    for i in range(N):
        score = list(map(int,input().split()))
        total_score = round(score[0]*0.35 + score[1]*0.45 + score[2]*0.2)
        total_list.append(total_score)

    k_score = total_list[K-1]

    total_list.sort(reverse=True)
    div = N // 10
    final_k_score = total_list.index(k_score) // div
    print('#{} {}'.format(tc,grades[final_k_score]))