#include <bits/stdc++.h>
using namespace std;

// Monotonic Deque tìm Max trong cửa sổ trượt độ dài K O(N)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> dq;
    for (int i = 0; i < n; ++i) {
        while (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
        dq.push_back(i);

        if (i >= k - 1) {
            cout << a[dq.front()] << " ";
        }
    }
    cout << "\n";
    return 0;
}
