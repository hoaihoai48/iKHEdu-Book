#include <bits/stdc++.h>
using namespace std;

long long countPartitions(int remain, int max_val) {
    if (remain == 0) return 1;
    if (remain < 0 || max_val <= 0) return 0;
    // Chọn dùng max_val hoặc không dùng max_val
    return countPartitions(remain - max_val, max_val) + countPartitions(remain, max_val - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << countPartitions(n, n) << "\n";
    return 0;
}
