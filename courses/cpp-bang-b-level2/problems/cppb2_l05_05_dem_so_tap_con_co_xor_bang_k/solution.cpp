#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target;
    if (!(cin >> n >> target)) return 0;

    vector<long long> a(n), b(n), c(n), d(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];
    for (int i = 0; i < n; ++i) cin >> c[i];
    for (int i = 0; i < n; ++i) cin >> d[i];

    unordered_map<long long, int> ab_sum;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            ab_sum[a[i] + b[j]]++;
        }
    }

    long long count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            long long rem = target - (c[i] + d[j]);
            if (ab_sum.count(rem)) {
                count += ab_sum[rem];
            }
        }
    }

    cout << count << "\n";
    return 0;
}
