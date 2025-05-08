#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    queue<int> p, s;
    for (int i = 0; i < progresses.size(); i++){
        p.push(progresses[i]);
        s.push(speeds[i]);
    }
    
    vector<int> answer;
    int days = 0, cnt = 0;
    
    while (!p.empty()){
    // for (int i = 0; i < 30; i++){
        // std::cout << p.front() << " , "<< s.front() << " : " << days <<endl;

        if (p.front() + s.front() * days >= 100) {
            cnt = 0;
            while (!p.empty() and p.front() + s.front() * days >= 100){
                // if (p.front() == 0) { break; }
                std::cout << p.front() << " , "<< s.front() << " : " << days <<endl;
                p.pop();
                s.pop();
                cnt++;
            }
            // std::cout << p.front() << " , "<< s.front() << " : " << days <<endl;
            // std::cout << cnt << " : " << days <<endl;
        
            answer.push_back(cnt);
            days = 0;
            // days++;
        }
        days++;
        // else {
        //     days++;
        // }
    }
    return answer;
}