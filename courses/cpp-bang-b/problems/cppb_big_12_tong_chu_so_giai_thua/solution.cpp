#include <bits/stdc++.h>
using namespace std;

string mulSmall(string a, int b) {
    reverse(a.begin(), a.end());
    string res = "";
    int carry = 0;
    for (int i = 0; i < (int)a.size() || carry; ++i) {
        int prod = carry;
        if (i < (int)a.size()) prod += (a[i] - '0') * b;
        res.push_back((prod % 10) + '0');
        carry = prod / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    string fact = "1";
    for (int i = 2; i <= n; ++i) {
        fact = mulSmall(fact, i);
    }

    long long sum_digits = 0;
    for (char c : fact) {
        sum_digits += (c - '0');
    }

    cout << sum_digits << "\n";
    return 0;
}