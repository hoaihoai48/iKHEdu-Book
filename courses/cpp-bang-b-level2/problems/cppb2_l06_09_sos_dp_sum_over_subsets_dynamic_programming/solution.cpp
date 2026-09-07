#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    int sz = 1 << n;
    vector<long long> f(sz);
    for (int i = 0; i < sz; ++i) cin >> f[i];
    for (int b = 0; b < n; ++b)
        for (int mask = 0; mask < sz; ++mask)
            if (mask & (1 << b)) f[mask] += f[mask ^ (1 << b)];
    for (int i = 0; i < sz; ++i) {
        if (i) cout << ' ';
        cout << f[i];
    }
    cout << "\n";
    return 0;
}
