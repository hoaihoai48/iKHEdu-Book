# Bậc của hoán vị (LCM độ dài chu trình)

## Bối cảnh

Xưởng in bao bì dùng băng chuyền gồm N khay mực được hoán đổi vị trí theo một quy tắc cố định sau mỗi ca sản xuất để mực không bị lắng cặn. Kỹ sư vận hành cần biết sau bao nhiêu ca thì mọi khay mực trở về đúng vị trí ban đầu để lên lịch bảo dưỡng toàn dây chuyền. Con số này chính là bội chung nhỏ nhất của độ dài các chu trình rời rạc trong hoán vị mô tả quy tắc đổi chỗ.

## Nhiệm vụ

Cho hoán vị $p_1, \dots, p_N$ của $1, \dots, N$. Hãy lập trình tính bậc của hoán vị, tức bội chung nhỏ nhất của độ dài các chu trình rời rạc, rồi in ra kết quả.

## Input

- Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $p_1, \dots, p_N$ là một hoán vị của $1, \dots, N$.

## Output

- In ra một dòng duy nhất là bậc của hoán vị.

## Sample 1

### Input

```text
4
2 1 4 3
```

### Output

```text
2
```

### Giải thích

- Hoán vị $2\ 1\ 4\ 3$ tách thành hai chu trình $(1\ 2)$ và $(3\ 4)$, mỗi chu trình dài $2$.
- Bội chung nhỏ nhất của $2$ và $2$ là $2$, nghĩa là sau $2$ ca mọi khay về chỗ cũ.
- Chương trình in ra $2$.

## Ràng buộc

- $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
