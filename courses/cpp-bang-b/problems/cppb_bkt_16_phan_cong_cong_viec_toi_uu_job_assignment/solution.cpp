#include <bits/stdc++.h>
using namespace std;

int n;
long long c[15][15];
bool job_assigned[15];
long long min_row[15];
long long best_cost = 1e18;

void branchAndBound(int worker, long long current_cost) {
    // Optimality Pruning
    long long bound = current_cost;
    for (int w = worker; w <= n; ++w) bound += min_row[w];
    if (bound >= best_cost) return;

    if (worker > n) {
        best_cost = min(best_cost, current_cost);
        return;
    }

    for (int job = 1; job <= n; ++job) {
        if (!job_assigned[job]) {
            job_assigned[job] = true;
            branchAndBound(worker + 1, current_cost + c[worker][job]);
            job_assigned[job] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= n; ++i) {
        min_row[i] = 1e9;
        for (int j = 1; j <= n; ++j) {
            cin >> c[i][j];
            min_row[i] = min(min_row[i], c[i][j]);
        }
    }
    memset(job_assigned, false, sizeof(job_assigned));
    branchAndBound(1, 0);
    cout << best_cost << "\n";
    return 0;
}
