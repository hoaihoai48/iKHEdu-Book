#include <bits/stdc++.h>
using namespace std;

// Convex Hull Trick (CHT) dùng vector<long long> m_line, c_line
vector<long long> m_line, c_line;

double intersect(int i, int j) {
    return (double)(c_line[j] - c_line[i]) / (m_line[i] - m_line[j]);
}

long long eval_line(int i, long long x) {
    return m_line[i] * x + c_line[i];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    vector<long long> dp(n, 0);

    m_line.push_back(b[0]);
    c_line.push_back(0);
    int ptr = 0;

    for (int i = 1; i < n; ++i) {
        long long x = a[i];
        while (ptr + 1 < (int)m_line.size() && eval_line(ptr + 1, x) <= eval_line(ptr, x)) {
            ptr++;
        }
        dp[i] = eval_line(ptr, x);

        long long cur_m = b[i], cur_c = dp[i];
        m_line.push_back(cur_m);
        c_line.push_back(cur_c);
        int sz = m_line.size();

        while (sz >= 3 && intersect(sz - 1, sz - 2) <= intersect(sz - 2, sz - 3)) {
            m_line.erase(m_line.end() - 2);
            c_line.erase(c_line.end() - 2);
            sz--;
            if (ptr >= (int)m_line.size()) ptr = m_line.size() - 1;
        }
    }

    cout << dp[n - 1] << "\n";
    return 0;
}
