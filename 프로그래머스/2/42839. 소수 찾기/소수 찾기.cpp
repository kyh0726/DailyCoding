#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

bool is_prime_number(int number) {
    if (number == 0 || number == 1) {
        return false;
    }
    
    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) {
            return false;
        }
    }
    return true;
}

void make_cases(int count, int max_num, set<int> & cases, vector<int> cur_case, string numbers) {
    if (count > 0) {
        string s = "";
        for (int val: cur_case) {
            s += numbers[val];
        }
        int number = std::stoi(s);
        if (is_prime_number(number)){
        cases.insert(number);}
    }
    if (count == max_num) {
        return ;
    }
    
    for (int i = 0; i < max_num; i++) {
        if ((std::find(cur_case.begin(), cur_case.end(), i)) != cur_case.end()) {
            continue;
        } else {
            cur_case.push_back(i);
            make_cases(count + 1, max_num, cases, cur_case, numbers);
            cur_case.pop_back();
        }
    }
    
}



int solution(string numbers) {
    int answer = 0;
    
    vector<char> numbers_vector;
    set<int> cases;
    make_cases(0, numbers.length(), cases, {}, numbers);
    return cases.size();
}