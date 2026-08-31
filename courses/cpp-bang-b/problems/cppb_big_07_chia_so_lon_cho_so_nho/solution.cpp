#include <bits/stdc++.h>
using namespace std;

string divSmall(string a, long long b) {
    string res = "";
    long long cur = 0;

    for (char c : a) {
        cur = cur * 10 + (c - '0');
        res.push_back((cur / b) + '0');
        cur %= b;
    }

    int pos = 0;
    while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
    return res.substr(pos);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    cout << divSmall(a, b) << "\n";
    return 0;
}