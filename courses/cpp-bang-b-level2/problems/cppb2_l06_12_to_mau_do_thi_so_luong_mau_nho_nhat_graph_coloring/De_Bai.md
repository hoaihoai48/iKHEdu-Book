# Tô màu đồ thị số lượng màu nhỏ nhất (graph coloring)

## Bối cảnh

Nhà trường cần xếp lịch thi cuối kỳ cho $N$ môn học nhưng phòng thi có hạn nên nhiều môn phải thi chung buổi. Hai môn có chung thí sinh không thể xếp cùng một buổi, vì một bạn không thể ngồi hai phòng cùng lúc. Mỗi buổi thi được coi là một màu tô cho các môn thi trong buổi đó, và hai môn xung đột phải mang màu khác nhau. Ban giám hiệu muốn dùng càng ít buổi thi càng tốt để kỳ thi kết thúc sớm và học sinh được nghỉ hè đúng hẹn.

## Nhiệm vụ

Cho $N$ môn học và danh sách các cặp môn xung đột (có chung thí sinh). Hãy lập trình tìm số buổi thi ít nhất sao cho có thể xếp mỗi môn vào một buổi mà hai môn xung đột luôn khác buổi, rồi in ra số buổi đó.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, M$ ($1 \le N \le 18$, $0 \le M \le N \times (N - 1) / 2$), là số môn học và số cặp xung đột.
- $M$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u, v$ ($1 \le u, v \le N$, $u \ne v$), nghĩa là môn $u$ và môn $v$ có chung thí sinh.

## Output

- In ra một số nguyên duy nhất là số buổi thi ít nhất.

## Sample 1

### Input

```text
3 2
1 2
2 3
```

### Output

```text
2
```

### Giải thích

- Môn $1$ xung đột với môn $2$, môn $2$ xung đột với môn $3$, còn môn $1$ và môn $3$ không chung thí sinh.
- Xếp môn $1$ và môn $3$ vào buổi thứ nhất, môn $2$ vào buổi thứ hai thì không có cặp xung đột nào chung buổi.
- Không thể xếp cả ba môn vào một buổi vì môn $1$ và môn $2$ xung đột nhau, nên đáp án là $2$.

## Ràng buộc

- $1 \le N \le 18$, $0 \le M \le N \times (N - 1) / 2$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
