#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long S;
    if (!(cin >> n >> S)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int min_len = n + 1;
    long long cur_sum = 0;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum >= S) {
            min_len = min(min_len, r - l + 1);
            cur_sum -= a[l];
            l++;
        }
    }

    cout << (min_len > n ? -1 : min_len) << "\n";
    return 0;
}
