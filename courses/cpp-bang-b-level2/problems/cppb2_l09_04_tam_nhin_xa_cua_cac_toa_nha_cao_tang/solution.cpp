#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string token;
    stack<long long> st;

    while (cin >> token) {
        if (token == "+" || token == "-" || token == "*" || token == "/") {
            long long b = st.top(); st.pop();
            long long a = st.top(); st.pop();
            if (token == "+") st.push(a + b);
            else if (token == "-") st.push(a - b);
            else if (token == "*") st.push(a * b);
            else if (token == "/") st.push(a / b);
        } else {
            st.push(stoll(token));
        }
    }

    if (!st.empty()) cout << st.top() << "\n";
    return 0;
}
