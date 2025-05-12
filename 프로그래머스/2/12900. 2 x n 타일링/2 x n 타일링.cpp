#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    vector<int> dp(60001);
    int answer = 0;
    dp[0] = 1;
    dp[1] = 2;
    for (int i = 2; i < n; i++) {
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007;
    }
    return dp[n-1];
}