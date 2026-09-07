# Ghép cặp trọng số cực đại (maximum matching bitmask)

## Bối cảnh

Ban tổ chức giải cầu lông đôi của tỉnh cần ghép $N$ vận động viên (số lượng chẵn) thành từng cặp thi đấu. Huấn luyện viên đã chấm trước chỉ số ăn ý cho mỗi cặp hai người có thể ghép với nhau, vì có cặp phối hợp rất nhuần nhuyễn nhưng cũng có cặp khắc lối đánh của nhau. Ban tổ chức muốn chia tất cả vận động viên thành các cặp sao cho tổng chỉ số ăn ý của toàn bộ các cặp là lớn nhất, để chất lượng các trận đấu mở màn được hấp dẫn nhất.

## Nhiệm vụ

Cho bảng chỉ số ăn ý $w_{ij}$ giữa từng cặp vận động viên. Hãy lập trình chia $N$ người thành $N / 2$ cặp (mỗi người thuộc đúng một cặp) sao cho tổng chỉ số ăn ý lớn nhất, rồi in ra tổng lớn nhất đó.

## Input

- Dòng đầu tiên chứa số nguyên chẵn $N$ ($2 \le N \le 18$), là số vận động viên.
- $N$ dòng tiếp theo, mỗi dòng chứa $N$ số nguyên $w_{ij}$ ($0 \le w_{ij} \le 10^6$, $w_{ii} = 0$, $w_{ij} = w_{ji}$), là chỉ số ăn ý giữa người $i$ và người $j$.

## Output

- In ra một số nguyên duy nhất là tổng chỉ số ăn ý lớn nhất.

## Sample 1

### Input

```text
4
0 5 1 2
5 0 3 4
1 3 0 6
2 4 6 0
```

### Output

```text
11
```

### Giải thích

- Liệt kê cả $3$ cách chia bốn người thành hai cặp cùng tổng chỉ số ăn ý.
- Ghép $\{0, 1\}$ với $\{2, 3\}$ được $5 + 6 = 11$.
- Ghép $\{0, 2\}$ với $\{1, 3\}$ được $1 + 4 = 5$.
- Ghép $\{0, 3\}$ với $\{1, 2\}$ được $2 + 3 = 5$.
- Tổng lớn nhất trong ba cách là $11$.

## Ràng buộc

- $2 \le N \le 18$ ($N$ chẵn), $0 \le w_{ij} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
