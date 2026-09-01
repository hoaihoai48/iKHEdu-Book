#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    int limit = 1 << n;
    vector<long long> f(limit);
    for (int i = 0; i < limit; ++i) cin >> f[i];
    for (int i = 0; i < n; ++i)
        for (int mask = 0; mask < limit; ++mask)
            if (mask & (1 << i))
                f[mask] += f[mask ^ (1 << i)];
    for (int i = 0; i < limit; ++i) cout << f[i] << (i == limit - 1 ? "" : " ");
    cout << "\n";
    return 0;
}
