#include <bits/stdc++.h>
using namespace std;

struct Student {
    string name;
    int math, it, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Student> a(n);
    for (int i = 0; i < n; ++i) {
        a[i].id = i;
        cin >> a[i].name >> a[i].math >> a[i].it;
    }

    sort(a.begin(), a.end(), [](const Student &x, const Student &y) {
        if (x.it != y.it) return x.it > y.it;
        if (x.math != y.math) return x.math > y.math;
        return x.id < y.id;
    });

    for (const auto &s : a) {
        cout << s.name << " " << s.math << " " << s.it << "\n";
    }
    return 0;
}
