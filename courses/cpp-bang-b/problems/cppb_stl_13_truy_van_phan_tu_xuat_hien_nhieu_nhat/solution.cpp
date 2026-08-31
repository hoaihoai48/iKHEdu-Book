#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    map<long long, int> freq;
    long long best_val = -1;
    int max_freq = 0;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        freq[x]++;
        if (freq[x] > max_freq || (freq[x] == max_freq && x < best_val)) {
            max_freq = freq[x];
            best_val = x;
        }
    }

    cout << best_val << " " << max_freq << "\n";
    return 0;
}
