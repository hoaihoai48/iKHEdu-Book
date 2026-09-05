# Đếm từ dài

## Bối cảnh

Cô giáo ra trò chơi: cho một câu văn và một số $K$, bạn nào đếm đúng có bao nhiêu từ dài hơn $K$ ký tự sẽ được điểm 10. Từ là một nhóm ký tự liền nhau, các từ cách nhau bởi dấu cách. Na nhờ em đếm giúp để chắc chắn được điểm 10.

## Nhiệm vụ

Cho số $K$ và câu văn $S$. Hãy đếm số từ có độ dài lớn hơn $K$.

## Input

Dòng 1: số nguyên $K$ ($0 \le K \le 100$). Dòng 2: câu văn $S$ ($1 \le |S| \le 10^4$).

## Output

In ra một số nguyên duy nhất là số từ thỏa mãn.

## Sample 1

### Input

```text
3
Hom nay Bin di hoc cung ban Na
```

### Output

```text
1
```

### Giải thích

Các từ là: Hom, nay, Bin, di, hoc, cung, ban, Na. Chỉ có từ `cung` dài 4 ký tự, lớn hơn 3 nên đáp án là 1.

## Ràng buộc

Subtask 1 (50% số điểm): $|S| \le 100$.

* Subtask 2 (50% số điểm): $100 < |S| \le 10^4$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
