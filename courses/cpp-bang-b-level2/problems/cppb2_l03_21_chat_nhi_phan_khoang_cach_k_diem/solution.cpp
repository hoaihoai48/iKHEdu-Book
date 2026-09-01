#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n, k; if (!(cin >> n >> k)) return 0; vector<long long> a(n); for (int i = 0; i < n; ++i) cin >> a[i]; sort(a.begin(), a.end()); long long l = 0, r = a.back() - a[0], ans = 0; while (l <= r) { long long mid = (l + r) / 2; int cnt = 1; long long last = a[0]; for (int i = 1; i < n; ++i) { if (a[i] - last >= mid) { cnt++; last = a[i]; } } if (cnt >= k) { ans = mid; l = mid + 1; } else r = mid - 1; } cout << ans << "
"; return 0; }
