#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    if (a + b > c && a + c > b && b + c > a) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
