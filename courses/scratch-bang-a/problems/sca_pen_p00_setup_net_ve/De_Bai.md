# Khởi động nét vẽ & Dấu cộng trung tâm

## Bối cảnh

Trước khi bắt đầu hành trình vẽ các kỳ quan và hoa văn hình học rực rỡ trên sân khấu Scratch, chú Mèo Scratch cần kiểm tra xem chiếc bút vẽ thần kỳ của mình có hoạt động hoàn hảo hay không. Để kiểm tra chiếc bút, chú Mèo quyết định vẽ một ký hiệu dấu cộng màu đỏ tươi rực rỡ ngay chính giữa tâm sân khấu.

## Nhiệm vụ

Em hãy lập trình điều khiển chú Mèo Scratch thực hiện các bước sau:
1. Xóa sạch toàn bộ nét vẽ cũ trên sân khấu.
2. Di chuyển về tâm sân khấu tại tọa độ $(0, 0)$ và quay mặt về hướng $90^\circ$ (hướng sang phải).
3. Thiết lập màu bút vẽ là màu đỏ và độ dày nét vẽ là $3$.
4. Đặt bút xuống và vẽ một dấu cộng gồm $4$ nhánh cân đối tỏa ra $4$ hướng chính (Đông, Tây, Nam, Bắc), mỗi nhánh có độ dài $50$ bước. Sau khi vẽ mỗi nhánh, nhân vật lùi về đúng tâm $(0, 0)$ rồi mới xoay hướng vẽ nhánh tiếp theo.

## Kịch bản tương tác (Input Scenario)

- Chương trình bắt đầu khi người dùng nhấn vào biểu tượng **Cờ Xanh**.
- Không yêu cầu nhập dữ liệu từ bàn phím.

## Kết quả mong đợi (Expected Behavior / Output)

- Màn hình được tẩy sạch mọi nét mực cũ.
- Tại chính giữa tâm sân khấu xuất hiện một dấu cộng màu đỏ gồm $4$ nhánh đều nhau, mỗi nhánh dài $50$ bước.
- Nhân vật chú Mèo kết thúc tại vị trí tâm $(0, 0)$ và quay về hướng ban đầu ($90^\circ$).

## Sample 1

### Kịch bản chạy
```text
Sự kiện: Nhấn Cờ Xanh
Hành động: 
- Xóa màn hình
- Đặt nét vẽ màu đỏ, độ dày 3
- Vẽ nhánh phải: đi 50 bước, lùi 50 bước, xoay phải 90 độ
- Vẽ nhánh dưới: đi 50 bước, lùi 50 bước, xoay phải 90 độ
- Vẽ nhánh trái: đi 50 bước, lùi 50 bước, xoay phải 90 độ
- Vẽ nhánh trên: đi 50 bước, lùi 50 bước, xoay phải 90 độ
```

### Kết quả trên sân khấu
Dấu cộng màu đỏ đối xứng 4 hướng xuất hiện tại $(0, 0)$.

### Giải thích
Nhân vật lần lượt di chuyển ra ngoài $50$ bước để vẽ nét mực, sau đó lùi lại $-50$ bước trên chính đường vừa vẽ để trở về tâm rồi mới đổi hướng $90^\circ$. Bằng cách này, cả 4 nhánh đều xuất phát từ tâm mà không cần phải nhấc bút nhiều lần.

## Ràng buộc

- Tọa độ tâm: $x = 0, y = 0$.
- Chiều dài mỗi nhánh: $50$ bước.
- Độ dày nét bút: $3$.
