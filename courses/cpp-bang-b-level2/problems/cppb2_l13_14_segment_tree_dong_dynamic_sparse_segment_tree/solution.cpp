#include <bits/stdc++.h>
using namespace std;

int block_sz;

struct Query {
    int l, r, id;
    bool operator<(const Query &other) const {
        if (l / block_sz != other.l / block_sz) return l / block_sz < other.l / block_sz;
        return (l / block_sz) % 2 ? r < other.r : r > other.r;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    block_sz = sqrt(n) + 1;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].l >> queries[i].r;
        queries[i].id = i;
    }

    sort(queries.begin(), queries.end());

    vector<int> freq(1000005, 0);
    vector<int> ans(q);
    int cur_l = 1, cur_r = 0, distinct = 0;

    for (const auto &qry : queries) {
        while (cur_l > qry.l) {
            cur_l--;
            if (freq[a[cur_l]]++ == 0) distinct++;
        }
        while (cur_r < qry.r) {
            cur_r++;
            if (freq[a[cur_r]]++ == 0) distinct++;
        }
        while (cur_l < qry.l) {
            if (--freq[a[cur_l]] == 0) distinct--;
            cur_l++;
        }
        while (cur_r > qry.r) {
            if (--freq[a[cur_r]] == 0) distinct--;
            cur_r--;
        }
        ans[qry.id] = distinct;
    }

    for (int i = 0; i < q; ++i) cout << ans[i] << "\n";
    return 0;
}
