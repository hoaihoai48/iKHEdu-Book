#include <bits/stdc++.h>
using namespace std;

struct Customer {
    int id, priority;
};

struct Compare {
    bool operator()(const Customer &a, const Customer &b) {
        if (a.priority != b.priority) return a.priority < b.priority;
        return a.id > b.id;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    priority_queue<Customer, vector<Customer>, Compare> pq;

    while (q--) {
        int type; cin >> type;
        if (type == 1) {
            int id, p; cin >> id >> p;
            pq.push({id, p});
        } else {
            if (!pq.empty()) {
                cout << pq.top().id << "\n";
                pq.pop();
            } else {
                cout << "-1\n";
            }
        }
    }
    return 0;
}
