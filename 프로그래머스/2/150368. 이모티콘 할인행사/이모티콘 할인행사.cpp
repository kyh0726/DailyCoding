#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

void make_cases(int count, int max, vector<vector<int>> & cases, vector<int> c) {
    if (count == max) {
        cases.push_back(c);
        return;
    }
    int percentages[4] = {10,20,30,40};
    
    for (int i = 0; i < 4; i++) {
        int percentage = percentages[i];
        
        c.push_back(percentage);
        make_cases(count + 1, max, cases, c);
        c.pop_back();
    }
}


vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    vector<int> answer;
    priority_queue<vector<int>> pq;
    vector<vector<int>> cases;
    int emoticon_size = emoticons.size();
    
    make_cases(0, emoticon_size, cases, {});
    
    for (vector<int> cur_case: cases) {
        int total_group_members = 0;
        int total_price = 0;
        for (vector<int> user: users) {
            int user_percentage = user[0];
            int user_max_price = user[1];
            int user_cur_price = 0;
            
            for (int i = 0; i < emoticon_size; i++) {
                int cur_item_percentage = cur_case[i];
                
                if (cur_item_percentage >= user_percentage) {
                    user_cur_price += emoticons[i] * (100 - cur_item_percentage) / 100;
                }
            }
            
            if (user_cur_price >= user_max_price) {
                total_group_members += 1;
            } else {
                total_price += user_cur_price;
            }
            
        }
        
        pq.push({total_group_members, total_price});

    }
    
    return pq.top();
}