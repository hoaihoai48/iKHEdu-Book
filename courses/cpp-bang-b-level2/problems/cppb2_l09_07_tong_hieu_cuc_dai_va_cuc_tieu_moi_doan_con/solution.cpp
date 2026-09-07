#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    vector<int> left(n), right(n), st;
    // sum of maximums: prev strictly greater, next greater-or-equal
    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.back()] <= a[i]) st.pop_back();
        left[i] = st.empty() ? i + 1 : i - st.back();
        st.push_back(i);
    }
    st.clear();
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.back()] < a[i]) st.pop_back();
        right[i] = st.empty() ? n - i : st.back() - i;
        st.push_back(i);
    }
    long long sumMax = 0;
    for (int i = 0; i < n; ++i) sumMax += a[i] * (long long)left[i] * right[i];
    // sum of minimums: prev strictly smaller, next smaller-or-equal
    st.clear();
    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.back()] >= a[i]) st.pop_back();
        left[i] = st.empty() ? i + 1 : i - st.back();
        st.push_back(i);
    }
    st.clear();
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.back()] > a[i]) st.pop_back();
        right[i] = st.empty() ? n - i : st.back() - i;
        st.push_back(i);
    }
    long long sumMin = 0;
    for (int i = 0; i < n; ++i) sumMin += a[i] * (long long)left[i] * right[i];
    cout << (sumMax - sumMin) << "\n";
    return 0;
}
