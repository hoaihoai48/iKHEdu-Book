#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    if (!(cin >> N)) return 0;
    vector<double> E(N + 7, 0.0);
    for (int x = N - 1; x >= 0; x--) {
        double s = 0;
        for (int d = 1; d <= 6; d++) s += E[x + d];
        E[x] = 1.0 + s / 6.0;
    }
    cout.setf(ios::fixed); cout << setprecision(6) << E[0] + 1e-12 << "\n";
    return 0;
}
