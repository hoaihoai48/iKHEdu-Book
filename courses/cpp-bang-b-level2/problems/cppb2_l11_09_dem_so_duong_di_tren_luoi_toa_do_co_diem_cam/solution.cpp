#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> bell(n + 1, vector<long long>(n + 1, 0));
    bell[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        bell[i][0] = bell[i - 1][i - 1];
        for (int j = 1; j <= i; ++j) {
            bell[i][j] = (bell[i][j - 1] + bell[i - 1][j - 1]) % MOD;
        }
    }

    cout << bell[n][0] << "\n";
    return 0;
}
