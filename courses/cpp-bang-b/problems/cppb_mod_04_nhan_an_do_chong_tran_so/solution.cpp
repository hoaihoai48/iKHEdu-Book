#include <bits/stdc++.h>
using namespace std;

long long mulMod(long long a, long long b, long long m) {
    long long ans = 0;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans + a) % m;
        a = (a + a) % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    cout << mulMod(a, b, m) << "\n";
    return 0;
}