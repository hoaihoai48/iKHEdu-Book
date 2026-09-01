#include <bits/stdc++.h>
using namespace std;

// Convex Hull Trick (CHT) tối ưu dp[i] = min(m_j * x_i + c_j)
struct Line {
    long long m, c;
    long long eval(long long x) { return m * x + c; }
    double intersect(const Line& o) const {
        return (double)(o.c - c) / (m - o.m);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    vector<Line> hull;
    vector<long long> dp(n, 0);

    hull.push_back({b[0], 0});
    int ptr = 0;

    for (int i = 1; i < n; ++i) {
        long long x = a[i];
        while (ptr + 1 < (int)hull.size() && hull[ptr + 1].eval(x) <= hull[ptr].eval(x)) {
            ptr++;
        }
        dp[i] = hull[ptr].eval(x);

        Line cur = {b[i], dp[i]};
        while (hull.size() >= 2 && cur.intersect(hull.back()) <= hull.back().intersect(hull[hull.size() - 2])) {
            hull.pop_back();
            if (ptr >= (int)hull.size()) ptr = hull.size() - 1;
        }
        hull.push_back(cur);
    }

    cout << dp[n - 1] << "\n";
    return 0;
}
