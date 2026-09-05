# Hệ thống bài tập thực hành — bài 16: Đề thi thử lập trình Python

---

## Ma trận 12 bài thi thử (phong cách contest: giấu pattern, có subtask)

| STT | Mã bài | Tên | Cấp độ | Ràng buộc | Mục tiêu |
|---|---|---|---|---|---|
| 01 | PYA-L16-P15 | Heo Đất Tiết Kiệm | Dễ | $N \le 10^6$ | Rèn vòng lặp có điều kiện và phép đếm ngày chẵn |
| 02 | PYA-L16-P16 | Vé Số May Mắn | Dễ | $N \le 10^{18}$ | Rèn tách chữ số và kiểm tra chia hết |
| 03 | PYA-L16-P17 | Bảng Điểm Lớp Học | Dễ | $N \le 10^5$ | Rèn đọc danh sách và thống kê cơ bản |
| 04 | PYA-L16-P18 | Mật Khẩu Bị Ẩn | Dễ | $\|S\| \le 10^5$ | Rèn duyệt chuỗi và phân loại ký tự |
| 05 | PYA-L16-P19 | Đếm Kẹo Chẵn Lẻ | Dễ | $N \le 10^5$ | Rèn phép chia dư và bộ đếm đôi |
| 06 | PYA-L16-P20 | Tổng Chữ Số Lớn Nhất | Trung bình | $N \le 10^5$ | Rèn tổng chữ số và chọn cực trị có điều kiện phụ |
| 07 | PYA-L16-P21 | Số Ghế Đối Xứng | Trung bình | $N \le 10^{18}$ | Rèn đảo ngược số và so sánh chuỗi |
| 08 | PYA-L16-P22 | Xếp Hàng Chiều Cao | Trung bình | $N \le 10^5$ | Rèn sắp xếp danh sách |
| 09 | PYA-L16-P23 | Thưởng Đọc Sách | Trung bình | $N \le 10^{12}$ | Rèn công thức toán thay vòng lặp chậm |
| 10 | PYA-L16-P24 | Đếm Từ Dài | Trung bình | $\|S\| \le 10^4$ | Rèn tách từ bằng split và so sánh độ dài |
| 11 | PYA-L16-P25 | Đếm Sao Nguyên Tố | Khó | $N \le 10^6$ | Rèn kiểm tra nguyên tố và vét điểm subtask nhỏ |
| 12 | PYA-L16-P26 | Chuyến Tàu Vượt Đèo | Khó | $N \le 10^5$ | Rèn giữ giá trị lớn nhất hiện tại trong một lượt duyệt |

---

### Bài 1 (Dễ): Heo Đất Tiết Kiệm (PYA-L16-P15)

* **Bối cảnh:** Bé Na bỏ vào heo mỗi ngày $A$ đồng, riêng các ngày chẵn được mẹ thưởng thêm $B$ đồng. Sau $N$ ngày, trong heo có bao nhiêu tiền?
* **Yêu cầu:** Cho $N, A, B$. Tính tổng số tiền sau $N$ ngày.
* **Input:** Ba số nguyên $N, A, B$ ($1 \le N \le 10^6$).
* **Output:** Tổng số tiền.
* **Ví dụ mẫu:**

  | Input | Output | Giải thích |
  |---|---|---|
  | `5 10 3` | `56` | $5 \times 10 + 2 \times 3 = 56$. |

### Bài 2 (Dễ): Vé Số May Mắn (PYA-L16-P16)

* **Bối cảnh:** Vé số được gọi là may mắn nếu tổng các chữ số của nó chia hết cho $7$. Tấm vé $1234$ có trúng thưởng không?
* **Yêu cầu:** Cho số $N$. In `YES` nếu là vé may mắn, ngược lại in `NO`.
* **Input:** Số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `1234` | `NO` |

### Bài 3 (Dễ): Bảng Điểm Lớp Học (PYA-L16-P17)

* **Bối cảnh:** Cô giáo nhờ bé Na tìm điểm cao nhất, điểm thấp nhất và điểm trung bình của $N$ bạn để ghi vào sổ thi đua.
* **Yêu cầu:** Cho điểm của $N$ bạn. In điểm cao nhất, thấp nhất và trung bình (1 chữ số thập phân).
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($0 \le A_i \le 10$).
* **Output:** 3 dòng: điểm cao nhất, điểm thấp nhất, điểm trung bình.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `5`<br>`8 7 10 6 9` | `10`<br>`6`<br>`8.0` |

### Bài 4 (Dễ): Mật Khẩu Bị Ẩn (PYA-L16-P18)

* **Bối cảnh:** Mật khẩu nhật ký của bé Bo gồm chữ cái và chữ số như `Abc123x`. Có bao nhiêu ký tự là chữ số?
* **Yêu cầu:** Cho chuỗi $S$. Đếm ký tự là chữ số từ `0` đến `9`.
* **Input:** Chuỗi $S$ ($1 \le \|S\| \le 10^5$).
* **Output:** Số lượng chữ số.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `Abc123x` | `3` |

### Bài 5 (Dễ): Đếm Kẹo Chẵn Lẻ (PYA-L16-P19)

