#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    int children[26];
    int count_words;
    int count_prefixes;
    TrieNode() {
        memset(children, -1, sizeof(children));
        count_words = 0;
        count_prefixes = 0;
    }
};

vector<TrieNode> trie;

void insert(const string& s) {
    int node = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (trie[node].children[idx] == -1) {
            trie[node].children[idx] = trie.size();
            trie.emplace_back();
        }
        node = trie[node].children[idx];
        trie[node].count_prefixes++;
    }
    trie[node].count_words++;
}

int query_prefix(const string& p) {
    int node = 0;
    for (char c : p) {
        int idx = c - 'a';
        if (trie[node].children[idx] == -1) return 0;
        node = trie[node].children[idx];
    }
    return trie[node].count_prefixes;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    trie.emplace_back(); // Node gốc 0

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        insert(s);
    }

    while (q--) {
        string p;
        cin >> p;
        cout << query_prefix(p) << "\n";
    }
    return 0;
}
