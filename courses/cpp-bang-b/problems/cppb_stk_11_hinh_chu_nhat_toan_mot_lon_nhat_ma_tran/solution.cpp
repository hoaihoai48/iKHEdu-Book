#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    vector<int> h(m, 0);
    int max_area = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '1') h[j]++;
            else h[j] = 0;
        }

        // Monotonic stack on row histogram
        vector<int> cur_h = h;
        cur_h.push_back(0);
        stack<int> st;

        for (int j = 0; j <= m; ++j) {
            while (!st.empty() && cur_h[j] < cur_h[st.top()]) {
                int height = cur_h[st.top()];
                st.pop();
                int width = st.empty() ? j : (j - st.top() - 1);
                max_area = max(max_area, height * width);
            }
            st.push(j);
        }
    }

    cout << max_area << "\n";
    return 0;
}
