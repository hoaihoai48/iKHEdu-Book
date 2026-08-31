#include <bits/stdc++.h>
using namespace std;
int main() {
    long long n;
    if (!(cin >> n)) return 0;
    string s = to_string(n);
    long long sum = 0;
    for (char c : s) sum += c - '0';
    cout << s.size() << " " << sum << "\n";
    return 0;
}
