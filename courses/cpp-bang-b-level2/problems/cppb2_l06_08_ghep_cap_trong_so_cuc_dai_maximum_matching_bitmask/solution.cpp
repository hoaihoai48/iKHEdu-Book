#include <bits/stdc++.h>
using namespace std;

struct Node {
    int next[2];
    Node() { next[0] = next[1] = -1; }
};

vector<Node> trie;

void insert_val(long long val) {
    int u = 0;
    for (int b = 31; b >= 0; --b) {
        int bit = (val >> b) & 1;
        if (trie[u].next[bit] == -1) {
            trie[u].next[bit] = trie.size();
            trie.push_back(Node());
        }
        u = trie[u].next[bit];
    }
}

long long query_max_xor(long long val) {
    int u = 0;
    long long ans = 0;
    for (int b = 31; b >= 0; --b) {
        int bit = (val >> b) & 1;
        int opp = 1 - bit;
        if (trie[u].next[opp] != -1) {
            ans |= (1LL << b);
            u = trie[u].next[opp];
        } else {
            u = trie[u].next[bit];
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    trie.push_back(Node());
    insert_val(0);

    long long pref_xor = 0, max_xor = 0;
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        pref_xor ^= x;
        max_xor = max(max_xor, query_max_xor(pref_xor));
        insert_val(pref_xor);
    }

    cout << max_xor << "\n";
    return 0;
}
