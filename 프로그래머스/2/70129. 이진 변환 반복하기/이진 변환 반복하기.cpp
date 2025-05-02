#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer(2,0);
    int ccnt = 0, zcnt = 0;
    
    while (s != "1"){
        ccnt++;
        string tmp = "";
        int num;
        for (char c: s){
            if (c == '0'){
                zcnt++;
                }
            else{
                tmp += c;
            }
        } 
        num = tmp.size();
        s = "";
        while(num > 0){
            s += to_string(num%2);
            num /= 2; 
        }
    }
    answer[0] = ccnt;
    answer[1] = zcnt;
    return answer;
}