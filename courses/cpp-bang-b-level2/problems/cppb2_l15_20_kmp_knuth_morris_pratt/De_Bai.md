# Đếm số lần mẫu xuất hiện (KMP)

## Bối cảnh

Hệ thống lọc thư rác của nhà cung cấp email quét từng thư đến để đếm số lần xuất hiện của chữ ký mã độc đã biết trong cơ sở dữ liệu an ninh mạng. Mỗi thư có thể dài hàng trăm nghìn ký tự và chữ ký cần tìm cũng dài nên thuật toán KMP được dùng để duyệt thư đúng một lần mà không bỏ sót lần khớp nào, kể cả các lần khớp giao nhau. Số lượt khớp giúp bộ lọc quyết định cách ly thư hay chuyển vào hộp thư đến.

## Nhiệm vụ

Cho xâu văn bản $T$ và xâu mẫu $P$. Hãy lập trình đếm số lần $P$ xuất hiện trong $T$ (kể cả giao nhau) bằng thuật toán KMP, rồi in ra kết quả.

## Input

- Dòng 1: xâu $T$ ($1 \le |T| \le 10^6$).
- Dòng 2: xâu $P$ ($1 \le |P| \le |T|$).

## Output

- In ra một dòng duy nhất là số lần xuất hiện.

## Sample 1

### Input

```text
ababa
aba
```

### Output

```text
2
```

### Giải thích

- Văn bản $ababa$ dài năm ký tự, mẫu $aba$ dài ba ký tự.
- Mẫu khớp tại vị trí $1$ ($aba$) và tại vị trí $3$ ($aba$), hai lần khớp giao nhau ở ký tự $a$ giữa.
- Tổng số lần xuất hiện là $2$ nên in ra $2$.

## Ràng buộc

- $1 \le |P| \le |T| \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
