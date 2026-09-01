#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a_str;
    long long b;
    if (!(cin >> a_str >> b)) return 0;

    long long rem = 0;
    for (char c : a_str) {
        rem = (rem * 10 + (c - '0')) % b;
    }

    cout << rem << "\n";
    cout << gcd_val(b, rem) << "\n";
    return 0;
}
