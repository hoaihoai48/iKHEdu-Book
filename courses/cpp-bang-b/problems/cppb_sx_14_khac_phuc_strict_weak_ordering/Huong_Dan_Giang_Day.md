# Hướng Dẫn Giảng Dạy: Sắp Xếp Đoạn Thẳng Không Giao Lỗi
- Sử dụng `vector<vector<long long>>` lưu `[l, r]`.
- Sử dụng `std::stable_sort` kết hợp Comparator chuẩn `<` và `>`. Tuyệt đối không dùng `<=` khi so sánh hai phần tử bằng nhau.
- Độ phức tạp: $\mathcal{O}(N \log N)$.
