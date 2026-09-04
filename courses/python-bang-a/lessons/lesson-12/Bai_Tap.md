# Hệ thống bài tập thực hành — bài 12: Thống kê danh sách và sắp xếp

---

## Bảng ma trận bài tập (14 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L17-P01` | Điểm số cao nhất & thấp nhất | `Cơ bản` | $N \le 1000$ | Dùng hàm `max()` và `min()` |
| 02 | `PYA-L17-P02` | Sắp xếp tăng dần đơn giản | `Cơ bản` | $N \le 1000$ | Sử dụng `a.sort()` |
| 03 | `PYA-L17-P03` | Điểm trung bình môn học | `Cơ bản` | $N \le 1000$ | Tính `sum(a) / len(a)` làm tròn 2 chữ số |
| 04 | `PYA-L17-P04` | Sắp xếp giảm dần bảng xếp hạng | `Cơ bản` | $N \le 10^5$ | Sử dụng `a.sort(reverse=True)` |
| 05 | `PYA-L17-P05` | Tìm số lớn thứ nhì trong mảng | `Cơ bản` | $N \le 10^5$ | Tìm số lớn thứ hai (loại trừ các số bằng max) |
| 06 | `PYA-L17-P06` | Đếm số lượng học sinh trên điểm trung bình | `Luyện tập` | $N \le 10^5$ | So sánh từng phần tử với giá trị trung bình |
| 07 | `PYA-L17-P07` | Lọc bỏ các số trùng lặp | `Luyện tập` | $N \le 10^5$ | Giữ lại các số độc nhất tăng dần |
| 08 | `PYA-L17-P08` | Điểm Olympic bỏ max bỏ min | `Luyện tập` | $N \ge 3, N \le 1000$ | Bỏ 1 điểm cao nhất và 1 điểm thấp nhất |
| 09 | `PYA-L17-P09` | Sắp xếp tên theo thứ tự bảng chữ cái | `Luyện tập` | $N \le 1000$ từ | Sắp xếp mảng chuỗi |
| 10 | `PYA-L17-P10` | Chênh lệch nhỏ nhất giữa hai số | `Luyện tập` | $N \le 10^5$ | Sắp xếp mảng rồi tìm $\min(A_{i+1} - A_i)$ |
| 11 | `PYA-L17-P11` | Trung vị của dãy số (median) | `Luyện tập` | $N \le 10^5$ | Tìm phần tử chính giữa sau khi sắp xếp |
| 12 | `PYA-L17-P12` | Số xuất hiện nhiều lần nhất (mode) | `Vận dụng` | $N \le 10^5$ | Thống kê tần số xuất hiện cực đại |
| 13 | `PYA-L17-P13` | Ghép hai dãy đã sắp xếp | `Vận dụng` | $N, M \le 10^5$ | Hợp nhất 2 mảng tăng dần thành mảng tăng dần |
| 14 | `PYA-L17-P14` | Xếp hàng mua trà sữa (tổng thời gian chờ ít nhất) | `Thử thách` | $N \le 10^5$ | Thuật toán tham lam (greedy) bằng sắp xếp |

---

### Bài 1 (Cơ bản): Điểm số cao nhất & thấp nhất (`PYA-L17-P01`)

* **Yêu cầu:** Cho danh sách điểm thi của $N$ bạn học sinh. Hãy in ra điểm số cao nhất và điểm số thấp nhất trong danh sách.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
  * Dòng 2: $N$ số nguyên là điểm của các bạn ($0 \le A_i \le 100$).
* **Output:** Điểm cao nhất, theo sau là điểm thấp nhất.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`80 95 60 100 75` | `100 60` |

---

### Bài 2 (Cơ bản): Sắp xếp tăng dần đơn giản (`PYA-L17-P02`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy sắp xếp dãy số theo thứ tự tăng dần và in ra màn hình trên một dòng.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Dãy số sau khi sắp xếp tăng dần, cách nhau bởi khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`9 2 7 1 5` | `1 2 5 7 9` |

---

### Bài 3 (Cơ bản): Điểm trung bình môn học (`PYA-L17-P03`)

* **Yêu cầu:** Cho danh sách điểm kiểm tra của $N$ bài thi. Hãy tính điểm trung bình cộng của các bài thi và in ra với đúng 2 chữ số sau dấu phẩy.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
  * Dòng 2: $N$ số thực hoặc số nguyên là điểm các bài thi.
