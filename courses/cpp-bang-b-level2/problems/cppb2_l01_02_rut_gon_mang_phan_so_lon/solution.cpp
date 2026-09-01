#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    a = abs(a); b = abs(b);
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n; ++i) {
        long long num, den;
        cin >> num >> den;
        if (den < 0) {
            num = -num;
            den = -den;
        }
        long long g = gcd_val(num, den);
        cout << num / g << " " << den / g << "\n";
    }
    return 0;
}
