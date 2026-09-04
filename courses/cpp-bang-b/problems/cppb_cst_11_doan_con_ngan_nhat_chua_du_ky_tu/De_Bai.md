# Đoạn Con Ngắn Nhất Chứa Đủ Mọi Ký Tự Của Tập Hợp

## Bối cảnh
Một chuyên gia giải mật mã cần tìm dấu vết của một tổ hợp mật mã T gồm M ký tự độc nhất bên trong một chuỗi tín hiệu thô S. Đoạn tín hiệu được trích xuất để giải mã cần phải chứa đầy đủ mọi ký tự xuất hiện trong T (mỗi ký tự có mặt ít nhất một lần). Để việc giải mã diễn ra nhanh nhất, đoạn tín hiệu trích xuất phải có độ dài ngắn nhất có thể.

## Nhiệm vụ
Cho chuỗi S gồm các chữ cái in thường và chuỗi mẫu T gồm M ký tự phân biệt. Hãy tìm độ dài nhỏ nhất của một đoạn con liên tiếp trong S chứa đầy đủ toàn bộ các ký tự của chuỗi T. Nếu không tồn tại, in ra -1.

## Input
- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 10^5$).
- Dòng 2: Chuỗi $T$ ($1 \le |T| \le 26$, các ký tự trong $T$ đôi một khác nhau).

## Output
- In ra độ dài nhỏ nhất tìm được, hoặc `-1` nếu không có đoạn con nào chứa đủ các ký tự của $T$.

## Sample 1
### Input
```text
adobecodebanc
abc
```
### Output
```text
4
```
### Giải thích
Chuỗi T = 'abc' yêu cầu phải có đủ 3 ký tự 'a', 'b', 'c'. Đoạn con ngắn nhất trong S chứa đủ cả 3 ký tự này là 'banc' ở cuối chuỗi S, có độ dài bằng 4. Kết quả in ra: 4.

## Ràng buộc
- $100\%$ số test có $|S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
