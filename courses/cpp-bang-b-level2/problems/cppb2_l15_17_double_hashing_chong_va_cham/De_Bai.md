# So khớp xâu con bằng double hashing

## Bối cảnh

Tòa soạn báo điện tử lưu trữ bài viết gốc dài hàng trăm nghìn ký tự và thường xuyên cần xác minh hai đoạn trích dẫn trong bài bình luận có trùng khớp từng chữ hay không để gỡ bài kịp thời. Mỗi yêu cầu đưa ra hai đoạn con và hệ thống phải trả lời trong thời gian hằng số nhờ tiền xử lý hàm băm kép với hai mô-đun nguyên tố độc lập. Việc dùng hai hàm băm song song giúp xác suất va chạm gần như bằng không trong thực tế vận hành.

## Nhiệm vụ

Cho xâu $S$ và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(l_1,r_1,l_2,r_2)$ (chỉ số từ $1$), hai xâu con tương ứng có bằng nhau hay không; in ra $YES$ hoặc $NO$.

## Input

- Dòng 1: xâu $S$ gồm chữ cái thường ($1 \le |S| \le 2 \cdot 10^5$) và số nguyên $Q$ ($1 \le Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $l_1, r_1, l_2, r_2$.

## Output

- Gồm $Q$ dòng, mỗi dòng là $YES$ hoặc $NO$.

## Sample 1

### Input

```text
ababa 2
1 3 3 5
1 2 2 3
```

### Output

```text
YES
NO
```

### Giải thích

- Truy vấn một so $S[1 \dots 3] =$ aba với $S[3 \dots 5] =$ aba: hai đoạn giống hệt nhau.
- Truy vấn hai so $S[1 \dots 2] =$ ab với $S[2 \dots 3] =$ ba: khác nhau ở ký tự đầu.
- Chương trình in ra $YES$ rồi $NO$ trên hai dòng.

## Ràng buộc

- $1 \le |S|, Q \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
