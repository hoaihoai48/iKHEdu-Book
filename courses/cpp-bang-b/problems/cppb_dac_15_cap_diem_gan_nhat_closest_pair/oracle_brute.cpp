#include <bits/stdc++.h>
using namespace std;
struct P { long long x, y; };
int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<P> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i].x >> p[i].y;
    long long mn = 4e18;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            long long d = (p[i].x - p[j].x)*(p[i].x - p[j].x) + (p[i].y - p[j].y)*(p[i].y - p[j].y);
            mn = min(mn, d);
        }
    }
    cout << mn << "\n";
    return 0;
}
