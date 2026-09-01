#include <bits/stdc++.h>
using namespace std;

// Căn bậc hai số nguyên lớn bằng Chặt nhị phân số lớn
bool compare_or_equal(string a, string b) {
    if (a.size() != b.size()) return a.size() > b.size();
    return a >= b;
}

string multiply_bigint(string a, string b) {
    int n = a.size(), m = b.size();
    vector<int> res(n + m, 0);
    for (int i = n - 1; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            res[i + j + 1] += (a[i] - '0') * (b[j] - '0');
        }
    }
    for (int i = n + m - 1; i > 0; --i) {
        res[i - 1] += res[i] / 10;
        res[i] %= 10;
    }
    string s = "";
    int pos = 0;
    while (pos < n + m - 1 && res[pos] == 0) pos++;
    for (int i = pos; i < n + m; ++i) s += to_string(res[i]);
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    // Chặt nhị phân tìm căn bậc hai nguyên
    string ans = "0";
    // Triển khai tìm căn theo từng chữ số từ trái qua phải
    string cur = "";
    for (size_t i = 0; i < s.size(); ++i) {
        cur += s[i];
        for (int d = 9; d >= 0; --d) {
            string test_ans = ans + to_string(d);
            if (test_ans[0] == '0' && test_ans.size() > 1) test_ans = test_ans.substr(1);
            if (compare_or_equal(s.substr(0, i + 1), multiply_bigint(test_ans, test_ans))) {
                ans = test_ans;
                break;
            }
        }
    }

    if (ans.empty()) ans = "0";
    cout << ans << "\n";
    return 0;
}
