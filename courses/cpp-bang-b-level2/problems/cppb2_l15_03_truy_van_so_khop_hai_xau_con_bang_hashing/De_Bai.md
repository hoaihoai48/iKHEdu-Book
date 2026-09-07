# So khớp hai xâu con bằng hashing

## Bối cảnh

Hệ thống phát hiện đạo văn của nhà xuất bản cần so sánh hàng nghìn cặp đoạn văn bản trong cuốn tiểu thuyết dài hàng trăm nghìn ký tự để tìm các đoạn trích lặp lại trái phép. Mỗi truy vấn đưa ra hai đoạn con và yêu cầu trả lời chúng có giống hệt nhau hay không trong thời gian hằng số sau khi tiền xử lý hàm băm lăn. Ban biên tập dùng kết quả này để khoanh vùng các chương cần kiểm tra thủ công trước khi ký duyệt phát hành.

## Nhiệm vụ

Cho xâu $S$ và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(l_1,r_1,l_2,r_2)$ (chỉ số từ $1$), hai xâu con $S[l_1 \dots r_1]$ và $S[l_2 \dots r_2]$ có bằng nhau hay không; in ra $YES$ hoặc $NO$.

## Input

- Dòng 1: xâu $S$ gồm chữ cái thường ($1 \le |S| \le 2 \cdot 10^5$).
- Dòng 2: số nguyên $Q$ ($1 \le Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $l_1, r_1, l_2, r_2$.

## Output

- Gồm $Q$ dòng, mỗi dòng là $YES$ hoặc $NO$.

## Sample 1

### Input

```text
ababa
2
1 3 3 5
1 2 2 3
```

### Output

```text
YES
NO```

### Giải thích

- Truy vấn một so $S[1 \dots 3] =$ aba với $S[3 \dots 5] =$ aba: hai đoạn giống hệt nhau.
- Truy vấn hai so $S[1 \dots 2] =$ ab với $S[2 \dots 3] =$ ba: khác nhau ở ký tự đầu.
- Chương trình in ra $YES$ rồi $NO$ trên hai dòng.

## Ràng buộc

- $1 \le |S|, Q \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
