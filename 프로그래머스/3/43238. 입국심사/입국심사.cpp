#include <string>
#include <vector>

using namespace std;

bool can_enter(long long people_number, long long total_time, vector<int> times) {
    
    long long pass_number = 0;
    
    for (int time: times) {
        pass_number += (long long) total_time / (long long)time;
    }
    
    return people_number <= pass_number;
}


long long solution(int n, vector<int> times) {
    long long answer = 0;
    
    long long left = 0;
    long long right = 10e16;
    
    while (left <= right) {
        long long middle = (long long)(left + right) / 2;
        
        if (can_enter((long long)n, middle, times)) {
            right = middle - 1;
            answer = middle;
        } else {
            left = middle + 1;
        }
    }
    
    
    return answer;
}