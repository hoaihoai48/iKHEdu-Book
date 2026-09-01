#include <bits/stdc++.h>
using namespace std;

map<pair<int, long long>, long long> memo[20][2];
string S;
long long Target_P;

long long solve(int idx, long long current_prod, bool tight, bool leading_zero) {
    if (current_prod > Target_P || (Target_P % max(1LL, current_prod) != 0)) return 0;
    if (idx == (int)S.size()) {
        return (!leading_zero && current_prod == Target_P) ? 1 : 0;
    }
    if (memo[idx][tight].count({leading_zero, current_prod})) {
        return memo[idx][tight][{leading_zero, current_prod}];
    }

    int limit = tight ? (S[idx] - '0') : 9;
    long long ans = 0;

    for (int d = 0; d <= limit; ++d) {
        bool next_tight = tight && (d == limit);
        if (leading_zero) {
            if (d == 0) {
                ans += solve(idx + 1, 0, next_tight, true);
            } else {
                ans += solve(idx + 1, d, next_tight, false);
            }
        } else {
            ans += solve(idx + 1, current_prod * d, next_tight, false);
        }
    }

    return memo[idx][tight][{leading_zero, current_prod}] = ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, P;
    if (!(cin >> N >> P)) return 0;

    S = to_string(N);
    Target_P = P;
    for (int i = 0; i < 20; ++i) {
        memo[i][0].clear();
        memo[i][1].clear();
    }

    cout << solve(0, 0, true, true) << "\n";
    return 0;
}
