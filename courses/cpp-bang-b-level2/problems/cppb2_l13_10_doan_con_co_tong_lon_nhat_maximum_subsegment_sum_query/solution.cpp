#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long sum;
    Node *left, *right;
    Node() : sum(0), left(nullptr), right(nullptr) {}
};

void update_dynamic(Node* &node, long long l, long long r, long long idx, long long val) {
    if (!node) node = new Node();
    node->sum += val;
    if (l == r) return;
    long long mid = l + (r - l) / 2;
    if (idx <= mid) update_dynamic(node->left, l, mid, idx, val);
    else update_dynamic(node->right, mid + 1, r, idx, val);
}

long long query_dynamic(Node *node, long long l, long long r, long long ql, long long qr) {
    if (!node || ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return node->sum;
    long long mid = l + (r - l) / 2;
    return query_dynamic(node->left, l, mid, ql, qr) + query_dynamic(node->right, mid + 1, r, ql, qr);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    Node *root = nullptr;
    long long MAXV = 1e18;

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            long long idx, val; cin >> idx >> val;
            update_dynamic(root, 1, MAXV, idx, val);
        } else {
            long long l, r; cin >> l >> r;
            cout << query_dynamic(root, 1, MAXV, l, r) << "\n";
        }
    }
    return 0;
}
