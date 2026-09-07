# Dãy con tăng dài nhất LIS $\mathcal{o}(n \log n)$

## Bối cảnh

Huấn luyện viên đội tuyển bơi lội ghi lại thành tích của $N$ vận động viên trẻ qua các buổi kiểm tra thể lực theo đúng thứ tự thời gian. Ông muốn tìm ra một nhóm vận động viên mà phong độ tăng dần đều đặn qua từng buổi (không cần liên tiếp nhau) để đưa vào danh sách bồi dưỡng chuyên sâu cho giải toàn quốc. Nhóm càng đông thì chương trình đào tạo càng hiệu quả, nên ông cần biết nhóm tăng dần dài nhất có thể chọn được gồm bao nhiêu người.

## Nhiệm vụ

Cho $N$ số nguyên theo đúng thứ tự thời gian. Hãy lập trình tìm dãy con (không cần liên tiếp, nhưng giữ nguyên thứ tự) tăng nghiêm ngặt dài nhất, rồi in ra độ dài của dãy đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số vận động viên.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^9$), là thành tích theo thứ tự thời gian.

## Output

- In ra một số nguyên duy nhất là độ dài của dãy con tăng dài nhất.

## Sample 1

### Input

```text
5
3 1 2 5 4
```

### Output

```text
3
```

### Giải thích

- Dãy thành tích theo thời gian là $3, 1, 2, 5, 4$.
- Chọn ba người có thành tích $1, 2, 5$ theo đúng thứ tự xuất hiện được dãy tăng dần.
- Mọi dãy con tăng khác đều chỉ dài tối đa $3$, ví dụ $1, 2, 4$ cũng dài $3$ nhưng không thể tìm được bốn người nào có thành tích tăng dần.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
