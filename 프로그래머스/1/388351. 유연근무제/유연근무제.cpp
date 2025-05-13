#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

int add10(int time) {
    int hours = time / 100;
    int minutes = time % 100;
    minutes += 10;
    
    if (minutes >= 60) {
        minutes -= 60;
        hours += 1;
    }
    
    return (hours * 100 + minutes);
    
}

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    int answer = 0;
    int idx = -1;
    for (const auto &timelog : timelogs) {
        idx++;
        bool flag = true;
        int day = startday % 7; // 0 or 6이면 continue
        int time = add10(schedules[idx]);
        for (int i = 0; i < 7; i++) {
            // if ((i == day && day == 0) || (i == day && day == 6)) {
            if ((day+i)%7 == 0 || (day+i)%7 == 6) {
                continue;
            }
            if (timelog[i] > time) {
                flag = false;
                break;
            }
        }
        
        // cout << day;
            
        if (flag) {
            answer++;
        }
    }
    
    return answer;
}