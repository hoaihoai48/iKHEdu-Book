#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    stack<int> st;
    long long water = 0;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && h[i] > h[st.top()]) {
            int top = st.top(); st.pop();
            if (st.empty()) break;
            int dist = i - st.top() - 1;
            long long bounded_h = min(h[i], h[st.top()]) - h[top];
            water += dist * bounded_h;
        }
        st.push(i);
    }

    cout << water << "\n";
    return 0;
}