* **Bối cảnh:** Cô giáo chia $N$ gói kẹo thành mâm gói chẵn và mâm gói lẻ. Mỗi mâm có bao nhiêu gói?
* **Yêu cầu:** Cho $N$ số nguyên. Đếm số chẵn và số lẻ, in trên một dòng.
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($0 \le A_i \le 10^9$).
* **Output:** Hai số: số lượng số chẵn trước, số lượng số lẻ sau.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `6`<br>`1 2 3 4 5 6` | `3 3` |

### Bài 6 (Trung bình): Tổng Chữ Số Lớn Nhất (PYA-L16-P20)

* **Bối cảnh:** Bạn nào có tổng các chữ số của số báo danh lớn nhất sẽ làm lớp trưởng. Nếu hòa thì bạn có số báo danh nhỏ hơn thắng.
* **Yêu cầu:** Cho $N$ số báo danh. Tìm số của bạn thắng cuộc.
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số tự nhiên ($0 \le A_i \le 10^{18}$).
* **Output:** Số báo danh thắng cuộc.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `5`<br>`12 99 45 100 38` | `99` |

### Bài 7 (Trung bình): Số Ghế Đối Xứng (PYA-L16-P21)

* **Bối cảnh:** Ghế vàng trong rạp xiếc mang số đối xứng (đọc xuôi ngược đều giống nhau như 121). Ghế số $N$ có phải ghế vàng không?
* **Yêu cầu:** Cho số $N$. In `YES` nếu đối xứng, ngược lại in `NO`.
* **Input:** Số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `121` | `YES` |

### Bài 8 (Trung bình): Xếp Hàng Chiều Cao (PYA-L16-P22)

* **Bối cảnh:** Thầy thể dục nhờ bé Na xếp $N$ bạn thành hàng từ thấp đến cao để tập đội hình.
* **Yêu cầu:** Cho chiều cao của $N$ bạn. In ra theo thứ tự tăng dần.
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($100 \le A_i \le 200$).
* **Output:** $N$ số tăng dần trên một dòng.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `5`<br>`160 150 175 165 155` | `150 155 160 165 175` |

### Bài 9 (Trung bình): Thưởng Đọc Sách (PYA-L16-P23)

* **Bối cảnh:** Đọc hết $N$ quyển sách sẽ được thưởng sao: quyển thứ 1 được 1 sao, quyển thứ 2 được 2 sao, tới quyển thứ $N$ được $N$ sao. Tổng cộng được bao nhiêu sao?
* **Yêu cầu:** Cho $N$. Tính tổng từ 1 đến $N$.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^{12}$).
* **Output:** Tổng số sao.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `5` | `15` |

### Bài 10 (Trung bình): Đếm Từ Dài (PYA-L16-P24)

* **Bối cảnh:** Cô giáo đố: trong câu văn $S$ có bao nhiêu từ dài hơn $K$ ký tự? Từ là nhóm ký tự liền nhau, cách nhau bởi dấu cách.
* **Yêu cầu:** Cho $K$ và câu $S$. Đếm số từ có độ dài lớn hơn $K$.
* **Input:**
  * Dòng 1: số nguyên $K$ ($0 \le K \le 100$).
  * Dòng 2: câu văn $S$ ($1 \le \|S\| \le 10^4$).
* **Output:** Số từ thỏa mãn.
* **Ví dụ mẫu:**

  | Input | Output |
  |---|---|
  | `3`<br>`Hom nay Bin di hoc cung ban Na` | `1` |

### Bài 11 (Khó): Đếm Sao Nguyên Tố (PYA-L16-P25)

* **Bối cảnh:** Trên bầu trời giấy có $N$ ngôi sao đánh số từ 1 đến $N$. Có bao nhiêu ngôi sao mang số nguyên tố? (Số 1 không phải số nguyên tố.)
* **Yêu cầu:** Cho $N$. Đếm số nguyên tố từ 1 đến $N$.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** Số lượng số nguyên tố.
* **Ví dụ mẫu:**

  | Input | Output | Giải thích |
  |---|---|---|
  | `10` | `4` | Các số 2, 3, 5, 7. |

### Bài 12 (Khó): Chuyến Tàu Vượt Đèo (PYA-L16-P26)

* **Bối cảnh:** Tàu đồ chơi chạy qua $N$ ngọn đèo cao $A_i$ mét. Bé lái tàu reo lên mỗi khi chinh phục ngọn đèo cao hơn tất cả các ngọn đã qua (ngọn đầu tiên luôn được reo một lần). Bé reo tất cả bao nhiêu lần?
* **Yêu cầu:** Cho dãy $N$ số. Đếm số lần phần tử lớn hơn mọi phần tử đứng trước nó.
* **Input:**
  * Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$).
  * Dòng 2: $N$ số nguyên ($\|A_i\| \le 10^9$).
* **Output:** Số lần reo.
* **Ví dụ mẫu:**

  | Input | Output | Giải thích |
  |---|---|---|
  | `6`<br>`1 3 5 2 4 7` | `4` | Các kỷ lục là 1, 3, 5, 7. |
