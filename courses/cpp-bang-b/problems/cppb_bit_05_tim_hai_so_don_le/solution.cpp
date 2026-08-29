#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_elements = 2 * n + 2;
    vector<long long> a(total_elements);
    long long xor_sum = 0;
    for (int i = 0; i < total_elements; ++i) {
        cin >> a[i];
        xor_sum ^= a[i];
    }

    // Lấy bit 1 phân biệt
    long long diff_bit = xor_sum & (-xor_sum);

    long long num1 = 0, num2 = 0;
    for (long long val : a) {
        if (val & diff_bit) {
            num1 ^= val;
        } else {
            num2 ^= val;
        }
    }

    if (num1 > num2) swap(num1, num2);
    cout << num1 << " " << num2 << "\n";
    return 0;
}
