# Đoạn Con Đối Xứng Liên Tiếp Dài Nhất

## Bối cảnh
Khác với chuỗi con rời rạc, một đoạn con liên tiếp (Substring) đối xứng đòi hỏi các ký tự phải đứng kề sát nhau và tạo thành một cụm đối xứng hoàn chỉnh. Đây là tác vụ trọng tâm trong việc nhận diện các đoạn lặp đảo ngược trong cấu trúc chuỗi gen sinh học.

## Nhiệm vụ
Cho chuỗi ký tự $S$. Hãy lập trình tìm độ dài của đoạn con liên tiếp đối xứng dài nhất trong $S$.

## Input
- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).

## Output
- In ra trên một dòng duy nhất độ dài của đoạn con đối xứng liên tiếp dài nhất.

## Sample 1
### Input
```text
babad
```
### Output
```text
3
bab
```

### Giải thích
Với chuỗi $S = \text{"babad"}$:
Đoạn con liên tiếp đối xứng dài nhất là $\text{"bab"}$ (hoặc $\text{"aba"}$) có độ dài bằng 3.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
