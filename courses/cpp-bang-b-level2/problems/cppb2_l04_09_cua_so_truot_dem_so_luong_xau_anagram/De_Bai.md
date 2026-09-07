# Cửa sổ trượt đếm số lượng xâu anagram

## Bối cảnh

Trong trò chơi ô chữ, bạn Mai có một xâu chữ dài và một từ khóa cần tìm các phiên bản đảo chữ của nó. Bạn muốn đếm xem có bao nhiêu đoạn con trong xâu dài là một cách sắp xếp lại các chữ cái của từ khóa.

Mai trượt một khung cửa sổ dọc theo xâu chữ, mỗi lần so sánh tần suất chữ cái trong khung với từ khóa.

## Nhiệm vụ

Cho xâu văn bản và từ khóa. Hãy lập trình đếm số đoạn con của văn bản là một hoán vị (anagram) của từ khóa.

## Input

- Gồm một dòng duy nhất chứa hai xâu $s, p$ (chỉ gồm chữ cái thường, $|s|, |p| \le 10^6$) cách nhau bởi một dấu cách — xâu văn bản và xâu mẫu.

## Output

- In ra một dòng duy nhất là số xâu con liên tiếp của $s$ có cùng độ dài với $p$ và là hoán vị ký tự (anagram) của $p$.

## Sample 1
### Input
```text
cbaebabacd abc
```
### Output
```text
2
```
### Giải thích

Mẫu `abc` dài $3$. Trượt cửa sổ dài $3$ trên `cbaebabacd`: vị trí $0$ được `cba` — đủ $a, b, c$ → đếm $1$; các vị trí $1$–$5$ (`bae`, `aeb`, `eba`, `bab`, `aba`) đều thiếu hoặc thừa ký tự; vị trí $6$ được `bac` — đủ bộ ba → đếm $2$; vị trí $7$ (`acd`) chứa $d$ nên loại. Tổng cộng $2$.

## Ràng buộc

- $|s|, |p| \le 10^6$, chỉ gồm `a`–`z`.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
