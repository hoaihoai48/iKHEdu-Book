#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q;
    if (!(cin >> Q)) return 0;
    vector<pair<int,int>> qs(Q);
    int mx = 0;
    for (int i = 0; i < Q; i++) { cin >> qs[i].first >> qs[i].second; mx = max(mx, qs[i].first); }
    vector<vector<long long>> S(mx + 1, vector<long long>(mx + 1, 0));
    S[0][0] = 1;
    for (int n = 1; n <= mx; n++)
        for (int k = 1; k <= n; k++)
            S[n][k] = (S[n - 1][k - 1] + (long long)k * S[n - 1][k]) % MOD;
    for (auto &q : qs) cout << S[q.first][q.second] % MOD << "\n";
    return 0;
}
