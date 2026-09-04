# Truy Vết Dãy Con Tăng Dài Nhất

## Bối cảnh
Sau khi tính toán được độ dài của xu thế gia tăng dữ liệu áp suất địa chấn, ban chỉ đạo cần xuất báo cáo chi tiết bao gồm chính xác các giá trị đo đạc cụ thể đã hình thành nên xu thế đó để gửi tới viện nghiên cứu phân tích.

## Nhiệm vụ
Cho dãy số nguyên $A$ gồm $N$ phần tử. Hãy lập trình tìm và in ra toàn bộ các phần tử thuộc về một dãy con tăng nghiêm ngặt dài nhất. Nếu có nhiều dãy con cùng đạt độ dài lớn nhất, bạn chỉ cần in ra một dãy con bất kỳ thỏa mãn.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- Dòng 1: In ra số nguyên $L$ là độ dài của dãy con tăng dài nhất.
- Dòng 2: In ra $L$ số nguyên là các giá trị của dãy con được chọn, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
5
2 1 4 3 5
```
### Output
```text
3
2 4 5
```

### Giải thích
Với dãy số gốc là $[2, 1, 4, 3, 5]$:
Dãy con tăng dài nhất có độ dài bằng 3. Một dãy con hợp lệ thỏa mãn điều kiện tăng nghiêm ngặt là $[2, 4, 5]$ (hoặc $[1, 4, 5]$, $[1, 3, 5]$). Kết quả dòng 1 in ra 3, dòng 2 in ra các số 2 4 5.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 2000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
