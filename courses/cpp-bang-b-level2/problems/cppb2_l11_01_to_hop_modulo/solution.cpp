#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long ans = 1;
    for (int i = 1; i <= n; ++i) {
        ans = (ans * i) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
