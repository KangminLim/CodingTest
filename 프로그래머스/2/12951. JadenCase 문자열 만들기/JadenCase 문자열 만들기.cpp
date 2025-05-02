#include <string>
#include <cctype>
using namespace std;

string solution(string s) {
    string answer = "";
    bool flag = true; 
    
    for (char c : s) {
        if (c == ' ') {
            answer += c;
            flag = true;
        }
        else{
            if (flag) {
                answer += toupper(c);
                flag = false;
            }
            else {
                answer += tolower(c);
            }
        }
        
    }

    return answer;
}
