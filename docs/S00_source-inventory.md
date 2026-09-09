# S00 — Source Inventory (Step 0A, evidence mode)

> Quyet pham vi (chu du an, 2026-09-09): chi dung ban full `python-level-1.docx`. Khong doi chieu Quyen 1/2 (chi la ban split phuc vu in).

## 1. Ket qua scan that (bang python-docx, Heading styles)

| File | Vai tro ket luan | Chapters | Lessons | Exercises (H3 `Bai NN [pya_*]`) |
|---|---|---:|---:|---:|
| `courses/python-bang-a/python-level-1.docx` (3.078.837 bytes, 2026-09-07) | **CANONICAL — full 5 chuong** | 5 | 14 | **287** |
| `courses/python-bang-a/python-level-1-quyen-1.docx` | Split Quyen 1 (Ch 01–02, Bai 01–06) | 2 | 6 | 157 |
| `courses/python-bang-a/python-level-1-quyen-2.docx` | Split Quyen 2 (Ch 03–05, Bai 07–14) | 3 | 8 | 130 |
| `*.bak`, `backup_*.docx`, `_test_*.docx`, `python-giaovien-*.docx` | Khong dung lam source hoc sinh | — | — | — |

Cross-check: 157 + 130 = 287; 6 + 8 = 14. Khop voi so lieu baseline (5/14/287) — **verified bang scan that, khong con la gia dinh**.

## 2. Cau truc H1 trong canonical (thu tu that)

LOI NOI DAU → CHUONG 01 (Bai 01–03) → CHUONG 02 (Bai 04–06) → CHUONG 03 (Bai 07–10) → CHUONG 04 (Bai 11–12) → CHUONG 05 (Bai 13–14) → Phu luc A/B → Muc luc.

Danh sach Bai: 01 I/O-bien-kieu; 02 toan tu/bieu thuc; 03 `// % **`; 04 re nhanh; 05 for/range; 06 while/flag; 07 day so/tam giac; 08 tach chu so; 09 uoc/boi/nguyen to; 10 dem/so dac biet; 11 list co ban; 12 thong ke/sap xep; 13 index/slicing/duyet chuoi; 14 duyet/bien doi/tach tu.

## 3. Quyet dinh gate 0A

- `DEC-S00`: `python-level-1.docx` la canonical source hoc sinh; Quyen 1/2 la ban split phuc vu in, chi doi chieu; `.bak/backup/giaovien/test` khong phai source.
- So lieu 5/14/287 duoc xac nhan tu scan Heading — cac step sau duoc phep trich dan file nay.
- Discrepancy: khong co (tong split khop full). Neu sau nay doi chieu noi dung chi tiet tung bai phat hien lech, mo issue moi, khong tu sua PLAN.

## 4. Handoff sang Step 0B

- Can chot: course slug (`scratch-bang-a` du kien), cay thu muc, file canonical, draft Curriculum Contract, G0.1–G0.4.
- Tiep theo: Step 0B truoc, sau do Step 1 lay 3–5 Problem Contract B01 that.

## Evidence

- Scan bang `python-docx` tren H1/H3, ngay 2026-09-09. Script: dem H1 startswith `CHƯƠNG`/`Bài `, H3 match `Bài \d+ \[pya_`.
