#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> split(string input, string delimiter) {
    vector<string> result;
    size_t start = 0;
    size_t end = input.find(delimiter);

    while (end != string::npos) {
        result.push_back(input.substr(start, end - start));
        start = end + delimiter.length();
        end = input.find(delimiter, start);
    }
    result.push_back(input.substr(start));

    return result;
}


string solution(string s) {
    string answer = "";
    
    vector<string> result = split(s, " ");
    int max_num = -10000;
    int min_num = 10000;
    for (int i = 0; i < result.size(); i++) {
        int cur_num = stoi(result[i]);
        if (cur_num > max_num) {
            max_num = (cur_num);
        }
        
        if (cur_num < min_num) {
            min_num = (cur_num);
        }
    }   
    string max_string = std::to_string(max_num);
    string min_string = std::to_string(min_num);
    answer = min_string + " " + max_string;
    return answer;
}