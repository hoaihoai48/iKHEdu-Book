#include <bits/stdc++.h>
using namespace std;
int main() {
    long long a, n, m;
    if (!(cin >> a >> n >> m)) return 0;
    long long sum = 0, cur = 1 % m;
    for (int i = 0; i <= n; ++i) {
        sum = (sum + cur) % m;
        cur = (cur * (a % m)) % m;
    }
    cout << sum << "\n";
    return 0;
}
