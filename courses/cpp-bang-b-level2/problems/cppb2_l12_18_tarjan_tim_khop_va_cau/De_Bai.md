# Tarjan tìm khớp và cầu

## Bối cảnh

Trung tâm dữ liệu quốc gia vận hành mạng N máy chủ nối với nhau bằng M tuyến cáp hai chiều phục vụ các dịch vụ công trực tuyến. Trước đợt diễn tập an ninh mạng, đội ngũ kỹ thuật cần liệt kê các máy chủ trọng yếu mà nếu ngừng hoạt động sẽ chia cắt hệ thống cùng các tuyến cáp đơn lẻ mà nếu đứt sẽ cô lập một phần mạng lưới. Thuật toán Tarjan duyệt theo chiều sâu được dùng để đánh dấu khớp và cầu trong một lần duyệt duy nhất.

## Nhiệm vụ

Cho đồ thị vô hướng gồm $N$ đỉnh và $M$ cạnh. Hãy lập trình đếm số khớp và số cầu bằng thuật toán Tarjan, rồi in ra hai số trên một dòng theo thứ tự: số khớp, số cầu.

## Input

- Dòng 1: hai số nguyên $N, M$ ($1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v$ là một cạnh hai chiều.

## Output

- In ra một dòng duy nhất gồm hai số: số khớp và số cầu.

## Sample 1

### Input

```text
4 3
1 2
2 3
3 4
```

### Output

```text
2 3
```

### Giải thích

- Mạng là đường thẳng $1-2-3-4$: cắt bất kỳ cạnh nào cũng chia cắt mạng nên có $3$ cầu.
- Ngừng máy $2$ hoặc $3$ sẽ làm mạng rời rạc, còn ngừng $1$ hay $4$ thì phần còn lại vẫn liên thông nên có $2$ khớp.
- Chương trình in ra $2\ 3$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
