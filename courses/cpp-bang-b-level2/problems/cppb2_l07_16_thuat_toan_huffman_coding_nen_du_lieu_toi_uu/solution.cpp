#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long freq;
    Node *left, *right;
    Node(long long f) : freq(f), left(nullptr), right(nullptr) {}
};

struct Compare {
    bool operator()(Node *l, Node *r) {
        return l->freq > r->freq;
    }
};

long long get_wpl(Node *root, int depth) {
    if (!root) return 0;
    if (!root->left && !root->right) return root->freq * depth;
    return get_wpl(root->left, depth + 1) + get_wpl(root->right, depth + 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<Node*, vector<Node*>, Compare> pq;
    for (int i = 0; i < n; ++i) {
        long long f; cin >> f;
        pq.push(new Node(f));
    }

    while (pq.size() > 1) {
        Node *l = pq.top(); pq.pop();
        Node *r = pq.top(); pq.pop();
        Node *parent = new Node(l->freq + r->freq);
        parent->left = l;
        parent->right = r;
        pq.push(parent);
    }

    cout << get_wpl(pq.top(), 0) << "\n";
    return 0;
}
