#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> left(n), right(n);
    stack<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.top()] > a[i]) st.pop();
        left[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }

    while (!st.empty()) st.pop();

    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.top()] >= a[i]) st.pop();
        right[i] = st.empty() ? n : st.top();
        st.push(i);
    }

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        long long l_count = i - left[i];
        long long r_count = right[i] - i;
        long long contrib = (l_count * r_count % MOD) * (a[i] % MOD) % MOD;
        total = (total + contrib) % MOD;
    }

    cout << total << "\n";
    return 0;
}
