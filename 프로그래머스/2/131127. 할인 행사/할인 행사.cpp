#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;


int sum(map<string, int>& m) {
    int total = 0;
    for (const auto& pair : m) {
        if (pair.second > 0) {
            total += pair.second;
        }
    }
    return total;
}


int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    map<string,int> m;
    
    for (int i = 0; i < want.size(); i++){
        m[want[i]] = number[i];
    }
    
    for (int i = 0; i < discount.size()-9; ++i){
        map<string,int> tmp(m);
        for (int j = i; j<i+10; ++j){
            tmp[discount[j]]--;
        }
        if (sum(tmp) == 0){
            answer++;
        }
    }
    
    return answer;
}