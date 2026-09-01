#include <bits/stdc++.h>
using namespace std;
double f(double x) { return (x - 5) * (x - 5) + 3; }
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); double l, r; if (!(cin >> l >> r)) return 0; for (int iter = 0; iter < 100; ++iter) { double m1 = l + (r - l) / 3; double m2 = r - (r - l) / 3; if (f(m1) < f(m2)) r = m2; else l = m1; } cout << fixed << setprecision(6) << (l + r) / 2 << "
"; return 0; }
