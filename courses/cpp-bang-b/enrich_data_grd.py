# enrich_data_grd.py
# Dữ liệu chuẩn hóa Sư phạm 15 bài GRD (CPPB-GRD-01 -> CPPB-GRD-15)

GRD_DATA = {
    "CPPB-GRD-01": {
        "title": "Đếm Số Ô Kề Cạnh Hợp Lệ (4 Hướng)",
        "bc": "Trong một hệ thống điều khiển lưới cảm biến kích thước $N \times M$ ô vuông (chỉ số các ô từ $(0, 0)$ đến $(N - 1, M - 1)$), một thiết bị di động đang đứng tại ô tọa độ $(r, c)$. Thiết bị chỉ có thể gửi tín hiệu không dây tới các ô kề sát cạnh theo 4 hướng chính: lên trên $(r - 1, c)$, xuống dưới $(r + 1, c)$, sang trái $(r, c - 1)$, và sang phải $(r, c + 1)$. Kỹ sư phần mềm cần kiểm tra xem có bao nhiêu hướng di chuyển hợp lệ vẫn nằm trọn vẹn bên trong phạm vi ma trận.",
        "nv": "Cho kích thước ma trận $N, M$ và tọa độ $(r, c)$. Hãy lập trình đếm số ô kề cạnh hợp lệ nằm trong ma trận.",
        "inp": "- Một dòng duy nhất chứa 4 số nguyên $N, M, r, c$ ($1 \le N, M \le 1000, 0 \le r < N, 0 \le c < M$).",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là số ô kề cạnh hợp lệ.",
        "gt": "Với lưới kích thước $3 \times 3$ và vị trí ô góc $(0, 0)$:\n- Hướng lên trên và sang trái đều vượt ra ngoài biên của lưới.\n- Chỉ có 2 hướng hợp lệ là xuống dưới $(1, 0)$ và sang phải $(0, 1)$.\nSố ô kề cạnh hợp lệ là 2."
    },
    "CPPB-GRD-02": {
        "title": "Đếm Số Lượng Hòn Đảo (Count Islands)",
        "bc": "Một bức ảnh viễn thám chụp một vùng biển được số hóa thành ma trận nhị phân kích thước $N \times M$. Ký tự `'0'` đại diện cho mặt nước biển, còn ký tự `'1'` đại diện cho đất liền. Một hòn đảo được định nghĩa là một tập hợp các ô đất liền `'1'` kết nối với nhau theo 4 hướng (lên, xuống, trái, phải) và được bao quanh hoàn toàn bởi nước biển.",
        "nv": "Cho bản đồ ma trận $N \times M$. Hãy lập trình đếm số lượng hòn đảo xuất hiện trên bản đồ.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi gồm $M$ ký tự `'0'` hoặc `'1'` biểu diễn bản đồ.",
        "outp": "- In ra trên một dòng duy nhất số lượng hòn đảo đếm được.",
        "gt": "Với bản đồ kích thước $3 \times 3$ chứa các cụm đất liền biệt lập không có ô kề cạnh chung:\nCác ô đất liền kết nối thành đúng 3 cụm độc lập, kết quả đếm được là 3 hòn đảo."
    },
    "CPPB-GRD-03": {
        "title": "Diện Tích Hòn Đảo Lớn Nhất (Max Area of Island)",
        "bc": "Vẫn trên bản đồ hải đồ nhị phân $N \times M$ gồm các ô đất liền `'1'` và nước biển `'0'`, ban quản lý khu bảo tồn thiên nhiên muốn chọn ra hòn đảo có diện tích lớn nhất (chứa số lượng ô đất liền liên thông nhiều nhất) để quy hoạch xây dựng trung tâm cứu hộ động vật hoang dã.",
        "nv": "Cho bản đồ ma trận $N \times M$. Hãy lập trình tìm diện tích (số lượng ô đất) của hòn đảo lớn nhất. Nếu bản đồ không có đảo nào, in ra `0`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi gồm $M$ ký tự `'0'` hoặc `'1'`.",
        "outp": "- In ra trên một dòng duy nhất diện tích của hòn đảo lớn nhất.",
        "gt": "Với bản đồ có cụm đảo lớn nhất gồm 5 ô đất liền kề cạnh kết nối liên tục với nhau, diện tích lớn nhất đo được là 5."
    },
    "CPPB-GRD-04": {
        "title": "Tìm Đường Thoát Khỏi Mê Cung BFS",
        "bc": "Một robot tìm kiếm cứu nạn được thả vào một mê cung hình chữ nhật kích thước $N \times M$. Bản đồ mê cung gồm các ô đường đi trống `.` và các ô tường đá không thể vượt qua `#`. Robot xuất phát từ ô ký hiệu `S` và cần di chuyển đến ô cửa thoát hiểm ký hiệu `E`. Mỗi bước di chuyển sang một ô kề cạnh mất đúng 1 giây.",
        "nv": "Cho bản đồ mê cung. Hãy lập trình tìm thời gian ngắn nhất (số bước ít nhất) để robot đến được cửa thoát hiểm `E`. Nếu không có đường thoát, in ra `-1`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi gồm $M$ ký tự biểu diễn mê cung.",
        "outp": "- In ra số bước ít nhất để đến đích, hoặc `-1` nếu không có đường đi.",
        "gt": "Với mê cung từ 'S' tại góc $(0, 0)$ đến 'E' tại góc $(2, 2)$ qua các ô đường trống:\nLộ trình ngắn nhất gồm 4 bước di chuyển: $(0,0) \to (0,1) \to (1,1) \to (1,2) \to (2,2)$. Số bước ít nhất là 4."
    },
    "CPPB-GRD-05": {
        "title": "Truy Vết Đường Đi Mê Cung (L, R, U, D)",
        "bc": "Sau khi xác định được thời gian thoát hiểm ngắn nhất trong mê cung, bộ điều khiển cần xuất ra chuỗi lệnh điều hướng chi tiết bằng các ký tự viết tắt phương hướng: `'U'` (lên trên), `'D'` (xuống dưới), `'L'` (sang trái), `'R'` (sang phải) để nạp trực tiếp vào bộ nhớ vi điều khiển của robot.",
        "nv": "Cho bản đồ mê cung $N \times M$ với điểm xuất phát `S` và đích `E`. Hãy lập trình tìm đường đi ngắn nhất và in ra chuỗi các bước di chuyển tương ứng.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi $M$ ký tự.",
        "outp": "- Dòng 1: In ra số bước đi ngắn nhất $K$ (hoặc in `NO` nếu không có đường đi).\n- Dòng 2: In ra chuỗi $K$ ký tự gồm `U, D, L, R` mô tả lộ trình di chuyển.",
        "gt": "Với lộ trình đi từ $(0, 0)$ sang phải rồi xuống dưới:\nChuỗi lệnh điều hướng tương ứng là: \"RRD\" hoặc \"DRR\" có độ dài 3 bước."
    },
    "CPPB-GRD-06": {
        "title": "Đếm Số Ô Vùng Kín Không Thông Ra Biên",
        "bc": "Một vùng trũng ngập nước được số hóa thành lưới $N \times M$. Các ô đất liền có giá trị `1`, ô ngập nước có giá trị `0`. Một vùng đất được gọi là \"vùng kín\" nếu nó là một cụm các ô `1` liên thông kề cạnh mà hoàn toàn không có bất kỳ ô nào chạm vào 4 mép biên ngoài của bản đồ (nghĩa là vùng đất bị bao bọc hoàn toàn bởi các ô nước).",
        "nv": "Cho ma trận nhị phân $N \times M$. Hãy lập trình đếm tổng số lượng ô đất liền `1` thuộc về các vùng đất kín không thông ra biên.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên `0` hoặc `1` cách nhau bởi khoảng trắng.",
        "outp": "- In ra trên một dòng duy nhất số lượng ô đất liền thuộc các vùng kín.",
        "gt": "Với ma trận có một cụm gồm 3 ô đất nằm lọt thỏm ở trung tâm và toàn bộ viền xung quanh đều là ô số 0:\nCụm này hoàn toàn không chạm biên, số ô đất kín đếm được là 3."
    },
    "CPPB-GRD-07": {
        "title": "Chu Vi Hòn Đảo (Island Perimeter)",
        "bc": "Trên bản đồ dạng lưới $N \times M$, có đúng một hòn đảo duy nhất được tạo thành bởi các ô đất liền `'1'` kết nối liên thông (các ô còn lại là nước biển `'0'`). Mỗi ô đất liền là một hình vuông có cạnh dài đúng 1 đơn vị. Chu vi của hòn đảo là tổng độ dài các cạnh của các ô đất liền tiếp xúc trực tiếp với nước biển hoặc tiếp xúc với mép ngoài của bản đồ.",
        "nv": "Cho bản đồ chứa đúng một hòn đảo. Hãy lập trình tính chu vi của hòn đảo đó.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số `0` hoặc `1` cách nhau bởi khoảng trắng.",
        "outp": "- In ra trên một dòng duy nhất chu vi của hòn đảo.",
        "gt": "Với một hòn đảo gồm 4 ô đất liền xếp thành hình chữ L:\nTổng số cạnh tiếp xúc với nước biển xung quanh đo được là 16 đơn vị chiều dài. Kết quả in ra là 16."
    },
    "CPPB-GRD-08": {
        "title": "Nước Tràn Mê Cung (Multi-Source BFS)",
        "bc": "Một hầm mỏ dưới lòng đất kích thước $N \times M$ gồm các buồng trống `.` và các khối đá chắn `#`. Đột ngột có một sự cố vỡ đê ngầm khiến nước tràn vào từ $K$ buồng mỏ cùng lúc tại thời điểm $t = 0$. Cứ sau mỗi phút, nước từ các buồng đã ngập sẽ tràn sang tất cả các buồng trống kề sát nó theo 4 hướng. Hãy tính thời gian để toàn bộ các buồng trống trong hầm mỏ đều bị ngập nước.",
        "nv": "Cho bản đồ hầm mỏ và vị trí các nguồn nước ban đầu. Hãy lập trình tính thời gian (phút) để nước tràn kín toàn bộ các buồng trống liên thông.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi $M$ ký tự (`.` là buồng trống, `W` là nguồn nước, `#` là tường đá).",
        "outp": "- In ra thời gian tối đa để nước tràn ngập khắp hầm mỏ.",
        "gt": "Nước bắt đầu loang đồng thời từ các điểm 'W' theo chiều rộng:\nSau đúng 4 phút, điểm buồng mỏ xa nhất đã bị nước tràn tới ngập hoàn toàn. Kết quả là 4."
    },
    "CPPB-GRD-09": {
        "title": "Bước Nhảy Quân Mã Ngắn Nhất (Knight Moves)",
        "bc": "Trên bàn cờ vua tiêu chuẩn kích thước $N \times N$, quân Mã di chuyển theo quy tắc hình chữ L đặc thù: tại mỗi bước, quân Mã di chuyển 2 ô theo một trục và 1 ô theo trục vuông góc (tối đa 8 hướng nhảy). Cho vị trí ban đầu của quân Mã tại ô $(x_1, y_1)$ và ô mục tiêu $(x_2, y_2)$. Hãy tính số bước nhảy ít nhất để quân Mã di chuyển đến được ô mục tiêu.",
        "nv": "Cho kích thước bàn cờ $N$ và hai tọa độ điểm xuất phát, điểm đích. Hãy lập trình tìm số bước nhảy ít nhất của quân Mã.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).\n- Dòng 2: Chứa 4 số nguyên $x_1, y_1, x_2, y_2$ ($1 \le x_1, y_1, x_2, y_2 \le N$).",
        "outp": "- In ra số bước nhảy ít nhất cần dùng.",
        "gt": "Để đi từ ô $(1, 1)$ tới ô $(4, 5)$ trên bàn cờ vua:\nQuân mã thực hiện lần lượt các bước nhảy: $(1, 1) \to (2, 3) \to (4, 4) \to (2, 5) \to (4, 5)$ hoặc lộ trình tối ưu tương tự với đúng 3 bước nhảy. Kết quả là 3."
    },
    "CPPB-GRD-10": {
        "title": "Đường Kính Của Cây (Tree Diameter)",
        "bc": "Một mạng cáp viễn thông kết nối $N$ máy trạm tạo thành một cấu trúc cây liên thông không chu trình gồm đúng $N - 1$ đường cáp hai chiều. Khoảng cách giữa hai máy trạm là số lượng đường cáp trên hành trình nối giữa chúng. Đường kính của cây là khoảng cách lớn nhất giữa hai máy trạm bất kỳ trong toàn bộ mạng lưới.",
        "nv": "Cho cấu trúc cây gồm $N$ đỉnh. Hãy lập trình tìm đường kính (khoảng cách lớn nhất giữa hai đỉnh) của cây.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- $N - 1$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$ biểu diễn một cạnh của cây.",
        "outp": "- In ra trên một dòng duy nhất đường kính của cây.",
        "gt": "Với cây gồm 5 đỉnh có các cạnh (1, 2), (1, 3), (2, 4), (4, 5):\nHành trình dài nhất nối giữa đỉnh 3 và đỉnh 5 qua các cạnh: $3 - 1 - 2 - 4 - 5$, gồm đúng 4 cạnh. Đường kính của cây là 4."
    },
    "CPPB-GRD-11": {
        "title": "Trọng Tâm Của Cây (Tree Centroid)",
        "bc": "Một tập đoàn vận tải muốn đặt trung tâm điều hành tổng tại một trong $N$ thành phố có kết nối hình cây ($N - 1$ tuyến đường). Thành phố được chọn làm trọng tâm của cây nếu khi tạm thời gỡ bỏ thành phố này khỏi mạng lưới, kích thước của thành phần liên thông lớn nhất còn lại là nhỏ nhất có thể.",
        "nv": "Cho đồ thị cây $N$ đỉnh. Hãy lập trình tìm đỉnh trọng tâm của cây. Nếu có nhiều đỉnh trọng tâm, in ra đỉnh có số hiệu nhỏ nhất.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- $N - 1$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.",
        "outp": "- In ra số hiệu của đỉnh trọng tâm tìm được.",
        "gt": "Với cây 5 đỉnh có đỉnh 1 nối với các đỉnh 2, 3, 4, 5 (cấu trúc hình sao):\nNếu chọn đỉnh 1 làm trọng tâm, các nhánh còn lại đều chỉ có kích thước là 1. Đỉnh trọng tâm duy nhất là đỉnh 1."
    },
    "CPPB-GRD-12": {
        "title": "Cổng Dịch Chuyển Tức Thời (Teleport Maze)",
        "bc": "Trong một trò chơi thực tế ảo trong mê cung lưới $N \times M$, ngoài các ô đường đi thông thường, mê cung còn bố trí một số cặp cổng dịch chuyển tức thời không gian. Khi bước vào một cổng dịch chuyển, người chơi sẽ ngay lập tức được dịch chuyển sang cổng tương ứng ở vị trí khác mà không tốn thời gian (0 giây). Hãy tìm thời gian ngắn nhất để đi từ điểm xuất phát `S` tới đích `E`.",
        "nv": "Cho bản đồ mê cung và danh sách các cặp cổng dịch chuyển. Hãy lập trình tìm số bước ít nhất để đến đích.",
        "inp": "- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N, M \le 1000$).\n- Các dòng tiếp theo mô tả bản đồ mê cung và các cặp cổng dịch chuyển.",
        "outp": "- In ra số bước ít nhất từ S tới E, hoặc `-1` nếu không có đường đi.",
        "gt": "Nhờ sử dụng cổng dịch chuyển tức thời, người chơi rút ngắn được quãng đường vòng qua tường đá, thời gian đến đích giảm xuống còn 3 bước."
    },
    "CPPB-GRD-13": {
        "title": "Lây Lan Quả Cam Hỏng (Rotting Oranges)",
        "bc": "Trong một thùng hàng hoa quả kích thước $N \times M$, mỗi ô có thể chứa: ô trống (số `0`), một quả cam tươi nguyên vẹn (số `1`), hoặc một quả cam đã bị hỏng mốc (số `2`). Cứ sau mỗi phút, những quả cam bị hỏng sẽ làm hỏng tất cả các quả cam tươi kề sát nó theo 4 hướng. Hãy tính số phút tối thiểu để toàn bộ cam tươi trong thùng đều bị hỏng. Nếu có quả cam tươi nào mãi mãi không bị hỏng (bị cô lập), in ra `-1`.",
        "nv": "Cho ma trận trạng thái thùng cam. Hãy lập trình tìm số phút ít nhất để tất cả cam tươi đều hỏng.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên 0, 1 hoặc 2 cách nhau bởi khoảng trắng.",
        "outp": "- In ra số phút ít nhất, hoặc `-1` nếu vẫn còn cam tươi không thể bị hỏng.",
        "gt": "Với thùng cam kích thước $3 \times 3$:\n- Phút 1: cam hỏng tại $(0, 0)$ lây sang các ô $(0, 1)$ và $(1, 0)$.\n- Phút 2: tiếp tục lây sang các ô kế tiếp.\nSau đúng 4 phút, toàn bộ cam tươi đều đã bị lây hỏng. Kết quả là 4."
    },
    "CPPB-GRD-14": {
        "title": "Hòn Đảo Nhân Tạo Lớn Nhất (Making A Large Island)",
        "bc": "Một dự án lấn biển quy hoạch trên vùng biển lưới $N \times M$ gồm các ô đất liền `'1'` và các ô nước biển `'0'`. Ban quản lý dự án được cấp ngân sách để cải tạo đúng một ô nước biển `'0'` duy nhất thành ô đất liền `'1'`. Hãy tìm diện tích hòn đảo lớn nhất có thể tạo thành sau khi đã biến đổi đúng một ô nước biển thích hợp.",
        "nv": "Cho ma trận nhị phân $N \times M$. Hãy lập trình tìm diện tích lớn nhất của một hòn đảo sau khi chuyển đổi tối đa một ô `0` thành `1`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên `0` hoặc `1`.",
        "outp": "- In ra trên một dòng duy nhất diện tích lớn nhất của hòn đảo thu được.",
        "gt": "Với hai hòn đảo nhỏ diện tích 2 và 3 nằm cách nhau đúng một ô nước biển '0':\nKhi chuyển ô nước đó thành ô đất '1', hai hòn đảo sẽ được nối liền thành một hòn đảo duy nhất có diện tích $2 + 3 + 1 = 6$. Diện tích lớn nhất đạt được là 6."
    },
    "CPPB-GRD-15": {
        "title": "Thoát Khỏi Mê Cung Quái Vật (Monsters Maze)",
        "bc": "Trong một trò chơi phiêu lưu sinh tồn trên lưới ô vuông $N \times M$, một người thám hiểm xuất phát tại ô `A` và cần chạy thoát ra một ô biên bất kỳ của mê cung. Trong mê cung cũng có sự xuất hiện của một số quái vật tại các ô `M`. Tại mỗi giây, người thám hiểm và tất cả quái vật đều có thể di chuyển 1 bước sang ô kề cạnh. Nếu một con quái vật có thể tới một ô cùng lúc hoặc trước người thám hiểm, người thám hiểm sẽ bị bắt.",
        "nv": "Cho bản đồ mê cung. Hãy lập trình kiểm tra xem người thám hiểm có thể thoát thân thành công ra mép biên hay không. Nếu có in ra `YES` kèm số bước, ngược lại in ra `NO`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ ký tự (`.` là đường, `#` là tường, `A` là người, `M` là quái vật).",
        "outp": "- Dòng 1: In ra `YES` nếu thoát được, ngược lại in ra `NO`.\n- Nếu `YES`, dòng 2 in ra số bước đi ngắn nhất ra biên.",
        "gt": "Người thám hiểm chọn lộ trình nhanh nhất hướng về phía mép biên phía đông, đến được biên an toàn sau 2 bước trước khi bất kỳ quái vật nào kịp tiếp cận. Kết quả in ra YES."
    }
}
