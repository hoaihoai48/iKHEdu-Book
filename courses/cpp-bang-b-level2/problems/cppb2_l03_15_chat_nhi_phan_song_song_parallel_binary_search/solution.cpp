#include <bits/stdc++.h>
using namespace std;

struct Query {
    int l, r;
    long long target;
    int id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].l >> queries[i].r >> queries[i].target;
        queries[i].id = i;
    }

    for (int i = 0; i < q; ++i) {
        long long sum = 0;
        int ans = -1;
        for (int j = queries[i].l; j <= queries[i].r; ++j) {
            sum += a[j];
            if (sum >= queries[i].target) {
                ans = j;
                break;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
