#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0, j = 0;
    long long min_diff = abs(a[0] - b[0]);

    while (i < n && j < m) {
        min_diff = min(min_diff, abs(a[i] - b[j]));
        if (a[i] == b[j]) break;
        else if (a[i] < b[j]) ++i;
        else ++j;
    }

    cout << min_diff << "\n";
    return 0;
}
