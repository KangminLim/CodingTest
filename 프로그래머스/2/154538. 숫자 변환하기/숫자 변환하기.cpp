#include <string>
#include <vector>

using namespace std;

int solution(int x, int y, int n) {
    int answer = 0;
    vector<int> dp(1000001,1000001);
    dp[y] = 0;
    
    for (int i = y; i > x; i--){
        if (dp[i] != 1000001){
            if (i%3 == 0) {
                dp[i/3] = min(dp[i/3],dp[i]+1);
                }
            if (i%2 == 0) {
                dp[i/2] = min(dp[i/2],dp[i]+1);
            }
            if (i-n > 0) {
                dp[i-n] = min(dp[i-n],dp[i]+1);
            }
            
        }
    }
    if (dp[x] == 1000001){
        return -1;
    }
    return dp[x];
}