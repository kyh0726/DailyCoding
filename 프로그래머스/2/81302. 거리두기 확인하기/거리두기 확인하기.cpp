#include <string>
#include <vector>
#include <queue>
using namespace std;

bool check(vector<string> place, pair<int,int> pos) {
    vector<vector<bool>> visited = vector<vector<bool>>(5, vector<bool>(5,false));
    queue<vector<int>> q;
    int dr[4] = {0,0,1,-1};
    int dc[4] = {1,-1,0,0};
    
    int r = pos.first;
    int c = pos.second;
    
    visited[r][c] = true;
    q.push({r,c,0});
    
    
    while (!q.empty()) {
        vector<int> pop_node = q.front();
        int row = pop_node[0];
        int col = pop_node[1];
        int count = pop_node[2];
        q.pop();
        if (count == 2) {
            continue;
        }
        
        for (int i = 0; i < 4; i++) {
            int next_r = row + dr[i];
            int next_c = col + dc[i];
            
            if (next_r < 0 || next_c < 0 || next_r >= 5 || next_c >= 5) {
                continue;
            }
            if (place[next_r][next_c] == 'X' || visited[next_r][next_c]) {
                continue;
            }
            if (place[next_r][next_c] == 'P') {
                return false;
            }
            q.push({next_r,next_c,count+1});
            visited[next_r][next_c] = true;
        }
            
    }
    return true;
}


vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    
    for (vector<string> place: places) {
        int R = place.size();
        int C = place[0].length();
        bool early_return = false;
        for (int i = 0; i < R; i++) {
            if (early_return) {
                break;
            }
            for (int j =0; j < C; j++) {
                if (early_return) {
                    break;
                }
                
                if (place[i][j] == 'P' && !check(place, {i,j})) {
                    early_return = true;
                }
            }
        }
        if (early_return) {
            answer.push_back(0);
        } else {
            answer.push_back(1);
        }
        
    }
    
    return answer;
}