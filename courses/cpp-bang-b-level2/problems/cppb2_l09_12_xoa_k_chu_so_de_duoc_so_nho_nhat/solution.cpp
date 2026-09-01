#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    stack<pair<long long, int>> st;
    long long count = 0;

    for (int i = 0; i < n; ++i) {
        int cnt = 1;
        while (!st.empty() && st.top().first <= h[i]) {
            count += st.top().second;
            if (st.top().first == h[i]) {
                cnt += st.top().second;
            }
            st.pop();
        }
        if (!st.empty()) count++;
        st.push({h[i], cnt});
    }

    cout << count << "\n";
    return 0;
}
