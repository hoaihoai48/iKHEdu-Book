#include <bits/stdc++.h>
using namespace std;

long long countBST(int n) {
    if (n <= 1) return 1;
    long long total = 0;
    for (int root = 1; root <= n; ++root) {
        int left_size = root - 1;
        int right_size = n - root;
        total += countBST(left_size) * countBST(right_size);
    }
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << countBST(n) << "\n";
    return 0;
}
