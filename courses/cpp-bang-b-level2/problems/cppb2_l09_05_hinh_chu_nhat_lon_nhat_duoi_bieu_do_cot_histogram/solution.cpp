#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];
    vector<int> st;
    long long ans = 0;
    for (int i = 0; i <= n; ++i) {
        long long cur = (i == n ? 0 : h[i]);
        while (!st.empty() && h[st.back()] >= cur) {
            long long height = h[st.back()];
            st.pop_back();
            long long width = st.empty() ? i : (i - st.back() - 1);
            ans = max(ans, height * width);
        }
        st.push_back(i);
    }
    cout << ans << "\n";
    return 0;
}
