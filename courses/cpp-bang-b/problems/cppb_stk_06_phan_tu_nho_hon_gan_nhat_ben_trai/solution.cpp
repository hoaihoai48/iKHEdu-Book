#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> pse(n, -1);
    stack<long long> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && st.top() >= a[i]) {
            st.pop();
        }
        if (!st.empty()) {
            pse[i] = st.top();
        }
        st.push(a[i]);
    }

    for (int i = 0; i < n; ++i) {
        cout << pse[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
