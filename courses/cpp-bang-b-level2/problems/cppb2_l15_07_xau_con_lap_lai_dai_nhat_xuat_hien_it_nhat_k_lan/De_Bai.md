# Xâu con lặp dài nhất xuất hiện ít nhất K lần

## Bối cảnh

Phòng phân tích gen của bệnh viện nghiên cứu đoạn ADN dài để tìm trình tự lặp lại ít nhất K lần vì những vùng lặp này thường liên quan đến cơ chế gây bệnh di truyền cần theo dõi. Các nhà khoa học cần biết độ dài lớn nhất của một trình tự như vậy để thiết kế kít xét nghiệm tập trung vào vùng gen đáng ngờ. Hậu tố kết hợp tìm kiếm nhị phân giúp xác định đáp án mà không cần so sánh từng cặp đoạn gen.

## Nhiệm vụ

Cho xâu $S$ và số nguyên $K$. Hãy lập trình tính độ dài lớn nhất của một xâu con xuất hiện ít nhất $K$ lần trong $S$ (các lần xuất hiện có thể giao nhau), rồi in ra kết quả.

## Input

- Dòng 1: xâu $S$ ($1 \le |S| \le 2 \cdot 10^5$).
- Dòng 2: số nguyên $K$ ($2 \le K \le |S|$).

## Output

- In ra một dòng duy nhất là độ dài cần tìm ($0$ nếu không tồn tại).

## Sample 1

### Input

```text
banana
2
```

### Output

```text
3```

### Giải thích

- Xâu $banana$: đoạn $ana$ xuất hiện tại vị trí $2$ và vị trí $4$ nên đủ hai lần.
- Mọi đoạn dài bốn ký tự trở lên như $bana$ hay $anan$ đều chỉ xuất hiện một lần.
- Độ dài lớn nhất là $3$ nên in ra $3$.

## Ràng buộc

- $1 \le |S| \le 2 \cdot 10^5$; $2 \le K \le |S|$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
