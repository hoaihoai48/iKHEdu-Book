#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    unordered_set<long long> distinct_hashes;

    for (int i = 0; i < n; ++i) {
        long long h = 0;
        for (int j = i; j < n; ++j) {
            h = (h * BASE + s[j]) % MOD;
            distinct_hashes.insert(h);
        }
    }

    cout << distinct_hashes.size() << "\n";
    return 0;
}
