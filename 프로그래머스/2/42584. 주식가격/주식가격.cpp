#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    queue<int> q;
    int time;
    int idx = 0;
    for (int i = 0; i < prices.size() ; i++){
        q.push(prices[i]);
    }
    while (q.size()>0) {
        int cur = q.front();
        q.pop(); 
        time = 0;
        // cout << cur << endl;
        for (int i = idx; i < prices.size() ; i++){
            // cout << cur << ":" << time << endl;
            time++;

            if (cur > prices[i]) {
                break;
            }
        }
        idx++;
        answer.push_back(time-1);
        }
    return answer;
}