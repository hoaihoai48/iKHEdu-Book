#include <bits/stdc++.h>
using namespace std;

int countInRange(const vector<long long> &a, long long target, int l, int r) {
    int cnt = 0;
    for (int i = l; i <= r; ++i) if (a[i] == target) cnt++;
    return cnt;
}

long long majorityDac(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    long long left_maj = majorityDac(a, l, mid);
    long long right_maj = majorityDac(a, mid + 1, r);

    if (left_maj == right_maj) return left_maj;

    int left_count = countInRange(a, left_maj, l, r);
    int right_count = countInRange(a, right_maj, l, r);

    return (left_count > right_count) ? left_maj : right_maj;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long cand = majorityDac(a, 0, n - 1);
    int total_cnt = 0;
    for (long long x : a) if (x == cand) total_cnt++;
    if (total_cnt > n / 2) {
        cout << cand << "\n";
    } else {
        cout << -1 << "\n";
    }
    return 0;
}
