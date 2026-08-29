#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    for (int i = 0; i <= n - k; ++i) {
        long long cur_min = a[i];
        for (int j = i + 1; j < i + k; ++j) {
            cur_min = min(cur_min, a[j]);
        }
        cout << cur_min << (i == n - k ? "" : " ");
    }
    cout << "\n";
    return 0;
}
