#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> c(n + m);
    for (int i = 0; i < n; ++i) cin >> c[i];
    for (int j = 0; j < m; ++j) cin >> c[n + j];
    sort(c.begin(), c.end());
    for (int i = 0; i < n + m; ++i) cout << c[i] << (i + 1 == n + m ? "" : " ");
    cout << "\n";
    return 0;
}
