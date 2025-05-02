#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n) {
    string bn = "";
    int j = n;
    int ocnt = 0;

    while (n > 0){
        if(n%2==1) ocnt++;
        n /= 2;
    }
    // printf("%d",ocnt);
    while (1){
        j++;
        int tmpj = j;
        int tmp = 0;
        while (tmpj > 0){
        if(tmpj%2==1) {
            tmp++;
        }
        tmpj /= 2;
    }
        if (ocnt == tmp)
            break;
    }
    return j;
}