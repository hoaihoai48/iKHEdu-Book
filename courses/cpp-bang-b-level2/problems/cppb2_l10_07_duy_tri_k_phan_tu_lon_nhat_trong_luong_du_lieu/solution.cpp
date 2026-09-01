#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<long long> max_heap; // Nửa nhỏ
    priority_queue<long long, vector<long long>, greater<long long>> min_heap; // Nửa lớn

    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        if (max_heap.empty() || x <= max_heap.top()) max_heap.push(x);
        else min_heap.push(x);

        if (max_heap.size() > min_heap.size() + 1) {
            min_heap.push(max_heap.top());
            max_heap.pop();
        } else if (min_heap.size() > max_heap.size()) {
            max_heap.push(min_heap.top());
            min_heap.pop();
        }

        cout << max_heap.top() << "\n";
    }
    return 0;
}
