#include <bits/stdc++.h>
using namespace std;

struct Job {
    int id, deadline;
    long long profit;
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        parent[root_i] = root_j;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Job> jobs(n);
    int max_d = 0;
    for (int i = 0; i < n; ++i) {
        jobs[i].id = i;
        cin >> jobs[i].deadline >> jobs[i].profit;
        max_d = max(max_d, jobs[i].deadline);
    }

    sort(jobs.begin(), jobs.end(), [](const Job &a, const Job &b) {
        return a.profit > b.profit;
    });

    DSU dsu(max_d);
    long long total_profit = 0;
    int count_jobs = 0;

    for (const auto &j : jobs) {
        int available_slot = dsu.find(min(j.deadline, max_d));
        if (available_slot > 0) {
            dsu.unite(available_slot, available_slot - 1);
            total_profit += j.profit;
            count_jobs++;
        }
    }

    cout << count_jobs << " " << total_profit << "\n";
    return 0;
}
