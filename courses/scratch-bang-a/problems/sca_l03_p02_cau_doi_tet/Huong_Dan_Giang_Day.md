# Hướng Dẫn Giảng Dạy: Câu đối ngày tết
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là in hai dòng chữ cố định: dòng 1 là `Chuc mung nam moi`, dòng 2 là `Van su nhu y`. Thầy cô giải thích mỗi lệnh `khối nói` tự xuống dòng một lần sau khi in xong.
- Quy trình gồm hai bước nối tiếp: lệnh `nói ("Chuc mung nam moi")` in vế đối thứ nhất, rồi lệnh `nói ("Van su nhu y")` in vế đối thứ hai xuống dòng dưới.
- Xử lý biên: bài này không có số liệu vào nên không có giá trị biên. Thầy cô nhắc các con giữ đúng thứ tự hai dòng, vì đổi chỗ hai dòng cho nhau cũng bị tính là kết quả sai.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: (không có dữ liệu vào))
| Bước | Lệnh chạy | Màn hình hiện ra |
|------|-----------|------------------|
| 1 | `nói ("Chuc mung nam moi")` | Dòng 1: `Chuc mung nam moi` |
| 2 | `nói ("Van su nhu y")` | Dòng 2: `Van su nhu y` |
| 3 | Kết thúc chương trình | Kết quả cuối cùng đúng hai dòng như trên. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: dồn cả hai vế vào một lệnh như `nói ("Chuc mung nam moi Van su nhu y")`. Màn hình chỉ hiện một dòng dài thay vì hai dòng riêng biệt. Cách sửa: tách thành hai lệnh `khối nói` riêng.
- Bẫy 2: viết liền hai lệnh trên cùng một logic in một dòng, ví dụ dùng `nói ("Chuc mung nam moi", end=" ")` rồi in tiếp vế hai. Kết quả ra `Chuc mung nam moi Van su nhu y` trên một dòng, không đúng yêu cầu. Cách sửa: để `khối nói` mặc định xuống dòng, không thêm `end=" "`.
- Bẫy 3: gõ sai chữ hoa thường, ví dụ `nói ("Chuc Mung Nam Moi")`. Màn hình hiện khác mẫu `Chuc mung nam moi` nên bị tính là kết quả sai. Cách sửa: sao chép đúng từng chữ trong đề bài.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - nói [Chuc mung nam moi]
> - nói [Van su nhu y]
