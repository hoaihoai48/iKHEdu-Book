# Bài toán người du lịch (tsp bitmask DP)

## Bối cảnh

Anh nhân viên giao hàng của một cửa hàng trực tuyến nhận nhiệm vụ mỗi sáng: xuất phát từ kho hàng, ghé qua mỗi địa chỉ giao hàng đúng một lần rồi quay trở về kho để nhận chuyến mới. Công ty đã đo sẵn giá cước di chuyển giữa từng cặp địa điểm và muốn anh chọn hành trình khép kín rẻ nhất có thể. Vì số địa điểm trong một chuyến chỉ khoảng hơn chục nơi, anh cần một chương trình tính ra tổng cước nhỏ nhất.

## Nhiệm vụ

Cho ma trận chi phí di chuyển giữa $N$ địa điểm (địa điểm $0$ là kho hàng). Hãy lập trình tìm hành trình khép kín rẻ nhất xuất phát từ kho, thăm mỗi địa điểm đúng một lần rồi quay về kho, và in ra tổng chi phí nhỏ nhất đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 18$), là số địa điểm.
- $N$ dòng tiếp theo, mỗi dòng chứa $N$ số nguyên $c_{ij}$ ($0 \le c_{ij} \le 10^6$), là chi phí đi từ địa điểm $i$ đến địa điểm $j$. Các phần tử trên đường chéo chính bằng $0$.

## Output

- In ra một số nguyên duy nhất là tổng chi phí nhỏ nhất của hành trình khép kín.

## Sample 1

### Input

```text
3
0 10 15
10 0 35
15 35 0
```

### Output

```text
60
```

### Giải thích

- Có đúng hai hành trình khép kín xuất phát từ kho $0$ thăm mỗi nơi một lần.
- Hành trình $0 \to 1 \to 2 \to 0$ tốn $10 + 35 + 15 = 60$.
- Hành trình $0 \to 2 \to 1 \to 0$ tốn $15 + 35 + 10 = 60$.
- Cả hai hành trình đều tốn $60$ nên đáp án nhỏ nhất là $60$.

## Ràng buộc

- $1 \le N \le 18$, $0 \le c_{ij} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
