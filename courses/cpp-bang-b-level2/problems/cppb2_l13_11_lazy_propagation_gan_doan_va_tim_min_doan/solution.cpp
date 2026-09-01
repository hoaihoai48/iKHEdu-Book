#include <bits/stdc++.h>
using namespace std;

struct Node {
    int count;
    Node *left, *right;
    Node(int c = 0) : count(c), left(nullptr), right(nullptr) {}
};

Node* build(int l, int r) {
    Node *node = new Node();
    if (l == r) return node;
    int mid = l + (r - l) / 2;
    node->left = build(l, mid);
    node->right = build(mid + 1, r);
    return node;
}

Node* update_pst(Node *prev, int l, int r, int idx) {
    Node *node = new Node(prev->count + 1);
    node->left = prev->left;
    node->right = prev->right;
    if (l == r) return node;
    int mid = l + (r - l) / 2;
    if (idx <= mid) node->left = update_pst(prev->left, l, mid, idx);
    else node->right = update_pst(prev->right, mid + 1, r, idx);
    return node;
}

int query_kth(Node *left_root, Node *right_root, int l, int r, int k) {
    if (l == r) return l;
    int count = right_root->left->count - left_root->left->count;
    int mid = l + (r - l) / 2;
    if (count >= k) return query_kth(left_root->left, right_root->left, l, mid, k);
    else return query_kth(left_root->right, right_root->right, mid + 1, r, k - count);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<long long> vals(a.begin() + 1, a.end());
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    int sz = vals.size();
    vector<Node*> roots(n + 1);
    roots[0] = build(1, sz);

    for (int i = 1; i <= n; ++i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        roots[i] = update_pst(roots[i - 1], 1, sz, rank);
    }

    while (q--) {
        int l, r, k; cin >> l >> r >> k;
        int rank = query_kth(roots[l - 1], roots[r], 1, sz, k);
        cout << vals[rank - 1] << "\n";
    }
    return 0;
}
