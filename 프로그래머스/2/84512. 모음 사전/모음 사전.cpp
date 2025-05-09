#include <string>
#include <vector>

using namespace std;

string target = "";
string aeiou = "AEIOU";
int cnt = 0;
int answer = 0;

void dfs(string cur) {
    
    if (cur == target) {
        answer = cnt;
        return;
    }
 
    if (cur.length() >= 5) {
        return;
    }
    
    for (int i = 0; i < 5; i++){
        cnt++;
        dfs(cur+aeiou[i]);
    }
}

int solution(string word) {
    target = word;
    dfs("");
    return answer;
}