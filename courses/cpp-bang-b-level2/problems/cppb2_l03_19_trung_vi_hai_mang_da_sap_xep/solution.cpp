#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n, m; if (!(cin >> n >> m)) return 0; vector<double> a(n + m); for (int i = 0; i < n + m; ++i) cin >> a[i]; sort(a.begin(), a.end()); int sz = n + m; if (sz % 2 == 1) cout << fixed << setprecision(1) << a[sz / 2] << "
"; else cout << fixed << setprecision(1) << (a[sz / 2 - 1] + a[sz / 2]) / 2.0 << "
"; return 0; }
