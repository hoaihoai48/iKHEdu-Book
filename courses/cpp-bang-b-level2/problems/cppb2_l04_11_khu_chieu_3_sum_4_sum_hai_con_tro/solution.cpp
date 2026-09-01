#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target;
    if (!(cin >> n >> target)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int count = 0;
    for (int i = 0; i < n - 2; ++i) {
        int l = i + 1, r = n - 1;
        while (l < r) {
            long long sum = a[i] + a[l] + a[r];
            if (sum == target) {
                count++;
                l++; r--;
            } else if (sum < target) {
                l++;
            } else {
                r--;
            }
        }
    }

    cout << count << "\n";
    return 0;
}
