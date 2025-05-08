#include <string>
#include <vector>
#include <iostream>
#include <stack>
using namespace std;

bool check(string s) {
    stack<char> st;
    for (int i = 0; i < s.size(); i++){
        // std::cout<<s<<endl;
        if (st.empty()){
            st.push(s[i]);
        }
        else if (s[i]=='(' || s[i]=='[' || s[i]=='{' ){
            st.push(s[i]);
        }
        else if ((st.top() == '(' && s[i] == ')') || (st.top() == '{' && s[i] == '}') || (st.top() == '[' && s[i] == ']') ){
            st.pop();
        }
        else {
            return false;
        }
    }
    // std::cout<<st.empty()<<endl;
    return st.empty();
}

int solution(string s) {
    int answer = 0;
    for (int i = 0; i < s.size(); i++){
        if (check(s)==1) {
            answer++;
        }
        s = s.substr(1) + s[0];
        }
    if (answer > 0) {
        return answer;
    }
    else return 0;
    }