#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    const int MAX_VAL = 4096;
    vector<long long> cnt(MAX_VAL, 0);

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    long long total_pairs = 0;

    // Trường hợp u == 0
    total_pairs += cnt[0] * (cnt[0] - 1) / 2;
    for (int v = 1; v < MAX_VAL; ++v) {
        total_pairs += cnt[0] * cnt[v];
    }

    // Trường hợp 1 <= u < v
    for (int u = 1; u < MAX_VAL; ++u) {
        if (cnt[u] == 0) continue;
        for (int v = u + 1; v < MAX_VAL; ++v) {
            if ((u & v) == 0) {
                total_pairs += cnt[u] * cnt[v];
            }
        }
    }

    cout << total_pairs << "\n";
    return 0;
}
