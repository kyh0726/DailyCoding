#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<vector<string>> chunk_minerals(vector<string> minerals, int & answer, int pick_num) {
    vector<vector<string>> result;
    int last_idx = 0;
    int count = 0;
    while (pick_num * 5 > minerals.size() && minerals.size() % 5 != 0) {
        minerals.push_back("stone");
        answer -= 1;
    }
    
    while (last_idx < minerals.size()) {
        if (pick_num <= count) {
            break;
        }
        
        vector<string> temp;
        
        int pop_num = std::min(5, (int)(minerals.size()) - last_idx);
        
        for (int i = 0; i < pop_num; i++) {
            temp.push_back(minerals[last_idx + i]);
        }
        last_idx += pop_num;
        result.push_back(temp);
        count += 1;
    }
    return result;
}


int solution(vector<int> picks, vector<string> minerals) {
    int answer = 0;
    int pick_num = 0;
    int cur_pick = 0;
    
    for (int pick: picks) {
        pick_num += pick;
    }
    vector<vector<string>> result = chunk_minerals(minerals, answer, pick_num);
    
    for (int i = 0; i < result.size(); i++) {
        sort(result[i].begin(), result[i].end());
    }
    sort(result.begin(),result.end());
    
    for (vector<string> chunk_minerals: result) {
        int cur_pick = -1;
        if (picks[0] > 0) {
            picks[0] -= 1;
            cur_pick = 0;
        } else if (picks[1] > 0) {
            picks[1] -= 1;
            cur_pick = 1;
        } else {
            picks[2] -= 1;
            cur_pick = 2;
        }
        
        for (string mineral: chunk_minerals) {
            if (cur_pick == 0) {
                answer += 1;
                continue;
            }
            
            if (cur_pick == 1) {
                if (mineral == "diamond") {
                    answer += 5;
                } else {
                    answer += 1;
                }
            }
            
            if (cur_pick == 2) {
                if (mineral == "diamond") {
                    answer += 25;
                } else if (mineral == "iron") {
                    answer += 5;
                } else {
                    answer += 1;
                }
            }
            
        }
    }
    
    
    return answer;
}