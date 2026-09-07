# Lập lịch công việc có deadline & tiền phạt

## Bối cảnh

Anh kỹ sư nhận sửa chữa máy móc cho nhiều hộ gia đình trong khu phố, mỗi việc có một hạn hoàn thành và một khoản tiền công. Anh chỉ làm được một việc trong mỗi ngày và muốn chọn ra những việc sẽ nhận sao cho vừa kịp hạn vừa thu được nhiều tiền công nhất, vì cuối tháng anh cần tiền đóng viện phí cho mẹ. Những việc không kịp làm đành phải từ chối ngay từ đầu để khách còn kịp tìm thợ khác, nên anh cần một lịch làm việc rõ ràng từng ngày.

## Nhiệm vụ

Cho $N$ công việc, mỗi việc có hạn hoàn thành $deadline_i$ (ngày) và tiền công $profit_i$ (mỗi việc làm trong đúng một ngày). Hãy lập trình chọn ra các việc có thể hoàn thành đúng hạn sao cho tổng tiền công lớn nhất, rồi in ra số việc được chọn và tổng tiền công đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số công việc.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $deadline_i, profit_i$ ($1 \le deadline_i \le 10^5$, $1 \le profit_i \le 10^6$), là hạn hoàn thành và tiền công của một việc.

## Output

- In ra hai số nguyên trên một dòng: số việc được chọn và tổng tiền công lớn nhất.

## Sample 1

### Input

```text
4
2 100
1 50
2 10
1 20
```

### Output

```text
2 150
```

### Giải thích

- Xét các việc theo tiền công giảm dần: $(2, 100)$, $(1, 50)$, $(1, 20)$, $(2, 10)$.
- Việc tiền công $100$ hạn ngày $2$ còn ngày $2$ trống nên nhận, làm vào ngày $2$.
- Việc tiền công $50$ hạn ngày $1$ còn ngày $1$ trống nên nhận, làm vào ngày $1$.
- Việc tiền công $20$ hạn ngày $1$ nhưng ngày $1$ đã bận nên phải từ chối.
- Việc tiền công $10$ hạn ngày $2$ nhưng cả hai ngày đều bận nên phải từ chối.
- Nhận $2$ việc với tổng tiền công $100 + 50 = 150$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le deadline_i \le 10^5$, $1 \le profit_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
