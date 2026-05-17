#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    vector<vector<int>> acc_sum = vector<vector<int>>(board.size() + 1, vector<int>(board[0].size() + 1, 0));
    
    
    for (vector<int> cmd: skill) {
        int type = cmd[0];
        int r1 = cmd[1];
        int c1 = cmd[2];
        int r2 = cmd[3]; 
        int c2 = cmd[4];
        int degree = cmd[5];

        if (type == 1){
            acc_sum[r1][c1] -= degree;
            acc_sum[r1][c2 + 1] += degree;
            acc_sum[r2+1][c1] += degree;
            acc_sum[r2+1][c2+1] -= degree;
        } else {
            acc_sum[r1][c1] += degree;
            acc_sum[r1][c2 + 1] -= degree;
            acc_sum[r2+1][c1] -= degree;
            acc_sum[r2+1][c2 + 1] += degree;
        }
    }
    
    for (int i = 0; i < acc_sum.size(); i++) {
        for (int j = 1; j < acc_sum[0].size(); j++) {
            acc_sum[i][j] += acc_sum[i][j-1];
        }
    }
    
    for (int j = 0; j < acc_sum[0].size(); j++) {
        for (int i = 1; i < acc_sum.size(); i++) {
            acc_sum[i][j] += acc_sum[i-1][j];
        }
    }
    
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            
            if (board[i][j] + acc_sum[i][j] >= 1) {
                answer += 1;
            }
        }
    }
    
    
    
    
    
    
    
    
    return answer;
}