#include <bits/stdc++.h>
using namespace std;

long long countSignificant(vector<long long> &a, vector<long long> &temp, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long cnt = 0;
    cnt += countSignificant(a, temp, l, mid);
    cnt += countSignificant(a, temp, mid + 1, r);

    // Bước đếm 2 con trỏ trước khi merge
    int j = mid + 1;
    for (int i = l; i <= mid; ++i) {
        while (j <= r && a[i] > 2LL * a[j]) j++;
        cnt += (j - (mid + 1));
    }

    // Merge bình thường
    int i = l, k = l;
    j = mid + 1;
    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), temp(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << countSignificant(a, temp, 0, n - 1) << "\n";
    return 0;
}
