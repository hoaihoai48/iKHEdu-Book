# Tổng Đoạn Con Không Liền Kề Lớn Nhất

## Bối cảnh
Một tuyến phố thương mại gồm $N$ căn nhà liền kề được đánh số từ $1$ đến $N$. Căn nhà thứ $i$ có giá trị thương mại là $A_i$. Một công ty quảng cáo muốn thuê mặt bằng để lắp đặt các màn hình LED kích thước lớn. Tuy nhiên, theo quy định an toàn đô thị về khoảng cách chiếu sáng, công ty không được phép thuê hai căn nhà đứng sát cạnh nhau trên cùng dãy phố.

## Nhiệm vụ
Cho danh sách giá trị thương mại của $N$ căn nhà. Hãy lập trình chọn ra một tập hợp các căn nhà không kề nhau sao cho tổng giá trị thu được là lớn nhất có thể.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$) biểu diễn số lượng căn nhà.
- Dòng 2: Chứa $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^4$) biểu diễn giá trị của từng căn nhà.

## Output
- In ra trên một dòng duy nhất một số nguyên là tổng giá trị lớn nhất tìm được.

## Sample 1
### Input
```text
4
1 2 3 1
```
### Output
```text
4
```

### Giải thích
Với dãy giá trị của 4 căn nhà là $[1, 2, 3, 1]$:
- Nếu chọn nhà 2 và nhà 4: Tổng giá trị là $2 + 1 = 3$.
- Phương án tối ưu: Chọn nhà 1 (giá trị 1) và nhà 3 (giá trị 3). Hai nhà này không kề nhau và mang lại tổng giá trị lớn nhất là $1 + 3 = 4$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
