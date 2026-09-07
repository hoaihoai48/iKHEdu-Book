#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K;
    if (!(cin >> N >> K)) return 0;
    vector<vector<long long>> S(N + 1, vector<long long>(K + 1, 0));
    S[0][0] = 1;
    for (int n = 1; n <= N; n++)
        for (int k = 1; k <= min(n, K); k++)
            S[n][k] = (S[n - 1][k - 1] + (long long)k * S[n - 1][k]) % MOD;
    cout << S[N][K] % MOD << "\n";
    return 0;
}
