#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int max_size = 0;
    int total_masks = (1 << n);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long used_bits = 0;
        bool valid = true;
        int current_count = 0;

        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if (used_bits & a[i]) {
                    valid = false;
                    break;
                }
                used_bits |= a[i];
                current_count++;
            }
        }

        if (valid) {
            max_size = max(max_size, current_count);
        }
    }

    cout << max_size << "\n";
    return 0;
}
