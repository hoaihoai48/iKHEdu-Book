#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<array<int, 2>> trie;
    trie.push_back({-1, -1});
    auto insert_val = [&](long long val) {
        int u = 0;
        for (int b = 30; b >= 0; --b) {
            int bit = (int)((val >> b) & 1LL);
            if (trie[u][bit] == -1) {
                trie[u][bit] = (int)trie.size();
                trie.push_back({-1, -1});
            }
            u = trie[u][bit];
        }
    };
    auto query_max = [&](long long val) {
        int u = 0;
        long long ans = 0;
        for (int b = 30; b >= 0; --b) {
            int bit = (int)((val >> b) & 1LL);
            int opp = 1 - bit;
            if (trie[u][opp] != -1) {
                ans |= (1LL << b);
                u = trie[u][opp];
            } else {
                u = trie[u][bit];
            }
        }
        return ans;
    };
    insert_val(0);
    long long pref = 0, best = 0;
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        pref ^= x;
        best = max(best, query_max(pref));
        insert_val(pref);
    }
    cout << best << "\n";
    return 0;
}
