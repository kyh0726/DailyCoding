#include <string>
#include <vector>
#include <iostream>
#include <utility>
#include <queue>
using namespace std;

struct Node {
    int r, c, count;
};

int bfs(pair<int,int> start, pair<int,int> target, int R, int C, vector<string> maps) {
    queue<Node> q;
    vector<vector<bool>> visited(R, vector<bool>(C, false));    
    int dr[4] = {1,-1,0,0};
    int dc[4] = {0,0,1,-1};
    
    q.push({start.first, start.second, 0});

    while (!q.empty()) {
        Node pop_node = q.front();
        q.pop();
        
        if (pop_node.r == target.first && pop_node.c == target.second) {
            return pop_node.count;
        }
        cout << pop_node.r << pop_node.c << pop_node.count << '\n';
        
        for (int i = 0; i < 4; i++) {
            int next_r = pop_node.r + dr[i];
            int next_c = pop_node.c + dc[i];
            int next_count = pop_node.count + 1;
            
            if (next_r < 0 || next_c < 0 || next_r >= R || next_c >= C) {
                continue;
            }
            if (maps[next_r][next_c] == 'X' || visited[next_r][next_c] == true) {
                continue;
            }
            visited[next_r][next_c] = true;
            q.push({next_r, next_c, next_count});
        }
    }
    return -1;
}



int solution(vector<string> maps) {        
    pair<int, int> start_pos;
    pair<int, int> end_pos;
    pair<int, int> lever_pos;
    
    int R = maps.size();
    int C = maps[0].size();
    

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (maps[i][j] == 'S') {
                start_pos.first = i;
                start_pos.second = j;
            }
            if (maps[i][j] == 'E') {
                end_pos.first = i;
                end_pos.second = j;
            }
            if (maps[i][j] == 'L') {
                lever_pos.first = i;
                lever_pos.second = j;
            }
        }
    }
    
    int result1 = bfs(start_pos, lever_pos, R, C, maps);
    
    int result2 = bfs(lever_pos, end_pos, R, C, maps);
    if (result1 == -1 || result2 == -1) {
        return -1;
    } else {
        return result1 + result2;
    }
}