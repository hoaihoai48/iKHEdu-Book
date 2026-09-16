#!/bin/bash
set -e

# Đảm bảo đang ở root của repo
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

# 1. Kiểm tra trạng thái git
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️ Working tree chưa commit hết. Vui lòng commit các thay đổi trên nhánh main trước khi đồng bộ!"
    exit 1
fi

current_branch=$(git branch --show-current)
if [ "$current_branch" != "main" ]; then
    echo "⚠️ Bạn đang ở nhánh '$current_branch'. Vui lòng checkout về 'main' trước khi chạy!"
    exit 1
fi

echo "🚀 Bắt đầu đồng bộ code từ main sang repo công ty (DKTECHVN)..."

# 2. Chuyển sang nhánh publish-dktech
git checkout publish-dktech

# 3. Merge code mới từ main sang (bỏ qua commit nếu không có thay đổi)
git merge main --no-edit -m "chore: sync latest content from main"

# 4. Đảm bảo triệt để các file agent không bị merge vào
git rm -rf --cached .agent .agents AGENTS.md GEMINI.md 2>/dev/null || true
git commit --amend --no-edit 2>/dev/null || true

# 5. Push lên nhánh main của DKTECHVN
git push dktech publish-dktech:main

# 6. Quay lại nhánh main để tiếp tục làm việc
git checkout main

echo "🎉 ĐỒNG BỘ THÀNH CÔNG lên https://github.com/DKTECHVN/giao-trinh-ikh (nhánh main)!"
