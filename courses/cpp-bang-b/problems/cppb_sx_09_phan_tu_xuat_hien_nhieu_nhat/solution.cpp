#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long best_val = a[0];
    int max_freq = 1;

    long long cur_val = a[0];
    int cur_freq = 1;

    for (int i = 1; i < n; ++i) {
        if (a[i] == cur_val) {
            ++cur_freq;
        } else {
            if (cur_freq > max_freq) {
                max_freq = cur_freq;
                best_val = cur_val;
            }
            cur_val = a[i];
            cur_freq = 1;
        }
    }
    if (cur_freq > max_freq) {
        max_freq = cur_freq;
        best_val = cur_val;
    }

    cout << best_val << " " << max_freq << "\n";
    return 0;
}
