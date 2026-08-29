#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    long long total_pairs = 0;

    for (int i = 0; i < n; ++i) {
        for (int k = 1; k <= 30; ++k) {
            long long target = (1LL << k) - a[i];
            if (target <= 0) continue;

            auto it1 = lower_bound(a.begin() + i + 1, a.end(), target);
            auto it2 = upper_bound(a.begin() + i + 1, a.end(), target);
            total_pairs += (it2 - it1);
        }
    }

    cout << total_pairs << "\n";
    return 0;
}
