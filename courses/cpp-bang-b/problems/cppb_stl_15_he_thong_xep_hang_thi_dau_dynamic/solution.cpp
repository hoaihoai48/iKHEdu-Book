#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    map<string, long long> scores;
    multiset<long long> all_scores;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) { // Cộng điểm cho thí sinh
            string name;
            long long delta;
            cin >> name >> delta;

            if (scores.count(name)) {
                auto it = all_scores.find(scores[name]);
                if (it != all_scores.end()) all_scores.erase(it);
            }

            scores[name] += delta;
            all_scores.insert(scores[name]);
        } else { // Truy vấn điểm của thí sinh
            string name;
            cin >> name;
            cout << (scores.count(name) ? scores[name] : 0) << "\n";
        }
    }
    return 0;
}
