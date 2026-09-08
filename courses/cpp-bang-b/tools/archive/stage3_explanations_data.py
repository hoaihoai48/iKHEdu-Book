# Dữ liệu 135 lời giải thích và chuẩn hóa cho Giai đoạn 3
# Khóa học C++ Quyển 2 — iKH Education

EXPLANATIONS = {
    # =========================================================================
    # CHƯƠNG 05 — BÀI 13: QUY HOẠCH ĐỘNG 1D & LIS (CPPB-DP1)
    # =========================================================================
    "CPPB-DP1-01": "Với N = 3 bậc thang, có tất cả 3 cách bước hợp lệ để lên đến đỉnh: (1 + 1 + 1), (1 + 2) và (2 + 1). Kết quả tính theo modulo 10^9 + 7 là 3.",
    "CPPB-DP1-02": "Với 4 phiến đá có độ cao [10, 30, 40, 20]: Lộ trình tối ưu là nhảy từ đá 1 sang đá 2 tốn chi phí |10 - 30| = 20, sau đó từ đá 2 nhảy sang đá 4 tốn |30 - 20| = 10. Tổng chi phí tối thiểu là 20 + 10 = 30.",
    "CPPB-DP1-03": "Với N = 5, K = 3 và độ cao các phiến đá [10, 30, 40, 50, 20]: Lộ trình tối ưu là nhảy từ đá 1 (độ cao 10) sang đá 2 (độ cao 30) tốn chi phí |10 - 30| = 20, sau đó nhảy xa 2 bước từ đá 2 tới đá 5 (độ cao 20) tốn |30 - 20| = 10. Tổng chi phí là 30.",
    "CPPB-DP1-04": "Với số tiền mục tiêu S = 11 và các mệnh giá [1, 5, 6]: Phương án tối ưu nhất là chọn 2 đồng xu gồm một đồng 5 và một đồng 6 (5 + 6 = 11).",
    "CPPB-DP1-05": "Với số tiền S = 9 và các loại xu [2, 3, 5]: Có đúng 3 tổ hợp đồng xu khác nhau có tổng bằng 9 gồm: (2 + 2 + 5), (3 + 3 + 3) và (2 + 2 + 2 + 3). Kết quả là 3.",
    "CPPB-DP1-06": "Với mảng [1, 2, 3, 1]: Tập hợp các phần tử không kề nhau có tổng lớn nhất là chọn phần tử thứ nhất (giá trị 1) và phần tử thứ ba (giá trị 3), tổng đạt được là 1 + 3 = 4.",
    "CPPB-DP1-07": "Với sàn nhà kích thước 2x4, số cách lát bằng các viên gạch 2x1 tương ứng với số Fibonacci thứ 5: f(1)=1, f(2)=2, f(3)=3, f(4)=5. Kết quả là 5 cách.",
    "CPPB-DP1-08": "Với bảng 3x2, chỉ có 3 cách lát kín bảng bằng các viên domino 2x1. Kết quả là 3.",
    "CPPB-DP1-09": "Với dãy số [10, 20, 10, 30, 20, 50]: Dãy con tăng nghiêm ngặt dài nhất là [10, 20, 30, 50] có độ dài bằng 4.",
    "CPPB-DP1-10": "Với dãy số [5, 2, 7, 4, 3, 8]: Dãy con tăng dài nhất tìm được bằng tìm kiếm nhị phân là [2, 4, 8] (hoặc [2, 3, 8], [5, 7, 8]) có độ dài bằng 3.",
    "CPPB-DP1-11": "Với dãy [2, 1, 4, 3, 5]: Dãy con tăng dài nhất có độ dài bằng 3, truy vết ra các phần tử cụ thể là [2, 4, 5] (hoặc [1, 4, 5], [1, 3, 5]).",
    "CPPB-DP1-12": "Với dãy 8 số [10, 9, 2, 5, 3, 7, 101, 18]: Dãy con giảm nghiêm ngặt dài nhất có độ dài 4, ví dụ dãy [10, 9, 5, 3].",
    "CPPB-DP1-13": "Với dãy [1, 11, 2, 10, 4, 5, 2, 1]: Dãy con sóng núi dài nhất là [1, 2, 10, 5, 2, 1] (hoặc [1, 2, 4, 5, 2, 1]) có độ dài bằng 6.",
    "CPPB-DP1-14": "Với dãy [1, 101, 2, 3, 100, 4, 5]: Dãy con tăng có tổng lớn nhất là [1, 2, 3, 100] với tổng 1 + 2 + 3 + 100 = 106.",
    "CPPB-DP1-15": "Với 3 dự án năng lượng [(10, 100), (5, 50), (20, 200)]: Chuỗi dự án hợp lệ có sản lượng tăng nghiêm ngặt [5, 10, 20] mang lại tổng lợi nhuận lớn nhất là 50 + 100 + 200 = 350.",

    # =========================================================================
    # CHƯƠNG 05 — BÀI 14: QUY HOẠCH ĐỘNG 2D & KNAPSACK (CPPB-DP2)
    # =========================================================================
    "CPPB-DP2-01": "Trên lưới kích thước 3x3, chỉ được di chuyển sang phải hoặc xuống dưới: Tổng số đường đi từ ô (1,1) đến ô (3,3) là C(2+2, 2) = 6 cách.",
    "CPPB-DP2-02": "Trên mê cung 3x3 với chướng ngại vật tại ô (2,2): Các đường đi đi qua ô (2,2) bị chặn, do đó chỉ còn lại đúng 2 đường đi hợp lệ đến đích.",
    "CPPB-DP2-03": "Trên bảng số 3x3: Lộ trình từ (1,1) xuống (3,3) thu thập tổng giá trị lớn nhất qua các ô là 1 -> 1 -> 4 -> 2 -> 1, cho tổng lớn nhất là 12.",
    "CPPB-DP2-04": "Với 4 đồ vật [(khối lượng 2, giá trị 3), (3, 4), (4, 5), (5, 6)] và balo sức chứa W = 5: Cách chọn tối ưu là lấy đồ vật 1 và đồ vật 2 với tổng khối lượng 2 + 3 = 5, đạt tổng giá trị lớn nhất là 3 + 4 = 7.",
    "CPPB-DP2-05": "Với sức chứa W = 100 và các đồ vật có số lượng không giới hạn: Ta có thể chọn nhiều lần cùng một loại vật phẩm có tỉ lệ giá trị trên khối lượng cao nhất để đạt tổng giá trị tối đa là 150.",
    "CPPB-DP2-06": "Với tập các số nguyên cho trước: Có thể phân chia tập thành hai tập con có tổng bằng nhau (mỗi nửa có tổng bằng 11), do đó in ra YES.",
    "CPPB-DP2-07": "Với mảng số nguyên và giá trị mục tiêu S: Đếm được chính xác 3 tập con khác nhau có tổng các phần tử đúng bằng S.",
    "CPPB-DP2-08": "Với tập các trọng số cho trước: Số lượng các giá trị tổng trọng lượng khác nhau có thể tạo thành từ một tập con bất kỳ là 4.",
    "CPPB-DP2-09": "Với 3 nhóm học tập và thời gian giới hạn K: Phương án phân bổ thời gian học cho các nhóm mang lại điểm số cao nhất là 17.",
    "CPPB-DP2-10": "Với mảng 2 chiều kích thước 4x4: Hình vuông con toàn số 1 lớn nhất có kích thước cạnh là 2 (chứa 2x2 = 4 ô số 1).",
    "CPPB-DP2-11": "Với mảng 2 chiều kích thước 3x3: Hình chữ nhật con có tổng các phần tử lớn nhất đạt giá trị là 15.",
    "CPPB-DP2-12": "Với dãy đá trên sông và các bước nhảy chênh lệch tối đa 1 đơn vị: Chú ếch có thể qua sông thành công đến bờ bên kia, in ra YES.",
    "CPPB-DP2-13": "Với 3 viên sỏi ban đầu: Trò chơi bốc sỏi kết thúc với phần thắng thuộc về người chơi thứ nhất nếu chơi tối ưu, in ra First.",
    "CPPB-DP2-14": "Với dãy số trên bàn: Người chơi thứ nhất luôn có chiến lược chọn ở hai đầu mút để đạt số điểm chênh lệch tối đa là 3 so với người thứ hai.",
    "CPPB-DP2-15": "Trong thị trường tài chính với giới hạn K giao dịch: Lợi nhuận tối đa thu được từ việc mua và bán cổ phiếu không trùng thời điểm là 15.",

    # =========================================================================
    # CHƯƠNG 05 — BÀI 15: QUY HOẠCH ĐỘNG CHUỖI & LCS (CPPB-DPS)
    # =========================================================================
    "CPPB-DPS-01": "Xét hai xâu 'ABCBDAB' và 'BDCAB': Xâu con chung dài nhất (LCS) là 'BCAB' (hoặc 'BDAB') có độ dài bằng 4.",
    "CPPB-DPS-02": "Xét hai xâu ký tự: Truy vết từ bảng quy hoạch động cho ra xâu con chung dài nhất có thứ tự xuất hiện đúng là 'BCAB'.",
    "CPPB-DPS-03": "Xét ba xâu ký tự: Xâu con chung dài nhất đồng thời xuất hiện trong cả 3 xâu có độ dài bằng 3.",
    "CPPB-DPS-04": "Để biến đổi xâu 'kitten' thành xâu 'sitting': Cần 3 phép biến đổi gồm thay 'k' bằng 's', thay 'e' bằng 'i' và chèn thêm 'g' ở cuối (Edit Distance = 3).",
    "CPPB-DPS-05": "Trong xâu 'BBABCBCAB': Xâu con đối xứng dài nhất (LPS) là 'BABCBAB' có độ dài bằng 7.",
    "CPPB-DPS-06": "Để xâu ký tự trở thành xâu đối xứng, ta cần chèn thêm số lượng ký tự ít nhất đúng bằng độ dài xâu trừ đi độ dài LPS, kết quả là 2 ký tự.",
    "CPPB-DPS-07": "Đếm tất cả các xâu con liên tiếp của chuỗi là xâu đối xứng (Palindrome): Có tổng cộng 6 xâu con đối xứng.",
    "CPPB-DPS-08": "Số phép cắt ít nhất để phân chia xâu thành các đoạn con mà mỗi đoạn đều là xâu đối xứng là 1.",
    "CPPB-DPS-09": "Xâu mẹ chung ngắn nhất (SCS) chứa cả hai xâu mẫu làm xâu con có độ dài nhỏ nhất là 9.",
    "CPPB-DPS-10": "Đếm số lần xâu mẫu T xuất hiện dưới dạng xâu con không liên tiếp trong xâu S: Có đúng 3 cách chọn chỉ số thỏa mãn.",
    "CPPB-DPS-11": "Kiểm tra xâu C có phải là sự đan xen (interleaving) có thứ tự của hai xâu A và B hay không: Chuỗi ký tự khớp hoàn toàn từng vị trí, in ra YES.",
    "CPPB-DPS-12": "Khớp chuỗi mẫu có ký tự đại diện '?' (khớp 1 ký tự bất kỳ) và '*' (khớp chuỗi bất kỳ): Chuỗi khớp hoàn toàn với mẫu, in ra YES.",
    "CPPB-DPS-13": "Khớp biểu thức chính quy (Regex) hỗ trợ '.' và '*': Chuỗi văn bản khớp hoàn toàn quy tắc chuyển trạng thái của mẫu biểu thức, in ra YES.",
    "CPPB-DPS-14": "Cho từ điển và một chuỗi không có dấu cách: Có thể tách chuỗi thành các từ hợp lệ trong từ điển, in ra YES.",
    "CPPB-DPS-15": "Trong hệ thống an ninh sinh trắc học: Độ tương đồng lớn nhất giữa hai chuỗi mã gen DNA theo ma trận tính điểm căn chỉnh tối ưu là 24.",

    # =========================================================================
    # CHƯƠNG 06 — BÀI 16: CẤU TRÚC DỮ LIỆU STL NÂNG CAO (CPPB-STL)
    # =========================================================================
    "CPPB-STL-01": "Xét dãy số [2, 3, 2, 1, 3, 5, 2]: Đưa vào std::set lọc các giá trị trùng lặp ta được tập hợp các phần tử phân biệt {1, 2, 3, 5} gồm đúng 4 phần tử.",
    "CPPB-STL-02": "Với dãy [1, 3, 2, 2, 3, 4, 3]: Sử dụng std::map để đếm tần suất ta ghi nhận: số 1 xuất hiện 1 lần, số 2 xuất hiện 2 lần, số 3 xuất hiện 3 lần, số 4 xuất hiện 1 lần.",
    "CPPB-STL-03": "Sắp xếp danh sách học sinh theo điểm số giảm dần; nếu trùng điểm thì sắp xếp theo họ tên tăng dần theo thứ tự từ điển, cho kết quả danh sách xếp hạng chính xác.",
    "CPPB-STL-04": "Sử dụng hàng đợi ưu tiên std::priority_queue (Max-Heap): Lần lượt thực hiện các thao tác thêm phần tử và rút trích phần tử lớn nhất hiện tại ra khỏi heap.",
    "CPPB-STL-05": "Sử dụng Min-Heap kích thước K để duy trì K phần tử lớn nhất: Tại mỗi bước nhập phần tử mới, phần tử nhỏ nhất trong K phần tử lớn nhất (tức phần tử lớn thứ K) được in ra chính xác.",
    "CPPB-STL-06": "Áp dụng std::multiset để duy trì hai nửa của dãy số: Sau mỗi số được thêm vào luồng dữ liệu, giá trị trung vị (median) luôn được tính toán và in ra với độ phức tạp O(log N).",
    "CPPB-STL-07": "Với mảng đã sắp xếp và giá trị X: std::lower_bound trả về vị trí đầu tiên >= X và std::upper_bound trả về vị trí đầu tiên > X.",
    "CPPB-STL-08": "Với mảng [1, 5, 7, 1] và K = 6: Tìm được 2 cặp số có tổng bằng 6 là (1 ở vị trí 1 ghép với 5) và (1 ở vị trí 4 ghép với 5).",
    "CPPB-STL-09": "Với dãy [1, 2, 1, 3, 4, 2, 3] và cửa sổ độ dài K = 4: Số lượng phần tử phân biệt trong các cửa sổ liên tiếp lần lượt là 3, 4, 4, 3.",
    "CPPB-STL-10": "Với các sợi dây có độ dài [4, 3, 2, 6]: Dùng Min-Heap luôn chọn 2 sợi ngắn nhất để nối: (2 + 3 = 5), sau đó (4 + 5 = 9), cuối cùng (6 + 9 = 15). Tổng chi phí nhỏ nhất là 5 + 9 + 15 = 29.",
    "CPPB-STL-11": "Cho khoảng thời gian bắt đầu và kết thúc của các công việc: Số lượng máy chủ tối thiểu cần sử dụng đồng thời để không công việc nào bị trùng lịch là 3 máy chủ.",
    "CPPB-STL-12": "Sử dụng std::unordered_map lưu trữ các giá trị đã duyệt: Đếm được chính xác số cặp số (Ai, Aj) có hiệu Ai - Aj = K.",
    "CPPB-STL-13": "Qua các truy vấn thêm phần tử: std::map kết hợp theo dõi tần suất lớn nhất cho phép trả về phần tử xuất hiện nhiều nhất (mode) tại mọi thời điểm trong O(log N).",
    "CPPB-STL-14": "Sử dụng kỹ thuật đường quét (Sweep-line) kết hợp std::set lưu trữ các điểm theo tung độ y: Khoảng cách ngắn nhất giữa hai điểm trong tập hợp được tìm thấy là 1.414.",
    "CPPB-STL-15": "Hệ thống xếp hạng thi đấu sử dụng cấu trúc bảng ánh xạ kép (id -> score và score -> ids): Mọi thao tác cập nhật điểm và truy vấn top đầu đều được xử lý tức thời trong O(log N).",

    # =========================================================================
    # CHƯƠNG 06 — BÀI 17: STACK & MONOTONIC STACK (CPPB-STK)
    # =========================================================================
    "CPPB-STK-01": "Xét dãy ngoặc '((()())())': Các dấu mở ngoặc và đóng ngoặc ghép cặp hoàn hảo không thừa thiếu, do đó dãy ngoặc đúng, in ra YES.",
    "CPPB-STK-02": "Xét dãy ngoặc hỗn hợp '{[()]}': Mọi cặp ngoặc đơn, ngoặc vuông và ngoặc nhọn đều đóng đúng thứ tự lồng nhau hợp lệ, in ra YES.",
    "CPPB-STK-03": "Đánh giá biểu thức hậu tố '2 3 1 * + 9 -': Thực hiện phép nhân 3 * 1 = 3, cộng 2 + 3 = 5, trừ 5 - 9 = -4. Kết quả là -4.",
    "CPPB-STK-04": "Với xâu 'abbaca': Sử dụng stack loại bỏ các cặp ký tự liền kề trùng nhau: 'bb' bị xóa thành 'aaca', sau đó 'aa' bị xóa còn lại 'ca'.",
    "CPPB-STK-05": "Với mảng [4, 5, 2, 25]: Phần tử lớn hơn tiếp theo bên phải của 4 là 5, của 5 là 25, của 2 là 25, của 25 không có (in -1). Kết quả: 5 25 25 -1.",
    "CPPB-STK-06": "Với mỗi vị trí trong mảng: Sử dụng Monotonic Stack đơn điệu tăng để tìm vị trí phần tử nhỏ hơn gần nhất nằm bên trái trong O(N).",
    "CPPB-STK-07": "Với chuỗi ngoặc ')()())': Đoạn ngoặc hợp lệ dài nhất liên tiếp là '()()' có độ dài bằng 4.",
    "CPPB-STK-08": "Với số '1432219' và K = 3: Dùng stack giữ chữ số tăng dần, loại bỏ 3 chữ số lớn đứng trước chữ số nhỏ hơn, thu được số nhỏ nhất là '1219'.",
    "CPPB-STK-09": "Trên biểu đồ cột Histogram có độ cao [2, 1, 5, 6, 2, 3]: Hình chữ nhật lớn nhất tạo bởi 2 cột có độ cao 5 và 6 với diện tích là min(5,6) * 2 = 10.",
    "CPPB-STK-10": "Với địa hình các cột [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]: Sử dụng stack tìm các vách ngăn, tổng lượng nước mưa đọng lại sau cơn mưa là 6 đơn vị.",
    "CPPB-STK-11": "Trong ma trận nhị phân kích thước NxM: Quy đổi mỗi hàng thành bài toán Histogram, hình chữ nhật toàn số 1 lớn nhất có diện tích là 6.",
    "CPPB-STK-12": "Áp dụng Monotonic Stack tính khoảng mở rộng sang trái và sang phải của từng phần tử: Tổng giá trị nhỏ nhất của tất cả các đoạn con của mảng được tính trong O(N).",
    "CPPB-STK-13": "Trên mảng xoay vòng (Circular Array): Duyệt mảng nhân đôi độ dài 2N với stack để tìm phần tử lớn hơn tiếp theo tính cả phần tử vòng lại đầu mảng.",
    "CPPB-STK-14": "Với giá cổ phiếu các ngày [100, 80, 60, 70, 60, 75, 85]: Số ngày liên tiếp trước đó có giá <= ngày hiện tại (Stock Span) lần lượt là 1, 1, 1, 2, 1, 4, 6.",
    "CPPB-STK-15": "Đánh giá biểu thức trung tố '3 + 5 * (2 - 8)': Chuyển đổi sang hậu tố qua thuật toán Shunting-yard và tính giá trị chính xác là -27.",

    # =========================================================================
    # CHƯƠNG 06 — BÀI 18: QUEUE & MONOTONIC DEQUE (CPPB-QUE)
    # =========================================================================
    "CPPB-QUE-01": "Mô phỏng hàng đợi FIFO: Các thao tác PUSH đưa phần tử vào cuối hàng đợi và POP lấy phần tử ở đầu hàng đợi được thực hiện chính xác theo thứ tự thời gian.",
    "CPPB-QUE-02": "Với N = 5: Sử dụng Queue sinh các số nhị phân từ 1 đến 5: lấy số hiện tại ra in và đẩy thêm '0' cùng '1' vào đuôi, thu được: 1, 10, 11, 100, 101.",
    "CPPB-QUE-03": "Sử dụng hàng đợi BFS duyệt đồ thị không trọng số: Tìm được số bước đi ít nhất từ đỉnh xuất phát tới đỉnh đích là 2 bước.",
    "CPPB-QUE-04": "Sử dụng mảng parent kết hợp Queue BFS: Truy vết chính xác từng đỉnh trên đường đi ngắn nhất từ đỉnh nguồn S đến đỉnh đích T.",
    "CPPB-QUE-05": "Với mảng [1, 3, -1, -3, 5, 3, 6, 7] và K = 3: Dùng Monotonic Deque lưu chỉ số tăng dần về giá trị, giá trị nhỏ nhất trong mỗi cửa sổ trượt lần lượt là: -1, -3, -3, -3, 3, 3.",
    "CPPB-QUE-06": "Với mảng [1, 3, -1, -3, 5, 3, 6, 7] và K = 3: Dùng Monotonic Deque lưu chỉ số giảm dần về giá trị, giá trị lớn nhất trong mỗi cửa sổ trượt lần lượt là: 3, 3, 5, 5, 6, 7.",
    "CPPB-QUE-07": "Duyệt BFS tô màu 2 màu xen kẽ cho các đỉnh kề nhau: Không có 2 đỉnh kề nào cùng màu, đồ thị là đồ thị hai phía (Bipartite), in ra YES.",
    "CPPB-QUE-08": "Biến đổi số A thành số B qua 2 thao tác (nhân đôi hoặc trừ 1): Sử dụng Queue tìm kiếm theo chiều rộng để đạt được số B với số bước ít nhất là 3.",
    "CPPB-QUE-09": "Trên đồ thị có trọng số các cạnh chỉ là 0 hoặc 1: Sử dụng 0-1 BFS với std::deque (đẩy cạnh trọng số 0 vào đầu, cạnh trọng số 1 vào cuối) tìm khoảng cách ngắn nhất trong O(V + E).",
    "CPPB-QUE-10": "Tìm đoạn con liên tiếp có độ dài tối đa K có tổng lớn nhất: Quy về tìm min của mảng tiền tố pref[j] trong cửa sổ trượt [i-K, i-1] bằng Monotonic Deque.",
    "CPPB-QUE-11": "Với N = 5 người và bước loại K = 2 trong bài toán Josephus: Dùng Queue đẩy người an toàn ra sau và loại người thứ K, người sống sót cuối cùng là người số 3.",
    "CPPB-QUE-12": "Từ nhiều trạm cứu hỏa đồng thời: Đẩy tất cả các trạm cứu hỏa vào Queue ở bước 0 (Multi-Source BFS), khoảng cách ngắn nhất từ mỗi ngôi nhà tới trạm cứu hỏa gần nhất được tính toán chính xác.",
    "CPPB-QUE-13": "Sử dụng đồng thời 2 Deque (một Deque duy trì Max và một Deque duy trì Min): Tìm được đoạn con dài nhất có độ chênh lệch max - min <= C là 5.",
    "CPPB-QUE-14": "Tối ưu hóa việc chọn các đoạn băng rôn quảng cáo: Sử dụng Monotonic Deque để tối ưu hóa công thức chuyển trạng thái quy hoạch động trong O(N).",
    "CPPB-QUE-15": "Đua xe trong mê cung với yêu cầu đổi hướng ít nhất: Sử dụng 0-1 BFS với trạng thái (ô hiện tại, hướng đi trước đó), số lần bẻ lái ít nhất để về đích là 2 lần.",

    # =========================================================================
    # CHƯƠNG 07 — BÀI 19: ĐỒ THỊ CƠ BẢN & BFS/DFS (CPPB-GRA)
    # =========================================================================
    "CPPB-GRA-01": "Chuyển danh sách M cạnh của đồ thị sang danh sách kề: Đỉnh 1 kề với các đỉnh [2, 3], đỉnh 2 kề với [1, 4]... được in ra theo đúng định dạng chuẩn.",
    "CPPB-GRA-02": "Duyệt đồ thị bằng thuật toán tìm kiếm theo chiều sâu (DFS) bắt đầu từ đỉnh S: Thăm các đỉnh theo thứ tự nhánh sâu nhất trước khi quay lui.",
    "CPPB-GRA-03": "Duyệt đồ thị bằng thuật toán tìm kiếm theo chiều rộng (BFS) bắt đầu từ đỉnh S: Thăm toàn bộ các đỉnh ở khoảng cách d trước khi sang khoảng cách d+1.",
    "CPPB-GRA-04": "Với đồ thị có N đỉnh và M cạnh: Duyệt qua toàn bộ các đỉnh chưa thăm, đếm được chính xác 3 thành phần liên thông độc lập.",
    "CPPB-GRA-05": "Duyệt qua các thành phần liên thông: Thành phần liên thông lớn nhất chứa 5 đỉnh.",
    "CPPB-GRA-06": "Sử dụng DFS hoặc BFS kiểm tra tính liên thông: Tồn tại đường đi từ đỉnh S tới đỉnh T trên đồ thị, in ra YES.",
    "CPPB-GRA-07": "Duyệt DFS phát hiện cạnh ngược (Back-edge) trỏ về tổ tiên khác cha trực tiếp: Đồ thị vô hướng chứa chu trình, in ra YES.",
    "CPPB-GRA-08": "Tìm đường đi ngắn nhất giữa hai đỉnh trên đồ thị không trọng số bằng BFS: Độ dài đường đi ngắn nhất là 3 cạnh.",
    "CPPB-GRA-09": "Kiểm tra đồ thị có phải là cây hay không: Đồ thị có đúng N - 1 cạnh, liên thông và không chứa chu trình, in ra YES.",
    "CPPB-GRA-10": "Sắp xếp tô-pô trên đồ thị có hướng không chu trình (DAG) bằng thuật toán Kahn (xóa dần các đỉnh có bán bậc vào in-degree bằng 0): Thứ tự thực hiện công việc hợp lệ là 1 2 3 4.",
    "CPPB-GRA-11": "Chạy BFS từ mỗi đỉnh để tìm chu trình có độ dài nhỏ nhất (Girth): Chu trình ngắn nhất trên đồ thị có độ dài bằng 3.",
    "CPPB-GRA-12": "Tính kích thước của từng thành phần liên thông: Số cặp đỉnh (u, v) không thể đi tới nhau được tính bằng tổng tích các cặp kích thước, kết quả là 8.",
    "CPPB-GRA-13": "Sử dụng Multi-Source BFS từ các máy chủ nhiễm virus ban đầu: Toàn bộ mạng lưới máy tính bị lây nhiễm sau đúng 3 giờ.",
    "CPPB-GRA-14": "Áp dụng thuật toán Tarjan tính num[u] và low[u]: Đếm được chính xác 2 cạnh cầu (cạnh mà khi xóa đi làm tăng số thành phần liên thông của đồ thị).",
    "CPPB-GRA-15": "Để kết nối toàn bộ hệ thống giao thông thành một mạng liên thông: Cần xây dựng thêm k - 1 tuyến đường mới nối giữa các thành phần liên thông (k = số thành phần liên thông).",

    # =========================================================================
    # CHƯƠNG 07 — BÀI 20: ĐỒ THỊ LƯỚI 2D & FLOOD FILL (CPPB-GRD)
    # =========================================================================
    "CPPB-GRD-01": "Trên ma trận kích thước 3x3: Duyệt 4 hướng (trên, dưới, trái, phải) từ ô (1,1) nằm ở góc chỉ có 2 ô kề cạnh hợp lệ nằm trong phạm vi ma trận.",
    "CPPB-GRD-02": "Sử dụng thuật toán loang (Flood Fill / BFS) trên lưới: Đếm được chính xác 3 hòn đảo riêng biệt (các vùng số 1 liên thông 4 hướng).",
    "CPPB-GRD-03": "Loang qua tất cả các ô của từng hòn đảo: Hòn đảo lớn nhất có diện tích bằng 5 ô.",
    "CPPB-GRD-04": "Sử dụng BFS tìm đường thoát khỏi mê cung từ điểm xuất phát 'S' đến điểm đích 'E': Số bước di chuyển ngắn nhất tránh các vật cản '#' là 6 bước.",
    "CPPB-GRD-05": "Truy vết đường đi ngắn nhất trong mê cung từ mảng parent: Chuỗi thao tác di chuyển tối ưu nhất là 'DDRRUU'.",
    "CPPB-GRD-06": "Loang Flood Fill từ các cạnh biên của ma trận để đánh dấu các ô thông ra ngoài: Số ô đất kín không thông ra biển bị bao bọc hoàn toàn là 4 ô.",
    "CPPB-GRD-07": "Với mỗi ô đất trên hòn đảo: Chu vi được tính bằng tổng số cạnh tiếp giáp với nước hoặc nằm ngoài biên giới ma trận, tổng chu vi hòn đảo là 16.",
    "CPPB-GRD-08": "Nước bắt đầu tràn từ nhiều cửa van cùng lúc: Áp dụng Multi-Source BFS, toàn bộ mê cung bị ngập nước sau 4 phút.",
    "CPPB-GRD-09": "Quân mã di chuyển theo 8 hướng chữ L trên bàn cờ vua: Số bước nhảy ít nhất để quân mã đi từ ô xuất phát đến ô đích là 3 bước.",
    "CPPB-GRD-10": "Chạy 2 lần BFS/DFS trên cây: Lần 1 tìm đỉnh u xa nhất từ gốc, lần 2 tìm đỉnh v xa nhất từ u; khoảng cách giữa u và v là đường kính của cây, bằng 5.",
    "CPPB-GRD-11": "Tính kích thước cây con tại mỗi đỉnh: Đỉnh có kích thước các cây con còn lại khi loại bỏ nó không vượt quá N/2 là trọng tâm (Centroid) của cây, kết quả là đỉnh 3.",
    "CPPB-GRD-12": "Trong mê cung có các cặp cổng dịch chuyển tức thời: Khi bước vào một cổng sẽ xuất hiện ngay ở cổng đối ứng trong 0 giây, thời gian thoát mê cung ngắn nhất là 5 giây.",
    "CPPB-GRD-13": "Các quả cam hỏng lây lan sang các quả cam tươi kề cạnh sau mỗi phút: Áp dụng Multi-Source BFS, toàn bộ cam bị hỏng sau 4 phút.",
    "CPPB-GRD-14": "Thử đổi lần lượt từng ô số 0 thành số 1 và liên kết các hòn đảo lân cận: Diện tích hòn đảo lớn nhất có thể tạo thành là 7 ô.",
    "CPPB-GRD-15": "Trong mê cung quái vật: Sử dụng BFS kép (tính thời gian quái vật lan tỏa tới từng ô và thời gian người chơi chạy tới ô đó), người chơi có thể thoát ra biên an toàn, in ra YES.",

    # =========================================================================
    # CHƯƠNG 07 — BÀI 21: CÂY PHÂN ĐOẠN (SEGMENT TREE & BIT) (CPPB-RNG)
    # =========================================================================
    "CPPB-RNG-01": "Cài đặt Fenwick Tree (Binary Indexed Tree): Các thao tác cập nhật điểm và truy vấn tổng tiền tố/tổng đoạn [L, R] được xử lý chính xác với thời gian O(log N).",
    "CPPB-RNG-02": "Cài đặt Segment Tree cơ bản: Xây dựng cây và trả về giá trị nhỏ nhất trong các đoạn con truy vấn [L, R] trong O(log N).",
    "CPPB-RNG-03": "Sử dụng Fenwick Tree dạng hiệu (Difference Array): Thao tác cộng giá trị V vào đoạn [L, R] và truy vấn giá trị tại một điểm được thực hiện trong O(log N).",
    "CPPB-RNG-04": "Tại mỗi nút của Segment Tree lưu cặp {giá trị max, số lần xuất hiện}: Đoạn [L, R] có giá trị lớn nhất là 9 xuất hiện 2 lần.",
    "CPPB-RNG-05": "Với mảng [2, 4, 1, 3, 5]: Rời rạc hóa giá trị và sử dụng Fenwick Tree đếm số phần tử lớn hơn đứng trước, tổng số cặp nghịch thế là 3.",
    "CPPB-RNG-06": "Tại mỗi nút Segment Tree lưu ước chung lớn nhất (GCD): Truy vấn gcd(A[L], ..., A[R]) trong O(log N * log(max_val)).",
    "CPPB-RNG-07": "Tìm kiếm nhị phân trên cây Fenwick Tree (Binary Lifting on BIT): Tìm được phần tử nhỏ thứ K hiện có trong tập hợp là 4.",
    "CPPB-RNG-08": "Tìm kiếm trên cây Segment Tree (Walk on Segment Tree): Vị trí đầu tiên trong đoạn [L, R] có giá trị >= X được tìm thấy tại chỉ số 3 trong O(log N).",
    "CPPB-RNG-09": "Rời rạc hóa giá trị và dùng Fenwick Tree lưu trữ độ dài LIS kết thúc tại mỗi giá trị: Độ dài dãy con tăng dài nhất là 4 tìm được trong O(N log N).",
    "CPPB-RNG-10": "Mỗi nút Segment Tree duy trì 4 giá trị (tổng, tiền tố max, hậu tố max, đoạn con max): Truy vấn đoạn con có tổng lớn nhất trên đoạn [L, R] trả về kết quả 16.",
    "CPPB-RNG-11": "Rời rạc hóa tọa độ và sử dụng kỹ thuật đường quét kết hợp Fenwick Tree: Đếm được chính xác 3 điểm nằm bên trong hình chữ nhật truy vấn.",
    "CPPB-RNG-12": "Tại mỗi nút lưu cả tổng và các giá trị cực đại/cực tiểu để hỗ trợ đảo dấu đoạn: Mọi truy vấn cập nhật và tính tổng lớn nhất được xử lý trong O(log N).",
    "CPPB-RNG-13": "Cài đặt Fenwick Tree 2 chiều (2D BIT): Cập nhật giá trị tại ô (x, y) và tính tổng các số trong hình chữ nhật con từ (x1, y1) đến (x2, y2) trong O(log N * log M).",
    "CPPB-RNG-14": "Cài đặt Lazy Propagation trên Segment Tree: Cập nhật cộng giá trị vào đoạn [L, R] và truy vấn tổng đoạn [L, R] đều đạt độ phức tạp O(log N) với bộ nhớ tối ưu.",
    "CPPB-RNG-15": "Hệ thống quản lý dữ liệu Olympic tích hợp toàn diện: Xử lý đồng thời các truy vấn cập nhật đoạn và tính tổng/max/min đảm bảo thời gian thực thi tối ưu dưới 1.0 giây."
}
