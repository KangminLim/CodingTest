#include <string>
#include <unordered_map>
#include <set>
#include <iostream>
using namespace std;

int di[4] = {-1,1,0,0}, dj[4] = {0,0,1,-1};
unordered_map<char,int> dmap;
set<tuple<int, int, int, int>> vset;
string dr = "UDRL";
int solution(string dirs) {
    int answer = 0;
    int ci = 0, cj = 0;
    int ni,nj;
    char dir;
    // vset.insert({ci,cj});
    for (int i = 0; i < 4; i++){
        dmap[dr[i]] = i;
    }
    
    for (int i = 0; i < dirs.length();i++){
        dir = dirs[i];
        ni = ci+di[dmap[dir]]; 
        nj = cj+dj[dmap[dir]];
        cout << ci << " : "<< cj << " : " << answer << endl;
        // cout << ni << " : "<< nj << endl;

        if (-5<=ni && ni<=5 && -5<=nj && nj<=5) {
            // if (vset.find({ni,nj}) == vset.end())
            if (vset.find({ci,cj, ni, nj}) == vset.end()){
                answer++;
                vset.insert({ci,cj,ni,nj});
                vset.insert({ni,nj,ci,cj});
                }            
            ci = ni ; cj = nj;
            }
        }
    cout << ci << " : "<< cj << " : " << answer << endl;
    return answer;
}