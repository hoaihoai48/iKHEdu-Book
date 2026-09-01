#include <bits/stdc++.h>
using namespace std;

// Thuật toán Aho-Corasick tìm kiếm đồng thời K mẫu trong văn bản O(N + \sum |P|)
const int MAX_NODES = 100005;
int trie[MAX_NODES][26], fail[MAX_NODES], term[MAX_NODES], node_count = 1;

void insert(const string& s, int id) {
    int u = 0;
    for (char c : s) {
        int idx = c - 'a';
        if (!trie[u][idx]) trie[u][idx] = node_count++;
        u = trie[u][idx];
    }
    term[u]++;
}

void build_aho() {
    queue<int> q;
    for (int c = 0; c < 26; ++c) {
        if (trie[0][c]) q.push(trie[0][c]);
    }
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int c = 0; c < 26; ++c) {
            int v = trie[u][c];
            if (v) {
                fail[v] = trie[fail[u]][c];
                term[v] += term[fail[v]];
                q.push(v);
            } else {
                trie[u][c] = trie[fail[u]][c];
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string text;
    int k;
    if (!(cin >> text >> k)) return 0;

    for (int i = 0; i < k; ++i) {
        string p;
        cin >> p;
        insert(p, i);
    }

    build_aho();

    int u = 0;
    long long total_matches = 0;
    for (char c : text) {
        u = trie[u][c - 'a'];
        total_matches += term[u];
    }

    cout << total_matches << "\n";
    return 0;
}
