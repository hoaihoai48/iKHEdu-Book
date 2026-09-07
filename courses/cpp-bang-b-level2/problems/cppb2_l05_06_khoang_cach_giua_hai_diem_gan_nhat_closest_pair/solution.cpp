#include <bits/stdc++.h>
using namespace std;

vector<vector<long long>> pts, tmp;

long double dist2(const vector<long long> &a, const vector<long long> &b) {
    long double dx = (long double)a[0] - (long double)b[0];
    long double dy = (long double)a[1] - (long double)b[1];
    return dx * dx + dy * dy;
}

long double rec(int l, int r) {
    int n = r - l;
    if (n <= 3) {
        long double best = 4e37L;
        for (int i = l; i < r; ++i)
            for (int j = i + 1; j < r; ++j)
                best = min(best, dist2(pts[i], pts[j]));
        sort(pts.begin() + l, pts.begin() + r,
             [](const vector<long long> &a, const vector<long long> &b) { return a[1] < b[1]; });
        return best;
    }
    int m = l + n / 2;
    long long midx = pts[m][0];
    long double d = min(rec(l, m), rec(m, r));
    merge(pts.begin() + l, pts.begin() + m, pts.begin() + m, pts.begin() + r, tmp.begin(),
          [](const vector<long long> &a, const vector<long long> &b) { return a[1] < b[1]; });
    copy(tmp.begin(), tmp.begin() + n, pts.begin() + l);
    int tsz = 0;
    for (int i = l; i < r; ++i) {
        long double dx = (long double)pts[i][0] - (long double)midx;
        if (dx * dx < d) tmp[tsz++] = pts[i];
    }
    for (int i = 0; i < tsz; ++i) {
        for (int j = i + 1; j < tsz; ++j) {
            long double dy = (long double)tmp[j][1] - (long double)tmp[i][1];
            if (dy * dy >= d) break;
            d = min(d, dist2(tmp[i], tmp[j]));
        }
    }
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    pts.assign(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) cin >> pts[i][0] >> pts[i][1];
    sort(pts.begin(), pts.end());
    tmp.assign(n, vector<long long>(2));
    long double best = rec(0, n);
    cout << fixed << setprecision(6) << (double)sqrtl(best) << "\n";
    return 0;
}
