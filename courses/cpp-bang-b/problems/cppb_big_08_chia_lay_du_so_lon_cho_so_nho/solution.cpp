#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    long long cur = 0;
    for (char c : a) {
        cur = (cur * 10 + (c - '0')) % b;
    }

    cout << cur << "\n";
    return 0;
}