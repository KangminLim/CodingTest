#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    stack<int> st;
    queue<int> q;
    bool flag = true;
    for (int i = 1; i <= order.size(); i++){
        q.push(i);
    }
    
    for (int i = 0; i < order.size(); i++) {
        while (true) {
            if (order[i] == q.front()){
                answer++;
                q.pop();
                break;
            }
            else if (st.size()>0 && st.top() == order[i]){
                answer++;
                st.pop();
                break;
            }
            else if (q.size() == 0) {
                flag = false;
                break;
            }
            else {
                int tmp = q.front();
                q.pop();
                st.push(tmp);
            }
        }
        if (not flag) {
            break;
        }
    }    
    return answer;
}