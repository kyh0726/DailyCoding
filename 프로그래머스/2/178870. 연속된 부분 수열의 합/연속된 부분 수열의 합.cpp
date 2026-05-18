#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    sequence.push_back(0);
    int left = 0;
    int right = 1;
    int total = sequence[0];
    int min_gap = sequence.size();
    while (left <= right && right < sequence.size()) {
        if (total > k) {
            total -= sequence[left];
            left += 1;
            continue;
        }
        if (total < k) {
            total += sequence[right];
            right += 1;
            continue;
        }
        if (total == k) {
            int gap = right - left;
            if (gap < min_gap) {
                answer = {left, right - 1};
                min_gap = gap;
            }
            total -= sequence[left];
            left += 1;
        }
    }
    return answer;
}