#include <bits/stdc++.h>
using namespace std;
long long ipow10(int e) { long long r = 1; while (e--) r *= 10; return r; }
long long countLE(long long X) {
    if (X < 0) return 0;
    if (X == 0) return 1; // 0 is palindrome
    string s = to_string(X);
    int n = (int)s.size();
    long long ans = 1; // number 0
    for (int l = 1; l < n; l++) ans += 9 * ipow10((l - 1) / 2);
    long long half = (n + 1) / 2;
    long long pre = stoll(s.substr(0, half));
    long long base = ipow10(half - 1);
    ans += pre - base;
    string t = s.substr(0, half);
    string q = t;
    if (n % 2 == 1) q.pop_back();
    reverse(q.begin(), q.end());
    t += q;
    if (stoll(t) <= X) ans++;
    return ans;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long L, R;
    if (!(cin >> L >> R)) return 0;
    cout << countLE(R) - countLE(L - 1) << "\n";
    return 0;
}
