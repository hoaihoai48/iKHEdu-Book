#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long max_gap = 0;
    for (int i = 0; i < n - 1; ++i) {
        max_gap = max(max_gap, a[i + 1] - a[i]);
    }

    cout << max_gap << "\n";
    return 0;
}
