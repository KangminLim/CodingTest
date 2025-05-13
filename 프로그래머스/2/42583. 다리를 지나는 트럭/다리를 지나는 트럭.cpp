#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0, idx = 0, sum = 0;
    queue<int> q;
    
    while(1) {
        if(idx == truck_weights.size()){ // 마지막 트럭일 떄
            answer += bridge_length;
            break;
        }
        
        answer ++;
        int tmp = truck_weights[idx];
        
        // 차가 다리를 다 건넜을 경우
        if (q.size() == bridge_length) {
            sum -= q.front();
            q.pop();
        }
        
        if (sum + tmp <= weight) { // 다리에 다음 차가 진입할 수 있다면
            sum += tmp; // 차량 무게 추가
            q.push(tmp);
            idx++; // 다음 차량을 위해
        }
        else {
            q.push(0); // 진입할 수 없다면 0을 푸시해서 시간초 계산
        }
    }
    
    return answer;
}