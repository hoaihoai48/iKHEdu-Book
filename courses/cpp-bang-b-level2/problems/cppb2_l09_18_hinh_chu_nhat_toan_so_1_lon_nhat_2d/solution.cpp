#include <bits/stdc++.h>
using namespace std;

int largest_rectangle_histogram(const vector<int>& heights) {
    int n = heights.size();
    vector<int> left(n), right(n);
    vector<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && heights[st.back()] >= heights[i]) st.pop_back();
        left[i] = st.empty() ? 0 : st.back() + 1;
        st.push_back(i);
    }

    st.clear();
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && heights[st.back()] >= heights[i]) st.pop_back();
        right[i] = st.empty() ? n - 1 : st.back() - 1;
        st.push_back(i);
    }

    int max_area = 0;
    for (int i = 0; i < n; ++i) {
        max_area = max(max_area, heights[i] * (right[i] - left[i] + 1));
    }
    return max_area;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> matrix[i][j];
        }
    }

    vector<int> heights(m, 0);
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (matrix[i][j] == 1) heights[j]++;
            else heights[j] = 0;
        }
        ans = max(ans, largest_rectangle_histogram(heights));
    }

    cout << ans << "\n";
    return 0;
}
