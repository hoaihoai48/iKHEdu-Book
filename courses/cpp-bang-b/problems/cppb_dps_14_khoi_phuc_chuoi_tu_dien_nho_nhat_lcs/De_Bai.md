# Độ Dài LCS Giữa Hai Chuỗi Gen

## Bối cảnh
Trong đề án nghiên cứu tiến hóa học phân tử, các nhà di truyền học so sánh hai chuỗi gen dài được biểu diễn dưới dạng hai chuỗi ký tự chỉ gồm 4 loại nucleotide cơ bản: `A`, `C`, `G`, `T`. Việc tìm độ dài xâu con chung dài nhất giữa hai chuỗi gen phản ánh mức độ gần gũi về mặt quan hệ tiến hóa giữa hai loài sinh vật.

## Nhiệm vụ
Cho hai chuỗi gen $S$ và $T$. Hãy lập trình tính độ dài chuỗi con chung dài nhất giữa hai chuỗi đó.

## Input
- Dòng 1: Chứa chuỗi gen thứ nhất $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chứa chuỗi gen thứ hai $T$ ($1 \le |T| \le 2000$).

## Output
- In ra trên một dòng duy nhất độ dài xâu con chung dài nhất.

## Sample 1
### Input
```text
ACCGGTCGAGTGCGCGGAAGCCGGCCGAA
GTCGTTCGGAATGCCGTTGCTCTGTAAA
```
### Output
```text
20
```

### Giải thích
Với hai chuỗi gen $S = \text{"AGGTAB"}$ và $T = \text{"GXTXAYB"}$:
Xâu con chung dài nhất giữa hai mẫu gen là $\text{"GTAB"}$ có độ dài bằng 4.

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |T| \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
