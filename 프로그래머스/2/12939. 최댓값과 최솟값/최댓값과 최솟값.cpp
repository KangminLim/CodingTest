#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string s) {
    string answer = "", tmp ="";
    vector<int> v;
    
    for (int i = 0; i < s.size(); ++i){
        if (s[i] == ' '){
        v.push_back(stoi(tmp));
        tmp = "";
        }
        else tmp += s[i];
    }
    v.push_back(stoi(tmp));
    answer += to_string(*min_element(v.begin(),v.end()));
    answer += ' ';
    answer += to_string(*max_element(v.begin(),v.end()));
    
    return answer;
}