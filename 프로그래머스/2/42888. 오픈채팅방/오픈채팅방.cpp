#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;


vector<string> split_string(string s, string splitter) {
    
    vector<string> result_string;
    size_t start = 0;
    size_t end = 0;
    
    while ((end = s.find(splitter, start)) != string::npos) {
        string temp = s.substr(start, end - start);
        start = end + splitter.length();
        result_string.push_back(temp);
    }
    result_string.push_back(s.substr(start));

    
    return result_string;
    
}

vector<string> solution(vector<string> record) {
    vector<string> answer;
    map<string, string> nickname_mapper;
    vector<vector<string>> user_records;
    
    
    for (string r: record) {
        vector<string> cur_record = split_string(r, " ");
        string cmd = cur_record[0];
        string uid = cur_record[1];

        
        if (cmd == "Enter") {
            string nickname = cur_record[2];
            nickname_mapper[uid] = nickname;
            user_records.push_back({uid, cmd});
        }
        
        if (cmd == "Change") {
            string nickname = cur_record[2];
            nickname_mapper[uid] = nickname;
        }
        
        if (cmd == "Leave") {
            user_records.push_back({uid, cmd});
        }
        
    }
    
    for (vector<string> cur_record: user_records) {
        string uid = cur_record[0];
        string cmd = cur_record[1];
        string nickname = nickname_mapper[uid];
        
        string result = "";
        if (cmd == "Enter") {
            result += nickname + "님이 들어왔습니다.";
        } else {
            result += nickname + "님이 나갔습니다.";
        }
        answer.push_back(result);
    }
    
    
    return answer;
}