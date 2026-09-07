# Tìm khớp và cầu bằng thuật toán Tarjan

## Bối cảnh

Tập đoàn viễn thông cần rà soát mạng lưới N tổng đài nối với nhau bằng M tuyến cáp quang hai chiều để tìm các điểm xung yếu trước mùa mưa bão. Một tuyến cáp gọi là cầu nếu đứt nó sẽ chia cắt mạng lưới, một tổng đài gọi là khớp nếu sập nó sẽ làm mạng rời rạc. Đội kỹ thuật dùng thuật toán Tarjan duyệt theo chiều sâu để đếm số khớp và số cầu, phục vụ kế hoạch gia cố hạ tầng trọng yếu.

## Nhiệm vụ

Cho đồ thị vô hướng gồm $N$ đỉnh và $M$ cạnh. Hãy lập trình đếm số khớp (articulation) và số cầu (bridge) bằng thuật toán Tarjan, rồi in ra hai số trên một dòng.

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
2 3```

### Giải thích

- Mạng là đường thẳng $1-2-3-4$: cắt bất kỳ cạnh nào cũng chia cắt mạng nên có $3$ cầu.
- Sập tổng đài $2$ hoặc $3$ sẽ làm mạng rời rạc, còn sập $1$ hay $4$ thì phần còn lại vẫn liên thông nên có $2$ khớp.
- Chương trình in ra $2\ 3$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
