# Tìm kiếm đa mẫu Aho-Corasick

## Bối cảnh

Trung tâm ứng cứu khẩn cấp quét log hệ thống dài hàng triệu dòng để đếm tổng số lượt xuất hiện của K từ khóa cảnh báo đã đăng ký trong sổ tay vận hành máy chủ. Mỗi dòng log có thể chứa nhiều từ khóa khác nhau và các từ khóa có thể giao nhau nên việc tìm từng mẫu riêng lẻ sẽ quá chậm. Thuật toán Aho-Corasick xây một lần automaton rồi quét văn bản đúng một lượt, cộng dồn mọi lượt khớp để ra tổng số cảnh báo trong ca trực.

## Nhiệm vụ

Cho văn bản $T$ và $K$ mẫu $P_i$ (chữ cái thường). Hãy lập trình đếm tổng số lượt xuất hiện của mọi mẫu trong $T$ (kể cả giao nhau, mỗi mẫu tính riêng) bằng thuật toán Aho-Corasick, rồi in ra kết quả.

## Input

- Dòng 1: xâu $T$ và số nguyên $K$ ($1 \le |T| \le 10^6$, $1 \le K$, tổng $|P_i| \le 10^5$).
- $K$ dòng tiếp theo, mỗi dòng là một mẫu.

## Output

- In ra một dòng duy nhất là tổng số lượt khớp.

## Sample 1

### Input

```text
ababa 2
aba
ba
```

### Output

```text
4
```

### Giải thích

- Mẫu $aba$ xuất hiện hai lần tại vị trí $1$ và $3$; mẫu $ba$ xuất hiện hai lần tại vị trí $2$ và $4$.
- Tổng bốn lượt khớp nên chương trình in ra $4$.

## Ràng buộc

- $1 \le |T| \le 10^6$; tổng $|P_i| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
