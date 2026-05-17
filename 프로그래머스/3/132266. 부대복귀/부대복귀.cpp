#include <bits/stdc++.h>
using namespace std;

struct Node {
    int cur_node;
};


vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> answer = vector<int>(sources.size(), -1);
    vector<int> costs = vector<int>(n+1, -1);
    map<int, vector<int>> graph;

    queue<Node> q;
    for (vector<int> road: roads) {
        int x = road[0];
        int y = road[1];
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    
    q.push({destination});
    costs[destination] = 0;
    while (!q.empty()) {
        Node pop_node = q.front();
        int cur_node = pop_node.cur_node;
        q.pop();
        
                
        
        for (int next_node: graph[cur_node]) {
            if (costs[next_node] != -1) {
                continue;
            }
            q.push({next_node});
            costs[next_node] = costs[cur_node] + 1;
        }
        
    }
    
    for (int i = 0; i < sources.size(); i++) {
        answer[i] = costs[sources[i]];
    }
    
    
    
    
    return answer;
}