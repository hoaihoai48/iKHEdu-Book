#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) s = "";
    vector<char> st;
    bool ok = true;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') st.push_back(c);
        else {
            if (st.empty()) { ok = false; break; }
            char t = st.back();
            if ((c == ')' && t == '(') || (c == ']' && t == '[') || (c == '}' && t == '{'))
                st.pop_back();
            else { ok = false; break; }
        }
    }
    if (!st.empty()) ok = false;
    cout << (ok ? "YES" : "NO") << "\n";
    return 0;
}
