#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string num;
    int k;
    if (!(cin >> num >> k)) return 0;

    string st = "";
    for (char c : num) {
        while (!st.empty() && k > 0 && st.back() > c) {
            st.pop_back();
            k--;
        }
        st.push_back(c);
    }

    while (k > 0 && !st.empty()) {
        st.pop_back();
        k--;
    }

    // Xóa các số 0 ở đầu
    int start = 0;
    while (start < (int)st.size() && st[start] == '0') start++;

    string ans = st.substr(start);
    if (ans.empty()) cout << "0\n";
    else cout << ans << "\n";
    return 0;
}
