#include <bits/stdc++.h>
using namespace std;

// Tham lam lập lịch công việc có Deadline & Tiền phạt
struct Job {
    int id, deadline;
    long long penalty;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Job> jobs(n);
    for (int i = 0; i < n; ++i) {
        jobs[i].id = i + 1;
        cin >> jobs[i].deadline >> jobs[i].penalty;
    }

    sort(jobs.begin(), jobs.end(), [](const Job& a, const Job& b) {
        return a.penalty > b.penalty;
    });

    vector<int> slot(n + 1, -1);
    long long total_penalty = 0;

    for (const auto& job : jobs) {
        int d = min(n, job.deadline);
        while (d > 0 && slot[d] != -1) d--;
        if (d > 0) {
            slot[d] = job.id;
        } else {
            total_penalty += job.penalty;
        }
    }

    cout << total_penalty << "\n";
    return 0;
}
