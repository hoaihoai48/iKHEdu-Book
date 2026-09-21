#!/bin/bash
set -e

# Đảm bảo đang ở root của repo
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

# 1. Kiểm tra trạng thái git trên main
if [ -n "$(git status --porcelain | grep -v '^\?\?')" ]; then
    echo "⚠️ Working tree còn thay đổi chưa commit. Vui lòng commit trên nhánh main trước khi đồng bộ!"
    exit 1
fi

current_branch=$(git branch --show-current)
if [ "$current_branch" != "main" ]; then
    echo "⚠️ Bạn đang ở nhánh '$current_branch'. Vui lòng checkout về 'main' trước khi chạy!"
    exit 1
fi

echo "🚀 Bắt đầu đồng bộ commit mới từ main sang repo công ty (DKTECHVN)..."

# 2. Đảm bảo nhánh publish-dktech tồn tại và theo dõi dktech/main
if ! git show-ref --verify --quiet refs/heads/publish-dktech; then
    git branch publish-dktech dktech/main
fi

# 3. Chuyển sang nhánh publish-dktech
git checkout publish-dktech

# 4. Lấy commit message mới nhất từ main để đặt làm message đồng bộ
LATEST_MSG=$(git log -1 --pretty=%B main)

# 5. Lấy toàn bộ diff mới nhất từ main đắp trực tiếp lên cây thư mục (Linear changes, KHÔNG DÙNG git merge)
git checkout main -- .

# 6. Loại bỏ triệt để file agent & script đồng bộ khỏi staging
git rm -rf --cached .agent .agents AGENTS.md GEMINI.md sync_company.sh 2>/dev/null || true
rm -f sync_company.sh 2>/dev/null || true

# Đảm bảo .gitignore trên nhánh publish luôn ignore các file agent và script nội bộ
if ! grep -q "sync_company.sh" .gitignore 2>/dev/null; then
    cat << 'GITIGNORE_EOF' >> .gitignore

# AI Agent configs & deployment tools
.agent/
.agents/
AGENTS.md
GEMINI.md
sync_company.sh
GITIGNORE_EOF
    git add .gitignore
fi

# 7. Tạo DUY NHẤT 1 commit mới nối tiếp vào lịch sử thẳng (Linear History)
if [ -n "$(git status --porcelain)" ]; then
    git add -A
    git commit -m "$LATEST_MSG"
    echo "✅ Đã tạo commit mới nối tiếp: $LATEST_MSG"
    
    # 8. Push thẳng lên nhánh main của DKTECHVN
    git push dktech publish-dktech:main
else
    echo "ℹ️ Không có thay đổi mới nào để commit sang repo công ty."
fi

# 9. Tự động quay về lại nhánh main cho bạn làm việc tiếp
git checkout main

echo "🎉 ĐỒNG BỘ THÀNH CÔNG! Lịch sử commit tuyến tính đã được ghi nhận trên https://github.com/DKTECHVN/giao-trinh-ikh"
