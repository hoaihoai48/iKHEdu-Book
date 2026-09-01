#include <bits/stdc++.h>
using namespace std;

struct Point {
    long long x, y;
};

double dist(Point a, Point b) {
    return hypot(a.x - b.x, a.y - b.y);
}

double closest_pair(vector<Point> &pts, int l, int r) {
    if (r - l <= 3) {
        double d = 1e18;
        for (int i = l; i <= r; ++i) {
            for (int j = i + 1; j <= r; ++j) {
                d = min(d, dist(pts[i], pts[j]));
            }
        }
        return d;
    }

    int mid = l + (r - l) / 2;
    long long mid_x = pts[mid].x;

    double d = min(closest_pair(pts, l, mid), closest_pair(pts, mid + 1, r));

    vector<Point> strip;
    for (int i = l; i <= r; ++i) {
        if (abs(pts[i].x - mid_x) < d) strip.push_back(pts[i]);
    }

    sort(strip.begin(), strip.end(), [](Point a, Point b) { return a.y < b.y; });

    for (size_t i = 0; i < strip.size(); ++i) {
        for (size_t j = i + 1; j < strip.size() && (strip[j].y - strip[i].y) < d; ++j) {
            d = min(d, dist(strip[i], strip[j]));
        }
    }
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

    sort(pts.begin(), pts.end(), [](Point a, Point b) { return a.x < b.x; });

    cout << fixed << setprecision(6) << closest_pair(pts, 0, n - 1) << "\n";
    return 0;
}
