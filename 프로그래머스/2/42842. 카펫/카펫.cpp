#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    
    for (int i = 1; i <= yellow + 1; i++) {
        if (yellow % i != 0) {
            continue;
        }
        int height = i;
        int width = yellow / i;
        
        if (brown == height * 2 + width * 2 + 4) {
            return {width + 2, height + 2};
        }
    }

}