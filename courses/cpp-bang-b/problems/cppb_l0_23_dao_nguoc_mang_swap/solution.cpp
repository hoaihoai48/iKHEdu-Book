#include <bits/stdc++.h>
using namespace std;

// Hàm đảo ngược mảng in-place bằng tham chiếu vector<int>&
void reverseArray(vector<int>& a) {
    int l = 0;
    int r = (int)a.size() - 1;
    while (l < r) {
        swap(a[l], a[r]);
        l++;
        r--;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    reverseArray(a);

    for (int i = 0; i < n; i++) {
        cout << a[i] << (i == n - 1 ? '\n' : ' ');
    }

    return 0;
}
