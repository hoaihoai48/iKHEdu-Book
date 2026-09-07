# Xâu con chung dài nhất (lcs)

## Bối cảnh

Hai nhà nghiên cứu ngôn ngữ độc lập ghi lại cùng một bài hát dân gian từ hai cụ cao niên ở hai bản khác nhau, thu được hai dãy ký tự có đôi chỗ khác biệt do cách phát âm vùng miền. Để khôi phục lại lời gốc của bài hát, họ muốn tìm đoạn lời chung dài nhất mà cả hai bản ghi đều chứa (không cần liên tiếp nhau, chỉ cần giữ đúng thứ tự). Đoạn chung càng dài thì bản phục dựng càng đáng tin cậy để đưa vào sách giáo khoa địa phương.

## Nhiệm vụ

Cho hai chuỗi $s$ và $t$. Hãy lập trình tìm xâu con chung (không cần liên tiếp) dài nhất của cả hai chuỗi, rồi in ra độ dài của xâu đó.

## Input

- Dòng đầu tiên chứa hai chuỗi $s$ và $t$ ($1 \le |s|, |t| \le 1000$), mỗi chuỗi chỉ gồm chữ cái thường.

## Output

- In ra một số nguyên duy nhất là độ dài của xâu con chung dài nhất.

## Sample 1

### Input

```text
abcde
ace
```

### Output

```text
3
```

### Giải thích

- Chuỗi thứ nhất là `abcde`, chuỗi thứ hai là `ace`.
- Ba ký tự `a`, `c`, `e` xuất hiện trong cả hai chuỗi theo đúng thứ tự nên ghép thành xâu chung `ace` dài $3$.
- Chuỗi thứ hai chỉ dài $3$ nên không thể có xâu chung nào dài hơn $3$.

## Ràng buộc

- $1 \le |s|, |t| \le 1000$, chỉ gồm chữ cái thường.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
