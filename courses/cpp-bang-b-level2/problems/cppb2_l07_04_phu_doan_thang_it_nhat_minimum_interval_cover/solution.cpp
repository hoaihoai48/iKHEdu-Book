#include <bits/stdc++.h>
using namespace std;

struct Seg {
    long long l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<Seg> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].l >> a[i].r;

    sort(a.begin(), a.end(), [](const Seg &x, const Seg &y) {
        if (x.l != y.l) return x.l < y.l;
        return x.r > y.r;
    });

    int count = 0;
    long long cur_end = 0;
    int i = 0;

    while (cur_end < L) {
        long long max_reach = cur_end;
        while (i < n && a[i].l <= cur_end) {
            max_reach = max(max_reach, a[i].r);
            i++;
        }
        if (max_reach == cur_end) {
            cout << "-1\n";
            return 0;
        }
        count++;
        cur_end = max_reach;
    }

    cout << count << "\n";
    return 0;
}
