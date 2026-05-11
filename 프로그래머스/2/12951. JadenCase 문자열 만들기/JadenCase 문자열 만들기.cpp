#include <string>
#include <vector>
#include <iostream>
#include <cctype>
#include <algorithm>

using namespace std;

vector<string> split(string input, string delimiter) {
    vector<string> result;
    int start = 0;
    int end = input.find(delimiter);
    
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
    
    for (int i = 0; i < result.size(); i++) {
        
        transform(result[i].begin(), result[i].end(), result[i].begin(), ::tolower);
        result[i][0] = toupper(result[i][0]);
        if (i > 0) {
            answer += " ";
        }
        answer += result[i];
    }
    
    
    
    
    
    return answer;
}