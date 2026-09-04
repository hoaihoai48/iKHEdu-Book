# enrich_data_stl.py
# Dữ liệu chuẩn hóa Sư phạm 15 bài STL (CPPB-STL-01 -> CPPB-STL-15)

STL_DATA = {
    "CPPB-STL-01": {
        "title": "Đếm Số Phần Tử Phân Biệt",
        "bc": "Tại một hội nghị thượng đỉnh về chuyển đổi số, ban lễ tân quét mã QR định danh của $N$ lượt đại biểu tham dự. Do một số đại biểu di chuyển nhiều lần qua cổng kiểm soát, danh sách các mã định danh thu thập được bị trùng lặp. Ban tổ chức cần thống kê chính xác số lượng đại biểu thực tế (tức số lượng mã định danh độc nhất, phân biệt) đã có mặt.",
        "nv": "Cho danh sách gồm $N$ số nguyên đại diện cho mã định danh. Hãy lập trình đếm và in ra số lượng giá trị phân biệt xuất hiện trong dãy số.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 2 \times 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$) cách nhau bởi khoảng trắng.",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là số lượng phần tử phân biệt trong dãy.",
        "gt": "Với dãy gồm 5 số nguyên $[2, 3, 2, 1, 3]$:\nCác giá trị phân biệt xuất hiện trong dãy là $\{1, 2, 3\}$. Có tất cả 3 giá trị phân biệt, kết quả in ra là 3."
    },
    "CPPB-STL-02": {
        "title": "Bảng Tra Cứu Tần Suất Từ Khóa",
        "bc": "Một công cụ tìm kiếm dữ liệu lớn ghi nhận $N$ từ khóa được người dùng nhập vào thanh tìm kiếm trong ngày. Để phục vụ việc tối ưu hóa máy chủ và đề xuất xu hướng tìm kiếm hàng đầu, kỹ sư hệ thống cần thiết lập một bảng thống kê tần suất xuất hiện của từng từ khóa theo thứ tự bảng chữ cái (thứ tự từ điển tăng dần).",
        "nv": "Cho danh sách gồm $N$ từ khóa. Hãy lập trình đếm tần suất xuất hiện của mỗi từ khóa và in ra kết quả theo thứ tự từ điển tăng dần của các từ khóa.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- $N$ dòng tiếp theo, mỗi dòng chứa một từ khóa gồm các chữ cái tiếng Anh in thường có độ dài từ 1 đến 30 ký tự.",
        "outp": "- In ra các dòng, mỗi dòng gồm một từ khóa và số lần xuất hiện của từ khóa đó, cách nhau bởi một dấu cách.",
        "gt": "Với danh sách 4 từ khóa: [\"apple\", \"banana\", \"apple\", \"cherry\"]:\n- Từ khóa \"apple\" xuất hiện 2 lần.\n- Từ khóa \"banana\" xuất hiện 1 lần.\n- Từ khóa \"cherry\" xuất hiện 1 lần.\nCác từ khóa được sắp xếp đúng thứ tự từ điển a -> b -> c."
    },
    "CPPB-STL-03": {
        "title": "Nén Tọa Độ Mảng Số Lớn",
        "bc": "Trong xử lý đồ họa máy tính, các điểm ảnh có tọa độ rất lớn lên tới $10^9$, nhưng tổng số lượng điểm ảnh thực tế xuất hiện trong khung hình chỉ tối đa là $N = 10^5$. Để tiết kiệm bộ nhớ khi đánh chỉ số mảng mà vẫn bảo toàn tuyệt đối thứ tự tương đối về độ lớn giữa các điểm ảnh, kỹ sư đồ họa áp dụng kỹ thuật nén tọa độ: thay thế mỗi giá trị bằng thứ hạng của nó từ $1$ đến $K$ (với $K$ là số giá trị phân biệt).",
        "nv": "Cho mảng gồm $N$ số nguyên. Hãy lập trình thay thế mỗi phần tử trong mảng bằng thứ hạng nén của nó (bắt đầu từ 1 cho giá trị nhỏ nhất).",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $N$ số nguyên là các giá trị sau khi đã nén tọa độ, cách nhau bởi khoảng trắng.",
        "gt": "Với mảng số ban đầu là $[100, 5, 100, 20, 5]$:\nCác giá trị phân biệt sau khi sắp xếp tăng dần là: $5 < 20 < 100$.\n- Giá trị 5 nhỏ nhất nhận thứ hạng 1.\n- Giá trị 20 nhận thứ hạng 2.\n- Giá trị 100 nhận thứ hạng 3.\nMảng sau khi nén tọa độ tương ứng là: $[3, 1, 3, 2, 1]$."
    },
    "CPPB-STL-04": {
        "title": "Tìm Phần Tử Nhỏ Nhất Lớn Hơn Hoặc Bằng X",
        "bc": "Một sàn giao dịch hàng hóa trực tuyến duy trì một kho các lệnh bán với mức giá niêm yết $A_1, A_2, \dots, A_N$. Khi một nhà đầu tư gửi lệnh mua với mức trần giá tối đa là $X$, hệ thống giao dịch tự động cần nhanh chóng tìm ra lệnh bán có mức giá nhỏ nhất thỏa mãn điều kiện lớn hơn hoặc bằng $X$ để khớp lệnh.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn, mỗi truy vấn gồm một số nguyên $X$. Hãy lập trình tìm phần tử nhỏ nhất trong mảng lớn hơn hoặc bằng $X$. Nếu không có phần tử nào thỏa mãn, in ra `-1`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).\n- $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên $X$ ($-10^9 \le X \le 10^9$).",
        "outp": "- Với mỗi truy vấn, in ra giá trị nhỏ nhất lớn hơn hoặc bằng $X$, hoặc `-1` nếu không có.",
        "gt": "Với mảng $[1, 4, 6, 8, 10]$ và các truy vấn $X$:\n- Truy vấn $X = 5$: Phần tử nhỏ nhất trong mảng $\ge 5$ là 6.\n- Truy vấn $X = 11$: Không có phần tử nào trong mảng $\ge 11$, in ra -1."
    },
    "CPPB-STL-05": {
        "title": "Hàng Đợi Ưu Tiên K Phần Tử Lớn Nhất",
        "bc": "Một nền tảng phát video trực tuyến theo dõi luồng tương tác của khán giả với hàng triệu lượt đánh giá. Trong luồng dữ liệu liên tục gồm $N$ lượt đánh giá điểm số, ban biên tập cần liên tục lọc ra danh sách $K$ lượt đánh giá có điểm số cao nhất để hiển thị lên bảng tin trang chủ.",
        "nv": "Cho danh sách gồm $N$ số nguyên và số nguyên dương $K$. Hãy lập trình tìm và in ra $K$ phần tử lớn nhất trong dãy theo thứ tự giảm dần.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $K$ số nguyên lớn nhất theo thứ tự giảm dần, cách nhau bởi khoảng trắng.",
        "gt": "Với mảng gồm 6 phần tử $[3, 2, 1, 5, 6, 4]$ và cần lấy $K = 2$ phần tử lớn nhất:\nHai phần tử lớn nhất trong dãy là 6 và 5. In ra theo thứ tự giảm dần: 6 5."
    },
    "CPPB-STL-06": {
        "title": "Quản Lý Tập Hợp Đa Trùng Lặp (Multiset)",
        "bc": "Một kho hàng thông minh hỗ trợ 3 loại thao tác quản lý sản phẩm: thêm một sản phẩm có mã giá $x$ vào kho, xóa bỏ đúng một sản phẩm có mã giá $x$ khỏi kho (nếu có), và truy vấn sản phẩm có mã giá rẻ nhất hiện đang có trong kho.",
        "nv": "Cho $Q$ thao tác thuộc một trong 3 loại: `1 x` (thêm $x$), `2 x` (xóa một phần tử $x$), `3` (in ra giá trị nhỏ nhất hiện tại). Hãy lập trình mô phỏng lại hệ thống và in ra kết quả cho các thao tác loại 3.",
        "inp": "- Dòng 1: Chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$).\n- $Q$ dòng tiếp theo chứa các thao tác mô tả như trên.",
        "outp": "- Với mỗi thao tác loại 3, in ra giá trị nhỏ nhất hiện tại trên một dòng.",
        "gt": "Với chuỗi thao tác: thêm 5, thêm 2, thêm 5, truy vấn min -> in ra 2; xóa 2, truy vấn min -> in ra 5."
    },
    "CPPB-STL-07": {
        "title": "Hợp Nhất Các Đoạn Số (Merge Intervals)",
        "bc": "Một máy chủ lập lịch tiếp nhận $N$ khoảng thời gian đặt lịch phòng họp, khoảng thời gian thứ $i$ bắt đầu từ thời điểm $L_i$ và kết thúc tại $R_i$. Một số khoảng thời gian bị chồng lấn (giao nhau) hoặc tiếp xúc liền kề. Ban quản trị tòa nhà cần hợp nhất tất cả các khoảng thời gian bị giao nhau lại thành các khối thời gian liền mạch độc lập.",
        "nv": "Cho danh sách $N$ khoảng thời gian $[L_i, R_i]$. Hãy lập trình hợp nhất các khoảng giao nhau và in ra danh sách các khoảng thời gian sau khi đã hợp nhất theo thứ tự thời điểm bắt đầu tăng dần.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $L_i$ và $R_i$ ($0 \le L_i \le R_i \le 10^9$).",
        "outp": "- Dòng 1: In ra số lượng khoảng thời gian $M$ sau khi hợp nhất.\n- $M$ dòng tiếp theo, mỗi dòng in ra hai số nguyên là điểm đầu và điểm cuối của một khoảng.",
        "gt": "Với các khoảng thời gian $[1, 3], [2, 6], [8, 10], [15, 18]$:\n- Khoảng $[1, 3]$ và $[2, 6]$ giao nhau vì $2 \le 3$, hợp nhất thành khoảng $[1, 6]$.\n- Các khoảng $[8, 10]$ và $[15, 18]$ độc lập không giao nhau.\nKết quả thu được 3 khoảng: $[1, 6], [8, 10], [15, 18]$."
    },
    "CPPB-STL-08": {
        "title": "Tìm Trung Vị Động Trong Luồng Dữ Liệu",
        "bc": "Trong hệ thống giám sát tải mạng máy tính, các gói tin liên tục gửi về các thông số độ trễ (ping). Để đánh giá độ trễ trung bình chuẩn xác mà không bị ảnh hưởng bởi các giá trị ngoại lai cá biệt, hệ thống cần tính toán giá trị trung vị (median) của luồng dữ liệu ngay sau mỗi khi tiếp nhận thêm một con số mới.",
        "nv": "Cho một luồng dữ liệu gồm $N$ số nguyên đến lần lượt từng số một. Với mỗi số được thêm vào, hãy in ra giá trị trung vị của toàn bộ dãy số đã nhận được từ đầu đến thời điểm đó (lấy phần nguyên dưới nếu số lượng phần tử chẵn).",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $N$ số nguyên là các giá trị trung vị tương ứng sau mỗi bước, cách nhau bởi khoảng trắng.",
        "gt": "Với luồng dữ liệu đến lần lượt: 5, 15, 1, 3:\n- Nhận 5: dãy [5] $\\to$ trung vị là 5.\n- Nhận 15: dãy [5, 15] $\\to$ trung vị là 5 (hoặc trung bình lấy nguyên).\n- Nhận 1: dãy [1, 5, 15] $\\to$ trung vị là 5.\n- Nhận 3: dãy [1, 3, 5, 15] $\\to$ trung vị là 3 (hoặc phần nguyên).\nKết quả in ra dãy trung vị động tương ứng."
    },
    "CPPB-STL-09": {
        "title": "Đếm Số Phần Tử Phân Biệt Trong Cửa Sổ K",
        "bc": "Một máy quét giám sát an ninh quét qua một chuỗi $N$ mã số xe lưu thông trên đường cao tốc. Máy quét sử dụng một khung quan sát (cửa sổ trượt) có kích thước cố định là $K$ xe liên tiếp. Khi cửa sổ trượt dịch chuyển từng vị trí từ đầu đến cuối hàng xe, hệ thống cần đếm xem trong mỗi cửa sổ hiện tại có bao nhiêu mã số xe phân biệt nhau.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên và kích thước cửa sổ $K$. Hãy lập trình in ra số lượng phần tử phân biệt trong mỗi cửa sổ kích thước $K$ khi trượt từ trái sang phải.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $N - K + 1$ số nguyên là số phần tử phân biệt trong từng cửa sổ, cách nhau bởi khoảng trắng.",
        "gt": "Với mảng gồm 7 phần tử $[1, 2, 1, 3, 4, 2, 3]$ và kích thước cửa sổ $K = 4$:\n- Cửa sổ 1 [1, 2, 1, 3]: gồm các giá trị phân biệt {1, 2, 3} $\\to$ 3 phần tử.\n- Cửa sổ 2 [2, 1, 3, 4]: gồm {1, 2, 3, 4} $\\to$ 4 phần tử.\n- Cửa sổ 3 [1, 3, 4, 2]: gồm {1, 2, 3, 4} $\\to$ 4 phần tử.\n- Cửa sổ 4 [3, 4, 2, 3]: gồm {2, 3, 4} $\\to$ 3 phần tử.\nKết quả in ra: 3 4 4 3."
    },
    "CPPB-STL-10": {
        "title": "Nối Dây Chi Phí Nhỏ Nhất (Huffman Greedy)",
        "bc": "Trong một xưởng cơ khí viễn thông, có $N$ đoạn cáp quang rời rạc với chiều dài lần lượt là $L_1, L_2, \dots, L_N$. Công nhân cần hàn nối tất cả các đoạn cáp này lại thành một sợi cáp duy nhất dài liên tục. Mỗi lần hàn nối hai sợi cáp bất kỳ có chiều dài $x$ và $y$, chi phí điện năng tiêu hao đúng bằng tổng chiều dài của hai sợi cáp đó ($x + y$). Sợi cáp mới ghép có chiều dài $x + y$ lại được đưa vào tập hợp để tiếp tục nối tiếp.",
        "nv": "Cho danh sách chiều dài $N$ đoạn cáp. Hãy lập trình tìm thứ tự nối cáp sao cho tổng chi phí hàn nối là nhỏ nhất có thể.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên dương $L_1, L_2, \dots, L_N$ ($1 \le L_i \le 10^4$).",
        "outp": "- In ra trên một dòng duy nhất tổng chi phí nhỏ nhất tìm được.",
        "gt": "Với 4 đoạn dây có độ dài $[4, 3, 2, 6]$:\n1. Nối hai dây ngắn nhất 2 và 3 thành dây độ dài 5, chi phí tốn $2 + 3 = 5$. Danh sách dây còn: [4, 5, 6].\n2. Nối tiếp hai dây ngắn nhất 4 và 5 thành dây độ dài 9, chi phí tốn $4 + 5 = 9$. Danh sách dây còn: [6, 9].\n3. Nối hai dây cuối 6 và 9 thành dây độ dài 15, chi phí tốn $6 + 9 = 15$.\nTổng chi phí nhỏ nhất là $5 + 9 + 15 = 29$."
    },
    "CPPB-STL-11": {
        "title": "Lập Lịch Công Việc Số Máy Chủ Ít Nhất",
        "bc": "Một trung tâm điện toán đám mây tiếp nhận $N$ tác vụ xử lý dữ liệu. Tác vụ thứ $i$ bắt đầu tại thời điểm $S_i$ và kết thúc tại thời điểm $E_i$. Một máy chủ chỉ có thể thực hiện một tác vụ tại một thời điểm. Nếu hai tác vụ có khoảng thời gian chạy bị chồng chéo nhau, chúng bắt buộc phải được giao cho hai máy chủ vật lý khác nhau.",
        "nv": "Cho danh sách thời gian bắt đầu và kết thúc của $N$ tác vụ. Hãy lập trình xác định số lượng máy chủ vật lý tối thiểu cần chuẩn bị để phục vụ toàn bộ các tác vụ.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $S_i$ và $E_i$ ($0 \le S_i < E_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất số lượng máy chủ tối thiểu cần dùng.",
        "gt": "Với 3 tác vụ: [0, 30], [5, 10], [15, 20]:\nTại thời điểm $t = 5$, tác vụ 1 [0, 30] đang chạy trên máy 1, nên tác vụ 2 [5, 10] bắt buộc phải mở thêm máy 2.\nTại thời điểm $t = 15$, tác vụ 2 đã xong nhưng tác vụ 1 vẫn đang chạy, nên tác vụ 3 có thể tái sử dụng máy 2.\nSố máy chủ tối thiểu cần dùng là 2."
    },
    "CPPB-STL-12": {
        "title": "Đếm Cặp Số Có Hiệu Bằng K",
        "bc": "Trong một thuật toán mã hóa khóa công khai, một danh sách gồm $N$ số nguyên bí mật được đưa vào xử lý. Kỹ sư an ninh cần đếm xem trong danh sách có bao nhiêu cặp chỉ số $(i, j)$ thỏa mãn điều kiện phần tử đứng sau lớn hơn phần tử đứng trước đúng một khoảng cách cố định $K$, tức là $A_j - A_i = K$ (với $i < j$).",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên và số nguyên $K$. Hãy lập trình đếm số lượng cặp $(i, j)$ có $i < j$ và $A_j - A_i = K$.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $K$ ($1 \le N \le 10^5, -10^9 \le K \le 10^9$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất số lượng cặp thỏa mãn.",
        "gt": "Với mảng $[1, 5, 3, 4, 2]$ và $K = 2$:\nCác cặp có hiệu bằng 2 là:\n- $A_2 - A_3 = 5 - 3 = 2$.\n- $A_3 - A_1 = 3 - 1 = 2$.\n- $A_4 - A_5 = 4 - 2 = 2$.\nCó tổng cộng 3 cặp số thỏa mãn."
    },
    "CPPB-STL-13": {
        "title": "Phần Tử Xuất Hiện Nhiều Nhất (Mode)",
        "bc": "Một hệ thống kiểm phiếu biểu quyết tiếp nhận $N$ lá phiếu được đánh mã số nguyên. Ban kiểm phiếu cần xác định giá trị mã số nào xuất hiện với tần suất nhiều nhất trong hòm phiếu (giá trị mốt - Mode). Nếu có nhiều mã số cùng đạt số phiếu cao nhất bằng nhau, hệ thống quy định sẽ ưu tiên chọn mã số có giá trị số học nhỏ nhất.",
        "nv": "Cho danh sách $N$ lá phiếu nguyên. Hãy lập trình tìm mã số xuất hiện nhiều lần nhất. Nếu có nhiều mã số cùng xuất hiện nhiều nhất, in ra mã số có giá trị nhỏ nhất trong số đó.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất giá trị mã số xuất hiện nhiều nhất theo quy ước trên.",
        "gt": "Với dãy số $[1, 2, 2, 3, 1]$:\nCả hai số 1 và 2 đều xuất hiện đúng 2 lần (nhiều nhất). Theo quy định ưu tiên giá trị số học nhỏ hơn, ta chọn số 1. Kết quả in ra là 1."
    },
    "CPPB-STL-14": {
        "title": "Cặp Điểm Gần Nhất (Closest Pair Of Points)",
        "bc": "Trên màn hình hiển thị radar hàng hải, có $N$ tàu biển đang hoạt động trên mặt biển. Tàu thứ $i$ có tọa độ vị trí là $(X_i, Y_i)$. Để cảnh báo nguy cơ va chạm sớm cho đài chỉ huy, hệ thống an toàn hàng hải cần tính toán khoảng cách hình học nhỏ nhất (khoảng cách Euclid) giữa hai tàu biển bất kỳ trong toàn bộ khu vực.",
        "nv": "Cho tọa độ của $N$ điểm trên mặt phẳng. Hãy lập trình tìm bình phương khoảng cách Euclid nhỏ nhất giữa hai điểm bất kỳ.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($2 \le N \le 10^5$).\n- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $X_i$ và $Y_i$ ($-10^9 \le X_i, Y_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất bình phương khoảng cách nhỏ nhất giữa hai điểm.",
        "gt": "Với 4 điểm tọa độ: $(0, 0), (1, 1), (2, 2), (2, 0)$:\nKhoảng cách giữa điểm $(1, 1)$ và $(2, 2)$ có bình phương là $(2-1)^2 + (2-1)^2 = 1 + 1 = 2$.\nKhoảng cách giữa điểm $(1, 1)$ và $(2, 0)$ có bình phương là $(2-1)^2 + (0-1)^2 = 1 + 1 = 2$.\nBình phương khoảng cách nhỏ nhất giữa hai điểm bất kỳ là 2."
    },
    "CPPB-STL-15": {
        "title": "Hệ Thống Xếp Hạng Thi Đấu Dynamic",
        "bc": "Tại kỳ thi lập trình thuật toán trực tuyến DKOJ của iKHEDU, hệ thống chấm thi thời gian thực cần liên tục ghi nhận điểm số và cập nhật kết quả thi đấu của các thí sinh. Mỗi khi thí sinh nộp bài hoặc cần tra cứu điểm, hệ thống sẽ thực thi một trong hai loại thao tác: cộng điểm cho một thí sinh hoặc truy vấn điểm tích lũy hiện tại của thí sinh đó.",
        "nv": "Cho danh sách $Q$ thao tác của hệ thống. Bạn hãy lập trình mô phỏng lại hệ thống và in ra kết quả cho mỗi thao tác tra cứu điểm.",
        "inp": "- Dòng 1: Chứa số nguyên dương $Q$ ($1 \le Q \le 20000$) là số lượng thao tác.\n- $Q$ dòng tiếp theo biểu diễn các thao tác thuộc một trong hai dạng:\n  - `1 Name Score`: Cộng thêm $Score$ điểm cho thí sinh có tên $Name$.\n  - `2 Name`: Yêu cầu in ra tổng điểm tích lũy hiện tại của thí sinh $Name$.",
        "outp": "- Với mỗi thao tác loại `2`, in ra trên một dòng một số nguyên duy nhất là tổng điểm của thí sinh đó (nếu thí sinh chưa có điểm, in ra `0`).",
        "gt": "Diễn biến 4 thao tác của hệ thống thi đấu:\n1. Thao tác 1 (`1 Alice 100`): Alice được cộng 100 điểm. Điểm hiện tại của Alice là 100.\n2. Thao tác 2 (`1 Bob 150`): Bob được cộng 150 điểm. Điểm hiện tại của Bob là 150.\n3. Thao tác 3 (`2 Alice`): Truy vấn điểm của Alice. Hệ thống in ra điểm hiện tại là 100.\n4. Thao tác 4 (`1 Alice 60`): Alice được cộng thêm 60 điểm nữa. Điểm tích lũy mới của Alice trở thành $100 + 60 = 160$."
    }
}
