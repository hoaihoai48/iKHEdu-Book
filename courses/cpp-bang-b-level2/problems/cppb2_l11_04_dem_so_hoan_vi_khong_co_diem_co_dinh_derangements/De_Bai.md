# Đếm hoán vị không có điểm cố định (Derangements)

## Bối cảnh

Bưu điện thành phố chạy chương trình đổi quà tri ân với đúng N hộp quà được đánh số và N phiếu trúng thưởng ghi số tương ứng. Máy phát quà bị lỗi nên hộp số i tuyệt đối không được rơi vào tay người cầm phiếu số i, nếu không hệ thống sẽ báo động và dừng dây chuyền. Người quản lý cần đếm có bao nhiêu cách phát quà hợp lệ, lấy phần dư cho 1 000 000 007 để đối chiếu với nhật ký kho hàng mỗi buổi tối.

## Nhiệm vụ

Cho số nguyên $N$. Hãy lập trình tính số hoán vị không có điểm cố định của $N$ phần tử (số derangement $D(N)$), rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng duy nhất: số nguyên $N$ ($1 \le N \le 10^6$).

## Output

- In ra một dòng duy nhất là $D(N) \bmod 1\,000\,000\,007$ ($D(1) = 0$, $D(2) = 1$).

## Sample 1

### Input

```text
4
```

### Output

```text
9
```

### Giải thích

- Với $N = 4$: liệt kê các hoán vị mà không vị trí nào giữ nguyên giá trị cũ.
- Đếm được $9$ hoán vị thỏa mãn, ví dụ $2\ 1\ 4\ 3$ và $2\ 3\ 4\ 1$ nằm trong danh sách.
- Chương trình in ra $9$.

## Ràng buộc

- $1 \le N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
