#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    answer.push_back(number[0]);
    
    for(int i = 1; i < number.length(); i++) {
        char num = number[i];
        
        while(!answer.empty() && k > 0 && answer.back() < num) {
            answer.pop_back();
            k--;
        }
        answer.push_back(num);
    }
    
    while(k > 0)
    {
        answer.pop_back();
        k--; 
    }
    
    return answer;
}