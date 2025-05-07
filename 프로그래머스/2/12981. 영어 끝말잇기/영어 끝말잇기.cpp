#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer(2);
    map<string,int> m;
    string cur = "", pre = "";
    m[words[0]]++;
    for (int i = 1; i < words.size(); i++) { 
        cur = words[i];
        pre = words[i-1];
        std::cout << cur << endl <<  pre << endl;
        if (cur.front() == pre.back()) {
            m[cur]++;
            // for (auto c:m) {
            // std :: cout << c.first << " : " << c.second << endl;    
            // }
            // std :: cout << m[cur] << endl;
            if (m[cur] > 1){
                answer[0] = i%n + 1;
                answer[1] = i/n + 1;
                return answer;
                }
            }
        else {
            answer[0] = i%n + 1;
            answer[1] = i/n + 1;
            return answer;
            }
    }       
    return answer;
}