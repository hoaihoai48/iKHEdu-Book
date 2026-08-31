#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, p;
    if (!(cin >> n >> p)) return 0;

    long long k = 0;
    while (n > 0) {
        k += (n / p);
        n /= p;
    }

    cout << k << "\n";
    return 0;
}