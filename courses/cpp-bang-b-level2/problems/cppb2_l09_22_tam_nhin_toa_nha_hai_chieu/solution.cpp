#include <bits/stdc++.h>
using namespace std;

// Đếm số lượng tòa nhà mà mỗi vị trí có thể nhìn thấy (trái + phải)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    vector<int> left_vis(n, 0), right_vis(n, 0);
    vector<int> st;

    for (int i = 0; i < n; ++i) {
        left_vis[i] = st.size();
        while (!st.empty() && h[st.back()] <= h[i]) st.pop_back();
        st.push_back(i);
    }

    st.clear();
    for (int i = n - 1; i >= 0; --i) {
        right_vis[i] = st.size();
        while (!st.empty() && h[st.back()] <= h[i]) st.pop_back();
        st.push_back(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << left_vis[i] + right_vis[i] + 1 << " ";
    }
    cout << "\n";
    return 0;
}
