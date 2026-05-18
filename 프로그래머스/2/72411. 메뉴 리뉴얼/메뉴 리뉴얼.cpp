#include <bits/stdc++.h>

using namespace std;

void make_cases(vector<string> & cases, string orders, int cur_count, string cur_string) {
    if (cur_string.length() >= 2) {
        cases.push_back(cur_string);
    }
    
    for (int i = cur_count + 1; i < orders.size(); i++) {
        cur_string += orders[i];
        make_cases(cases, orders, i, cur_string);
        cur_string.pop_back();
    }
}


vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    map<string, int> order_map;
    map<int, int> max_value;
    map<int, string> max_value_strings;
    for (string order: orders) {
        vector<string> cases;
        make_cases(cases, order, -1, "");
        
        for (string c: cases) {
            sort(c.begin(), c.end());
            order_map[c] += 1;
        }
    }
    
for (auto [key, value] : order_map) {
        int len = key.length();
        
        // 스카피가 원하는 코스 요리 길이에 포함되는지 확인
        if (find(course.begin(), course.end(), len) == course.end()) {
            continue;
        }
        
        // 최소 2명 이상의 손님이 주문한 경우에만 후보 등록
        if (value >= 2) {
            max_value[len] = max(max_value[len], value);
        }
    }
    
    // 2단계: 다시 맵을 돌며 각 길이별 '최대 빈도수(1등)'와 일치하는 메뉴들을 정답에 추가
    for (auto [key, value] : order_map) {
        int len = key.length();
        
        // 해당 길이의 최대 빈도수와 일치하는 공동 1등 메뉴들만 수집
        if (max_value[len] != 0 && value == max_value[len]) {
            answer.push_back(key);
        }
    }
    
    // 최종 정답을 사전 순으로 오름차순 정렬
    sort(answer.begin(), answer.end());
    
    return answer;
}