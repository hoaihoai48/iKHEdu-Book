import os
import zipfile
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
SCRATCH_DIR = BASE_DIR / "courses" / "scratch-bang-a"
ASSETS_DIR = SCRATCH_DIR / "assets"

SOURCE_DOCS = [
    {
        "file": BASE_DIR / "CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx",
        "category": "pen_drawings",
        "prefix": "pen_img",
        "description": "Hình mẫu vẽ hình đồ họa và bút vẽ Pen (Chương 1)"
    },
    {
        "file": BASE_DIR / "DeTHT.docx",
        "category": "contest_scenarios",
        "prefix": "tht_img",
        "description": "Sơ đồ và hình ảnh minh họa đề thi Tin học trẻ Bảng A"
    },
    {
        "file": BASE_DIR / "52 bài lập trình Scratch.docx",
        "category": "block_screenshots",
        "prefix": "block_img",
        "description": "Ảnh chụp màn hình khối lệnh Scratch giải mẫu"
    }
]

def extract_all():
    manifest = {
        "title": "Danh mục tài nguyên hình ảnh khóa học Scratch Bảng A",
        "total_images": 0,
        "categories": {},
        "images": []
    }

    for src in SOURCE_DOCS:
        doc_path = src["file"]
        category = src["category"]
        prefix = src["prefix"]
        out_dir = ASSETS_DIR / category
        out_dir.mkdir(parents=True, exist_ok=True)

        if not doc_path.exists():
            print(f"Warning: File not found: {doc_path}")
            continue

        print(f"Extracting from: {doc_path.name} -> {category}...")
        count = 0
        with zipfile.ZipFile(doc_path, 'r') as z:
            media_files = sorted([f for f in z.namelist() if f.startswith('word/media/')])
            for i, mf in enumerate(media_files, start=1):
                ext = Path(mf).suffix.lower()
                dest_name = f"{prefix}_{i:03d}{ext}"
                dest_path = out_dir / dest_name
                
                with z.open(mf) as source_file, open(dest_path, "wb") as target_file:
                    target_file.write(source_file.read())
                
                file_size = dest_path.stat().st_size
                img_info = {
                    "id": f"{prefix}_{i:03d}",
                    "filename": dest_name,
                    "category": category,
                    "relative_path": f"assets/{category}/{dest_name}",
                    "source_doc": doc_path.name,
                    "original_entry": mf,
                    "size_bytes": file_size
                }
                manifest["images"].append(img_info)
                count += 1

        manifest["categories"][category] = {
            "description": src["description"],
            "count": count
        }
        manifest["total_images"] += count
        print(f"  -> Extracted {count} images to {category}/")

    manifest_path = ASSETS_DIR / "image_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"\nCompleted! Total extracted images: {manifest['total_images']}")
    print(f"Manifest written to: {manifest_path}")

if __name__ == "__main__":
    extract_all()
