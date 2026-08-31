#include <bits/stdc++.h>
using namespace std;

long long findPeak(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    if (a[mid] < a[mid + 1]) {
        return findPeak(a, mid + 1, r);
    } else {
        return findPeak(a, l, mid);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << findPeak(a, 0, n - 1) << "\n";
    return 0;
}
