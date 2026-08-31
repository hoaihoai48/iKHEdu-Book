#include <bits/stdc++.h>
using namespace std;
long long gcdL(long long a, long long b) {
    while (b) { long long r = a % b; a = b; b = r; }
    return a;
}
void print128(__int128 n) {
    if (n == 0) { cout << 0; return; }
    string s = "";
    while (n > 0) { s.push_back(char('0' + (n % 10))); n /= 10; }
    reverse(s.begin(), s.end());
    cout << s;
}
int main() {
    long long a, b;
    if (!(cin >> a >> b)) return 0;
    long long g = gcdL(a, b);
    __int128 lcm = ((__int128)a / g) * b;
    cout << g << " ";
    print128(lcm);
    cout << "\n";
    return 0;
}
