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

# 5. Merge các thay đổi mới từ main vào nhánh publish (nối tiếp commit history)
# Dùng --no-commit để luôn kiểm tra và lọc sạch file agent trước khi tạo commit
git merge main --no-commit --no-ff -m "$LATEST_MSG" || true

# 6. Loại bỏ triệt để các file agent khỏi staging trước khi commit
git rm -rf --cached .agent .agents AGENTS.md GEMINI.md 2>/dev/null || true

# Đảm bảo .gitignore trên nhánh publish luôn ignore các file agent
if ! grep -q "^\.agent/" .gitignore 2>/dev/null; then
    cat << 'GITIGNORE_EOF' >> .gitignore

# AI Agent configs & prompt guidelines
.agent/
.agents/
AGENTS.md
GEMINI.md
GITIGNORE_EOF
    git add .gitignore
fi

# 7. Tạo commit mới nối tiếp vào lịch sử (nếu có thay đổi)
if [ -n "$(git status --porcelain)" ]; then
    git commit -m "$LATEST_MSG"
    echo "✅ Đã tạo commit mới nối tiếp: $LATEST_MSG"
    
    # 8. Push nối tiếp bình thường lên nhánh main của DKTECHVN (KHÔNG DÙNG --force)
    git push dktech publish-dktech:main
else
    echo "ℹ️ Không có thay đổi mới nào để commit sang repo công ty."
fi

# 9. Tự động quay về lại nhánh main cho bạn làm việc tiếp
git checkout main

echo "🎉 ĐỒNG BỘ THÀNH CÔNG! Lịch sử commit đã được ghi nhận trên https://github.com/DKTECHVN/giao-trinh-ikh"
