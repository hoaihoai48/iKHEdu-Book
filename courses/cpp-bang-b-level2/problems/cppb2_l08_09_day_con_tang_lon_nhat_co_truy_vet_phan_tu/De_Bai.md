# Dãy con tăng lớn nhất có truy vết phần tử

## Bối cảnh

Câu lạc bộ cờ vua ghi lại hệ số elo của một kỳ thủ trẻ qua $N$ giải đấu liên tiếp để đánh giá sự tiến bộ. Ban huấn luyện muốn chỉ ra một chuỗi các giải mà elo tăng dần nghiêm ngặt (không cần là các giải liên tiếp nhau) và dài nhất có thể, để đưa vào hồ sơ đề nghị phong kiện tướng. Không chỉ cần biết chuỗi dài bao nhiêu giải, hồ sơ còn phải liệt kê cụ thể hệ số elo của từng giải trong chuỗi đó để hội đồng thẩm định kiểm tra.

## Nhiệm vụ

Cho $N$ số nguyên là hệ số elo qua các giải theo đúng thứ tự thời gian. Hãy lập trình tìm một dãy con tăng nghiêm ngặt dài nhất, rồi in ra độ dài của nó ở dòng đầu và các phần tử của dãy đó ở dòng thứ hai.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 1000$), là số giải đấu.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^9$), là hệ số elo theo thứ tự thời gian.

## Output

- Dòng đầu tiên in ra độ dài của dãy con tăng dài nhất.
- Dòng thứ hai in ra các phần tử của một dãy con tăng dài nhất (được chấp nhận bất kỳ dãy nào đạt độ dài tối đa).

## Sample 1

### Input

```text
5
3 1 2 5 4
```

### Output

```text
3
1 2 5
```

### Giải thích

- Dãy elo theo thời gian là $3, 1, 2, 5, 4$.
- Ba giải có elo $1, 2, 5$ xuất hiện theo đúng thứ tự và tăng dần nên tạo thành dãy con tăng dài $3$.
- Không tồn tại bốn giải nào có elo tăng dần, nên độ dài tối đa là $3$ và dãy $1, 2, 5$ là một đáp án hợp lệ.

## Ràng buộc

- $1 \le N \le 1000$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
