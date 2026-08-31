#include <bits/stdc++.h>
using namespace std;

string mulSmall(string a, long long b) {
    if (a == "0" || b == 0) return "0";

    reverse(a.begin(), a.end());
    string res = "";
    long long carry = 0;

    for (int i = 0; i < (int)a.size() || carry; ++i) {
        long long prod = carry;
        if (i < (int)a.size()) prod += 1LL * (a[i] - '0') * b;
        res.push_back((prod % 10) + '0');
        carry = prod / 10;
    }

    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    cout << mulSmall(a, b) << "\n";
    return 0;
}