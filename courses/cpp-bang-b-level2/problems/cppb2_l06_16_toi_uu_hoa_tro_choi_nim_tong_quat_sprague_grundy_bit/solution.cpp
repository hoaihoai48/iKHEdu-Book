#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long xor_sum = 0;
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        xor_sum ^= x;
    }

    if (xor_sum != 0) {
        cout << "FIRST\n";
    } else {
        cout << "SECOND\n";
    }
    return 0;
}
