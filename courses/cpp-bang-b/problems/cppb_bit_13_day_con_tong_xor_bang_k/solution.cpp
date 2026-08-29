#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int count_k = 0;
    int total_masks = (1 << n);

    for (int mask = 1; mask < total_masks; ++mask) {
        long long current_xor = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                current_xor ^= a[i];
            }
        }
        if (current_xor == k) {
            count_k++;
        }
    }

    cout << count_k << "\n";
    return 0;
}
