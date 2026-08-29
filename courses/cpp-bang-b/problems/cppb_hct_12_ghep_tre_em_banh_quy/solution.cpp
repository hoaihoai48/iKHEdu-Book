#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> g(n), s(m);
    for (int i = 0; i < n; ++i) cin >> g[i];
    for (int i = 0; i < m; ++i) cin >> s[i];

    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    int i = 0, j = 0;
    int satisfied = 0;

    while (i < n && j < m) {
        if (s[j] >= g[i]) {
            ++satisfied;
            ++i;
            ++j;
        } else {
            ++j;
        }
    }

    cout << satisfied << "\n";
    return 0;
}