* **Output:** Điểm trung bình cộng (định dạng `f"{tb:.2f}"`).
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4`<br>`8 9 7 10` | `8.50` | $(8 + 9 + 7 + 10) / 4 = 8.5$. |

---

### Bài 4 (Cơ bản): Sắp xếp giảm dần bảng xếp hạng (`PYA-L17-P04`)

* **Yêu cầu:** Cho danh sách điểm số của $N$ thí sinh tham gia cuộc thi. Hãy sắp xếp bảng điểm theo thứ tự từ cao xuống thấp (giảm dần) để trao giải.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Bảng điểm sắp xếp giảm dần trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `5`<br>`20 80 40 100 60` | `100 80 60 40 20` |

---

### Bài 5 (Cơ bản): Tìm số lớn thứ nhì trong mảng (`PYA-L17-P05`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn thứ nhì trong dãy số (nghĩa là giá trị lớn nhất trong số các phần tử nhỏ hơn giá trị cực đại). Nếu tất cả các phần tử trong mảng đều bằng nhau, in ra `KHONG CO`.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Giá trị lớn thứ nhì, hoặc `KHONG CO`.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`10 20 20 15 5` | `15` | Số lớn nhất là 20. Số lớn thứ hai nhỏ hơn 20 là 15. |
  | `3`<br>`5 5 5` | `KHONG CO` | Tất cả bằng nhau. |

---

### Bài 6 (Luyện tập): Đếm số lượng học sinh trên điểm trung bình (`PYA-L17-P06`)

* **Yêu cầu:** Cho điểm thi của $N$ học sinh. Hãy đếm xem có bao nhiêu bạn học sinh có điểm số lớn hơn hoặc bằng điểm trung bình cộng của cả lớp.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số thực.
* **Output:** Số lượng học sinh đạt điểm $\ge$ điểm trung bình.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4`<br>`8 6 10 4` | `2` | Điểm TB: $(8+6+10+4)/4 = 7.0$. Các bạn có điểm $\ge 7$ là 8 và 10 (có 2 bạn). |

---

### Bài 7 (Luyện tập): Lọc bỏ các số trùng lặp (`PYA-L17-P07`)

* **Yêu cầu:** Cho dãy gồm $N$ số nguyên có thể chứa nhiều số bị trùng lặp. Hãy lọc bỏ các phần tử trùng lặp và in ra các số độc nhất theo thứ tự tăng dần.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Các số độc nhất sắp xếp tăng dần trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `7`<br>`3 1 4 1 5 9 2` | `1 2 3 4 5 9` |

---

### Bài 8 (Luyện tập): Điểm Olympic bỏ max bỏ min (`PYA-L17-P08`)

* **Bối cảnh:** Trong hội thi Bơi lội Olympic, có $N$ giám khảo chấm điểm ($N \ge 3$). Để đảm bảo công bằng tuyệt đối, điểm số chính thức của vận động viên là trung bình cộng sau khi đã **bỏ đi một điểm cao nhất và một điểm thấp nhất**.
* **Yêu cầu:** Cho $N$ điểm số. Hãy tính điểm chính thức của vận động viên (làm tròn 2 chữ số thập phân).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($3 \le N \le 1000$).
  * Dòng 2: $N$ số thực cách nhau bởi khoảng trắng.
* **Output:** Điểm trung bình sau khi loại bỏ 1 điểm max và 1 điểm min.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`7.0 9.0 8.0 10.0 6.0` | `8.00` | Bỏ min là 6.0, bỏ max là 10.0. Còn lại: 7.0, 8.0, 9.0. Trung bình là 8.00. |

---

### Bài 9 (Luyện tập): Sắp xếp tên theo thứ tự bảng chữ cái (`PYA-L17-P09`)

* **Yêu cầu:** Cho danh sách gồm $N$ từ tiếng Anh. Hãy sắp xếp danh sách từ theo thứ tự từ điển A-Z (tăng dần).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
  * Dòng 2: $N$ từ viết thường cách nhau bởi khoảng trắng.
* **Output:** Danh sách từ sau khi sắp xếp trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `4`<br>`orange apple banana grape` | `apple banana grape orange` |

---

### Bài 10 (Luyện tập): Chênh lệch nhỏ nhất giữa hai số (`PYA-L17-P10`)
*(Đề thi Tin học trẻ Bảng A)*

