# Phục hồi dãy số đơn điệu với chi phí nhỏ nhất (slope trick cơ bản)

## Bối cảnh

Thầy giáo thể dục ghi lại chiều cao của $N$ bạn học sinh đang xếp thành một hàng dọc để chuẩn bị đội hình diễu hành. Thầy muốn điều chỉnh chiều cao (bằng cách cho các bạn đứng lên bục hoặc xuống hố nhỏ) sao cho cả hàng tăng dần nghiêm ngặt từ đầu đến cuối cho đẹp đội hình. Mỗi xăng-ti-mét điều chỉnh của một bạn tốn một đơn vị công sức, và thầy muốn tổng công sức bỏ ra là ít nhất để buổi tập kết thúc sớm trước giờ nắng gắt.

## Nhiệm vụ

Cho $N$ số nguyên là chiều cao ban đầu của từng bạn theo thứ tự. Được thay mỗi số thành một số nguyên mới sao cho dãy mới tăng nghiêm ngặt, chi phí bằng tổng độ chênh lệch tuyệt đối từng vị trí. Hãy lập trình tính chi phí nhỏ nhất, rồi in ra chi phí đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số học sinh.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^6$), là chiều cao ban đầu.

## Output

- In ra một số nguyên duy nhất là tổng chi phí điều chỉnh nhỏ nhất.

## Sample 1

### Input

```text
3
3 2 1
```

### Output

```text
4
```

### Giải thích

- Dãy ban đầu $3, 2, 1$ giảm dần nên buộc phải điều chỉnh để thành dãy tăng nghiêm ngặt.
- Thử dãy đích $1, 2, 3$: chi phí $|3 - 1| + |2 - 2| + |1 - 3| = 2 + 0 + 2 = 4$.
- Thử dãy đích $2, 3, 4$: chi phí $|3 - 2| + |2 - 3| + |1 - 4| = 1 + 1 + 3 = 5$.
- Mọi dãy tăng nghiêm ngặt khác đều tốn từ $4$ trở lên, nên chi phí nhỏ nhất là $4$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le a_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
