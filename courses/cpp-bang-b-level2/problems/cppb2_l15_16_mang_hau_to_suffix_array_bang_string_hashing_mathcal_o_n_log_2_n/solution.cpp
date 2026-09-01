#include <bits/stdc++.h>
using namespace std;

string bwt_transform(string s) {
    s += "$";
    int n = s.size();
    vector<string> rotations(n);
    for (int i = 0; i < n; ++i) {
        rotations[i] = s.substr(i) + s.substr(0, i);
    }
    sort(rotations.begin(), rotations.end());
    string bwt = "";
    for (int i = 0; i < n; ++i) bwt += rotations[i].back();
    return bwt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    cout << bwt_transform(s) << "\n";
    return 0;
}
