#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <queue>
#include <set>
using namespace std;

bool can_transfer(string s1, string s2) {
    int count = 0;
    for (int i = 0; i < s1.length(); i++) {
        if (s1[i] != s2[i]) {
            count += 1;
        }
        if (count > 1) {
            return false;
        }

    }
    return true;
}

struct Node {
    int cur_node;
    set<int> visited_nodes;
};


int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    queue<Node> q;
    
    map<int, vector<int>> word_mapper;
    words.push_back(begin);
    for (int i = 0; i < words.size(); i++) {
        for (int j = i+1; j < words.size(); j++) {
            string s1 = words[i];
            string s2 = words[j];
            if (can_transfer(s1,s2)) {
                word_mapper[i].push_back(j);
                word_mapper[j].push_back(i);
            }
        }
    }

    q.push({(int)(words.size()) - 1, set<int>()});
    
    while (!q.empty()) {
        Node pop_node = q.front();
        q.pop();
        
        set<int> visited_nodes = pop_node.visited_nodes;
        int cur_node = pop_node.cur_node;
        
        
        if (words[cur_node] == target) {
            return visited_nodes.size();
        }
        
        for (int next_node: word_mapper[cur_node]) {
            if (visited_nodes.count(next_node)) {
                continue;
            }
            
            visited_nodes.insert(next_node);
            q.push({next_node, visited_nodes});
            visited_nodes.erase(next_node);
        }
    }
    
    
    
    
    
    return answer;
}