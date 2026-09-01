#include <bits/stdc++.h>
using namespace std;

// Nối dây K đầu với chi phí nhỏ nhất bằng Priority Queue
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    priority_queue<long long, vector<long long>, greater<long long>> pq;
    for (int i = 0; i < n; ++i) {
        long long len;
        cin >> len;
        pq.push(len);
    }

    // Đệm thêm số 0 để số phần tử giảm đúng mỗi bước k-1
    while ((pq.size() - 1) % (k - 1) != 0) {
        pq.push(0);
    }

    long long total_cost = 0;
    while (pq.size() > 1) {
        long long sum = 0;
        for (int i = 0; i < k && !pq.empty(); ++i) {
            sum += pq.top();
            pq.pop();
        }
        total_cost += sum;
        pq.push(sum);
    }

    cout << total_cost << "\n";
    return 0;
}
