# Đếm hoán vị có đúng K điểm cố định

## Bối cảnh

Thư viện tỉnh tổ chức trò chơi bốc thăm trúng thưởng với N phong bì được đánh số và N phần quà tương ứng đặt ngẫu nhiên vào các phong bì. Ban tổ chức muốn tạo kịch tính nên yêu cầu có đúng K phong bì chứa đúng phần quà mang số của chính nó, các phong bì còn lại đều chứa quà khác số. Để in vé mời, ban tổ chức cần biết có bao nhiêu cách xếp quà thỏa mãn, lấy dư cho 1 000 000 007.

## Nhiệm vụ

Cho hai số nguyên $N, K$. Hãy lập trình tính số hoán vị của $N$ phần tử có đúng $K$ điểm cố định, tức $C(N,K) \times D(N-K)$ với $D$ là số derangement, rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng duy nhất: hai số nguyên $N, K$ ($0 \le K \le N \le 10^6$).

## Output

- In ra một dòng duy nhất là đáp án theo modulo $1\,000\,000\,007$ (quy ước $D(0) = 1$, $D(1) = 0$).

## Sample 1

### Input

```text
4 2
```

### Output

```text
6```

### Giải thích

- Chọn $2$ vị trí cố định trong $4$ vị trí: có $C(4,2) = 6$ cách.
- Hai vị trí còn lại phải xáo trộn hoàn toàn không giữ nguyên: $D(2) = 1$ cách duy nhất là đổi chỗ cho nhau.
- Tổng $6 \times 1 = 6$ nên chương trình in ra $6$.

## Ràng buộc

- $0 \le K \le N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
