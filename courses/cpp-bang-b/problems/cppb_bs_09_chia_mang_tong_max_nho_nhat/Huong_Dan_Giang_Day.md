# Hướng Dẫn Giảng Dạy: Book Allocation / Split Array
- Miền nghiệm: $low = \max(A_i), high = \sum A_i$.
- Hàm `check(S)`: Duyệt gom các phần tử vào đoạn con chừng nào tổng $\le S$. Đếm số đoạn con tạo thành $\le K$.
- Độ phức tạp: $\mathcal{O}(N \log(\sum A))$.
