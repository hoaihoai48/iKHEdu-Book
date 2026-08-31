#include <bits/stdc++.h>
using namespace std;
void h(int n, char a, char c, char b) {
    if (!n) return;
    h(n-1, a, b, c);
    cout << a << " -> " << c << "\n";
    h(n-1, b, c, a);
}
int main() {
    int n;
    if (!(cin >> n)) return 0;
    cout << (1 << n) - 1 << "\n";
    h(n, 'A', 'C', 'B');
    return 0;
}
