#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    queue<long long> qu;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) { // Push x
            long long x;
            cin >> x;
            qu.push(x);
        } else if (type == 2) { // Pop
            if (!qu.empty()) qu.pop();
        } else if (type == 3) { // Front
            if (qu.empty()) cout << "EMPTY\n";
            else cout << qu.front() << "\n";
        }
    }
    return 0;
}
