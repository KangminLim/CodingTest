#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    
    arr.erase(min_element(arr.begin(),arr.end())); // v.erase(first,last) : first 이상, last 미만의 범위의 원소를 삭제
    if(arr.empty()) arr.push_back(-1);
    return arr;
}