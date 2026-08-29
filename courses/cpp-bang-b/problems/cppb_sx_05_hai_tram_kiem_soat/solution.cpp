#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    sort(x.begin(), x.end());

    long long min_dist = x[1] - x[0];
    for (int i = 1; i < n - 1; ++i) {
        min_dist = min(min_dist, x[i + 1] - x[i]);
    }

    cout << min_dist << "\n";
    return 0;
}
