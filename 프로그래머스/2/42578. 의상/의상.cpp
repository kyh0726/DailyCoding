#include <string>
#include <vector>
#include <map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string,int> clothes_map;
    
    int clothes_num = clothes.size();
    
    for (int i = 0; i < clothes_num; i++) {
        string clothes_name = clothes[i][0];
        string clothes_type = clothes[i][1];
        clothes_map[clothes_type] += 1;    
    }
    
    for (auto const& [clothes_type, clothes_num]: clothes_map) {
        answer *= (clothes_num + 1);
    }
    answer -= 1;
    
    
    return answer;
}