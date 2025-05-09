#include<vector>
#include<queue>
using namespace std;



int bfs(vector<vector<int>> &maps){
    queue<pair<int,int>>q;
    int ci,cj;
    int di[4] = {-1,0,1,0};
    int dj[4] = {0,1,0,-1};
    int n = maps.size();
    int m = maps[0].size();
    q.push({0,0});
    vector<vector<int> > v(n,vector<int>(m,0));
    v[0][0] = 1;
    while (q.size()) {
        pair<int,int> cur = q.front(); q.pop();
        int ci = cur.first;
        int cj = cur.second;
        for (int i = 0; i<4; i++){
            int ni = ci + di[i];
            int nj = cj + dj[i];
            if (0<=ni && ni < n && 0<=nj && nj <m && maps[ni][nj] == 1 && v[ni][nj] == 0){
            // if (0 <= ni && ni < n && 0 <= nj && nj < m && maps[ni][nj] == 1 && v[ni][nj] == 0){
                q.push({ni,nj});
                v[ni][nj] = v[ci][cj] + 1;
            }
        }
    }
    return v[n-1][m-1] > 0 ? v[n-1][m-1] : -1; 
}

int solution(vector<vector<int> > maps)
{
    int answer = -1;

    answer = bfs(maps);
    return answer;
}