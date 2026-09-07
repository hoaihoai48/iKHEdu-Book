#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<pair<long long, long long>> segs(n);
    for (int i = 0; i < n; ++i) cin >> segs[i].first >> segs[i].second;
    sort(segs.begin(), segs.end());
    long long cl = segs[0].first, cr = segs[0].second;
    for (int i = 1; i < n; ++i) {
        if (segs[i].first <= cr) {
            cr = max(cr, segs[i].second);
        } else {
            cout << cl << ' ' << cr << "\n";
            cl = segs[i].first;
            cr = segs[i].second;
        }
    }
    cout << cl << ' ' << cr << "\n";
    return 0;
}
