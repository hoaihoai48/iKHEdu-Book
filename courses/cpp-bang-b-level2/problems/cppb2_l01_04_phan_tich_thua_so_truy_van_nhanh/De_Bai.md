# Phân tích thừa số truy vấn nhanh

## Bối cảnh
Phân tích một số nguyên dương $N$ thành tích các thừa số nguyên tố:
$$N = p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k} \quad (p_1 < p_2 < \dots < p_k, a_i \ge 1)$$
là thao tác kinh điển trong số học. Khi cần phân tích số lượng lớn các số ($Q = 10^5$), thuật toán thử chia $\mathcal{O}(\sqrt{N})$ cho từng số sẽ bị quá thời gian. Việc áp dụng mảng **Sàng ước số nguyên tố nhỏ nhất (SPF)** cho phép phân tích mỗi số chỉ trong thời gian $\mathcal{O}(\log N)$.

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $N$ ($2 \le N \le 10^6$). Hãy in ra dạng phân tích thừa số nguyên tố của $N$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Phân Tích Thừa Số Truy Vấn Nhanh với độ phức tạp tối ưu nhất.

## Input
- Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$) — số lượng truy vấn.
- $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $N$ ($2 \le N \le 10^6$).

## Output
- Gồm $Q$ dòng, mỗi dòng in ra dạng phân tích của $N$. Mỗi thừa số nguyên tố và số mũ được in dưới dạng `p^a`, các cặp thừa số cách nhau bởi một dấu cách theo thứ tự các số nguyên tố tăng dần.

## Sample 1
### Input
```text
4
12
84
13
1000000
```
### Output
```text
2^2 3^1
2^2 3^1 7^1
13^1
2^6 5^6
```
### Giải thích
* $12 = 2^2 \times 3^1$.
* $84 = 2^2 \times 3^1 \times 7^1$.
* $13 = 13^1$.
* $1000000 = 10^6 = 2^6 \times 5^6$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
