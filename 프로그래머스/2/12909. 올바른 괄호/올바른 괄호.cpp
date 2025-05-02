#include <string>
#include <iostream>
#include <vector>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    vector<int> v;
    
    for (int i = 0; i < s.size(); i++){
        if (s[i] == '('){
            v.push_back('(');
        }
        else if (s[i] == ')'){
            if (v.empty())
                answer = false;
            else
                v.pop_back();
        }
    }
    
    if (not v.empty())
        answer = false;
        
    return answer;
}