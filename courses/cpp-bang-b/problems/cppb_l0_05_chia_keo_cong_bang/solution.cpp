#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m, n;
    if (!(cin >> m >> n)) return 0;

    cout << m / n << ' ' << m % n << '\n';
    return 0;
}
