# Hướng Dẫn Giảng Dạy: In số trên một hàng với sep
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là in năm số `1 2 3 4 5` trên cùng một hàng, nhưng giữa các số là dấu gạch ngang `-` thay vì dấu cách. Thầy cô giải thích tham số `sep="-"` chính là sợi dây nối các số lại với nhau.
- Quy trình chỉ có một bước: gọi `nói (1, 2, 3, 4, 5, sep="-")`, máy sẽ đặt dấu `-` vào giữa mỗi cặp số kề nhau rồi in ra `1-2-3-4-5`.
- Xử lý biên: bài này không có số liệu vào nên không có giá trị biên. Thầy cô nhắc các con đếm đủ năm số từ 1 tới 5, thiếu số 5 hay thừa số 6 đều làm kết quả khác đi.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: (không có dữ liệu vào))
| Bước | Lệnh chạy | Màn hình hiện ra |
|------|-----------|------------------|
| 1 | `nói (1, 2, 3, 4, 5, sep="-")` | `1-2-3-4-5` |
| 2 | Kết thúc chương trình | Kết quả cuối cùng: `1-2-3-4-5`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên tham số `sep`, viết `nói (1, 2, 3, 4, 5)` thì màn hình hiện `1 2 3 4 5` với dấu cách thay vì `1-2-3-4-5`. Cách sửa: thêm `sep="-"` vào trong khối lệnh `nói ()`.
- Bẫy 2: đặt dấu nối sai, ví dụ `nói (1, 2, 3, 4, 5, sep="_")` thì màn hình hiện `1_2_3_4_5` thay vì `1-2-3-4-5`. Cách sửa: dùng đúng dấu gạch ngang `"-"`.
- Bẫy 3: in từng số trên từng dòng bằng năm lệnh `nói (1)` ... `nói (5)` thì màn hình hiện năm dòng rời nhau thay vì một hàng `1-2-3-4-5`. Cách sửa: gom cả năm số vào một khối lệnh `nói ()` duy nhất.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - nói [1, 2, 3, 4, 5, sep="-]
