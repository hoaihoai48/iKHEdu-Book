#include <bits/stdc++.h>
using namespace std;
struct Point { long long x, y; };
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<Point> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i].x >> p[i].y;
    long long min_d2 = 8e18;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            long long d2 = (p[i].x - p[j].x) * (p[i].x - p[j].x) + (p[i].y - p[j].y) * (p[i].y - p[j].y);
            min_d2 = min(min_d2, d2);
        }
    }
    cout << min_d2 << "\n";
    return 0;
}
