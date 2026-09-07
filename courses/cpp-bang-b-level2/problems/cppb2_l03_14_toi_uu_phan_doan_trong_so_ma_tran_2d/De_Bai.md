# Tối ưu phân đoạn trọng số ma trận 2d

## Bối cảnh

Bác nông dân có một cánh đồng hình chữ nhật chia thành nhiều ô, mỗi ô cho năng suất khác nhau. Bác muốn khoanh các vùng trồng sao cho mỗi vùng có tổng năng suất đạt mức yêu cầu, với số vùng khoanh đúng như kế hoạch.

Bác ghi lại năng suất từng ô rồi tính mức năng suất tối thiểu mỗi vùng cần đạt.

## Nhiệm vụ

Cho ma trận trọng số không âm kích thước $n \times m$ và số phần $k$. Người ta cắt ngang ma trận thành các dải hàng liên tiếp (mỗi dải gồm một số hàng kề nhau). Hãy lập trình tìm tổng lớn nhất của một dải là nhỏ nhất có thể khi số vết cắt không vượt quá $k$.

## Input

- Dòng đầu tiên chứa ba số nguyên $n, m, k$ ($1 \le n, m \le 500$, $1 \le k \le n$) — kích thước ma trận và số phần cho phép.
- $n$ dòng tiếp theo, mỗi dòng chứa $m$ số nguyên không âm $a_{ij}$ ($0 \le a_{ij} \le 10^6$).

## Output

- In ra một dòng duy nhất là tổng lớn nhất của một dải trong phương án cắt tốt nhất (tổng của dải tính trên toàn bộ các cột).

## Sample 1
### Input
```text
2 2 2
1 2
3 4
```
### Output
```text
4
```
### Giải thích

Phần tử lớn nhất trong bảng là $4$ nên đáp án không thể nhỏ hơn $4$. Với ngưỡng $4$: dải hàng $1$ có tổng theo từng tiền tố cột là $1$ rồi $3$, đều không vượt $4$ nên giữ nguyên; gộp thêm hàng $2$ thì tổng cột $1$ thành $1 + 3 = 4$ vẫn đạt, nhưng tổng cả hai cột thành $10 > 4$ nên phải cắt ngang sau hàng $1$ — chỉ dùng $1$ vết cắt, nằm trong giới hạn $2$ phần. Vậy $4$ là đáp án.

## Ràng buộc

- $1 \le n, m \le 500$, $1 \le k \le n$, $0 \le a_{ij} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
