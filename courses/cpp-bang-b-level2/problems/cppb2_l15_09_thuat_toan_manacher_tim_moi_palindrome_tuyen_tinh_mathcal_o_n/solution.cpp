#include <bits/stdc++.h>
using namespace std;

const long long BASE1 = 311, MOD1 = 1000000007;
const long long BASE2 = 317, MOD2 = 1000000009;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    set<pair<long long, long long>> hashes;

    for (int i = 0; i < n; ++i) {
        string s; cin >> s;
        long long h1 = 0, h2 = 0;
        for (char c : s) {
            h1 = (h1 * BASE1 + c) % MOD1;
            h2 = (h2 * BASE2 + c) % MOD2;
        }
        hashes.insert({h1, h2});
    }

    cout << hashes.size() << "\n";
    return 0;
}
