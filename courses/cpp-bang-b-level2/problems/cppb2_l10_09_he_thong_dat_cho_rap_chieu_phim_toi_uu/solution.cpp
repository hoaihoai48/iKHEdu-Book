#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<tuple<int, int, int>> a(n);
    for (int i = 0; i < n; ++i) {
        int x, y, z; cin >> x >> y >> z;
        a[i] = make_tuple(x, y, z);
    }

    sort(a.begin(), a.end());

    for (const auto &t : a) {
        int x, y, z;
        tie(x, y, z) = t;
        cout << x << " " << y << " " << z << "\n";
    }
    return 0;
}
