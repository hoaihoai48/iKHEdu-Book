#include <bits/stdc++.h>
using namespace std;

// Phân tích hoán vị thành các chu trình rời rạc và tính chu kỳ lặp
long long gcd_val(long long a, long long b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

long long lcm_val(long long a, long long b) {
    return (a / gcd_val(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1);
    for (int i = 1; i <= n; ++i) cin >> p[i];

    vector<bool> visited(n + 1, false);
    long long total_lcm = 1;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            int len = 0, cur = i;
            while (!visited[cur]) {
                visited[cur] = true;
                cur = p[cur];
                len++;
            }
            total_lcm = lcm_val(total_lcm, len);
        }
    }

    cout << total_lcm << "\n";
    return 0;
}
