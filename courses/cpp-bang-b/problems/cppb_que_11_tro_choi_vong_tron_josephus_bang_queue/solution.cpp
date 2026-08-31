#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0) return 0;

    queue<int> q;
    for (int i = 1; i <= n; ++i) q.push(i);

    while (q.size() > 1) {
        for (int i = 1; i < k; ++i) {
            q.push(q.front());
            q.pop();
        }
        q.pop(); // Loại bỏ người thứ k
    }

    cout << q.front() << "\n";
    return 0;
}
