#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> c(n + m);
    for (int i = 0; i < n; ++i) cin >> c[i];
    for (int j = 0; j < m; ++j) cin >> c[n + j];
    sort(c.begin(), c.end());
    int total = n + m;
    int k = (total % 2 == 1) ? (total / 2 + 1) : (total / 2);
    cout << c[k - 1] << "\n";
    return 0;
}
