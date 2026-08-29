#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> cnt(k, 0);
    cnt[0] = 1; // P[0] = 0

    long long current_sum = 0;
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        current_sum += x;
        long long rem = (current_sum % k + k) % k;
        cnt[rem]++;
    }

    long long total_pairs = 0;
    for (int r = 0; r < k; ++r) {
        total_pairs += cnt[r] * (cnt[r] - 1) / 2;
    }

    cout << total_pairs << "\n";
    return 0;
}
