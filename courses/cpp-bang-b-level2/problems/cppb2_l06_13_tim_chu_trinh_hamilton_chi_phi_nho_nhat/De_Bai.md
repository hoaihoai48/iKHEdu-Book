# Tìm chu trình hamilton chi phí nhỏ nhất

## Bối cảnh

Đoàn kiểm tra của tổng công ty phải đi thăm mỗi chi nhánh đúng một lần rồi quay về trụ sở chính để nộp báo cáo tổng hợp. Phòng tài chính đã tính sẵn chi phí di chuyển giữa từng cặp chi nhánh, bao gồm tiền xe và phụ cấp đường dài. Trưởng đoàn muốn chọn hành trình khép kín rẻ nhất để tiết kiệm ngân sách công tác cho cả đoàn, và cần một chương trình tính ra hành trình đó.

## Nhiệm vụ

Cho ma trận chi phí di chuyển giữa $N$ địa điểm (địa điểm $0$ là trụ sở). Hãy lập trình tìm hành trình khép kín rẻ nhất xuất phát từ trụ sở, thăm mỗi địa điểm đúng một lần rồi quay về trụ sở, và in ra tổng chi phí nhỏ nhất đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 18$), là số địa điểm.
- $N$ dòng tiếp theo, mỗi dòng chứa $N$ số nguyên $c_{ij}$ ($0 \le c_{ij} \le 10^6$), là chi phí đi từ địa điểm $i$ đến địa điểm $j$. Các phần tử trên đường chéo chính bằng $0$.

## Output

- In ra một số nguyên duy nhất là tổng chi phí nhỏ nhất của hành trình khép kín.

## Sample 1

### Input

```text
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```

### Output

```text
80
```

### Giải thích

- Xét các hành trình khép kín xuất phát từ trụ sở $0$ thăm mỗi nơi một lần.
- Hành trình $0 \to 1 \to 3 \to 2 \to 0$ tốn $10 + 25 + 30 + 15 = 80$.
- Hành trình $0 \to 1 \to 2 \to 3 \to 0$ tốn $10 + 35 + 30 + 20 = 95$.
- Hành trình $0 \to 2 \to 1 \to 3 \to 0$ tốn $15 + 35 + 25 + 20 = 95$.
- Mọi hành trình còn lại đều tốn từ $80$ trở lên, nên chi phí nhỏ nhất là $80$.

## Ràng buộc

- $1 \le N \le 18$, $0 \le c_{ij} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
