#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    stack<int> st;
    long long total_water = 0;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && h[i] > h[st.top()]) {
            int top = st.top();
            st.pop();
            if (st.empty()) break;

            int dist = i - st.top() - 1;
            long long bounded_height = min(h[i], h[st.top()]) - h[top];
            total_water += dist * bounded_height;
        }
        st.push(i);
    }

    cout << total_water << "\n";
    return 0;
}
