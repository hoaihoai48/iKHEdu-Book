# enrich_data_dps.py
# Dữ liệu chuẩn hóa Sư phạm 15 bài DPS (CPPB-DPS-01 -> CPPB-DPS-15)

DPS_DATA = {
    "CPPB-DPS-01": {
        "title": "Xâu Con Chung Dài Nhất Cơ Bản (LCS)",
        "bc": "Trong lĩnh vực xử lý ngôn ngữ tự nhiên và kiểm tra đạo văn số học, hai văn bản số được chuyển hóa thành hai chuỗi ký tự $S$ và $T$. Một chuỗi con chung là một chuỗi các ký tự cùng xuất hiện trong cả hai văn bản theo đúng thứ tự tương đối ban đầu nhưng không nhất thiết phải đứng liền kề nhau. Các nhà nghiên cứu cần xác định độ dài chuỗi con chung dài nhất giữa hai văn bản để đo lường mức độ tương đồng nội dung.",
        "nv": "Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm độ dài của xâu con chung dài nhất của hai chuỗi đó.",
        "inp": "- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).\n- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).\nCác chuỗi chỉ chứa các ký tự chữ cái tiếng Anh in hoa hoặc in thường.",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là độ dài xâu con chung dài nhất.",
        "gt": "Với hai xâu $S = \\text{\"ABCBDAB\"}$ và $T = \\text{\"BDCAB\"}$:\nXâu con chung dài nhất có thể tìm được là $\\text{\"BCAB\"}$ (hoặc $\\text{\"BDAB\"}$) có độ dài đúng bằng 4."
    },
    "CPPB-DPS-02": {
        "title": "Truy Vết Xâu Con Chung Dài Nhất",
        "bc": "Sau khi tính toán được độ dài tương đồng giữa hai chuỗi văn bản, hệ thống kiểm tra đạo văn cần trích xuất chính xác chuỗi ký tự chung dài nhất đó để làm bằng chứng đánh dấu nổi bật (highlight) trên giao diện phần mềm cho người thẩm định theo dõi.",
        "nv": "Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm và in ra xâu con chung dài nhất của hai chuỗi. Nếu có nhiều xâu con chung cùng đạt độ dài lớn nhất, in ra một xâu bất kỳ thỏa mãn.",
        "inp": "- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).\n- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất xâu con chung dài nhất tìm được.",
        "gt": "Với hai xâu $S = \\text{\"ABCBDAB\"}$ và $T = \\text{\"BDCAB\"}$:\nXâu con chung dài nhất đồng thời xuất hiện trong cả hai xâu là $\\text{\"BCAB\"}$ với độ dài là 4. Kết quả in ra chuỗi BCAB."
    },
    "CPPB-DPS-03": {
        "title": "Khoảng Cách Chỉnh Sửa (Edit Distance / Levenshtein)",
        "bc": "Trong tính năng gợi ý tự động sửa lỗi chính tả của bàn phím thông minh, khi người dùng gõ nhầm một từ, máy tính cần tìm khoảng cách biến đổi tối thiểu từ chuỗi người dùng gõ thành chuỗi từ điển chuẩn. Có 3 thao tác chỉnh sửa ký tự cơ bản được hỗ trợ: chèn thêm 1 ký tự, xóa bớt 1 ký tự, hoặc thay thế 1 ký tự bằng 1 ký tự khác. Mỗi thao tác đều có chi phí là 1 đơn vị.",
        "nv": "Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm số lượng thao tác chỉnh sửa ít nhất để biến đổi chuỗi $S$ thành chuỗi $T$.",
        "inp": "- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).\n- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất số thao tác chỉnh sửa ít nhất cần dùng.",
        "gt": "Để biến đổi chuỗi $S = \\text{\"kitten\"}$ thành $T = \\text{\"sitting\"}$:\n1. Thay thế ký tự 'k' thành 's' $\\to \\text{\"sitten\"}$.\n2. Thay thế ký tự 'e' thành 'i' $\\to \\text{\"sittin\"}$.\n3. Chèn thêm ký tự 'g' vào cuối $\\to \\text{\"sitting\"}$.\nTổng cộng cần đúng 3 thao tác chỉnh sửa, kết quả là 3."
    },
    "CPPB-DPS-04": {
        "title": "Chỉ Dùng Phép Xóa Biến Đổi Hai Xâu",
        "bc": "Tại một máy nén dữ liệu truyền thông, hệ thống chỉ hỗ trợ duy nhất một thao tác cơ học là xóa bỏ ký tự. Cho hai chuỗi văn bản $S$ và $T$. Kỹ sư cần đưa cả hai chuỗi về cùng một chuỗi hoàn toàn giống nhau bằng cách chỉ xóa bỏ các ký tự trên mỗi chuỗi.",
        "nv": "Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm tổng số lượng ký tự ít nhất cần phải xóa bỏ trên cả hai chuỗi để phần còn lại của chúng trở nên đồng nhất.",
        "inp": "- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).\n- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất tổng số ký tự ít nhất cần xóa.",
        "gt": "Với hai chuỗi $S = \\text{\"sea\"}$ và $T = \\text{\"eat\"}$:\nĐể hai chuỗi trở nên giống nhau, ta đưa cả hai về chuỗi chung là $\\text{\"ea\"}$:\n- Trên chuỗi $S$: Xóa ký tự 's' (1 ký tự).\n- Trên chuỗi $T$: Xóa ký tự 't' (1 ký tự).\nTổng số ký tự cần xóa là $1 + 1 = 2$."
    },
    "CPPB-DPS-05": {
        "title": "Xâu Con Đối Xứng Dài Nhất (Longest Palindromic Subsequence)",
        "bc": "Một chuỗi ký tự được gọi là đối xứng (Palindrome) nếu đọc từ trái sang phải hay từ phải sang trái đều thu được chuỗi hoàn toàn giống nhau (ví dụ: `RADAR`, `MADAM`). Trong phân tích mã vạch bảo mật, ban kỹ thuật muốn trích xuất từ chuỗi gốc một chuỗi con (không nhất thiết liên tiếp) có tính đối xứng sao cho độ dài của nó là lớn nhất.",
        "nv": "Cho chuỗi ký tự $S$. Hãy lập trình tìm độ dài của chuỗi con đối xứng dài nhất trích xuất được từ $S$.",
        "inp": "- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất độ dài của chuỗi con đối xứng dài nhất.",
        "gt": "Với chuỗi $S = \\text{\"BBABCBCAB\"}$:\nMột chuỗi con đối xứng dài nhất có thể chọn là $\\text{\"BABCBAB\"}$ (hoặc $\\text{\"BACBCAB\"}$) có độ dài bằng 7."
    },
    "CPPB-DPS-06": {
        "title": "Đoạn Con Đối Xứng Liên Tiếp Dài Nhất",
        "bc": "Khác với chuỗi con rời rạc, một đoạn con liên tiếp (Substring) đối xứng đòi hỏi các ký tự phải đứng kề sát nhau và tạo thành một cụm đối xứng hoàn chỉnh. Đây là tác vụ trọng tâm trong việc nhận diện các đoạn lặp đảo ngược trong cấu trúc chuỗi gen sinh học.",
        "nv": "Cho chuỗi ký tự $S$. Hãy lập trình tìm độ dài của đoạn con liên tiếp đối xứng dài nhất trong $S$.",
        "inp": "- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất độ dài của đoạn con đối xứng liên tiếp dài nhất.",
        "gt": "Với chuỗi $S = \\text{\"babad\"}$:\nĐoạn con liên tiếp đối xứng dài nhất là $\\text{\"bab\"}$ (hoặc $\\text{\"aba\"}$) có độ dài bằng 3."
    },
    "CPPB-DPS-07": {
        "title": "Đếm Số Đoạn Con Đối Xứng Liên Tiếp",
        "bc": "Trong một kỳ thi mật mã học sinh viên, ban giám khảo đưa ra một chuỗi văn bản và yêu cầu các thí sinh thống kê tất cả các phân đoạn liên tiếp có tính đối xứng xuất hiện trong chuỗi (kể cả các đoạn con có độ dài 1 ký tự).",
        "nv": "Cho chuỗi ký tự $S$. Hãy lập trình đếm tổng số lượng đoạn con liên tiếp đối xứng có trong chuỗi.",
        "inp": "- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất tổng số lượng đoạn con đối xứng liên tiếp đếm được.",
        "gt": "Với chuỗi $S = \\text{\"aaa\"}$:\nCó tất cả 6 đoạn con liên tiếp đối xứng gồm:\n- 3 đoạn độ dài 1: \"a\" (vị trí 0), \"a\" (vị trí 1), \"a\" (vị trí 2).\n- 2 đoạn độ dài 2: \"aa\" (vị trí 0-1), \"aa\" (vị trí 1-2).\n- 1 đoạn độ dài 3: \"aaa\" (toàn bộ chuỗi).\nTổng số đoạn đối xứng là 6."
    },
    "CPPB-DPS-08": {
        "title": "Chèn Ít Ký Tự Nhất Tạo Chuỗi Đối Xứng",
        "bc": "Một máy in nhãn hàng hóa bị lỗi chỉ in được một chuỗi ký tự khuyết thiếu. Để nhãn hàng có tính thẩm mỹ cân đối, kỹ thuật viên cần chèn thêm vào các vị trí bất kỳ trong chuỗi một số lượng ký tự ít nhất sao cho chuỗi thu được trở thành một chuỗi đối xứng hoàn hảo.",
        "nv": "Cho chuỗi ký tự $S$. Hãy lập trình tìm số lượng ký tự ít nhất cần phải chèn thêm vào chuỗi $S$ để biến nó thành một chuỗi đối xứng.",
        "inp": "- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất số ký tự ít nhất cần chèn thêm.",
        "gt": "Với chuỗi $S = \\text{\"mbadm\"}$:\nĐể chuỗi trở thành đối xứng, ta có thể chèn thêm 2 ký tự 'd' và 'b' vào các vị trí thích hợp để tạo thành chuỗi $\\text{\"mbdadbm\"}$. Số ký tự chèn thêm ít nhất là 2."
    },
    "CPPB-DPS-09": {
        "title": "Xâu Mẹ Chung Ngắn Nhất (Shortest Common Supersequence)",
        "bc": "Một máy phát tín hiệu cần gửi một chuỗi mã nguồn sao cho máy thu khi nhận được có thể trích xuất ra đồng thời cả hai bản tin $S$ và $T$ dưới dạng các chuỗi con. Để tiết kiệm băng thông truyền dẫn số, độ dài của chuỗi mã phát đi phải là ngắn nhất có thể.",
        "nv": "Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm độ dài ngắn nhất của một chuỗi chứa cả $S$ và $T$ dưới dạng các chuỗi con.",
        "inp": "- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).\n- Dòng 2: Chứa chuỗi ký tự $T$ ($1 \le |T| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất độ dài ngắn nhất của xâu mẹ chung.",
        "gt": "Với hai chuỗi $S = \\text{\"abac\"}$ và $T = \\text{\"cab\"}$:\nXâu mẹ chung ngắn nhất chứa cả hai chuỗi là $\\text{\"cabac\"}$ có độ dài đúng bằng 5 (chứa \"cab\" ở tiền tố và \"abac\" ở hậu tố)."
    },
    "CPPB-DPS-10": {
        "title": "Đếm Số Lần Xuất Hiện Xâu Con Rời Rạc (Distinct Subsequences)",
        "bc": "Trong bộ lọc từ khóa độc hại của mạng xã hội, hệ thống cần kiểm tra tần suất mà một từ khóa nhạy cảm $T$ xuất hiện dưới dạng chuỗi con rời rạc bên trong một bài viết $S$. Hai cách xuất hiện được tính là khác nhau nếu tập hợp các vị trí chỉ số ký tự được chọn trong bài viết $S$ là khác nhau.",
        "nv": "Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình đếm số cách khác nhau để chọn ra chuỗi con trong $S$ bằng đúng chuỗi $T$, lấy dư cho $10^9 + 7$.",
        "inp": "- Dòng 1: Chứa chuỗi văn bản $S$ ($1 \le |S| \le 2000$).\n- Dòng 2: Chứa chuỗi mẫu $T$ ($1 \le |T| \le 500$).",
        "outp": "- In ra số cách xuất hiện hợp lệ theo modulo $10^9 + 7$.",
        "gt": "Với $S = \\text{\"rabbbit\"}$ và $T = \\text{\"rabbit\"}$:\nTrong chuỗi $S$ có 3 ký tự 'b' liên tiếp. Để tạo thành từ \"rabbit\", ta có thể loại bỏ 1 trong 3 ký tự 'b' đó. Do đó có đúng 3 cách chọn khác nhau để thu được từ \"rabbit\". Kết quả in ra là 3."
    },
    "CPPB-DPS-11": {
        "title": "Khớp Chuỗi Ký Tự Đại Diện (Wildcard Matching)",
        "bc": "Một công cụ tìm kiếm tệp tin hỗ trợ tìm kiếm theo mẫu (pattern) chứa các ký tự đại diện thông dụng: Ký tự `?` có thể khớp với đúng một ký tự bất kỳ, và ký tự `*` có thể khớp với bất kỳ chuỗi ký tự nào (kể cả chuỗi rỗng). Quản trị viên cần kiểm tra xem tên tệp văn bản $S$ có khớp hoàn toàn với mẫu $P$ hay không.",
        "nv": "Cho chuỗi văn bản $S$ và chuỗi mẫu $P$. Hãy lập trình kiểm tra xem chuỗi $S$ có khớp toàn bộ với mẫu $P$ hay không. Nếu khớp in ra `YES`, ngược lại in ra `NO`.",
        "inp": "- Dòng 1: Chứa chuỗi văn bản $S$ ($0 \le |S| \le 2000$).\n- Dòng 2: Chứa chuỗi mẫu $P$ ($0 \le |P| \le 2000$).",
        "outp": "- In ra `YES` nếu khớp hoàn toàn, ngược lại in ra `NO`.",
        "gt": "Với văn bản $S = \\text{\"adceb\"}$ và mẫu $P = \\text{\"*a*b\"}$:\nKý tự '*' đầu tiên khớp với chuỗi rỗng, sau đó ký tự 'a' khớp 'a', ký tự '*' thứ hai khớp với đoạn \"dce\", và cuối cùng ký tự 'b' khớp 'b'. Chuỗi khớp hoàn toàn với mẫu, kết quả in ra là YES."
    },
    "CPPB-DPS-12": {
        "title": "Xâu Con Chung Của Ba Chuỗi (LCS 3 Strings)",
        "bc": "Ba viện nghiên cứu sinh học độc lập cùng giải mã trình tự một đoạn gen kháng bệnh ở ba giống cây trồng khác nhau, thu được 3 chuỗi ADN ký hiệu là $S_1, S_2$ và $S_3$. Để xác định đoạn gen chung cốt lõi quy định tính trạng kháng bệnh, các nhà khoa học cần tìm độ dài của chuỗi con chung dài nhất xuất hiện đồng thời trong cả ba chuỗi ADN.",
        "nv": "Cho ba chuỗi ký tự $S_1, S_2$ và $S_3$. Hãy lập trình tính độ dài chuỗi con chung dài nhất của cả ba chuỗi.",
        "inp": "- Dòng 1: Chứa chuỗi ký tự $S_1$ ($1 \le |S_1| \le 100$).\n- Dòng 2: Chứa chuỗi ký tự $S_2$ ($1 \le |S_2| \le 100$).\n- Dòng 3: Chứa chuỗi ký tự $S_3$ ($1 \le |S_3| \le 100$).",
        "outp": "- In ra trên một dòng duy nhất một số nguyên là độ dài xâu con chung dài nhất của 3 chuỗi.",
        "gt": "Với 3 chuỗi ký tự:\n$S_1 = \\text{\"geeks\"}$, $S_2 = \\text{\"geeksfor\"}$, $S_3 = \\text{\"geeksforgeeks\"}$:\nChuỗi con chung dài nhất xuất hiện trong cả 3 chuỗi là $\\text{\"geeks\"}$ với độ dài bằng 5."
    },
    "CPPB-DPS-13": {
        "title": "Xóa Ít Ký Tự Nhất Để Chuỗi Đối Xứng",
        "bc": "Một thiết bị viễn thông thu nhận một chuỗi tín hiệu bị nhiễu chứa một số ký tự rác. Để khôi phục lại tính toàn vẹn của tín hiệu đối xứng nguyên bản, kỹ sư cần loại bỏ bớt một số lượng ký tự ít nhất từ chuỗi thu được sao cho chuỗi còn lại trở thành một chuỗi đối xứng.",
        "nv": "Cho chuỗi ký tự $S$. Hãy lập trình tìm số lượng ký tự ít nhất cần xóa bỏ để chuỗi còn lại là một chuỗi đối xứng.",
        "inp": "- Một dòng duy nhất chứa chuỗi ký tự $S$ ($1 \le |S| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất số ký tự ít nhất cần xóa.",
        "gt": "Với chuỗi $S = \\text{\"aebcbda\"}$:\nChuỗi con đối xứng dài nhất có thể giữ lại là $\\text{\"abcba\"}$ (độ dài 5). Để thu được chuỗi này, ta chỉ cần xóa đi đúng 2 ký tự là 'e' và 'd'. Số ký tự cần xóa ít nhất là 2."
    },
    "CPPB-DPS-14": {
        "title": "Độ Dài LCS Giữa Hai Chuỗi Gen",
        "bc": "Trong đề án nghiên cứu tiến hóa học phân tử, các nhà di truyền học so sánh hai chuỗi gen dài được biểu diễn dưới dạng hai chuỗi ký tự chỉ gồm 4 loại nucleotide cơ bản: `A`, `C`, `G`, `T`. Việc tìm độ dài xâu con chung dài nhất giữa hai chuỗi gen phản ánh mức độ gần gũi về mặt quan hệ tiến hóa giữa hai loài sinh vật.",
        "nv": "Cho hai chuỗi gen $S$ và $T$. Hãy lập trình tính độ dài chuỗi con chung dài nhất giữa hai chuỗi đó.",
        "inp": "- Dòng 1: Chứa chuỗi gen thứ nhất $S$ ($1 \le |S| \le 2000$).\n- Dòng 2: Chứa chuỗi gen thứ hai $T$ ($1 \le |T| \le 2000$).",
        "outp": "- In ra trên một dòng duy nhất độ dài xâu con chung dài nhất.",
        "gt": "Với hai chuỗi gen $S = \\text{\"AGGTAB\"}$ và $T = \\text{\"GXTXAYB\"}$:\nXâu con chung dài nhất giữa hai mẫu gen là $\\text{\"GTAB\"}$ có độ dài bằng 4."
    },
    "CPPB-DPS-15": {
        "title": "Tách Từ Trong Chuỗi (Word Break)",
        "bc": "Một hệ thống nhận dạng quang học chữ viết (OCR) quét văn bản tiếng Anh cổ nhưng do lỗi khoảng cách, tất cả các từ trong câu bị dính liền thành một chuỗi ký tự duy nhất $S$. Cho trước một cuốn từ điển gồm $N$ từ vựng chuẩn. Kỹ sư ngôn ngữ cần xác định xem chuỗi ký tự dính liền $S$ có thể được phân tách thành một chuỗi các từ hợp lệ nằm trong cuốn từ điển hay không.",
        "nv": "Cho chuỗi ký tự $S$ và từ điển gồm $N$ từ. Hãy lập trình kiểm tra xem chuỗi $S$ có thể được phân tách hoàn toàn thành các từ trong từ điển hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.",
        "inp": "- Dòng 1: Chứa chuỗi ký tự $S$ ($1 \le |S| \le 300$).\n- Dòng 2: Chứa số nguyên dương $N$ ($1 \le N \le 1000$) là số lượng từ trong từ điển.\n- $N$ dòng tiếp theo, mỗi dòng chứa một từ trong từ điển có độ dài không quá 20 ký tự.",
        "outp": "- In ra `YES` nếu chuỗi có thể phân tách hợp lệ, ngược lại in ra `NO`.",
        "gt": "Với chuỗi $S = \\text{\"leetcode\"}$ và từ điển gồm các từ {\"leet\", \"code\"}:\nChuỗi $S$ có thể phân tách thành hai từ hợp lệ là \"leet\" và \"code\". Cả hai từ đều có mặt trong từ điển, do đó kết quả in ra là YES."
    }
}
