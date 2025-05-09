#include <string>
#include <vector>
#include <stack>
using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer(numbers.size(),-1);
    stack<int> st;
    st.push(0);
    for (int i = 1; i < numbers.size() ; i++){
        while (st.size() > 0 && numbers[st.top()] < numbers[i]){
            answer[st.top()] = numbers[i];
            st.pop();

        }
        st.push(i);
    }
    
    return answer;
}