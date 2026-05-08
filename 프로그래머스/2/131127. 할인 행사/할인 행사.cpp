#include <string>
#include <vector>
#include <map>
#include <unordered_set>
#include <iostream>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    
    map<string, int> required_number;
    map<string, int> cur_number;
    unordered_set<string> want_set;
    int cur_counter = 0;
    int max_counter = number.size();
    
    for (string fruit: want) {
        want_set.insert(fruit);
    }
    
    for (int i = 0; i < want.size(); i++) {
        required_number[want[i]] = number[i];
    }
            
    for (int i = 0; i < 10; i++) {
        string cur_fruit = discount[i];
        cur_number[cur_fruit] += 1;
        if (cur_number[cur_fruit] == required_number[cur_fruit]) {
            cur_counter += 1;
        } 
    }
    if (cur_counter == max_counter) {
        answer += 1;
    }
    
    
    for (int i = 0; i < discount.size() - 10; i++) {
        string pop_fruit = discount[i];
        string add_fruit = discount[i+10];
        
        
        
        cur_number[pop_fruit] -= 1;
        cur_number[add_fruit] += 1;
        
        if (add_fruit == pop_fruit) {
            if (cur_counter == max_counter) {
                answer += 1;
            }
            continue;
        }
        
        if (want_set.count(pop_fruit) == 1 && cur_number[pop_fruit] == required_number[pop_fruit] - 1) {
            cur_counter -= 1;
        } 
        
        if (want_set.count(add_fruit) == 1 && cur_number[add_fruit] == required_number[add_fruit]) {
            cur_counter += 1;
        }
        
        if (cur_counter == max_counter) {
            answer += 1;
        }
    }
    
        
    
    
    

    return answer;
}