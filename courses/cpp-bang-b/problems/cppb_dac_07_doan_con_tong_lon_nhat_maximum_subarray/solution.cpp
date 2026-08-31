#include <bits/stdc++.h>
using namespace std;

long long maxCrossingSum(const vector<long long> &a, int l, int mid, int r) {
    long long left_sum = -1e18, sum = 0;
    for (int i = mid; i >= l; --i) {
        sum += a[i];
        left_sum = max(left_sum, sum);
    }
    long long right_sum = -1e18;
    sum = 0;
    for (int i = mid + 1; i <= r; ++i) {
        sum += a[i];
        right_sum = max(right_sum, sum);
    }
    return left_sum + right_sum;
}

long long maxSubarrayDac(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    long long left_max = maxSubarrayDac(a, l, mid);
    long long right_max = maxSubarrayDac(a, mid + 1, r);
    long long cross_max = maxCrossingSum(a, l, mid, r);
    return max({left_max, right_max, cross_max});
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << maxSubarrayDac(a, 0, n - 1) << "\n";
    return 0;
}