* **Yêu cầu:** Cho dãy $N$ số nguyên đôi một khác nhau. Hãy tìm độ chênh lệch nhỏ nhất giữa 2 phần tử bất kỳ trong dãy (tức là giá trị $|A_i - A_j|$ nhỏ nhất với $i \ne j$).
* **Input:**
  * Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Độ chênh lệch nhỏ nhất.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `4`<br>`10 1 8 15` | `2` | Sắp xếp: [1, 8, 10, 15]. Chênh lệch giữa 8 và 10 là $|10 - 8| = 2$ (nhỏ nhất). |

---

### Bài 11 (Luyện tập): Trung vị của dãy số (median) (`PYA-L17-P11`)

* **Bối cảnh:** Cho một dãy gồm $N$ số nguyên lẻ phần tử ($N$ là số lẻ). Trung vị của dãy là phần tử nằm chính giữa sau khi dãy đã được sắp xếp tăng dần.
* **Yêu cầu:** Cho dãy $N$ số nguyên ($N$ lẻ). Hãy tìm số trung vị của dãy số.
* **Input:**
  * Dòng 1: Số nguyên lẻ $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Giá trị trung vị.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `5`<br>`10 2 8 4 6` | `6` | Sắp xếp: [2, 4, 6, 8, 10]. Số chính giữa là 6. |

---

### Bài 12 (Vận dụng): Số xuất hiện nhiều lần nhất (mode) (`PYA-L17-P12`)

* **Yêu cầu:** Cho dãy $N$ số nguyên. Hãy tìm số xuất hiện nhiều lần nhất trong dãy. Nếu có nhiều số có cùng số lần xuất hiện nhiều nhất, hãy in ra số có giá trị nhỏ nhất trong các số đó.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên.
* **Output:** Số xuất hiện nhiều nhất.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `7`<br>`2 3 5 2 3 7 2` | `2` |

---

### Bài 13 (Vận dụng): Ghép hai dãy đã sắp xếp (`PYA-L17-P13`)

* **Yêu cầu:** Cho hai dãy số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ phần tử) đều đã được sắp xếp tăng dần. Hãy ghép hai dãy lại thành một dãy duy nhất gồm $(N + M)$ phần tử cũng được sắp xếp tăng dần.
* **Input:**
  * Dòng 1: Hai số $N$ và $M$ ($1 \le N, M \le 10^5$).
  * Dòng 2: $N$ số nguyên của dãy $A$.
  * Dòng 3: $M$ số nguyên của dãy $B$.
* **Output:** Dãy hợp nhất gồm $(N + M)$ phần tử tăng dần trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `3 4`<br>`1 4 7`<br>`2 3 5 8` | `1 2 3 4 5 7 8` |

---

### Bài 14 (Thử thách): Xếp hàng mua trà sữa (greedy) (`PYA-L17-P14`)
*(Đề thi Tin học trẻ Quốc gia Bảng A)*

* **Bối cảnh:** Có $N$ bạn học sinh cùng xếp hàng mua trà sữa. Bạn thứ $i$ cần $T_i$ phút để người bán hàng pha chế xong cốc trà sữa của mình.
  Tổng thời gian chờ đợi của tất cả các bạn sẽ là tổng thời gian mà mỗi bạn phải đứng xếp hàng chờ cho đến khi nhận được trà sữa.
* **Yêu cầu:** Hãy tìm cách sắp xếp thứ tự các bạn vào mua trà sữa sao cho **tổng thời gian chờ đợi của tất cả các bạn là NHỎ NHẤT CÓ THỂ**. Hãy in ra tổng thời gian chờ đợi nhỏ nhất đó.
* **Input:**
  * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên $T_i$ ($1 \le T_i \le 1000$).
* **Output:** Một số nguyên duy nhất là tổng thời gian chờ đợi nhỏ nhất.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `3`<br>`3 1 2` | `10` | Sắp xếp người làm nhanh lên trước: thời gian làm lần lượt là 1, 2, 3.<br>- Bạn 1 chờ 1 phút.<br>- Bạn 2 chờ $1 + 2 = 3$ phút.<br>- Bạn 3 chờ $1 + 2 + 3 = 6$ phút.<br>Tổng thời gian chờ: $1 + 3 + 6 = 10$ phút (tối ưu nhất). |
