#include <string>
#include <cctype>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

vector<string> split_string(string s) {
    int string_size = s.size();
    
    vector<string> result;
    for (int i = 0; i < string_size - 1; i++) {
        char str1 = s[i];
        char str2 = s[i+1];
        
        
        if (isalpha(str1) && isalpha(str2)) {
            string temp = "";
            
            temp += (char)toupper(str1);
            temp += (char)toupper(str2);
            result.push_back(temp);
        }
        
    }
    return result;
}

int calc_jacad(vector<string> s1, vector<string> s2) {
    
    map<string,int> s1_map;
    map<string,int> s2_map;
    set<string> candidate_keys;
    
    for (string s: s1) {
        candidate_keys.insert(s);
        s1_map[s] += 1;
    }
    for (string s: s2) {
        candidate_keys.insert(s);
        s2_map[s] += 1;
    }
    
    int intersection_num = 0;
    int union_num = 0;
    
    for (string key: candidate_keys) {
        int s1_num = s1_map[key];
        int s2_num = s2_map[key];
        
        intersection_num += std::min(s1_num, s2_num);
        union_num += std::max(s1_num, s2_num);
    }
    if (union_num == 0) {
        return 65536;
    }
    
    return (int)((intersection_num * 65536) / union_num);
    
}


int solution(string str1, string str2) {
    int answer = 0;
    
    vector<string> str1_vector = split_string(str1);
    vector<string> str2_vector = split_string(str2);
    

    
    
    return calc_jacad(str1_vector, str2_vector);
}