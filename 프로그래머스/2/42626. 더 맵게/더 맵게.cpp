#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int first, second, tmp;
    priority_queue<int,vector<int>,greater<int>> pq(scoville.begin(),scoville.end());
    while (pq.size() > 1 && pq.top() < K) {
        first = pq.top();
        pq.pop();
        second = pq.top();
        pq.pop();
        tmp = first + 2 * second;
        pq.push(tmp);
        answer++;
    }
    if (pq.top() < K) {
        return -1 ;
    }
    return answer;
}