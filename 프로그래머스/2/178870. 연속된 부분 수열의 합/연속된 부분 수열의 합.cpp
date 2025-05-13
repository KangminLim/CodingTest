#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer(2,0);
    int s=0,e=0;
    int mn = 10000001;
    int slen = sequence.size();
    int tmp = sequence[0];
    
    while (s<=e && e<slen){
        if (tmp == k) {
            if (e-s+1 < mn) {
                mn = e-s+1;
                answer[0] = s;
                answer[1] = e;
            }
            tmp -= sequence[s];
            s++;
        }    
        else if (tmp > k) {
            tmp -= sequence[s];
            s++;
        }
        else if (tmp < k) {
            e++;
            if (e < slen) { 
                tmp += sequence[e];
            }
        }
    }
    return answer;
}