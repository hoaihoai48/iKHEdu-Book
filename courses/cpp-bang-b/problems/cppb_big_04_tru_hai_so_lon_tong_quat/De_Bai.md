# Trừ Hai Số Lớn Tổng Quát (Có Thể Âm)

## Bối cảnh
Báo cáo cán cân thương mại quốc tế cần tính toán mức chênh lệch giữa kim ngạch xuất khẩu A và kim ngạch nhập khẩu B (cả A và B đều là số nguyên lớn). Nếu kim ngạch nhập khẩu lớn hơn xuất khẩu (A < B), cán cân sẽ thâm hụt và kết quả phải mang dấu âm '-'.

## Nhiệm vụ
Cho 2 số nguyên dương lớn A và B. Hãy tính hiệu A - B (in dấu '-' phía trước nếu kết quả mang giá trị âm).

## Input
- Dòng 1: Chuỗi số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Chuỗi số $B$ ($1 \le |B| \le 10^5$).

## Output
- In ra kết quả phép trừ $A - B$.

## Sample 1
### Input
```text
1
1000
```
### Output
```text
-999
```
### Giải thích
1 - 1000 = -999. Kết quả in ra: -999.

## Ràng buộc
- $100\%$ số test có $|A|, |B| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
