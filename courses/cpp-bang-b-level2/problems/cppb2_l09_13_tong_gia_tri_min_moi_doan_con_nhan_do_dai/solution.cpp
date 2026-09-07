#include <bits/stdc++.h>
using namespace std;

string toString(__int128 x) {
    if (x == 0) return "0";
    string s;
    while (x > 0) {
        s.push_back((char)('0' + (int)(x % 10)));
        x /= 10;
    }
    reverse(s.begin(), s.end());
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    vector<long long> L(n), R(n);
    vector<int> st;
    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.back()] >= a[i]) st.pop_back();
        L[i] = st.empty() ? i + 1 : i - st.back();
        st.push_back(i);
    }
    st.clear();
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.back()] > a[i]) st.pop_back();
        R[i] = st.empty() ? n - i : st.back() - i;
        st.push_back(i);
    }
    __int128 ans = 0;
    for (int i = 0; i < n; ++i)
        ans += (__int128)a[i] * L[i] * R[i] * (L[i] + R[i]) / 2;
    cout << toString(ans) << "\n";
    return 0;
}
