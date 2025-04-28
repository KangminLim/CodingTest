#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    int mn = std::min(a,b);
    int mx = std::max(a,b);

    for (int i = mn ; i <= mx ; i++)
        answer += i;
    return answer;
}