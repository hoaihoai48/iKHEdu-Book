#include <bits/stdc++.h>
using namespace std;

struct Query {
    int l, r, id;
};

struct FenwickTree {
    int n;
    vector<int> tree;
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].l >> queries[i].r;
        queries[i].id = i;
    }

    sort(queries.begin(), queries.end(), [](const Query &x, const Query &y) {
        return x.r < y.r;
    });

    FenwickTree bit(n);
    map<int, int> last_pos;
    vector<int> ans(q);
    int cur_r = 1;

    for (const auto &qry : queries) {
        while (cur_r <= qry.r) {
            if (last_pos.count(a[cur_r])) {
                bit.update(last_pos[a[cur_r]], -1);
            }
            bit.update(cur_r, 1);
            last_pos[a[cur_r]] = cur_r;
            cur_r++;
        }
        ans[qry.id] = bit.query(qry.r) - bit.query(qry.l - 1);
    }

    for (int i = 0; i < q; ++i) cout << ans[i] << "\n";
    return 0;
}
