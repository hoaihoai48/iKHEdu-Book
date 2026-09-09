#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    if (a > b) {
        cout << a << '\n';
    } else if (b > a) {
        cout << b << '\n';
    } else {
        cout << "BANG NHAU\n";
    }

    return 0;
}
