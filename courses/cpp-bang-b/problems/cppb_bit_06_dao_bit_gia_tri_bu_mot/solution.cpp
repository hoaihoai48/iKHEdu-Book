#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned long long n;
    if (!(cin >> n)) return 0;

    int length = 64 - __builtin_clzll(n);
    unsigned long long mask = (1ULL << length) - 1;
    unsigned long long ans = n ^ mask;

    cout << ans << "\n";
    return 0;
}
