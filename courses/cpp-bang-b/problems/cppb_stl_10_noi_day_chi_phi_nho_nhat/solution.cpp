#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 1) { cout << 0 << "\n"; return 0; }

    priority_queue<long long, vector<long long>, greater<long long>> min_heap;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        min_heap.push(x);
    }

    long long total_cost = 0;
    while (min_heap.size() > 1) {
        long long a = min_heap.top(); min_heap.pop();
        long long b = min_heap.top(); min_heap.pop();
        long long sum = a + b;
        total_cost += sum;
        min_heap.push(sum);
    }

    cout << total_cost << "\n";
    return 0;
}
