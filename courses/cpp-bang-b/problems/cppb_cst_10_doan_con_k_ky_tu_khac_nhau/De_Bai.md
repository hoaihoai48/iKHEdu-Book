# Đoạn Con Dài Nhất Chứa Tối Đa K Ký Tự Khác Nhau

## Bối cảnh
Trong kỹ thuật nén văn bản không mất dữ liệu, một bộ mã hóa cần phân tích một chuỗi ký tự văn bản S. Để tối ưu từ điển ký tự trong bộ đệm nhanh, bộ mã hóa muốn trích xuất một đoạn văn bản liên tiếp dài nhất mà trong đó chỉ sử dụng không quá K loại ký tự khác nhau.

## Nhiệm vụ
Cho chuỗi ký tự S gồm các chữ cái tiếng Anh in thường và số nguyên dương K. Hãy tìm độ dài lớn nhất của một chuỗi con liên tiếp chứa tối đa K ký tự khác nhau.

## Input
- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 10^5$).
- Dòng 2: Chứa số nguyên dương $K$ ($1 \le K \le 26$).

## Output
- In ra độ dài lớn nhất của chuỗi con tìm được.

## Sample 1
### Input
```text
eceba
2
```
### Output
```text
3
```
### Giải thích
Chuỗi con liên tiếp dài nhất chứa tối đa 2 ký tự khác nhau là 'ece' (chỉ chứa 2 ký tự 'e' và 'c') với độ dài bằng 3. Kết quả in ra: 3.

## Ràng buộc
- $100\%$ số test có $|S| \le 10^5, 1 \le K \le 26$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
