#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long N;
    if (!(cin >> N)) return 0;
    __int128 r = (__int128)N * (N - 1) * (N - 2) / 6;
    long long hi = (long long)(r / 1000000000000000000LL);
    if (hi == 0) { cout << (long long)r << "\n"; return 0; }
    string s;
    __int128 t = r;
    while (t > 0) { s.push_back(char('0' + t % 10)); t /= 10; }
    reverse(s.begin(), s.end());
    cout << s << "\n";
    return 0;
}
