#include <string>
#include <stack>

using namespace std;

bool solution(string s)
{
    stack<char> st;
    
    for (char c : s) {
        if (c == '(') {
            st.push(c);
        } else {
            if (!st.empty()) {
                st.pop();
            } else {
                return false;
            }
        }
    }
    
    return st.empty();
}