#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

pair<int,int> can_change_block(pair<int,int> cur_pos, vector<string> board) {
    
    int cur_r = cur_pos.first;
    int cur_c = cur_pos.second;
    
    for (int next_r = cur_r - 1; next_r >= 0; next_r--) {
        if (board[next_r][cur_c] != '.') {
            return {next_r,cur_c};
        }
    }
    
    return {-1,-1};
}

bool can_pop(pair<int,int> pos, vector<string> board) {
    int dr[4] = {1,1,0};
    int dc[4] = {0,1,1};
    int r = pos.first;
    int c = pos.second;
    char cur_block = board[r][c];
    
    
    
    for (int i = 0; i < 3; i++) {
        int next_r = r + dr[i];
        int next_c = c + dc[i];
        if (cur_block != board[next_r][next_c]) {
            return false;
        }
    }
    
    return true;
}


int solution(int m, int n, vector<string> board) {
    int answer = 0;
    
    while (true) {
        bool result = false;
        vector<pair<int,int>> targets;

        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                if (can_pop({i,j}, board)) {
                    result = true;
                    targets.push_back({i,j});
                }
            }
        }
        
        for (pair<int,int> target: targets) {
            int target_r = target.first;
            int target_c = target.second;
            board[target_r][target_c] = '.';
            board[target_r+1][target_c] = '.';
            board[target_r+1][target_c+1] = '.';
            board[target_r][target_c+1] = '.';
        }
        
        
        for (int r = m-1; r >= 0; r--) {
            for (int c = 0; c < n; c++) {
                if (board[r][c] == '.') {
                    pair<int,int> swap_pos = can_change_block({r,c}, board);
                    if (swap_pos.first == -1) {
                        continue;
                    }
                    board[r][c] = board[swap_pos.first][swap_pos.second];
                    board[swap_pos.first][swap_pos.second] = '.';
                }
            }
        }
        
        
        
        
        if (!result) {
            break;
        }
    }
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == '.') {
                answer += 1;
            }
        }
    }
    
    
    
    return answer;
}