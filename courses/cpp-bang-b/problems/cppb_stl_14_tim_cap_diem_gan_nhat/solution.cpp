#include <bits/stdc++.h>
using namespace std;

struct Point {
    long long x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 1) { cout << 0 << "\n"; return 0; }

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

    sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        if (a.x != b.x) return a.x < b.x;
        return a.y < b.y;
    });

    long long min_dist_sq = LLONG_MAX;
    set<pair<long long, long long>> active_set; // Lưu (y, x)

    int left = 0;
    for (int i = 0; i < n; ++i) {
        long long d = ceil(sqrt(min_dist_sq));
        while (left < i && pts[i].x - pts[left].x >= d) {
            active_set.erase({pts[left].y, pts[left].x});
            left++;
        }

        auto it_low = active_set.lower_bound({pts[i].y - d, LLONG_MIN});
        auto it_high = active_set.upper_bound({pts[i].y + d, LLONG_MAX});

        for (auto it = it_low; it != it_high; ++it) {
            long long dy = pts[i].y - it->first;
            long long dx = pts[i].x - it->second;
            min_dist_sq = min(min_dist_sq, dx * dx + dy * dy);
        }

        active_set.insert({pts[i].y, pts[i].x});
    }

    cout << min_dist_sq << "\n";
    return 0;
}
