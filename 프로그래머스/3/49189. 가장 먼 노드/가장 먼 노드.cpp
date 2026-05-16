#include <string>
#include <vector>
#include <queue>
#include <map>
using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    
    map<int,vector<int>> graph;
    queue<vector<int>> q;
    vector<bool> visited = vector<bool>(n+1, false);
    
    for (vector<int> vertex: edge) {
        int x = vertex[0];
        int y = vertex[1];
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    
    int start_node = 1;
    int max_count = 0;
    visited[start_node] = true;
    q.push({start_node, 0});
    while (!q.empty()) {
        vector<int> pop_node = q.front();
        int cur_node = pop_node[0];
        int count = pop_node[1];
        q.pop();
        
        if (count > max_count) {
            max_count = count;
            answer = 1;
        } else {
            answer += 1;
        }
        
        for (int next_node: graph[cur_node]) {
            if (visited[next_node]) {
                continue;
            }
            q.push({next_node, count + 1});
            visited[next_node] = true;
            
        }
    }
    
    
    
    
    
    return answer;
}