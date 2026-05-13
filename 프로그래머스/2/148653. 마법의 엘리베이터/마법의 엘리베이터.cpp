#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int storey) {
    int answer = 0;

    while (storey > 0) {
        int cur_storey = storey % 10;
        storey /= 10;
        
        if (cur_storey < 5) {
            answer += cur_storey;
        } 
        if (cur_storey > 5) {
            answer += (10 - cur_storey);
            storey += 1;
        }
        
        if (cur_storey == 5) {
            if (storey > 0 && storey % 10 >= 5) {
                answer += (10 - cur_storey);
                storey += 1;
            } else {
                answer += cur_storey;
            }
        }
        
        
        
    }
    
    return answer;
}