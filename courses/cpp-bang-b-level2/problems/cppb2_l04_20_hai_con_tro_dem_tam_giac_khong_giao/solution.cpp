#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n; if (!(cin >> n)) return 0; vector<long long> a(n); for (int i = 0; i < n; ++i) cin >> a[i]; sort(a.begin(), a.end()); long long ans = 0; for (int k = 2; k < n; ++k) { int i = 0, j = k - 1; while (i < j) { if (a[i] + a[j] > a[k]) { ans += j - i; j--; } else i++; } } cout << ans << "
"; return 0; }
