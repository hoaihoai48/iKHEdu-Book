#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    if (!(cin >> n)) return 0;
    long long c[15][15];
    for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) cin >> c[i][j];
    vector<int> p(n);
    iota(p.begin(), p.end(), 1);
    long long best = 1e18;
    do {
        long long sum = 0;
        for (int i = 0; i < n; ++i) sum += c[i + 1][p[i]];
        best = min(best, sum);
    } while (next_permutation(p.begin(), p.end()));
    cout << best << "\n";
    return 0;
}
