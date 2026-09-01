#include <bits/stdc++.h>
using namespace std;

// Tham lam lập lịch công việc dùng vector<vector<long long>>
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> jobs(n, vector<long long>(3));
    for (int i = 0; i < n; ++i) {
        long long d, p;
        cin >> d >> p;
        jobs[i] = {p, d, i + 1}; // {tiền phạt, deadline, id} để sort giảm dần
    }

    sort(jobs.rbegin(), jobs.rend());

    vector<int> slot(n + 1, -1);
    long long total_penalty = 0;

    for (const auto& job : jobs) {
        long long p = job[0];
        int d = min((long long)n, job[1]);
        int id = job[2];

        while (d > 0 && slot[d] != -1) d--;
        if (d > 0) {
            slot[d] = id;
        } else {
            total_penalty += p;
        }
    }

    cout << total_penalty << "\n";
    return 0;
}
