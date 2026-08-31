#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    if (n == 1) { cout << 1 << "\n"; return 0; }
    if (n == 2) { cout << 2 << "\n"; return 0; }

    int p2 = 1, p1 = 2, cur = 0;
    for (int i = 3; i <= n; ++i) {
        cur = (p1 + p2) % MOD;
        p2 = p1;
        p1 = cur;
    }

    cout << cur << "\n";
    return 0;
}
