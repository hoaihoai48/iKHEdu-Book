#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> left_bound(n), right_bound(n);
    stack<int> st;

    // Tìm biên trái nghiêm ngặt nhỏ hơn
    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.top()] > a[i]) st.pop();
        left_bound[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }

    while (!st.empty()) st.pop();

    // Tìm biên phải nhỏ hơn hoặc bằng
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.top()] >= a[i]) st.pop();
        right_bound[i] = st.empty() ? n : st.top();
        st.push(i);
    }

    long long total_sum = 0;
    for (int i = 0; i < n; ++i) {
        long long count = (1LL * (i - left_bound[i]) * (right_bound[i] - i)) % MOD;
        total_sum = (total_sum + a[i] * count) % MOD;
    }

    cout << total_sum << "\n";
    return 0;
}
