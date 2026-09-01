#include <bits/stdc++.h>
using namespace std;

int search_rotated(const vector<int> &a, int target) {
    int low = 0, high = a.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == target) return mid;

        if (a[low] <= a[mid]) {
            if (a[low] <= target && target < a[mid]) high = mid - 1;
            else low = mid + 1;
        } else {
            if (a[mid] < target && target <= a[high]) low = mid + 1;
            else high = mid - 1;
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, target;
    if (!(cin >> n >> target)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << search_rotated(a, target) << "\n";
    return 0;
}
