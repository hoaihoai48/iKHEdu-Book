#include <bits/stdc++.h>
using namespace std;
int n;
vector<int> cur;
void bkt(int step) {
    if (step > n) {
        for (int i = 0; i < (int)cur.size(); ++i) cout << cur[i] << (i + 1 == (int)cur.size() ? "" : " ");
        cout << "\n";
        return;
    }
    bkt(step + 1);
    cur.push_back(step);
    bkt(step + 1);
    cur.pop_back();
}
int main() {
    if (!(cin >> n)) return 0;
    bkt(1);
    return 0;
}
