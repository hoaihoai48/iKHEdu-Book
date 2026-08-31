#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    int total = 0;
    for (int i = 0; i < n; ++i) { cin >> a[i]; total += a[i]; }
    if (total % 2 != 0) { cout << "NO\n"; return 0; }
    int target = total / 2;
    bool ok = false;
    for (int mask = 0; mask < (1 << n); ++mask) {
        int sum = 0;
        for (int i = 0; i < n; ++i) if (mask & (1 << i)) sum += a[i];
        if (sum == target) { ok = true; break; }
    }
    cout << (ok ? "YES\n" : "NO\n");
    return 0;
}
