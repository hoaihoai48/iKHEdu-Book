#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> nge(n, -1);
    stack<int> st;

    // Duyệt vòng tròn 2 vòng (2N)
    for (int i = 0; i < 2 * n; ++i) {
        while (!st.empty() && a[i % n] > a[st.top()]) {
            nge[st.top()] = a[i % n];
            st.pop();
        }
        if (i < n) st.push(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << nge[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
