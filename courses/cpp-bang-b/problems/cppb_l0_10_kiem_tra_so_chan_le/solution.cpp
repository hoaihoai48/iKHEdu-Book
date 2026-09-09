#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    if (n % 2 == 0) {
        cout << "CHAN\n";
    } else {
        cout << "LE\n";
    }

    return 0;
}
