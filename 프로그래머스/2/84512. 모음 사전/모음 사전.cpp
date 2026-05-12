#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void make_cases(int count, string cur_word, vector<string>& cases) {
    vector<char> alphabets = {'A', 'E', 'I', 'O', 'U'};
    
    if (count > 0) {
        cases.push_back(cur_word);
    }
    
    if (count == 5) {
        return;
    }
    
    for (int i = 0; i < 5; i++) {
        make_cases(count + 1, cur_word + alphabets[i], cases);
    }
    
}


int solution(string word) {
    int answer = 0;
    
    vector<string> cases;
    
    make_cases(0, "", cases);
    
    sort(cases.begin(), cases.end());
    
    for (int i = 0; i < cases.size(); i++) {
        if (cases[i] == word) {
            return i + 1;
        }
    }
    
    
    
    return answer;
}