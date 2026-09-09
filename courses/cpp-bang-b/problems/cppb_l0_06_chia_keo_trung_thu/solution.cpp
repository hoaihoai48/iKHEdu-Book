#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    long long each = n / k;
    long long rem = n % k;

    cout << each << ' ' << rem << '\n';
    return 0;
}
