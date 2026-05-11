#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <functional>
using namespace std;

bool compare(int a, int b, map<int,int> tangerine_mapper) {
    return tangerine_mapper[a] - tangerine_mapper[b];
}


int solution(int k, vector<int> tangerine) {
    int answer = 0;
    
    map<int, int> tangerine_mapper;
    vector<int> tangerine_numbers;
    for (int val: tangerine) {
        if (tangerine_mapper[val]) {
            tangerine_mapper[val] += 1;
        } else {
            tangerine_mapper[val] = 1;
        }
    }
    
    for (auto const& [size, count]: tangerine_mapper) {
        tangerine_numbers.push_back(count);
    }
    
    sort(tangerine_numbers.begin(), tangerine_numbers.end(), greater<int>());
    int sum = 0;
    for (int val: tangerine_numbers) {
        sum += val;
        answer += 1;
        
        if (sum >= k) {
            return answer;
        }
    }
    
    
    
    return answer;
}