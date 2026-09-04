# enrich_data_stk.py
# Dữ liệu chuẩn hóa Sư phạm 15 bài STK (CPPB-STK-01 -> CPPB-STK-15)

STK_DATA = {
    "CPPB-STK-01": {
        "title": "Kiểm Tra Dãy Ngoặc Đúng Đơn Loại",
        "bc": "Trong một trình biên dịch ngôn ngữ lập trình, việc đóng mở các cặp dấu ngoặc tròn `(` và `)` phải tuân thủ nghiêm ngặt quy tắc ngữ pháp: Mỗi dấu mở ngoặc `(` phải có một dấu đóng ngoặc `)` tương ứng xuất hiện sau nó, và tại mọi thời điểm tính từ đầu chuỗi, số lượng dấu mở ngoặc không bao giờ được ít hơn số lượng dấu đóng ngoặc.",
        "nv": "Cho một chuỗi chỉ gồm các ký tự `(` và `)`. Hãy lập trình kiểm tra xem chuỗi đó có phải là một dãy ngoặc đúng hay không. Nếu đúng in ra `YES`, ngược lại in ra `NO`.",
        "inp": "- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 10^5$).",
        "outp": "- In ra `YES` nếu chuỗi là dãy ngoặc đúng, ngược lại in ra `NO`.",
        "gt": "Với chuỗi $S = \\text{\"(()())\"}$:\nMỗi dấu mở ngoặc đều có đúng một dấu đóng ngoặc tương ứng ghép đôi hợp lệ và không có dấu đóng ngoặc nào bị thừa. Kết quả in ra là YES."
    },
    "CPPB-STK-02": {
        "title": "Dãy Ngoặc Hỗn Hợp Nhiều Loại",
        "bc": "Trình biên dịch mã nguồn mở rộng hỗ trợ đồng thời 3 loại cặp dấu ngoặc khác nhau: ngoặc tròn `()`, ngoặc vuông `[]` và ngoặc nhọn `{}`. Một chuỗi ngoặc hỗn hợp được coi là hợp lệ nếu các cặp ngoặc cùng loại được đóng mở đúng quy tắc lồng nhau, không bị đóng chéo (ví dụ: `([)]` là sai quy tắc vì ngoặc tròn mở trước nhưng lại bị ngoặc vuông xen vào đóng trước).",
        "nv": "Cho chuỗi $S$ chỉ gồm các ký tự `(`, `)`, `[`, `]`, `{`, `}`. Hãy lập trình kiểm tra tính hợp lệ của chuỗi. Nếu hợp lệ in ra `YES`, ngược lại in ra `NO`.",
        "inp": "- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 10^5$).",
        "outp": "- In ra `YES` nếu chuỗi hợp lệ, ngược lại in ra `NO`.",
        "gt": "Với chuỗi $S = \\text{\"{[()]}\"}$:\nCặp ngoặc tròn nằm hoàn toàn bên trong ngoặc vuông, và ngoặc vuông nằm bên trong ngoặc nhọn. Quy tắc lồng nhau được bảo đảm trọn vẹn, kết quả in ra là YES."
    },
    "CPPB-STK-03": {
        "title": "Đánh Giá Biểu Thức Hậu Tố (Reverse Polish Notation)",
        "bc": "Trong thiết kế vi xử lý và máy tính cầm tay, biểu thức toán học thường được chuyển đổi sang dạng ký pháp nghịch đảo Ba Lan (hậu tố - Postfix) để máy tính dễ dàng tính toán mà không cần quan tâm đến độ ưu tiên của dấu ngoặc. Trong biểu thức hậu tố, toán tử luôn đứng sau hai toán hạng của nó (ví dụ: `2 3 +` tương đương `2 + 3 = 5`).",
        "nv": "Cho một biểu thức hậu tố gồm các số nguyên và 4 phép toán cơ bản `+`, `-`, `*`, `/` (chia lấy phần nguyên). Hãy lập trình tính và in ra giá trị cuối cùng của biểu thức.",
        "inp": "- Một dòng duy nhất chứa các toán hạng và toán tử cách nhau bởi khoảng trắng ($1 \le \\text{số lượng token} \le 10^4$).",
        "outp": "- In ra một số nguyên duy nhất là giá trị của biểu thức.",
        "gt": "Với biểu thức hậu tố \"2 1 + 3 *\":\n1. Gặp toán tử '+': Thực hiện $2 + 1 = 3$.\n2. Biểu thức trở thành \"3 3 *\".\n3. Gặp toán tử '*': Thực hiện $3 \\times 3 = 9$.\nGiá trị cuối cùng thu được là 9."
    },
    "CPPB-STK-04": {
        "title": "Xóa Ký Tự Trùng Lặp Liền Kề",
        "bc": "Một trò chơi xếp chữ tương tác có quy tắc: Khi hai ký tự giống hệt nhau đứng sát cạnh nhau trong chuỗi, chúng sẽ tự động va chạm và cùng biến mất. Sau khi hai ký tự đó biến mất, hai phần còn lại của chuỗi sẽ dồn sát vào nhau và nếu lại tạo ra hai ký tự giống nhau kề nhau thì quá trình triệt tiêu lại tiếp tục diễn ra cho đến khi không còn cặp ký tự kề nhau nào giống nhau.",
        "nv": "Cho chuỗi ký tự $S$. Hãy lập trình xác định chuỗi ký tự cuối cùng thu được sau khi tất cả các cặp trùng lặp liền kề đã bị triệt tiêu hoàn toàn.",
        "inp": "- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 10^5$).",
        "outp": "- In ra chuỗi ký tự còn lại sau khi triệt tiêu. Nếu chuỗi bị triệt tiêu hết, in ra chuỗi rỗng hoặc thông báo quy định.",
        "gt": "Với chuỗi $S = \\text{\"abbaca\"}$:\n1. Cặp \"bb\" ở giữa triệt tiêu $\\to$ chuỗi còn lại là \"aaca\".\n2. Cặp \"aa\" mới tạo thành kề nhau lại tiếp tục triệt tiêu $\\to$ chuỗi còn lại là \"ca\".\nKhông còn cặp nào trùng nhau kề nhau, chuỗi kết quả in ra là ca."
    },
    "CPPB-STK-05": {
        "title": "Phần Tử Lớn Hơn Tiếp Theo (Next Greater Element)",
        "bc": "Một đồ thị phân tích thị trường chứng khoán gồm $N$ mốc thời gian liên tiếp với mức giá cổ phiếu lần lượt là $A_1, A_2, \dots, A_N$. Với mỗi phiên giao dịch tại mốc $i$, nhà phân tích tài chính muốn biết mức giá của phiên giao dịch đầu tiên xuất hiện sau phiên $i$ (bên phải $i$) có giá trị lớn hơn hẳn $A_i$. Nếu từ mốc $i$ về sau không có phiên nào có giá cao hơn, ghi nhận giá trị `-1`.",
        "nv": "Cho dãy số nguyên $A$ gồm $N$ phần tử. Với mỗi phần tử trong mảng, hãy tìm phần tử đầu tiên nằm bên phải nó có giá trị lớn hơn nó. Nếu không có, gán giá trị `-1`.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $N$ số nguyên là phần tử lớn hơn tiếp theo tương ứng, cách nhau bởi khoảng trắng.",
        "gt": "Với mảng gồm 4 phần tử $[4, 5, 2, 25]$:\n- Phần tử 4: Bên phải phần tử đầu tiên lớn hơn 4 là 5.\n- Phần tử 5: Bên phải phần tử đầu tiên lớn hơn 5 là 25.\n- Phần tử 2: Bên phải phần tử đầu tiên lớn hơn 2 là 25.\n- Phần tử 25: Bên phải không còn số nào lớn hơn 25 $\\to$ in ra -1.\nKết quả in ra: 5 25 25 -1."
    },
    "CPPB-STK-06": {
        "title": "Phần Tử Nhỏ Hơn Gần Nhất Bên Trái (Previous Smaller Element)",
        "bc": "Một hệ thống băng tải tự động gồm $N$ vị trí cảm biến. Với mỗi vị trí cảm biến $i$, hệ thống cần xác định vị trí của cảm biến đầu tiên nằm về phía bên trái có chỉ số đọc nhỏ hơn cảm biến $i$ để tính toán độ dốc địa hình ngược chiều dòng sản phẩm.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên. Với mỗi phần tử $A_i$, hãy tìm phần tử đầu tiên nằm bên trái nó có giá trị nhỏ hơn nó. Nếu không có phần tử nào thỏa mãn, gán `-1`.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $N$ số nguyên là các giá trị nhỏ hơn gần nhất bên trái tương ứng.",
        "gt": "Với mảng $[4, 5, 2, 10, 8]$:\n- Số 4: Bên trái không có số nào $\\to$ -1.\n- Số 5: Số đầu tiên bên trái nhỏ hơn 5 là 4.\n- Số 2: Bên trái không có số nào nhỏ hơn 2 $\\to$ -1.\n- Số 10: Số đầu tiên bên trái nhỏ hơn 10 là 2.\n- Số 8: Số đầu tiên bên trái nhỏ hơn 8 là 2.\nKết quả in ra: -1 4 -1 2 2."
    },
    "CPPB-STK-07": {
        "title": "Độ Dài Đoạn Ngoặc Đúng Liên Tiếp Dài Nhất",
        "bc": "Trong một chuỗi ký tự ngoặc hỗn độn bị lỗi truyền dẫn, kỹ sư phần mềm muốn khôi phục lại phần thông điệp hợp lệ dài nhất. Hãy tìm độ dài của một đoạn con liên tiếp dài nhất trong chuỗi sao cho đoạn con đó tạo thành một dãy ngoặc đúng hoàn chỉnh.",
        "nv": "Cho chuỗi $S$ chỉ gồm các ký tự `(` và `)`. Hãy lập trình tìm độ dài lớn nhất của một đoạn con liên tiếp là dãy ngoặc đúng.",
        "inp": "- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 10^5$).",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là độ dài lớn nhất của đoạn ngoặc đúng liên tiếp.",
        "gt": "Với chuỗi $S = \\text{\")()())\"}$:\nĐoạn con liên tiếp bắt đầu từ vị trí 1 đến vị trí 4 là \"()()\" tạo thành dãy ngoặc đúng hoàn chỉnh có độ dài bằng 4. Đây là đoạn ngoặc đúng dài nhất."
    },
    "CPPB-STK-08": {
        "title": "Xóa K Chữ Số Để Được Số Nhỏ Nhất",
        "bc": "Một mã định danh số lớn gồm $N$ chữ số dạng chuỗi ký tự. Do yêu cầu rút gọn mã trong hệ thống lưu trữ, quản trị viên cần xóa bỏ đúng $K$ chữ số bất kỳ khỏi chuỗi sao cho các chữ số còn lại giữ nguyên thứ tự ban đầu và tạo thành một số nguyên có giá trị nhỏ nhất có thể (không để số 0 vô nghĩa đứng ở đầu nếu kết quả lớn hơn 0).",
        "nv": "Cho chuỗi số $S$ và số nguyên $K$. Hãy lập trình tìm số nguyên nhỏ nhất thu được sau khi xóa đúng $K$ chữ số.",
        "inp": "- Dòng 1: Chứa chuỗi ký tự số $S$ ($1 \le |S| \le 10^5$).\n- Dòng 2: Chứa số nguyên không âm $K$ ($0 \le K < |S|$).",
        "outp": "- In ra chuỗi ký tự đại diện cho số nhỏ nhất tìm được.",
        "gt": "Với số ban đầu là \"1432219\" và cần xóa đi $K = 3$ chữ số:\nTa xóa các chữ số 4, 3, 2 tại các vị trí đầu để giữ lại số \"1219\". Đây là số nguyên nhỏ nhất có thể tạo thành."
    },
    "CPPB-STK-09": {
        "title": "Hình Chữ Nhật Lớn Nhất Trên Histogram",
        "bc": "Một biểu đồ cột (histogram) gồm $N$ cột hình chữ nhật đứng xếp kề sát nhau trên cùng một đường nằm ngang. Mỗi cột có chiều rộng cố định là 1 đơn vị, cột thứ $i$ có chiều cao là $H_i$. Ban thiết kế đồ họa cần tìm diện tích của hình chữ nhật lớn nhất có thể vẽ lọt hoàn toàn vào bên trong biểu đồ cột này.",
        "nv": "Cho danh sách chiều cao của $N$ cột. Hãy lập trình tìm diện tích lớn nhất của một hình chữ nhật nằm gọn bên trong biểu đồ cột.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên không âm $H_1, H_2, \dots, H_N$ ($0 \le H_i \le 10^9$).",
        "outp": "- In ra trên một dòng duy nhất diện tích lớn nhất của hình chữ nhật.",
        "gt": "Với biểu đồ có chiều cao các cột là $[2, 1, 5, 6, 2, 3]$:\nHình chữ nhật lớn nhất được tạo thành bởi hai cột có chiều cao 5 và 6. Chiều cao của hình chữ nhật này là $\\min(5, 6) = 5$, chiều rộng là 2 cột. Diện tích lớn nhất đạt được là $5 \\times 2 = 10$."
    },
    "CPPB-STK-10": {
        "title": "Hứng Nước Mưa (Trapping Rain Water)",
        "bc": "Một mô hình địa hình gồm $N$ khối bê tông thẳng đứng có chiều rộng 1 đơn vị được xếp thẳng hàng kề sát nhau, khối thứ $i$ có độ cao $H_i$. Sau một cơn mưa rào lớn, nước mưa sẽ đọng lại ở các thung lũng giữa các khối bê tông cao hơn hai bên. Hãy tính toán tổng lượng nước mưa tối đa có thể đọng lại sau cơn mưa.",
        "nv": "Cho danh sách chiều cao của $N$ khối bê tông. Hãy lập trình tính tổng đơn vị thể tích nước mưa có thể đọng lại.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên không âm $H_1, H_2, \dots, H_N$ ($0 \le H_i \le 10^5$).",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là tổng thể tích nước mưa đọng lại.",
        "gt": "Với độ cao địa hình là $[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]$:\nNước mưa sẽ bị giữ lại ở các vùng trũng giữa các cột cao:\n- Tại vị trí 2: nước đọng 1 đơn vị.\n- Tại vị trí 4: nước đọng 1 đơn vị.\n- Tại vị trí 5: nước đọng 2 đơn vị.\n- Tại vị trí 6: nước đọng 1 đơn vị.\n- Tại vị trí 9: nước đọng 1 đơn vị.\nTổng lượng nước đọng lại là $1 + 1 + 2 + 1 + 1 = 6$ đơn vị."
    },
    "CPPB-STK-11": {
        "title": "Hình Chữ Nhật Toàn 1 Lớn Nhất Trong Ma Trận",
        "bc": "Một tấm tôn kích thước $N \times M$ ô vuông bị đục thủng một số vị trí (ô bị đục ký hiệu bằng số `0`, ô nguyên vẹn ký hiệu bằng số `1`). Người thợ cơ khí cần cắt ra từ tấm tôn một miếng hình chữ nhật nguyên vẹn (chỉ chứa toàn số `1`) sao cho diện tích của miếng tôn cắt ra là lớn nhất có thể.",
        "nv": "Cho ma trận nhị phân $N \times M$. Hãy lập trình tìm diện tích lớn nhất của hình chữ nhật con chỉ chứa toàn số `1`.",
        "inp": "- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).\n- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên `0` hoặc `1` cách nhau bởi khoảng trắng.",
        "outp": "- In ra trên một dòng duy nhất diện tích lớn nhất của hình chữ nhật tìm được.",
        "gt": "Với ma trận kích thước $4 \times 5$:\nHình chữ nhật con toàn số 1 lớn nhất có kích thước $2 \\times 3$ (chiều cao 2, chiều rộng 3) gồm 6 ô số 1. Diện tích lớn nhất đạt được là 6."
    },
    "CPPB-STK-12": {
        "title": "Tổng Giá Trị Nhỏ Nhất Của Mọi Đoạn Con",
        "bc": "Cho mảng $A$ gồm $N$ số nguyên. Một đoạn con của mảng là một chuỗi các phần tử liên tiếp $A[L..R]$ ($1 \le L \le R \le N$). Với mỗi đoạn con, ta xác định giá trị nhỏ nhất của đoạn con đó là $\\min(A[L..R])$. Ban toán học cần tính tổng của tất cả các giá trị nhỏ nhất này trên mọi đoạn con có thể tạo thành từ mảng.",
        "nv": "Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình tính tổng giá trị nhỏ nhất của tất cả các đoạn con, lấy dư cho $10^9 + 7$.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^5$).",
        "outp": "- In ra trên một dòng duy nhất tổng tìm được theo modulo $10^9 + 7$.",
        "gt": "Với mảng gồm 4 phần tử $[3, 1, 2, 4]$:\nCác đoạn con có giá trị nhỏ nhất tương ứng:\n- Độ dài 1: [3] -> 3, [1] -> 1, [2] -> 2, [4] -> 4 (tổng = 10).\n- Độ dài 2: [3,1] -> 1, [1,2] -> 1, [2,4] -> 2 (tổng = 4).\n- Độ dài 3: [3,1,2] -> 1, [1,2,4] -> 1 (tổng = 2).\n- Độ dài 4: [3,1,2,4] -> 1 (tổng = 1).\nTổng cộng toàn bộ là $10 + 4 + 2 + 1 = 17$."
    },
    "CPPB-STK-13": {
        "title": "Next Greater Element Trên Mảng Vòng Tròn",
        "bc": "Một vòng đu quay gồm $N$ cabin được đánh số theo vòng tròn từ $1$ đến $N$, cabin thứ $N$ lại kết nối liền kề với cabin số $1$. Cabin thứ $i$ có chiều cao $A_i$. Khi đứng tại cabin $i$ và nhìn theo chiều kim đồng hồ quanh vòng tròn, hãy tìm giá trị của cabin đầu tiên có chiều cao lớn hơn cabin $i$. Nếu đi hết một vòng tròn mà không có cabin nào cao hơn, ghi nhận `-1`.",
        "nv": "Cho mảng tròn $A$ gồm $N$ phần tử. Với mỗi phần tử, hãy tìm phần tử lớn hơn đầu tiên tiếp theo trên mảng vòng tròn. Nếu không có, in ra `-1`.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $N$ số nguyên tương ứng, cách nhau bởi khoảng trắng.",
        "gt": "Với mảng tròn gồm 3 phần tử $[1, 2, 1]$:\n- Phần tử 1 (đầu): Nhìn tiếp theo gặp số 2 lớn hơn 1 $\\to$ in ra 2.\n- Phần tử 2 (giữa): Nhìn tiếp theo gặp 1, rồi vòng lại đầu gặp 1, không có số nào lớn hơn 2 $\\to$ in ra -1.\n- Phần tử 1 (cuối): Vòng lại đầu mảng gặp 1, tiếp tục gặp 2 lớn hơn 1 $\\to$ in ra 2.\nKết quả in ra: 2 -1 2."
    },
    "CPPB-STK-14": {
        "title": "Tầm Nhìn Tòa Tháp (Stock Span)",
        "bc": "Trên một tuyến phố ven biển có $N$ tòa tháp cao tầng xếp thẳng hàng từ trái sang phải, tòa tháp thứ $i$ có chiều cao $H_i$. Tầm nhìn về phía sau của một tòa tháp $i$ được định nghĩa là số lượng tòa tháp liên tiếp nằm ngay bên trái nó (tính cả chính nó) mà có chiều cao nhỏ hơn hoặc bằng $H_i$.",
        "nv": "Cho danh sách chiều cao của $N$ tòa tháp. Hãy lập trình tính tầm nhìn cho từng tòa tháp trong dãy.",
        "inp": "- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).\n- Dòng 2: Chứa $N$ số nguyên dương $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^9$).",
        "outp": "- In ra trên một dòng gồm $N$ số nguyên là tầm nhìn tương ứng của từng tòa tháp, cách nhau bởi khoảng trắng.",
        "gt": "Với chiều cao các tháp $[100, 80, 60, 70, 60, 75, 85]$:\n- Tháp 1 (100): tầm nhìn 1 (chính nó).\n- Tháp 2 (80): tầm nhìn 1.\n- Tháp 3 (60): tầm nhìn 1.\n- Tháp 4 (70): bao trùm tháp 60 và chính nó $\\to$ tầm nhìn 2.\n- Tháp 5 (60): tầm nhìn 1.\n- Tháp 6 (75): bao trùm tháp 60, 70, 60 và chính nó $\\to$ tầm nhìn 4.\n- Tháp 7 (85): bao trùm tất cả các tháp trừ tháp 100 $\\to$ tầm nhìn 6.\nKết quả in ra: 1 1 1 2 1 4 6."
    },
    "CPPB-STK-15": {
        "title": "Đánh Giá Biểu Thức Trung Tố (Infix Expression)",
        "bc": "Một máy tính bỏ túi thông minh tiếp nhận biểu thức số học viết ở dạng trung tố tự nhiên (dạng toán học thông thường có chứa các dấu ngoặc tròn `()`, số nguyên và 4 phép toán cơ bản `+`, `-`, `*`, `/`). Biểu thức tuân thủ độ ưu tiên toán học: nhân chia trước, cộng trừ sau, trong ngoặc trước, ngoài ngoặc sau.",
        "nv": "Cho một chuỗi biểu thức số học trung tố hợp lệ. Hãy lập trình tính toán và in ra giá trị số học cuối cùng của biểu thức.",
        "inp": "- Một dòng duy nhất chứa chuỗi biểu thức gồm các chữ số, dấu ngoặc `(` `)` và các toán tử `+ - * /` ($1 \le |S| \le 10^5$).",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là kết quả của biểu thức.",
        "gt": "Với biểu thức số học \"1 + (2 * 3) - 4 / 2\":\n1. Tính trong ngoặc: $2 \\times 3 = 6$.\n2. Biểu thức trở thành: $1 + 6 - 4 / 2$.\n3. Thực hiện phép chia: $4 / 2 = 2$.\n4. Biểu thức thành: $1 + 6 - 2 = 5$.\nKết quả in ra là 5."
    }
}
