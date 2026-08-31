#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<int> bit;
    FenwickTree(int n) : n(n), bit(n + 1, 0) {}

    void update(int x, int val) {
        for (; x <= n; x += x & -x) bit[x] = max(bit[x], val);
    }

    int query(int x) {
        int max_val = 0;
        for (; x > 0; x -= x & -x) max_val = max(max_val, bit[x]);
        return max_val;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    int sz = vals.size();
    FenwickTree ft(sz);
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        int best_prev = ft.query(rank - 1);
        int cur_lis = best_prev + 1;
        ans = max(ans, cur_lis);
        ft.update(rank, cur_lis);
    }

    cout << ans << "\n";
    return 0;
}
