#include <bits/stdc++.h>
using namespace std;
int cmpStr(const string &a, const string &b) {
    if (a.size() != b.size()) return a.size() < b.size() ? -1 : 1;
    if (a == b) return 0;
    return a < b ? -1 : 1;
}
string stripL(const string &s) {
    size_t i = 0;
    while (i + 1 < s.size() && s[i] == '0') i++;
    return s.substr(i);
}
string mulSmall(const string &a, int d) {
    if (d == 0) return "0";
    string r(a.size() + 2, '0');
    int carry = 0, n = (int)a.size();
    for (int i = n - 1, k = (int)r.size() - 1; i >= 0; i--, k--) {
        int v = (a[i] - '0') * d + carry;
        r[k] = char('0' + v % 10); carry = v / 10;
    }
    r[0] = char('0' + carry / 10); r[1] = char('0' + carry % 10);
    return stripL(r);
}
string subStr(const string &a, const string &b) { // a >= b
    string r = a;
    int i = (int)r.size() - 1, j = (int)b.size() - 1, borrow = 0;
    while (j >= 0 || borrow) {
        int v = (r[i] - '0') - borrow - (j >= 0 ? b[j] - '0' : 0);
        if (v < 0) { v += 10; borrow = 1; } else borrow = 0;
        r[i] = char('0' + v); i--; j--;
    }
    return stripL(r);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string A, B;
    if (!(cin >> A)) return 0;
    cin >> B;
    A = stripL(A); B = stripL(B);
    if (cmpStr(A, B) < 0) { cout << 0 << "\n" << A << "\n"; return 0; }
    string Q, cur = "0";
    for (char c : A) {
        cur = stripL(cur + string(1, c));
        int d = 0;
        // binary search digit 0..9
        int lo = 0, hi = 9;
        while (lo <= hi) {
            int m = (lo + hi) / 2;
            if (cmpStr(mulSmall(B, m), cur) <= 0) { d = m; lo = m + 1; } else hi = m - 1;
        }
        Q.push_back(char('0' + d));
        cur = subStr(cur, mulSmall(B, d));
    }
    cout << stripL(Q) << "\n" << stripL(cur) << "\n";
    return 0;
}
