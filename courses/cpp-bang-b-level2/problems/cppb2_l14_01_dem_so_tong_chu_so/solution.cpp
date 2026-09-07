#include <bits/stdc++.h>
using namespace std;

long long Kglob;
vector<int> dig;
long long memo[20][185];
bool vis[20][185];

long long dfs(int pos, int sum, bool tight) {
    if (sum > Kglob) return 0;
    if (pos == (int)dig.size()) return (sum == Kglob) ? 1 : 0;
    if (!tight && vis[pos][sum]) return memo[pos][sum];
    int lim = tight ? dig[pos] : 9;
    long long res = 0;
    for (int d = 0; d <= lim; ++d) {
        res += dfs(pos + 1, sum + d, tight && (d == lim));
    }
    if (!tight) {
        vis[pos][sum] = true;
        memo[pos][sum] = res;
    }
    return res;
}

long long countLE(long long x) {
    if (x <= 0) return 0;
    dig.clear();
    string s = to_string(x);
    for (char c : s) dig.push_back(c - '0');
    memset(vis, 0, sizeof(vis));
    return dfs(0, 0, true);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    long long K;
    if (!(cin >> L >> R >> K)) return 0;
    Kglob = K;

    cout << countLE(R) - countLE(L - 1) << "\n";
    return 0;
}
