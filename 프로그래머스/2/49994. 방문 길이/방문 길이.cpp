#include <string>
#include <map>
#include <iostream>
#include <vector>

using namespace std;

int solution(string dirs) {
    int answer = 0;
    int dr[4] = {0,0,1,-1};
    int dc[4] = {1,-1,0,0};
    map<vector<int>,bool> visited;
    
    map<char,int> dir_mapper;
    dir_mapper['U'] = 0;
    dir_mapper['D'] = 1;
    dir_mapper['R'] = 2;
    dir_mapper['L'] = 3;
    
    
    
    pair<int,int> cur_pos = {0,0};
    
    
    
    for (char dir: dirs) {
        int cur_r = cur_pos.first;
        int cur_c = cur_pos.second;
        int next_r = cur_r + dr[dir_mapper[dir]];
        int next_c = cur_c + dc[dir_mapper[dir]];
        
        if (next_r < -5 || next_c < -5 || next_r > 5 || next_c > 5) {
            continue;
        }
        
        if (visited[{cur_r, cur_c, next_r, next_c}] || visited[{next_r, next_c, cur_r, cur_c}]) {
            cur_pos.first = next_r;
            cur_pos.second = next_c;
        } else {
            visited[{cur_r, cur_c, next_r, next_c}] = true;
            answer += 1;
            cur_pos.first = next_r;
            cur_pos.second = next_c;
        }
    }
    
    
    
    
    return answer;
}