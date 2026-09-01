#include <bits/stdc++.h>
using namespace std;

struct Point {
    double x, y;
};

double dist(Point A, Point B) {
    return hypot(A.x - B.x, A.y - B.y);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> P(n);
    for (int i = 0; i < n; ++i) cin >> P[i].x >> P[i].y;

    Point Q;
    cin >> Q.x >> Q.y;

    auto get_d = [&](int idx) {
        return dist(P[idx], Q);
    };

    double max_dist = 0;
    for (int i = 0; i < n; ++i) {
        max_dist = max(max_dist, get_d(i));
    }

    cout << fixed << setprecision(6) << max_dist << "\n";
    return 0;
}
