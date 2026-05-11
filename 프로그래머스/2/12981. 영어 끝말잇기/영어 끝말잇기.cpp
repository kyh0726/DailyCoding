#include <string>
#include <vector>
#include <iostream>
#include <set>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    set<string> cur_words;
    string last_word = " ";
    for (int i = 0; i < words.size(); i++) {
        string word = words[i];
        if (i > 0 && last_word.back() != word.front()) {
            return {i%n + 1, int(i/n) + 1};
        }
        last_word = word;
        
        if (!cur_words.count(word)) {
            cur_words.insert(word);
        } else {
            return {i%n + 1, int(i/n) + 1};
        }
    }
    
    return {0,0};

}