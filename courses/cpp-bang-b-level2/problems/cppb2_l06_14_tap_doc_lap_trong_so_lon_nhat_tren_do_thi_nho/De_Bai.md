# Tập độc lập trọng số lớn nhất trên đồ thị nhỏ

## Bối cảnh

Huyện miền núi muốn chọn vị trí đặt các trạm phát sóng mới để phủ sóng điện thoại cho bà con. Mỗi vị trí ứng cử mang lại một lợi ích khác nhau tùy theo số hộ dân xung quanh, và ban quản lý đã chấm điểm lợi ích cho từng nơi. Tuy nhiên hai vị trí kề nhau không thể cùng đặt trạm vì sóng sẽ gây nhiễu lẫn nhau. Huyện cần chọn ra một nhóm vị trí đôi một không kề nhau sao cho tổng điểm lợi ích là lớn nhất.

## Nhiệm vụ

Cho $N$ vị trí với điểm lợi ích $val_i$ và danh sách $M$ cặp vị trí kề nhau. Hãy lập trình chọn một tập vị trí đôi một không kề nhau có tổng lợi ích lớn nhất, rồi in ra tổng lớn nhất đó.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, M$ ($1 \le N \le 20$, $0 \le M \le N \times (N - 1) / 2$), là số vị trí và số cặp kề nhau.
- Dòng thứ hai chứa $N$ số nguyên $val_i$ ($0 \le val_i \le 10^6$), là điểm lợi ích của từng vị trí.
- $M$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u, v$ ($1 \le u, v \le N$, $u \ne v$), nghĩa là vị trí $u$ và vị trí $v$ kề nhau.

## Output

- In ra một số nguyên duy nhất là tổng lợi ích lớn nhất (chọn tập rỗng được tổng $0$).

## Sample 1

### Input

```text
4 2
10 20 30 40
1 2
3 4
```

### Output

```text
60
```

### Giải thích

- Vị trí $1$ kề vị trí $2$, vị trí $3$ kề vị trí $4$, các cặp còn lại không kề nhau.
- Xét các nhóm đôi một không kề nhau: nhóm $\{2, 4\}$ được $20 + 40 = 60$; nhóm $\{1, 4\}$ được $10 + 40 = 50$; nhóm $\{2, 3\}$ được $20 + 30 = 50$; nhóm $\{1, 3\}$ được $10 + 30 = 40$.
- Mọi nhóm hợp lệ khác đều có tổng không vượt quá $60$, nên đáp án là $60$.

## Ràng buộc

- $1 \le N \le 20$, $0 \le M \le N \times (N - 1) / 2$, $0 \le val_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
