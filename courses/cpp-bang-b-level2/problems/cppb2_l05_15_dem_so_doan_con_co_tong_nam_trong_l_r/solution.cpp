#include <bits/stdc++.h>
using namespace std;

long long count_range(vector<long long> &pref, int l, int r, long long L, long long R) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long count = count_range(pref, l, mid, L, R) + count_range(pref, mid + 1, r, L, R);

    int j1 = mid + 1, j2 = mid + 1;
    for (int i = l; i <= mid; ++i) {
        while (j1 <= r && pref[j1] - pref[i] < L) j1++;
        while (j2 <= r && pref[j2] - pref[i] <= R) j2++;
        count += (j2 - j1);
    }

    inplace_merge(pref.begin() + l, pref.begin() + mid + 1, pref.begin() + r + 1);
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L, R;
    if (!(cin >> n >> L >> R)) return 0;

    vector<long long> a(n);
    vector<long long> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        pref[i + 1] = pref[i] + a[i];
    }

    cout << count_range(pref, 0, n, L, R) << "\n";
    return 0;
}
