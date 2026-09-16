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

echo "🚀 Bắt đầu đồng bộ snapshot mới nhất sang repo công ty (DKTECHVN)..."

# 2. Tạo nhánh mồ côi tạm thời không có lịch sử cũ
git checkout --orphan dktech-sync-temp

# 3. Loại bỏ triệt để các file agent khỏi staging
git rm -rf --cached .agent .agents AGENTS.md GEMINI.md 2>/dev/null || true

# 4. Thêm rule ignore vào .gitignore trên snapshot này
cat << 'GITIGNORE_EOF' >> .gitignore

# AI Agent configs & prompt guidelines
.agent/
.agents/
AGENTS.md
GEMINI.md
GITIGNORE_EOF
git add .gitignore

# 5. Tạo duy nhất 1 commit snapshot mới nhất
DATE_STR=$(date +"%Y-%m-%d %H:%M:%S")
git commit -m "feat: release curriculum update ($DATE_STR)"

# 6. Đẩy đè thẳng lên nhánh main của DKTECHVN (giữ lịch sử 1 commit sạch)
git push dktech dktech-sync-temp:main --force

# 7. Quay lại main và dọn dẹp nhánh tạm
git checkout main
git branch -D dktech-sync-temp

echo "🎉 ĐỒNG BỘ THÀNH CÔNG lên https://github.com/DKTECHVN/giao-trinh-ikh!"
