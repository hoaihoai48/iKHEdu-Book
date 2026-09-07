# Xóa ký tự để thành palindrome ngắn nhất

## Bối cảnh

Em học sinh đang tập làm thơ lục bát và viết ra một dòng chữ nháp, nhưng cô giáo yêu cầu dòng thơ khi đọc xuôi hay đọc ngược phải giống hệt nhau mới đạt điểm tối đa về vần điệu. Em được phép xóa bớt một số chữ cái trong dòng nháp (giữ nguyên thứ tự các chữ còn lại) để tạo thành một chuỗi đối xứng. Vì mỗi chữ bị xóa đều làm mất một ý thơ, em muốn xóa càng ít chữ càng tốt mà vẫn được chuỗi đối xứng.

## Nhiệm vụ

Cho một chuỗi $s$. Được xóa một số ký tự (có thể không xóa) sao cho chuỗi còn lại đối xứng (đọc xuôi ngược như nhau). Hãy lập trình tính số ký tự ít nhất cần xóa, rồi in ra số đó.

## Input

- Dòng đầu tiên chứa chuỗi $s$ ($1 \le |s| \le 1000$) gồm các chữ cái thường.

## Output

- In ra một số nguyên duy nhất là số ký tự ít nhất cần xóa.

## Sample 1

### Input

```text
abca
```

### Output

```text
1
```

### Giải thích

- Chuỗi ban đầu `abca` đọc ngược thành `acba` nên chưa đối xứng.
- Xóa đúng một chữ `c` ở giữa còn lại `aba`, đọc xuôi ngược đều như nhau.
- Không thể giữ nguyên cả bốn chữ vì `abca` không đối xứng, nên số chữ ít nhất cần xóa là $1$.

## Ràng buộc

- $1 \le |s| \le 1000$, chỉ gồm chữ cái thường.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
