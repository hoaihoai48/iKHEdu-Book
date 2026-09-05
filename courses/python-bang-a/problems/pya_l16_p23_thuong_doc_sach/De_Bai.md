# Thưởng đọc sách

## Bối cảnh

Để khuyến khích đọc sách, thư viện treo giải: bạn nào đọc hết $N$ quyển sách sẽ được thưởng sao. Quyển thứ 1 được 1 sao, quyển thứ 2 được 2 sao, cứ thế quyển thứ $N$ được $N$ sao. An quyết tâm đọc hết $N$ quyển và muốn biết trước mình sẽ nhận được bao nhiêu sao.

## Nhiệm vụ

Cho số $N$. Hãy tính tổng số sao từ quyển 1 đến quyển $N$.

## Input

Một số nguyên $N$ ($1 \le N \le 10^{12}$).

## Output

In ra một số nguyên duy nhất là tổng số sao.

## Sample 1

### Input

```text
5
```

### Output

```text
15
```

### Giải thích

$1 + 2 + 3 + 4 + 5 = 15$ sao.

## Ràng buộc

Subtask 1 (50% số điểm): $1 \le N \le 10^4$. Cộng từng quyển vẫn kịp giờ.

* Subtask 2 (50% số điểm): $10^4 < N \le 10^{12}$. Cộng từng quyển sẽ không kịp, cần công thức tính nhanh.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
