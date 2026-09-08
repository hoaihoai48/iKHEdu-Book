# enrich_data_que.py
# Dữ liệu chuẩn hóa Sư phạm 15 bài QUE (CPPB-QUE-01 -> CPPB-QUE-15)

QUE_DATA = {
    "CPPB-QUE-01": {
        "title": "Cài Đặt Hàng Đợi Cơ Bản",
        "bc": "Một hệ thống xếp hàng tự động tại quầy giao dịch ngân hàng hoạt động theo nguyên tắc vào trước ra trước (FIFO - First In First Out). Hệ thống tiếp nhận $Q$ yêu cầu thuộc các dạng: thêm một khách hàng có số định danh $x$ vào cuối hàng đợi, phục vụ khách hàng đang đứng ở đầu hàng (loại bỏ khỏi hàng), và kiểm tra số định danh của khách hàng đang đứng đầu hàng hiện tại.",
        "nv": "Cho danh sách $Q$ thao tác thuộc 3 loại: `1 x` (thêm $x$ vào cuối hàng), `2` (loại bỏ phần tử đầu hàng nếu hàng không rỗng), `3` (in ra phần tử đầu hàng, nếu rỗng in ra `-1`). Hãy lập trình mô phỏng lại hàng đợi và in ra kết quả cho các thao tác loại 3.",
        "inp": "- Dòng 1: Chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$).\n- $Q$ dòng tiếp theo chứa các thao tác mô tả như trên.",
        "outp": "- Với mỗi thao tác loại 3, in ra kết quả trên một dòng.",
        "gt": "Với chuỗi thao tác: thêm 10, thêm 20, truy vấn đầu hàng -> in ra 10; phục vụ đầu hàng (loại 10), truy vấn đầu hàng -> in ra 20."
    },
    "CPPB-QUE-02": {
        "title": "Sinh Chuỗi Số Nhị Phân Bằng Queue",
        "bc": "Một chip tạo mã nhị phân cần xuất ra liên tục danh sách biểu diễn nhị phân của các số tự nhiên từ $1$ đến $N$ theo thứ tự tăng dần (ví dụ: với $N = 3$, danh sách là `1`, `10`, `11`). Nhờ tính chất hàng đợi, mỗi khi lấy ra một chuỗi nhị phân $S$, ta có thể dễ dàng tạo ra hai chuỗi nhị phân kế tiếp bằng cách ghép thêm ký tự `'0'` và `'1'` vào cuối.",
        "nv": "Cho số nguyên dương $N$. Hãy lập trình sinh và in ra chuỗi biểu diễn nhị phân của tất cả các số từ $1$ đến $N$, các chuỗi cách nhau bởi khoảng trắng.",
        "inp": "- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^4$).",
        "outp": "- In ra trên một dòng gồm $N$ chuỗi nhị phân tương ứng theo thứ tự tăng dần.",
        "gt": "Với $N = 5$, danh sách biểu diễn nhị phân của các số từ 1 đến 5 là: 1 (số 1), 10 (số 2), 11 (số 3), 100 (số 4), 101 (số 5)."
    },
    "CPPB-QUE-03": {
        "title": "BFS Tìm Bước Đi Ngắn Nhất Đồ Thị",
        "bc": "Một mạng máy tính gồm $N$ máy chủ được đánh số từ $1$ đến $N$ và $M$ kênh kết nối hai chiều không trọng số. Một gói tin xuất phát từ máy chủ nguồn $S$ muốn truyền đến máy chủ đích $D$. Mỗi lần truyền qua một kênh kết nối tốn đúng 1 bước nhảy (hop). Quản trị viên cần xác định số bước nhảy ít nhất để gói tin đến được đích.",
        "nv": "Cho đồ thị $N$ đỉnh $M$ cạnh và hai đỉnh $S, D$. Hãy lập trình tìm số bước đi ngắn nhất từ $S$ tới $D$. Nếu không thể đến được, in ra `-1`.",
        "inp": "- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5, 1 \le S, D \le N$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u$ và $v$ biểu diễn một kênh kết nối giữa đỉnh $u$ và $v$.",
        "outp": "- In ra một số nguyên duy nhất là số bước đi ngắn nhất, hoặc `-1` nếu không có đường đi.",
        "gt": "Với mạng gồm 4 máy chủ kết nối theo chuỗi $1 - 2 - 3 - 4$ và một kênh tắt nối trực tiếp $1 - 3$:\nĐể đi từ 1 tới 4, gói tin đi qua kênh tắt $1 \to 3$ tốn 1 bước, sau đó từ $3 \to 4$ tốn 1 bước nữa. Tổng số bước đi ít nhất là 2."
    },
    "CPPB-QUE-04": {
        "title": "Truy Vết Lộ Trình Ngắn Nhất Bằng BFS",
        "bc": "Sau khi tính toán được số bước nhảy tối thiểu để truyền gói tin giữa hai máy chủ, trung tâm điều hành cần in ra chính xác danh sách thứ tự các máy chủ mà gói tin đã đi qua để cấu hình bảng định tuyến mạng.",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và hai đỉnh $S, D$. Hãy lập trình tìm và in ra một đường đi ngắn nhất từ $S$ tới $D$. Nếu không có đường đi, in ra `-1`.",
        "inp": "- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.",
        "outp": "- Dòng 1: In ra số lượng đỉnh trên đường đi $K$.\n- Dòng 2: In ra $K$ số nguyên là thứ tự các đỉnh trên hành trình từ $S$ tới $D$.",
        "gt": "Với đồ thị có đường đi ngắn nhất từ 1 tới 4 là $1 \to 3 \to 4$:\nDòng 1 in ra 3 (số đỉnh trên đường đi).\nDòng 2 in ra 1 3 4."
    },
    "CPPB-QUE-05": {
        "title": "Min Mọi Cửa Sổ Trượt Bằng Monotonic Deque O(N)",
        "bc": "Một máy đo nhiệt độ lò phản ứng hạt nhân ghi nhận chuỗi $N$ giá trị đo liên tiếp. Một cửa sổ quan sát kích thước cố định gồm $K$ phép đo trượt dần từ đầu đến cuối dãy đo. Tại mỗi vị trí của cửa sổ trượt, hệ thống cảnh báo an toàn cần xác định giá trị nhiệt độ thấp nhất bên trong cửa sổ đó với tốc độ xử lý tức thời.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên và kích thước cửa sổ $K$. Hãy lập trình tìm giá trị nhỏ nhất trong mỗi cửa sổ trượt kích thước $K$ khi di chuyển từ trái sang phải.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $N - K + 1$ số nguyên là giá trị nhỏ nhất của từng cửa sổ trượt, cách nhau bởi khoảng trắng.",
        "gt": "Với mảng $[1, 3, -1, -3, 5, 3, 6, 7]$ và cửa sổ $K = 3$:\n- Cửa sổ 1 [1, 3, -1] -> min = -1.\n- Cửa sổ 2 [3, -1, -3] -> min = -3.\n- Cửa sổ 3 [-1, -3, 5] -> min = -3.\n- Cửa sổ 4 [-3, 5, 3] -> min = -3.\n- Cửa sổ 5 [5, 3, 6] -> min = 3.\n- Cửa sổ 6 [3, 6, 7] -> min = 3.\nKết quả in ra: -1 -3 -3 -3 3 3."
    },
    "CPPB-QUE-06": {
        "title": "Max Mọi Cửa Sổ Trượt Bằng Monotonic Deque O(N)",
        "bc": "Tương tự hệ thống giám sát lò phản ứng, để kịp thời phát hiện các đỉnh áp suất bất thường, hệ thống cần đồng thời theo dõi giá trị áp suất lớn nhất bên trong mỗi cửa sổ trượt gồm $K$ mốc đo liên tiếp.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên và kích thước cửa sổ $K$. Hãy lập trình tìm giá trị lớn nhất trong mỗi cửa sổ trượt kích thước $K$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $N - K + 1$ số nguyên là giá trị lớn nhất của từng cửa sổ trượt.",
        "gt": "Với mảng $[1, 3, -1, -3, 5, 3, 6, 7]$ và $K = 3$:\n- Cửa sổ [1, 3, -1] -> max = 3.\n- Cửa sổ [3, -1, -3] -> max = 3.\n- Cửa sổ [-1, -3, 5] -> max = 5.\n- Cửa sổ [-3, 5, 3] -> max = 5.\n- Cửa sổ [5, 3, 6] -> max = 6.\n- Cửa sổ [3, 6, 7] -> max = 7.\nKết quả in ra: 3 3 5 5 6 7."
    },
    "CPPB-QUE-07": {
        "title": "Kiểm Tra Đồ Thị Hai Phía (Bipartite Graph)",
        "bc": "Trong một hội thảo giao lưu quốc tế, có $N$ đại biểu và $M$ mối quan hệ quen biết lẫn nhau. Ban tổ chức muốn chia toàn bộ $N$ đại biểu vào đúng 2 phòng thảo luận khác nhau sao cho không có hai người nào quen nhau lại ngồi chung trong cùng một phòng (tương đương bài toán tô màu đồ thị bằng 2 màu sao cho hai đỉnh kề nhau luôn có màu khác nhau).",
        "nv": "Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình kiểm tra xem đồ thị có phải là đồ thị hai phía hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.",
        "outp": "- In ra `YES` nếu đồ thị là hai phía, ngược lại in ra `NO`.",
        "gt": "Với đồ thị là hình vuông gồm 4 đỉnh có các cạnh: 1-2, 2-3, 3-4, 4-1:\nTa có thể chia thành hai tập đỉnh độc lập: tập 1 gồm {1, 3} và tập 2 gồm {2, 4}. Không có hai đỉnh nào cùng tập có cạnh nối. Đồ thị là hai phía, kết quả in ra YES."
    },
    "CPPB-QUE-08": {
        "title": "Biến Đổi Số Bước Nhỏ Nhất Từ A Sang B",
        "bc": "Một trò chơi giải đố toán học bắt đầu với số nguyên dương $A$. Tại mỗi bước, người chơi có thể thực hiện một trong hai thao tác: nhân đôi số hiện tại ($x \\to 2x$) hoặc trừ số hiện tại đi 1 đơn vị ($x \\to x - 1$). Hãy tìm số thao tác ít nhất để biến đổi số $A$ ban đầu thành đúng số mục tiêu $B$.",
        "nv": "Cho hai số nguyên dương $A$ và $B$. Hãy lập trình tìm số bước biến đổi ít nhất từ $A$ thành $B$.",
        "inp": "- Một dòng duy nhất chứa hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^4$).",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là số bước ít nhất.",
        "gt": "Để biến đổi từ $A = 4$ sang $B = 6$:\n- Bước 1: Trừ 1 đơn vị: $4 - 1 = 3$.\n- Bước 2: Nhân đôi: $3 \\times 2 = 6$.\nChỉ cần đúng 2 bước biến đổi, kết quả in ra là 2."
    },
    "CPPB-QUE-09": {
        "title": "0-1 BFS Tìm Đường Đi Ngắn Nhất Trọng Số 0/1",
        "bc": "Một mạng lưới giao thông gồm $N$ nút giao và $M$ tuyến đường một chiều. Điểm đặc biệt là mỗi tuyến đường chỉ có trọng số chi phí hoặc là 0 đồng (đường công cộng miễn phí) hoặc là 1 đồng (đường cao tốc có thu phí tượng trưng). Cần tìm tổng chi phí ít nhất để di chuyển từ nút giao xuất phát $S$ tới nút giao đích $D$.",
        "nv": "Cho đồ thị có hướng $N$ đỉnh $M$ cạnh với trọng số mỗi cạnh thuộc $\{0, 1\}$. Hãy lập trình tìm khoảng cách ngắn nhất từ $S$ tới $D$. Nếu không đến được, in ra `-1`.",
        "inp": "- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2 \times 10^5, 1 \le S, D \le N$).\n- $M$ dòng tiếp theo, mỗi dòng chứa 3 số nguyên $u, v, w$ biểu diễn đường một chiều từ $u$ tới $v$ với trọng số $w \\in \\{0, 1\\}$.",
        "outp": "- In ra khoảng cách ngắn nhất từ $S$ tới $D$, hoặc `-1` nếu không có đường đi.",
        "gt": "Với đồ thị có đường đi từ 1 tới 3 qua cạnh trọng số 1, và từ 3 tới 4 qua cạnh trọng số 0:\nTổng chi phí từ 1 tới 4 là $1 + 0 = 1$ đồng. Đây là chi phí tối thiểu."
    },
    "CPPB-QUE-10": {
        "title": "Đoạn Con Tổng Lớn Nhất Độ Dài Tối Đa K",
        "bc": "Một công ty dầu khí phân tích chỉ số lưu lượng khai thác của một giếng dầu qua $N$ ngày liên tiếp tạo thành dãy số $A_1, A_2, \dots, A_N$. Ban giám đốc muốn chọn một đợt vận hành thử nghiệm gồm một chuỗi các ngày liên tiếp sao cho số ngày vận hành không vượt quá $K$ ngày và tổng lưu lượng khai thác thu được là lớn nhất có thể.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên và số nguyên $K$. Hãy lập trình tìm tổng lớn nhất của một đoạn con liên tiếp có độ dài tối đa là $K$.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất tổng lớn nhất tìm được.",
        "gt": "Với mảng $[-1, 2, 3, -2, 4]$ và độ dài tối đa $K = 2$:\nĐoạn con liên tiếp có độ dài không quá 2 có tổng lớn nhất là đoạn $[2, 3]$ (độ dài 2) cho tổng là $2 + 3 = 5$ (hoặc đoạn [4] có tổng 4)."
    },
    "CPPB-QUE-11": {
        "title": "Trò Chơi Vòng Tròn Josephus",
        "bc": "Trong một trò chơi dân gian, $N$ bạn học sinh đứng thành một vòng tròn và được đánh số từ $1$ đến $N$ theo chiều kim đồng hồ. Bắt đầu đếm từ bạn số 1, cứ mỗi khi đếm đến người thứ $K$ thì người đó sẽ phải rời khỏi vòng tròn. Quá trình đếm tiếp tục với người đứng kế tiếp cho đến khi chỉ còn lại đúng một người cuối cùng trụ lại.",
        "nv": "Cho số lượng người $N$ và bước đếm $K$. Hãy lập trình xác định số thứ tự của người cuối cùng còn lại trong vòng tròn.",
        "inp": "- Một dòng duy nhất chứa hai số nguyên dương $N$ và $K$ ($1 \le N \le 10^5, 1 \le K \le 100$).",
        "outp": "- In ra một số nguyên duy nhất là vị trí của người trụ lại cuối cùng.",
        "gt": "Với $N = 7$ người và bước đếm $K = 3$:\nThứ tự các người bị loại lần lượt là: 3, 6, 2, 7, 5, 1. Người cuối cùng còn lại là người số 4."
    },
    "CPPB-QUE-12": {
        "title": "Khoảng Cách Đến Trạm Cứu Hỏa Gần Nhất (Multi-Source BFS)",
        "bc": "Một bản đồ đô thị gồm $N$ khu dân cư và $M$ tuyến đường hai chiều. Trong thành phố có $K$ trạm cứu hỏa được đặt tại một số khu dân cư nhất định. Để đảm bảo an toàn phòng cháy chữa cháy, ban điều hành cứu hộ cần xác định khoảng cách ngắn nhất (số cạnh) từ mỗi khu dân cư tới trạm cứu hỏa gần nhất.",
        "nv": "Cho bản đồ thành phố và danh sách vị trí các trạm cứu hỏa. Hãy lập trình tính khoảng cách ngắn nhất từ từng khu dân cư đến trạm cứu hỏa gần nhất.",
        "inp": "- Dòng 1: Chứa 3 số nguyên $N, M, K$ ($1 \le K \le N \le 10^5, 0 \le M \le 2 \times 10^5$).\n- Dòng 2: Chứa $K$ số nguyên là vị trí đặt các trạm cứu hỏa.\n- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh biểu diễn một tuyến đường.",
        "outp": "- In ra trên một dòng gồm $N$ số nguyên là khoảng cách từ mỗi đỉnh đến trạm cứu hỏa gần nhất, cách nhau bởi khoảng trắng.",
        "gt": "Với 4 khu dân cư nối liên tiếp 1 - 2 - 3 - 4 và trạm cứu hỏa đặt tại khu 2:\n- Khu 1: cách trạm cứu hỏa 1 bước.\n- Khu 2: có sẵn trạm cứu hỏa $\\to$ khoảng cách 0.\n- Khu 3: cách trạm cứu hỏa 1 bước.\n- Khu 4: cách trạm cứu hỏa 2 bước.\nKết quả in ra: 1 0 1 2."
    },
    "CPPB-QUE-13": {
        "title": "Đoạn Con Dài Nhất Có Độ Chênh Lệch Max-Min <= C",
        "bc": "Một dây chuyền kiểm soát chất lượng linh kiện điện tử quét qua một dãy gồm $N$ sản phẩm với chỉ số dung sai $A_1, A_2, \dots, A_N$. Một lô sản phẩm đạt chuẩn ổn định là một đoạn con các sản phẩm liên tiếp sao cho độ chênh lệch giữa sản phẩm có dung sai lớn nhất và sản phẩm có dung sai nhỏ nhất trong lô không vượt quá một ngưỡng cho phép $C$.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên và ngưỡng chênh lệch $C$. Hãy lập trình tìm độ dài lớn nhất của một đoạn con liên tiếp có $\\max - \\min \\le C$.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $C$ ($1 \le N \le 10^5, 0 \le C \le 10^9$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất độ dài lớn nhất của đoạn con tìm được.",
        "gt": "Với mảng $[8, 2, 4, 7]$ và ngưỡng $C = 4$:\nĐoạn con $[2, 4]$ có $\\max = 4, \\min = 2$, độ chênh lệch là $4 - 2 = 2 \\le 4$ có độ dài 2.\nĐoạn con $[4, 7]$ có $\\max = 7, \\min = 4$, độ chênh lệch là $7 - 4 = 3 \\le 4$ có độ dài 2.\nĐộ dài lớn nhất đạt được là 2."
    },
    "CPPB-QUE-14": {
        "title": "Chọn Đoạn Tối Đa Không Quá K Phần Tử Liền Kề",
        "bc": "Một tuyến phố đi bộ có $N$ vị trí treo biển quảng cáo, vị trí thứ $i$ đem lại doanh thu $A_i$. Để đảm bảo không gian cảnh quan xanh cho tuyến phố, quy định đô thị yêu cầu không được phép treo biển quảng cáo tại quá $K$ vị trí đứng liền sát nhau.",
        "nv": "Cho danh sách doanh thu của $N$ vị trí và giới hạn $K$. Hãy lập trình chọn các vị trí treo biển sao cho không có quá $K$ vị trí liền kề được chọn và tổng doanh thu thu về là lớn nhất.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất tổng doanh thu lớn nhất đạt được.",
        "gt": "Với 5 vị trí có doanh thu $[1, 2, 3, 4, 5]$ và giới hạn $K = 2$ (không được chọn quá 2 vị trí liên tiếp):\nPhương án tối ưu là bỏ chọn vị trí thứ 3 (doanh thu 3), giữ lại các vị trí 1, 2, 4, 5. Các cụm chọn gồm [1, 2] (độ dài 2) và [4, 5] (độ dài 2), mang lại tổng doanh thu tối đa là $1 + 2 + 4 + 5 = 12$."
    },
    "CPPB-QUE-15": {
        "title": "Đua Xe Mê Cung Đổi Hướng Ít Nhất (0-1 BFS State)",
        "bc": "Trong một giải đua xe robot trong mê cung lưới ô vuông $N \times M$, robot cần di chuyển từ ô xuất phát $S$ tới ô đích $D$. Mỗi lần robot đi thẳng theo hướng đang di chuyển thì hoàn toàn miễn phí (chi phí 0), nhưng mỗi khi robot phải bẻ lái đổi sang một trong các hướng vuông góc thì bánh lái sẽ tiêu hao 1 đơn vị năng lượng.",
        "nv": "Cho bản đồ mê cung $N \times M$ và vị trí $S, D$. Hãy lập trình tìm số lần đổi hướng ít nhất để robot đi từ $S$ tới $D$. Nếu không có đường đi, in ra `-1`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi $M$ ký tự biểu diễn mê cung (`.` là đường đi, `*` là vật cản, `S` là xuất phát, `D` là đích).",
        "outp": "- In ra số lần đổi hướng ít nhất, hoặc `-1` nếu không có đường đi.",
        "gt": "Với mê cung $3 \\times 3$ không vật cản từ góc $(1,1)$ tới $(3,3)$:\nRobot chỉ cần đi thẳng hết hàng 1 sang phải, sau đó rẽ lái 1 lần duy nhất để đi thẳng xuống dưới tới đích. Số lần đổi hướng ít nhất là 1."
    }
}
