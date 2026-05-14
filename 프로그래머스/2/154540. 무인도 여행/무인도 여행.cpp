#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;

vector<pair<int,int>> find_near_positions(vector<string> maps, pair<int,int> cur_pos, int R, int C) {
    queue<pair<int,int>> q;
    int dr[4] = {1,-1,0,0};
    int dc[4] = {0,0,1,-1};
    vector<vector<bool>> visited = vector<vector<bool>>(R, vector<bool>(C, false));
    vector<pair<int,int>> result;
    int r = cur_pos.first;
    int c = cur_pos.second;
    visited[r][c] = true;

    q.push({r,c});    
    while (!q.empty()) {
        pair<int,int> pop_node = q.front();
        q.pop();
        int r = pop_node.first;
        int c = pop_node.second;
        result.push_back({r,c});
        for (int i = 0; i < 4; i++) {
            int next_r = r + dr[i];
            int next_c = c + dc[i];
            
            if (next_r < 0 || next_c < 0 || next_r >= R || next_c >= C) {
                continue;
            }
            
            if (visited[next_r][next_c] || maps[next_r][next_c] == 'X') {
                continue;
            }
            
            visited[next_r][next_c] = true;
            q.push({next_r,next_c});            
            
        }
    }
    return result;
}


vector<int> solution(vector<string> maps) {
    vector<int> answer;
    int R = maps.size();
    int C = maps[0].length();
    vector<vector<bool>> visited = vector<vector<bool>>(R, vector<bool>(C, false));
    
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {

            if (visited[i][j] || maps[i][j] == 'X') {
                continue;
            }
            cout << i << j <<'\n';
            vector<pair<int,int>> visited_vector = find_near_positions(maps, {i,j}, R, C);
            int result = 0;
            
            cout << '\n';
            for (pair<int,int> visited_node: visited_vector) {
                int r = visited_node.first;
                int c = visited_node.second;
                
                visited[r][c] = true;
                cout << maps[r][c];
                result += int(maps[r][c]) - '0';   
            }
            answer.push_back(result);
        }
    }
    if (answer.empty()) {
        answer.push_back(-1);
    }
    sort(answer.begin(), answer.end());
    
    return answer;
}