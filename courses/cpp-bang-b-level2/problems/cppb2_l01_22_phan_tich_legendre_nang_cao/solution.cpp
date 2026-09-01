#include <bits/stdc++.h>
using namespace std;

long long legendre(long long n, long long p) {
    long long cnt = 0;
    while (n > 0) {
        cnt += n / p;
        n /= p;
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m, p;
    if (!(cin >> n >> m >> p)) return 0;
    cout << legendre(n, p) + legendre(m, p) << "\n";
    return 0;
}
