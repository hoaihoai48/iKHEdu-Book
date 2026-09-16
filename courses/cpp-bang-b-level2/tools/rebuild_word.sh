#!/bin/bash
# rebuild_word.sh — Pipeline rebuild Word Level 2 (Quyển 1 + Quyển 2).
# Chạy từ thư mục courses/cpp-bang-b-level2:
#     bash rebuild_word.sh --volume 2
#     bash rebuild_word.sh --volume 1
#     bash rebuild_word.sh --all
#
# Thứ tự pipeline (khớp docs/MASTER_WORD_BUILD_SPECIFICATION.md §7):
#   B0. Backup docx hiện tại (.bak-rebuild-<timestamp>)
#   B1. Đồng bộ ma trận 346 bài vào MASTER_ALL_LESSONS.md (nguồn De_Bai.md mới)
#   B2. Build Word bằng build_docx.py (pandoc + reference-doc + postprocess OpenXML)
#   B3. Audit 7 điểm bằng audit_docx.py (exit != 0 = còn FAIL)
#
# Yêu cầu môi trường: python3 + python-docx, pandoc, npx @resvg/resvg-js-cli.
# KHÔNG đụng thư mục problems/*/test (test regen làm riêng ở giai đoạn server).

set -e
cd "$(dirname "$0")"

MODE="${1:---all}"
STAMP=$(date +%Y%m%d_%H%M%S)

echo "=== B0. Kiểm tra công cụ ==="
command -v pandoc >/dev/null || { echo "❌ Thiếu pandoc"; exit 1; }
python3 -c "import docx" 2>/dev/null || { echo "❌ Thiếu python-docx (pip install python-docx)"; exit 1; }

echo "=== B0. Backup docx hiện tại ==="
for f in IKHEDU_CPP_Nang_Cao_Quyen_1.docx IKHEDU_CPP_Nang_Cao_Quyen_2.docx; do
  if [ -f "$f" ]; then
    cp "$f" "$f.bak-rebuild-$STAMP"
    echo "  → $f.bak-rebuild-$STAMP"
  fi
done

echo "=== B1. Sync ma trận 346 bài vào MASTER ==="
python3 sync_master_matrix.py

build_and_audit() {
  echo "=== B2. Build Quyển $1 ==="
  python3 build_docx.py --volume "$1"
  echo "=== B3. Audit Quyển $1 ==="
  python3 audit_docx.py --volume "$1"
}

case "$MODE" in
  --volume)
    build_and_audit "$2"
    ;;
  --volume=1|--volume=2)
    build_and_audit "${MODE#--volume=}"
    ;;
  --all)
    build_and_audit 2
    build_and_audit 1
    ;;
  *)
    echo "Dùng: bash rebuild_word.sh --volume 1|2 | --all"
    exit 1
    ;;
esac

echo ""
echo "🎉 Rebuild + audit xong. Mở file .docx bằng Word thật để đối chiếu visual lần cuối."
