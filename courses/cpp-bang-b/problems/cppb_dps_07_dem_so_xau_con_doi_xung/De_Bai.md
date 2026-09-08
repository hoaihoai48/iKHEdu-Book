# Đếm Số Đoạn Con Đối Xứng Liên Tiếp

## Bối cảnh
Trong một kỳ thi mật mã học sinh viên, ban giám khảo đưa ra một chuỗi văn bản và yêu cầu các thí sinh thống kê tất cả các phân đoạn liên tiếp có tính đối xứng xuất hiện trong chuỗi (kể cả các đoạn con có độ dài 1 ký tự).

## Nhiệm vụ
Cho chuỗi ký tự $S$. Hãy lập trình đếm tổng số lượng đoạn con liên tiếp đối xứng có trong chuỗi.

## Input
- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).

## Output
- In ra trên một dòng duy nhất tổng số lượng đoạn con đối xứng liên tiếp đếm được.

## Sample 1
### Input
```text
aaa
```
### Output
```text
6
```

### Giải thích
Với chuỗi $S = \text{"aaa"}$:
Có tất cả 6 đoạn con liên tiếp đối xứng gồm:

- 3 đoạn độ dài 1: "a" (vị trí 0), "a" (vị trí 1), "a" (vị trí 2).
- 2 đoạn độ dài 2: "aa" (vị trí 0-1), "aa" (vị trí 1-2).
- 1 đoạn độ dài 3: "aaa" (toàn bộ chuỗi).
Tổng số đoạn đối xứng là 6.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
