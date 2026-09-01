#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> bit_count(31, 0);
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        for (int b = 0; b < 31; ++b) {
            if ((x >> b) & 1) bit_count[b]++;
        }
    }

    for (int b = 0; b < 31; ++b) {
        cout << "Bit " << b << ": " << bit_count[b] << "\n";
    }
    return 0;
}
