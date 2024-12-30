class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        answer = sum(jobs)
        # v = [False] * len(jobs)
        wt = [0] * k
        jobs.sort()
        def bt(idx,wt):
            nonlocal answer,k
            if idx == len(jobs):
                answer = min(answer,max(wt))
                return
            
            for i in range(len(wt)):
                if jobs[idx] + wt[i] <= answer:
                    wt[i] += jobs[idx]
                    bt(idx+1,wt)
                    wt[i] -= jobs[idx]
                if wt[i] == 0:
                    break
        bt(0,wt)
        return answer   