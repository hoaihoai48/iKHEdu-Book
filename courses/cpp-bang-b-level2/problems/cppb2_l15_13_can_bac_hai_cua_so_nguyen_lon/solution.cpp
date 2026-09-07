#include <bits/stdc++.h>
using namespace std;
const int BASE = 1000000000;
using Big = vector<int>; // little-endian
int cmp(const Big &a, const Big &b) {
    if (a.size() != b.size()) return a.size() < b.size() ? -1 : 1;
    for (int i = (int)a.size() - 1; i >= 0; i--) if (a[i] != b[i]) return a[i] < b[i] ? -1 : 1;
    return 0;
}
Big fromStr(const string &s) {
    Big a;
    for (int i = (int)s.size(); i > 0; i -= 9) {
        int l = max(0, i - 9);
        a.push_back(stoi(s.substr(l, i - l)));
    }
    while (a.size() > 1 && a.back() == 0) a.pop_back();
    return a;
}
string toStr(const Big &a) {
    string s = to_string(a.back());
    char buf[16];
    for (int i = (int)a.size() - 2; i >= 0; i--) {
        // 9 digits with leading zeros
        int v = a[i];
        string t(9, '0');
        for (int z = 8; z >= 0; z--) { t[z] = char('0' + v % 10); v /= 10; }
        s += t;
    }
    (void)buf;
    return s;
}
Big addB(const Big &a, const Big &b) {
    Big c; c.reserve(max(a.size(), b.size()) + 1);
    long long carry = 0;
    for (size_t i = 0; i < max(a.size(), b.size()) || carry; i++) {
        long long v = carry;
        if (i < a.size()) v += a[i];
        if (i < b.size()) v += b[i];
        c.push_back(int(v % BASE)); carry = v / BASE;
    }
    return c;
}
Big div2B(const Big &a) {
    Big c(a.size());
    long long carry = 0;
    for (int i = (int)a.size() - 1; i >= 0; i--) {
        long long v = carry * BASE + a[i];
        c[i] = int(v / 2); carry = v % 2;
    }
    while (c.size() > 1 && c.back() == 0) c.pop_back();
    return c;
}
Big mulB(const Big &a, const Big &b) {
    if ((a.size() == 1 && a[0] == 0) || (b.size() == 1 && b[0] == 0)) return Big{0};
    vector<long long> t(a.size() + b.size(), 0);
    for (size_t i = 0; i < a.size(); i++)
        for (size_t j = 0; j < b.size(); j++) t[i + j] += (long long)a[i] * b[j];
    Big c(t.size());
    long long carry = 0;
    for (size_t i = 0; i < t.size(); i++) {
        long long v = t[i] + carry;
        c[i] = int(v % BASE); carry = v / BASE;
    }
    while (carry) { c.push_back(int(carry % BASE)); carry /= BASE; }
    while (c.size() > 1 && c.back() == 0) c.pop_back();
    return c;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    Big A = fromStr(s);
    int half = ((int)s.size() + 1) / 2;
    Big lo{0}, hi = fromStr(string("1") + string(half, '0'));
    while (cmp(lo, hi) < 0) {
        Big mid = div2B(addB(lo, hi));
        if (cmp(mid, lo) == 0) { // lo and hi adjacent: test hi directly
            if (cmp(mulB(hi, hi), A) <= 0) lo = hi;
            break;
        }
        if (cmp(mulB(mid, mid), A) <= 0) lo = mid;
        else {
            Big m = mid; // m = mid - 1 (mid >= 1 here)
            int i = 0;
            while (i < (int)m.size() && m[i] == 0) { m[i] = BASE - 1; i++; }
            if (i < (int)m.size()) m[i]--;
            while (m.size() > 1 && m.back() == 0) m.pop_back();
            hi = m;
        }
    }
    cout << toStr(lo) << "\n";
    return 0;
}
