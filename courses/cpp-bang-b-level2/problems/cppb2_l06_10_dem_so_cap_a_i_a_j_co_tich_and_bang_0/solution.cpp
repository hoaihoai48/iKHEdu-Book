#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    vector<int> freq(1 << 20, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        freq[a[i]]++;
    }

    vector<int> sos = freq;
    for (int b = 0; b < 20; ++b) {
        for (int mask = 0; mask < (1 << 20); ++mask) {
            if ((mask >> b) & 1) {
                sos[mask] += sos[mask ^ (1 << b)];
            }
        }
    }

    long long count = 0;
    int all_mask = (1 << 20) - 1;
    for (int x : a) {
        int comp = all_mask ^ x;
        count += sos[comp];
    }

    cout << count << "\n";
    return 0;
}
