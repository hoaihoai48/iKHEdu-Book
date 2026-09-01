#include <bits/stdc++.h>
using namespace std;

long long max_hist(const vector<long long> &h) {
    int n = h.size();
    stack<int> st;
    long long max_area = 0;
    for (int i = 0; i <= n; ++i) {
        long long cur_h = (i == n ? 0 : h[i]);
        while (!st.empty() && h[st.top()] >= cur_h) {
            long long height = h[st.top()];
            st.pop();
            long long width = st.empty() ? i : (i - st.top() - 1);
            max_area = max(max_area, height * width);
        }
        st.push(i);
    }
    return max_area;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> mat(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) cin >> mat[i][j];
    }

    vector<long long> h(m, 0);
    long long max_rec = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (mat[i][j] == 1) h[j]++;
            else h[j] = 0;
        }
        max_rec = max(max_rec, max_hist(h));
    }

    cout << max_rec << "\n";
    return 0;
}
