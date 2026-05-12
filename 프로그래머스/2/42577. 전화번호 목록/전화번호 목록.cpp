#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    // 1. 기본 사전순 정렬 (O(N log N))
    // "119", "1195524421", "97674223" 순으로 정렬됨
    sort(phone_book.begin(), phone_book.end());

    // 2. 단 한 번의 루프로 인접한 번호만 비교 (O(N))
    for (int i = 0; i < (int)phone_book.size() - 1; i++) {
        // C++20 starts_with 혹은 find() == 0 사용
        // 바로 다음 번호가 현재 번호로 시작하는지만 보면 됩니다.
        if (phone_book[i + 1].find(phone_book[i]) == 0) {
            return false;
        }
    }

    return true;
}