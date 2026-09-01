#include <bits/stdc++.h>
using namespace std;

// Ternary Search tìm cực tiểu hàm lồi f(x)
double f(double x, double a, double b, double c) {
    return a * x * x + b * x + c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double a, b, c, left_bound, right_bound;
    if (!(cin >> a >> b >> c >> left_bound >> right_bound)) return 0;

    for (int iter = 0; iter < 100; ++iter) {
        double m1 = left_bound + (right_bound - left_bound) / 3.0;
        double m2 = right_bound - (right_bound - left_bound) / 3.0;
        if (f(m1, a, b, c) < f(m2, a, b, c)) {
            right_bound = m2;
        } else {
            left_bound = m1;
        }
    }

    cout << fixed << setprecision(6) << left_bound << "\n";
    return 0;
}
