# Dãy con hình sóng núi dài nhất (bitonic subsequence)

## Bối cảnh

Đội địa hình ghi lại độ cao của $N$ trạm quan trắc dọc theo tuyến đường leo núi theo đúng thứ tự hành trình. Ban tổ chức giải chạy trail muốn chọn ra một nhóm trạm (giữ nguyên thứ tự) mà độ cao tăng dần lên tới một đỉnh rồi giảm dần xuống, tạo thành hình sóng núi đẹp mắt để đặt các điểm tiếp sức. Nhóm trạm càng đông thì đường chạy càng dài và càng hấp dẫn, nên ban tổ chức cần biết có thể chọn được nhiều nhất bao nhiêu trạm.

## Nhiệm vụ

Cho $N$ số nguyên là độ cao các trạm theo thứ tự. Hãy lập trình tìm dãy con (giữ nguyên thứ tự) dài nhất mà tăng nghiêm ngặt rồi giảm nghiêm ngặt (chỉ tăng hoặc chỉ giảm cũng được tính), rồi in ra độ dài của dãy đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 1000$), là số trạm quan trắc.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^9$), là độ cao từng trạm.

## Output

- In ra một số nguyên duy nhất là độ dài của dãy con hình sóng núi dài nhất.

## Sample 1

### Input

```text
5
1 4 2 5 3
```

### Output

```text
4
```

### Giải thích

- Dãy độ cao theo thứ tự là $1, 4, 2, 5, 3$.
- Chọn bốn trạm $1, 2, 5, 3$ theo đúng thứ tự: đoạn $1, 2, 5$ tăng dần lên đỉnh $5$ rồi giảm xuống $3$.
- Không tồn tại năm trạm nào tạo thành hình sóng núi vì cả dãy $1, 4, 2, 5, 3$ lên xuống hai lần, nên đáp án là $4$.

## Ràng buộc

- $1 \le N \le 1000$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
