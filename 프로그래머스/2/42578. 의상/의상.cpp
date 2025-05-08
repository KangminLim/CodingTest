#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;

int solution(vector<vector<string>> clothes) {
    map<string,int> mp;
    
    for (auto c : clothes) {
        std::cout << c[0] << " : " << c[1] << endl;
        mp[c[1]]++;
    }
    int answer = 1;
    for (auto pair : mp){
        std::cout << pair.second << endl;

        answer *= (pair.second+1);
    }
    return answer-1;
}