#include <bits/stdc++.h>
using namespace std;

struct Node {
    int next[26], link;
    bool is_word;
    Node() {
        memset(next, -1, sizeof(next));
        link = 0;
        is_word = false;
    }
};

vector<Node> trie;

void insert_word(const string &s) {
    int u = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (trie[u].next[idx] == -1) {
            trie[u].next[idx] = trie.size();
            trie.push_back(Node());
        }
        u = trie[u].next[idx];
    }
    trie[u].is_word = true;
}

void build_ac() {
    queue<int> q;
    for (int c = 0; c < 26; ++c) {
        if (trie[0].next[c] != -1) q.push(trie[0].next[c]);
        else trie[0].next[c] = 0;
    }
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int c = 0; c < 26; ++c) {
            if (trie[u].next[c] != -1) {
                int v = trie[u].next[c];
                trie[v].link = trie[trie[u].link].next[c];
                trie[v].is_word |= trie[trie[v].link].is_word;
                q.push(v);
            } else {
                trie[u].next[c] = trie[trie[u].link].next[c];
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    trie.push_back(Node());
    for (int i = 0; i < k; ++i) {
        string w; cin >> w;
        insert_word(w);
    }
    build_ac();

    string text; cin >> text;
    int u = 0, matches = 0;
    for (char c : text) {
        u = trie[u].next[c - 'a'];
        if (trie[u].is_word) matches++;
    }

    cout << matches << "\n";
    return 0;
}
