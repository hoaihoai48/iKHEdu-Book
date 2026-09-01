#include <bits/stdc++.h>
using namespace std;

bool verify_preorder_bst(const vector<int> &a) {
    stack<int> st;
    int root = -1e9;
    for (int x : a) {
        if (x < root) return false;
        while (!st.empty() && st.top() < x) {
            root = st.top();
            st.pop();
        }
        st.push(x);
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << (verify_preorder_bst(a) ? "YES" : "NO") << "\n";
    return 0;
}
