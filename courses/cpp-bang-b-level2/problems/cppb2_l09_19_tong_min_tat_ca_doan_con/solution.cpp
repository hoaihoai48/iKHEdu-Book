#include <bits/stdc++.h>
using namespace std;

// Tổng min tất cả các đoạn con bằng Monotonic Stack O(N)
const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> left(n), right(n);
    vector<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.back()] > a[i]) st.pop_back();
        left[i] = st.empty() ? (i + 1) : (i - st.back());
        st.push_back(i);
    }

    st.clear();
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.back()] >= a[i]) st.pop_back();
        right[i] = st.empty() ? (n - i) : (st.back() - i);
        st.push_back(i);
    }

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        long long count = (1LL * left[i] * right[i]) % MOD;
        total = (total + count * (a[i] % MOD)) % MOD;
    }

    cout << (total + MOD) % MOD << "\n";
    return 0;
}
