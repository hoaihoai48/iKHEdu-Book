#include <bits/stdc++.h>
using namespace std;

int n;
long long S;
vector<long long> c;
long long best_coins = 1e9;

void branchAndBound(int idx, long long remain, long long count) {
    // Optimality Pruning
    if (count + (remain + c[0] - 1) / c[0] >= best_coins) return;

    if (remain == 0) {
        best_coins = min(best_coins, count);
        return;
    }
    if (idx >= n) return;

    long long max_use = remain / c[idx];
    for (long long k = max_use; k >= 0; --k) {
        if (count + k + (remain - k * c[idx] + c[0] - 1) / c[0] < best_coins) {
            branchAndBound(idx + 1, remain - k * c[idx], count + k);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> S)) return 0;
    c.resize(n);
    for (int i = 0; i < n; ++i) cin >> c[i];
    sort(c.rbegin(), c.rend());
    branchAndBound(0, S, 0);
    if (best_coins > 1e8) cout << -1 << "\n";
    else cout << best_coins << "\n";
    return 0;
}
