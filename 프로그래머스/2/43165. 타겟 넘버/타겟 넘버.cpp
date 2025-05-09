#include <string>
#include <vector>

using namespace std;
int answer = 0;

void dfs(vector<int> numbers, int target, int sm, int n) {
    if (n == numbers.size()){
        if (sm == target){
            answer++;
        }
        return;
    }
    dfs(numbers,target,sm+numbers[n],n+1);
    dfs(numbers,target,sm-numbers[n],n+1);
}
    
    
int solution(vector<int> numbers, int target) {
    dfs(numbers,target,0,0);
    return answer;
}