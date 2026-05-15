#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> q;
    
    for (int node: scoville) {
        q.push(node);
    }

    while (!q.empty() && q.size() >= 2) {
        int f_node = q.top();
        q.pop();
        int s_node = q.top();
        q.pop();
        if (f_node >= K && s_node >= K) {
            return answer;
        }
        int new_node = f_node + s_node * 2;
        q.push(new_node);
        answer += 1;
    }
    
    if (!q.empty() && q.top() < K) {
        return -1;
    }
    
    return answer;
}