#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const string &a, const string &b) {
    if (a + b > b + a) 
        return true;
    else
        return false;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> temp;
    
    for (const auto &num : numbers) {
        temp.push_back(to_string(num));
    }
    
    sort(temp.begin(), temp.end(), compare);
    
    for (const auto &num : temp){
        answer += num;
    }
    
    if (answer[0] == '0'){
        return "0";
    }
    
    return answer;
}