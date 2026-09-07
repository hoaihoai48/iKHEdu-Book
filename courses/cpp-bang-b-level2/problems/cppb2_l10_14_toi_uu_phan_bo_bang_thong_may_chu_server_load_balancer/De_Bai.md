# Tối ưu phân bổ băng thông máy chủ (server load balancer)

## Bối cảnh

Đội thi tin học của trường được phát $N$ mảnh giấy, mỗi mảnh ghi một số nguyên không âm, để tham gia trò chơi ghép số trên sân khấu. Các bạn được phép sắp xếp các mảnh giấy theo bất kỳ thứ tự nào rồi ghép chúng lại thành một con số duy nhất, và đội nào tạo ra con số lớn nhất sẽ giành giải nhất cùng phần thưởng là một chuyến dã ngoại. Trước giờ thi đấu, cả đội muốn tính trước xem với bộ mảnh giấy hiện có thì con số lớn nhất ghép được là gì.

## Nhiệm vụ

Cho $N$ chuỗi chỉ gồm chữ số. Hãy lập trình sắp xếp chúng theo một thứ tự rồi ghép lại sao cho con số tạo thành là lớn nhất có thể, rồi in ra con số đó (nếu mọi mảnh đều là `0` thì in ra `0`).

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số mảnh giấy.
- Dòng thứ hai chứa $N$ chuỗi $s_i$ ($1 \le |s_i| \le 100$, chỉ gồm chữ số), là các mảnh giấy.

## Output

- In ra con số lớn nhất có thể ghép được.

## Sample 1

### Input

```text
5
3 30 34 5 9
```

### Output

```text
9534330
```

### Giải thích

- So sánh từng cặp mảnh giấy khi đặt cạnh nhau: đặt `9` trước `5` vì `95` lớn hơn `59`; đặt `5` trước `34` vì `534` lớn hơn `345`; đặt `34` trước `3` vì `343` lớn hơn `334`; đặt `3` trước `30` vì `330` lớn hơn `303`.
- Thứ tự tốt nhất là `9`, `5`, `34`, `3`, `30`, ghép lại được `9534330`.
- Mọi thứ tự khác đều cho con số không vượt quá `9534330`.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le |s_i| \le 100$, chỉ gồm chữ số.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
