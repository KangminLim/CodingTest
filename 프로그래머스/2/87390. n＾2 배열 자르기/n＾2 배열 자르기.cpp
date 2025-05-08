#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, long long left, long long right) {
    vector<int> answer;
    long long div = 0,  mod = 0;
    for (long long i = left; i <= right; i++){
        div = i / n;
        mod = i % n;
        if (div < mod) {
            answer.push_back(mod+1);
        }
        else {
            answer.push_back(div+1);
        }
    }
    return answer;
}