# Khôi phục cây khảo sát tầm nhìn đa hướng

## Bối cảnh

Trạm quan trắc môi trường ghi lại chỉ số bụi mịn mỗi giờ trong suốt $N$ giờ của đợt ô nhiễm không khí. Để đánh giá mức độ nghiêm trọng theo từng khung thời gian, trạm cần tính với mỗi khoảng $K$ giờ liên tiếp thì chỉ số cao nhất là bao nhiêu, rồi cộng dồn các giá trị cao nhất này thành một con số tổng hợp duy nhất. Con số tổng càng lớn thì đợt ô nhiễm càng kéo dài và đậm đặc, giúp thành phố quyết định có nên cho học sinh nghỉ học hay không.

## Nhiệm vụ

Cho $N$ số nguyên là chỉ số bụi mịn từng giờ và độ dài cửa sổ $K$. Với mỗi cửa sổ gồm $K$ giờ liên tiếp, lấy giá trị lớn nhất trong cửa sổ. Hãy lập trình tính tổng các giá trị lớn nhất này trên mọi cửa sổ, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, K$ ($1 \le K \le N \le 10^6$), là số giờ quan trắc và độ dài cửa sổ.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($-10^9 \le a_i \le 10^9$), là chỉ số từng giờ.

## Output

- In ra một số nguyên duy nhất là tổng các giá trị lớn nhất.

## Sample 1

### Input

```text
8 3
1 3 -1 -3 5 3 6 7
```

### Output

```text
29
```

### Giải thích

- Cửa sổ $[1, 3, -1]$ có giá trị lớn nhất $3$; trượt sang $[3, -1, -3]$ được $3$.
- Cửa sổ $[-1, -3, 5]$ được $5$; cửa sổ $[-3, 5, 3]$ được $5$.
- Cửa sổ $[5, 3, 6]$ được $6$; cửa sổ cuối $[3, 6, 7]$ được $7$.
- Tổng sáu giá trị là $3 + 3 + 5 + 5 + 6 + 7 = 29$.

## Ràng buộc

- $1 \le K \le N \le 10^6$, $-10^9 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
