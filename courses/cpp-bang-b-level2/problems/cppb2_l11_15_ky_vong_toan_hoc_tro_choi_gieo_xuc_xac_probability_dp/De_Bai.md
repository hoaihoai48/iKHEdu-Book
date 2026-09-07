# Kỳ vọng số lần gieo xúc xắc để tổng đạt N

## Bối cảnh

Câu lạc bộ boardgame của trường thiết kế trò chơi mới trong đó người chơi gieo một con xúc xắc sáu mặt công bằng rồi cộng dồn số chấm vào điểm của mình. Ván chơi kết thúc ngay khi tổng điểm đạt ít nhất N, và nhóm thiết kế cần biết trung bình phải gieo bao nhiêu lượt để in thời lượng dự kiến lên vỏ hộp. Vì đáp án là số thực nên nhóm quy định in đúng sáu chữ số sau dấu chấm thập phân.

## Nhiệm vụ

Cho số nguyên $N$. Hãy lập trình tính kỳ vọng số lần gieo một xúc xắc công bằng sáu mặt để tổng tích lũy đạt ít nhất $N$, rồi in ra với đúng sáu chữ số thập phân.

## Input

- Dòng duy nhất: số nguyên $N$ ($1 \le N \le 1000$).

## Output

- In ra một dòng duy nhất là kỳ vọng cần tính với đúng sáu chữ số sau dấu chấm thập phân.

## Sample 1

### Input

```text
1
```

### Output

```text
1.000000```

### Giải thích

- Với $N = 1$: chỉ cần gieo đúng một lần vì mặt nào của xúc xắc cũng cho ít nhất $1$ điểm.
- Tổng sau lần gieo đầu tiên chắc chắn đạt yêu cầu nên số lần gieo luôn bằng $1$.
- Kỳ vọng bằng $1$ nên chương trình in ra $1.000000$.

## Ràng buộc

- $1 \le N \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
