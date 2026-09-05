# Trò chơi đoán số nhị phân


## Bối cảnh

Giờ ra chơi, bạn An nghĩ ra một số bí mật từ 1 đến $N$ rồi đố cả lớp cùng đoán. Bạn Bình xung phong với chiến thuật rất hay tên là "Chặt đôi khoảng tìm kiếm" (Tìm kiếm nhị phân) để đoán số: mỗi câu hỏi Bình chia đôi khoảng đang xét ($N = N // 2$). Cả lớp nín thở theo dõi từng lượt đoán của Bình. Hãy giúp Bình tính trước xem mình cần đoán mấy lượt.
## Nhiệm vụ

Hỏi trong trường hợp xấu nhất, Bình phải đoán **nhiều nhất bao nhiêu lần** thì chắc chắn tìm ra số của An (lặp cho đến khi khoảng chỉ còn 1 số: $N == 1$)?
## Input

Một số tự nhiên $N$ ($1 \le N \le 10^9$).
## Output

Số bước đoán tối đa.
## Sample 1

### Input
```text
8
```
### Output
```text
4
```
### Giải thích

Các bước: $8 \to 4 \to 2 \to 1$ (cần 4 bước).


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
