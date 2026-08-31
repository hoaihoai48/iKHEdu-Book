#include <bits/stdc++.h>
using namespace std;

long long countSubarraysDac(vector<long long> &prefix, vector<long long> &temp, int l, int r, long long lower, long long upper) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long cnt = 0;
    cnt += countSubarraysDac(prefix, temp, l, mid, lower, upper);
    cnt += countSubarraysDac(prefix, temp, mid + 1, r, lower, upper);

    int j1 = mid + 1, j2 = mid + 1;
    for (int i = l; i <= mid; ++i) {
        while (j1 <= r && prefix[j1] - prefix[i] < lower) j1++;
        while (j2 <= r && prefix[j2] - prefix[i] <= upper) j2++;
        cnt += (j2 - j1);
    }

    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        if (prefix[i] <= prefix[j]) temp[k++] = prefix[i++];
        else temp[k++] = prefix[j++];
    }
    while (i <= mid) temp[k++] = prefix[i++];
    while (j <= r) temp[k++] = prefix[j++];
    for (int idx = l; idx <= r; ++idx) prefix[idx] = temp[idx];

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long lower, upper;
    if (!(cin >> n >> lower >> upper)) return 0;
    vector<long long> a(n);
    vector<long long> prefix(n + 1, 0), temp(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        prefix[i + 1] = prefix[i] + a[i];
    }
    cout << countSubarraysDac(prefix, temp, 0, n, lower, upper) << "\n";
    return 0;
}
