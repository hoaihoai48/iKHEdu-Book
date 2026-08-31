#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    if (n == 1) { cout << a[0] << "\n"; return 0; }

    long long prev2 = a[0];
    long long prev1 = max(a[0], a[1]);
    long long cur = prev1;

    for (int i = 2; i < n; ++i) {
        cur = max(prev1, prev2 + a[i]);
        prev2 = prev1;
        prev1 = cur;
    }

    cout << cur << "\n";
    return 0;
}
