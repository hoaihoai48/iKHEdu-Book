#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    int next[26];
    bool is_end;
    TrieNode() {
        memset(next, -1, sizeof(next));
        is_end = false;
    }
};

vector<TrieNode> trie;

void insert_str(const string &s) {
    int u = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (trie[u].next[idx] == -1) {
            trie[u].next[idx] = trie.size();
            trie.push_back(TrieNode());
        }
        u = trie[u].next[idx];
    }
    trie[u].is_end = true;
}

bool search_str(const string &s) {
    int u = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (trie[u].next[idx] == -1) return false;
        u = trie[u].next[idx];
    }
    return trie[u].is_end;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    trie.push_back(TrieNode());
    for (int i = 0; i < n; ++i) {
        string w; cin >> w;
        insert_str(w);
    }

    while (q--) {
        string qry; cin >> qry;
        cout << (search_str(qry) ? "YES" : "NO") << "\n";
    }
    return 0;
}
