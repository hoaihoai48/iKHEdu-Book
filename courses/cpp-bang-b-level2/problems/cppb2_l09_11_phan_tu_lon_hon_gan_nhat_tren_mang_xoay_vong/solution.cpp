#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    vector<long long> ans(n, -1);
    vector<int> st;
    for (int i = 2 * n - 1; i >= 0; --i) {
        int idx = i % n;
        while (!st.empty() && a[st.back()] <= a[idx]) st.pop_back();
        if (i < n && !st.empty()) ans[idx] = a[st.back()];
        st.push_back(idx);
    }
    for (int i = 0; i < n; ++i) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    cout << "\n";
    return 0;
}
