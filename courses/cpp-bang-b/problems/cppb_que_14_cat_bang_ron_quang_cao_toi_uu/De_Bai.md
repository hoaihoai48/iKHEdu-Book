# Chọn Đoạn Tối Đa Không Quá K Phần Tử Liền Kề

## Bối cảnh
Một tuyến phố đi bộ có $N$ vị trí treo biển quảng cáo, vị trí thứ $i$ đem lại doanh thu $A_i$. Để đảm bảo không gian cảnh quan xanh cho tuyến phố, quy định đô thị yêu cầu không được phép treo biển quảng cáo tại quá $K$ vị trí đứng liền sát nhau.

## Nhiệm vụ
Cho danh sách doanh thu của $N$ vị trí và giới hạn $K$. Hãy lập trình chọn các vị trí treo biển sao cho không có quá $K$ vị trí liền kề được chọn và tổng doanh thu thu về là lớn nhất.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất tổng doanh thu lớn nhất đạt được.

## Sample 1
### Input
```text
5 2
1 2 3 4 5
```
### Output
```text
12
```

### Giải thích
Với 5 vị trí có doanh thu $[1, 2, 3, 4, 5]$ và giới hạn $K = 2$ (không được chọn quá 2 vị trí liên tiếp):
Phương án tối ưu là bỏ chọn vị trí thứ 3 (doanh thu 3), giữ lại các vị trí 1, 2, 4, 5. Các cụm chọn gồm [1, 2] (độ dài 2) và [4, 5] (độ dài 2), mang lại tổng doanh thu tối đa là $1 + 2 + 4 + 5 = 12$.

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
