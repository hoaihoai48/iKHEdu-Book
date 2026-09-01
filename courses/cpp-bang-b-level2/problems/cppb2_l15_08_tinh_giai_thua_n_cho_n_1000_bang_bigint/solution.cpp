#include <bits/stdc++.h>
using namespace std;

string add_bigint(string a, string b) {
    string res = "";
    int i = a.size() - 1, j = b.size() - 1, carry = 0;
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';
        carry = sum / 10;
        res += to_string(sum % 10);
    }
    reverse(res.begin(), res.end());
    return res;
}

string mul_bigint(string a, string b) {
    if (a == "0" || b == "0") return "0";
    int n = a.size(), m = b.size();
    vector<int> res(n + m, 0);
    for (int i = n - 1; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            int mul = (a[i] - '0') * (b[j] - '0');
            int p1 = i + j, p2 = i + j + 1;
            int sum = mul + res[p2];
            res[p2] = sum % 10;
            res[p1] += sum / 10;
        }
    }
    string s = "";
    for (int val : res) if (!(s.empty() && val == 0)) s += to_string(val);
    return s.empty() ? "0" : s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    cout << add_bigint(a, b) << "\n";
    cout << mul_bigint(a, b) << "\n";
    return 0;
}
