# Tổng các chữ số của số có 3 chữ số

## Bối cảnh
Bạn Tâm tham gia cuộc thi đố vui toán học với thử thách: nhìn vào một số nguyên dương có đúng 3 chữ số, phải nhanh chóng cộng tổng cả ba chữ số lại. Ví dụ với số $496$, tổng các chữ số là $4 + 9 + 6 = 19$. Thay vì tính nhẩm, Tâm muốn viết một chương trình Scratch giúp tự động tách ba chữ số hàng trăm, hàng chục, hàng đơn vị rồi cộng lại.


## Nhiệm vụ
Nhập số nguyên $N$ ($100 \le N \le 999$). In ra tổng của 3 chữ số hàng trăm, hàng chục và hàng đơn vị.

## Input
Một dòng chứa số nguyên $N$.

## Output
In ra tổng các chữ số.

## Sample 1
### Input
```text
385
```
### Output
```text
16
```
### Giải thích
Chữ số hàng trăm $385 // 100 = 3$. Chữ số hàng chục $(385 // 10) \% 10 = 8$. Chữ số hàng đơn vị $385 \% 10 = 5$. Tổng $= 3 + 8 + 5 = 16$.
