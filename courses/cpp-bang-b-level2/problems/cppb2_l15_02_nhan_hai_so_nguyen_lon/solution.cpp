#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string A, B;
    if (!(cin >> A)) return 0;
    cin >> B;
    if (A == "0" || B == "0") { cout << 0 << "\n"; return 0; }
    int n = (int)A.size(), m = (int)B.size();
    vector<int> a(n), b(m);
    for (int i = 0; i < n; i++) a[i] = A[n - 1 - i] - '0';
    for (int i = 0; i < m; i++) b[i] = B[m - 1 - i] - '0';
    vector<long long> r(n + m, 0);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) r[i + j] += (long long)a[i] * b[j];
    for (size_t i = 0; i + 1 < r.size(); i++) { r[i + 1] += r[i] / 10; r[i] %= 10; }
    while (r.size() > 1 && r.back() == 0) r.pop_back();
    for (int i = (int)r.size() - 1; i >= 0; i--) cout << char('0' + r[i]);
    cout << "\n";
    return 0;
}
