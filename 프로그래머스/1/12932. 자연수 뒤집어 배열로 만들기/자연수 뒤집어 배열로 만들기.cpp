#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    int cur = 0;
    while (n != 0) {
        cur = n % 10;
        answer.push_back(cur);
        n = n / 10;
        }
    return answer;
}