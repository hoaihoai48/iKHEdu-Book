#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    long long c[15][15];
    for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) cin >> c[i][j];
    vector<int> p;
    for (int i = 2; i <= n; ++i) p.push_back(i);
    long long best = 1e18;
    do {
        long long cost = c[1][p[0]];
        for (int i = 0; i < (int)p.size() - 1; ++i) cost += c[p[i]][p[i + 1]];
        cost += c[p.back()][1];
        best = min(best, cost);
    } while (next_permutation(p.begin(), p.end()));
    cout << best << "\n";
    return 0;
}
