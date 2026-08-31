#include <bits/stdc++.h>
using namespace std;
struct It { long long w, v; };
int main() {
    int n;
    long long max_w;
    if (!(cin >> n >> max_w)) return 0;
    vector<It> it(n);
    for (int i = 0; i < n; ++i) cin >> it[i].w >> it[i].v;
    long long mx = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        long long tw = 0, tv = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) { tw += it[i].w; tv += it[i].v; }
        }
        if (tw <= max_w) mx = max(mx, tv);
    }
    cout << mx << "\n";
    return 0;
}
