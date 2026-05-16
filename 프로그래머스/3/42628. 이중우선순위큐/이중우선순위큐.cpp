#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <map>
using namespace std;

vector<string> splitter(string s, string delimiter) {
    vector<string> result;
    int start = 0;
    int end = 0;
    
    while ((end = s.find(delimiter, start)) != string::npos) {
        result.push_back(s.substr(start, end - start));
        start = end + delimiter.length();
    }
    result.push_back(s.substr(start));
    return result;
    
}

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    map<int, int> nums_dict;
    priority_queue<int> max_queue;
    priority_queue<int, vector<int>, greater<int>> min_queue;
    
    for (string operation: operations) {
        vector<string> operation_vector = splitter(operation, " ");
        string cmd = operation_vector[0];
        int number = std::stoi(operation_vector[1]);
        
        
        if (cmd == "I") {
            max_queue.push(number);
            min_queue.push(number);
            nums_dict[number] += 1;
        } 
        
        if (cmd == "D") {
            if (number == 1) {
                while (!max_queue.empty() && nums_dict[max_queue.top()] == 0) {
                    max_queue.pop();
                }
                if (!max_queue.empty()) {
                    int top_node = max_queue.top();
                    nums_dict[top_node] -= 1;
                    max_queue.pop();
                }
                
            } else {
                while (!min_queue.empty() && nums_dict[min_queue.top()] == 0) {
                    min_queue.pop();
                }
                if (!min_queue.empty()) {
                    int top_node = min_queue.top();
                    nums_dict[top_node] -= 1;
                    min_queue.pop();
                }
                
            }
        }
        
    }
    
    while (!min_queue.empty() && nums_dict[min_queue.top()] == 0) {
        min_queue.pop();
    }
    while (!max_queue.empty() && nums_dict[max_queue.top()] == 0) {
        max_queue.pop();
    }
    
    if (max_queue.empty()) {
        answer = {0,0};
    } else {
        answer = {max_queue.top(), min_queue.top()};
    }
    
    return answer;
}