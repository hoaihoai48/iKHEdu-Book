#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    int don_vi = n % 10;
    int hang_chuc = (n / 10) % 10;

    cout << hang_chuc << ' ' << don_vi << '\n';
    return 0;
}
