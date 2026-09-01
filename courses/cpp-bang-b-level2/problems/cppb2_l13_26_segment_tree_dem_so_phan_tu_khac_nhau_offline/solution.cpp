#include <bits/stdc++.h>
using namespace std;

// Đếm số phần tử phân biệt dùng vector<vector<int>>: {r, l, id}
const int MAXN = 200005;
int bit_tree[MAXN], a[MAXN], ans[MAXN];
int N;

void update_bit(int idx, int val) {
    for (; idx <= N; idx += idx & -idx) bit_tree[idx] += val;
}

int query_bit(int idx) {
    int sum = 0;
    for (; idx > 0; idx -= idx & -idx) sum += bit_tree[idx];
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> N >> q)) return 0;

    for (int i = 1; i <= N; ++i) cin >> a[i];

    vector<vector<int>> queries(q, vector<int>(3));
    for (int i = 0; i < q; ++i) {
        int l, r;
        cin >> l >> r;
        queries[i] = {r, l, i}; // Sắp xếp theo r
    }

    sort(queries.begin(), queries.end());

    map<int, int> last_pos;
    int cur_r = 1;

    for (const auto& qry : queries) {
        int r = qry[0], l = qry[1], id = qry[2];
        while (cur_r <= r) {
            if (last_pos.count(a[cur_r])) {
                update_bit(last_pos[a[cur_r]], -1);
            }
            last_pos[a[cur_r]] = cur_r;
            update_bit(cur_r, 1);
            cur_r++;
        }
        ans[id] = query_bit(r) - query_bit(l - 1);
    }

    for (int i = 0; i < q; ++i) cout << ans[i] << "\n";
    return 0;
}
