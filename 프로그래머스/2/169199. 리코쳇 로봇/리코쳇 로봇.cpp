#include <bits/stdc++.h>
using namespace std;

vector<int> can_go(vector<string> & board, int cur_r, int cur_c, int cur_dir) {
    int dr[4] = {1,-1,0,0};
    int dc[4] = {0,0,1,-1};
    int R = board.size();
    int C = board[0].length();
    int idx = 0;
    while (true) {
        
        int next_r = cur_r + dr[cur_dir];
        int next_c = cur_c + dc[cur_dir];
        
        if (next_r < 0 || next_c < 0 || next_r >= R || next_c >= C) {
            return {cur_r, cur_c};
        } 
        if (board[next_r][next_c] == 'D') {
            return {cur_r, cur_c};
        }
        
        cur_r = next_r;
        cur_c = next_c;
        
    }
    
}


int solution(vector<string> board) {
    int answer = 0;
    vector<vector<vector<int>>> visited = 
        vector<vector<vector<int>>>(board.size(), 
                                    vector<vector<int>>(board[0].length(), 
                                                        vector<int>(4, 0)));
    
    pair<int,int> start_pos;
    pair<int,int> end_pos;
    queue<vector<int>> q;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            if (board[i][j] == 'R') {
                start_pos.first = i;
                start_pos.second = j;
            }
            if (board[i][j] == 'G') {
                end_pos.first = i;
                end_pos.second = j;
            }
        }
    }
    
    q.push({start_pos.first, start_pos.second, 0});
    
    while (!q.empty()) {
        vector<int> pop_node = q.front();
        q.pop();
        
        int pop_r = pop_node[0];
        int pop_c = pop_node[1];
        int count = pop_node[2];
        if (pop_r == end_pos.first && pop_c == end_pos.second) {
            return count;
        }
        for (int cur_dir = 0; cur_dir < 4; cur_dir++) {
            vector<int> result = can_go(board, pop_r, pop_c, cur_dir);
            int next_r = result[0];
            int next_c = result[1];
            
            if (next_r == pop_r && next_c == pop_c) {
                continue;
            }
            if (visited[next_r][next_c][cur_dir]) {
                continue;
            }
            q.push({next_r,next_c,count+1});
            visited[next_r][next_c][cur_dir] = 1;
            
        }
        
    }
    
    
    
    
    return -1;
}