#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    set<long long> st;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        st.insert(x);
    }

    while (q--) {
        long long x;
        cin >> x;
        auto it = st.lower_bound(x);
        if (it == st.end()) {
            cout << -1 << "\n";
        } else {
            cout << *it << "\n";
        }
    }
    return 0;
}
