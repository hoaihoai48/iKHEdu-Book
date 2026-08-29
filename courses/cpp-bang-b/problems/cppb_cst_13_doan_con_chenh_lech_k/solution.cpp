#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int max_len = 0;

    for (int l = 0; l < n; ++l) {
        long long cur_min = a[l], cur_max = a[l];
        for (int r = l; r < n; ++r) {
            cur_min = min(cur_min, a[r]);
            cur_max = max(cur_max, a[r]);
            if (cur_max - cur_min <= k) {
                max_len = max(max_len, r - l + 1);
            } else {
                break;
            }
        }
    }

    cout << max_len << "\n";
    return 0;
}
