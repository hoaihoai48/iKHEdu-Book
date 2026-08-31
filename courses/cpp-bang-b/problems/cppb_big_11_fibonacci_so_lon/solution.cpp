#include <bits/stdc++.h>
using namespace std;

string addBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string res = "";
    int carry = 0;
    int n = max(a.size(), b.size());
    for (int i = 0; i < n || carry; ++i) {
        int sum = carry;
        if (i < (int)a.size()) sum += a[i] - '0';
        if (i < (int)b.size()) sum += b[i] - '0';
        res.push_back((sum % 10) + '0');
        carry = sum / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n == 0) { cout << "0\n"; return 0; }
    if (n == 1) { cout << "1\n"; return 0; }

    string f0 = "0", f1 = "1", f2 = "";
    for (int i = 2; i <= n; ++i) {
        f2 = addBig(f0, f1);
        f0 = f1;
        f1 = f2;
    }

    cout << f1 << "\n";
    return 0;
}