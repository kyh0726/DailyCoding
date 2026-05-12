#include <string>
#include <vector>
#include <set>
using namespace std;

int solution(vector<int> elements) {
    int answer = 0;
    int N = elements.size();
    set<int> element_set;
    for (int i = 0; i < N; i++) {
        int start_idx = i;
        int cur_value = elements[start_idx];
        element_set.insert(cur_value);
        for (int j = 1; j < N; j++) {
            int add_idx = (start_idx + j) % N;
            cur_value += elements[add_idx];
            element_set.insert(cur_value);
        }    
    }
    answer = element_set.size();
    return answer;
}