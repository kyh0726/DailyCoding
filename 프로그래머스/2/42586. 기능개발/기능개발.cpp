#include <string>
#include <vector>
#include <queue>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    queue<int> stk;
    
    
    for (int i = 0; i < progresses.size(); i++) {
        int progress = progresses[i];
        int speed = speeds[i];
        
        int val = ((100 - progress + speed - 1) / speed);
        
        int counter = 0;
        if (!stk.empty() && stk.front() < val) {
            while (!stk.empty()) {
                stk.pop();
                counter += 1; 
            }
        }
        
        stk.push(val);
        
        if (counter > 0) {
            answer.push_back(counter);
        }
    }
    
    int counter = 0;
    while (!stk.empty()) {
        stk.pop();
        counter += 1;
    }
    
    if (counter > 0) {
        answer.push_back(counter);
    }

    
    
    return answer;
}