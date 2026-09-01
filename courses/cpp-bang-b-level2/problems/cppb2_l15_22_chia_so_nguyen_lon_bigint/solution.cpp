#include <bits/stdc++.h>
using namespace std;

string divide_bigint(string a, long long b) {
    string res = "";
    long long rem = 0;
    for (char c : a) {
        rem = rem * 10 + (c - '0');
        res += to_string(rem / b);
        rem %= b;
    }
    int pos = 0;
    while (pos < (int)res.size() - 1 && res[pos] == '0') pos++;
    return res.substr(pos);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    cout << divide_bigint(a, b) << "\n";
    return 0;
}
