# Điểm Olympic Bỏ Max Bỏ Min


## Bối cảnh

Trong hội thi Bơi lội Olympic, có $N$ giám khảo chấm điểm ($N \ge 3$). Để đảm bảo công bằng tuyệt đối, điểm số chính thức của vận động viên là trung bình cộng sau khi đã **bỏ đi một điểm cao nhất và một điểm thấp nhất**.
## Nhiệm vụ

Cho $N$ điểm số. Hãy tính điểm chính thức của vận động viên (làm tròn 2 chữ số thập phân).
## Input

  * Dòng 1: Số nguyên $N$ ($3 \le N \le 1000$).
  * Dòng 2: $N$ số thực cách nhau bởi khoảng trắng.
## Output

Điểm trung bình sau khi loại bỏ 1 điểm max và 1 điểm min.
## Sample 1

### Input
```text
5
7.0 9.0 8.0 10.0 6.0
```
### Output
```text
8.00
```
### Giải thích

Bỏ min là 6.0, bỏ max là 10.0. Còn lại: 7.0, 8.0, 9.0. Trung bình là 8.00.


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
