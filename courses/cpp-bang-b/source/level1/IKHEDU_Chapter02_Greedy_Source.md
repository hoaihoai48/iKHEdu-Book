# TÀI LIỆU GỐC — CHƯƠNG 2: THAM LAM

## Vai trò tài liệu

Tài liệu này là bản gốc nội dung dùng để biên soạn Chương 2 — Tham lam. Nội dung được viết và review tại đây trước khi tổng hợp sang bản thảo sách. Chương này kế thừa tư duy sắp xếp từ Chương 1 nhưng tập trung vào câu hỏi mới: **sau mỗi bước, nên chọn phương án nào?**

## Đối tượng và phạm vi

Tài liệu dành cho học sinh mới bắt đầu học thuật toán. Em cần biết `vector`, vòng lặp, điều kiện, `sort`, comparator đơn giản và cách phân tích trực tiếp một dãy dữ liệu. Phạm vi cốt lõi là chiến lược chọn hoạt động không giao nhau, cách sắp xếp theo thời điểm kết thúc, lập luận đổi chỗ và nhận biết phản ví dụ. Các biến thể như lập lịch có thời hạn, ba lô phân số và cây khung nhỏ nhất được giới thiệu như hướng mở rộng, không đặt vào luồng đầu tiên.

## Nguyên tắc biên soạn

Tham lam không được trình bày như quy tắc “luôn chọn số lớn nhất” hoặc “luôn chọn số nhỏ nhất”. Mỗi lựa chọn tham lam phải đi cùng ba câu hỏi: tiêu chí chọn là gì, vì sao lựa chọn đó an toàn, và khi nào tiêu chí đó thất bại. Nội dung dùng ví dụ bằng tay trước, sau đó mới chuyển sang sắp xếp, vòng lặp, code và lập luận đúng đắn.

---

## Chương 2 — Tham lam

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Hiểu cách xây dựng lời giải bằng các lựa chọn cục bộ có căn cứ |
| Kiến thức cần có | Sắp xếp, comparator, vòng lặp, điều kiện, `vector` và mô tả Input–Process–Output |
| Phạm vi | Khái niệm tham lam, chọn hoạt động, chứng minh đổi chỗ, phản ví dụ và các biến thể cơ bản |
| Số bài | 6 bài học, kết hợp mô phỏng, code, lập luận và bài chuyển giao |

**Vị trí trong lộ trình:** Sách trình bày Chương 2 ngay sau Chương 1 để tạo mạch đọc liền nhau từ Sorting sang Greedy. Giáo viên có thể điều chỉnh thứ tự dạy theo mức độ lớp học và teaching sequence của trung tâm, miễn là học sinh đã có prerequisite về sắp xếp, vòng lặp và so sánh.

### Learning outcomes

Sau chương này, em có thể:

1. Giải thích thuật toán tham lam bằng một ví dụ cụ thể.
2. Phân biệt lựa chọn cục bộ với mục tiêu tối ưu toàn cục.
3. Nhận biết bài toán chọn nhiều hoạt động không giao nhau.
4. Sắp xếp hoạt động theo thời điểm kết thúc và duyệt để chọn hoạt động hợp lệ.
5. Mô phỏng trạng thái sau từng lựa chọn.
6. Trình bày vì sao chọn hoạt động kết thúc sớm là an toàn.
7. Dùng phản ví dụ để kiểm tra một quy tắc tham lam đáng ngờ.
8. Phân biệt bài dùng được tham lam với bài cần phân tích thêm hoặc cân nhắc quy hoạch động, tìm kiếm.
9. Phân tích độ phức tạp `O(N log N)` của lời giải chọn hoạt động.
10. Giải thích sau khi chọn một phương án thì phần còn lại của bài toán thay đổi như thế nào.

### Câu hỏi trung tâm của chương

> **Ở mỗi bước, ta chọn gì để vừa tốt ngay lúc này, vừa không làm mất cơ hội đạt lời giải tốt nhất về sau?**

---

### Bài 2.1 — Tham lam là gì?

#### Mục tiêu bài

Sau Bài 2.1, em có thể mô tả một chiến lược tham lam, phân biệt “chọn ngay” với “thử mọi khả năng”, và biết rằng một quy tắc nghe có vẻ hợp lý vẫn cần được kiểm tra.

#### Khởi động

Có một hàng người đang chờ lấy vé. Mỗi người có một khoảng thời gian có thể vào quầy. Nếu quầy chỉ phục vụ được một người tại một thời điểm, ta muốn phục vụ càng nhiều người càng tốt.

Một suy nghĩ tự nhiên là chọn người đến sớm nhất. Nhưng người đến sớm nhất có thể chờ rất lâu và chiếm mất phần lớn thời gian. Một suy nghĩ khác là chọn người có khoảng thời gian ngắn nhất. Điều đó cũng chưa chắc đúng, vì một khoảng ngắn nằm ở giữa có thể chặn hai khoảng khác.

Muốn chọn đúng, ta phải tìm **tiêu chí liên quan trực tiếp đến mục tiêu**.

#### Ý tưởng “chọn tốt trước”

Một thuật toán tham lam thường làm như sau:

```text
1. Xác định mục tiêu cần tối ưu.
2. Chọn một phương án hợp lệ có vẻ tốt nhất theo tiêu chí đã đặt ra.
3. Cố định lựa chọn đó.
4. Cập nhật phần bài toán còn lại.
5. Lặp lại cho đến khi hoàn thành.
```

Điểm quan trọng là bước 2 không được chọn tùy tiện. Ta cần trả lời vì sao lựa chọn hiện tại không làm mất lời giải tối ưu về sau.

#### Cục bộ và toàn cục

**Lựa chọn cục bộ** là lựa chọn tốt ở bước hiện tại. **Lời giải toàn cục** là kết quả tốt nhất sau khi hoàn thành tất cả các bước.

Tham lam chỉ đúng khi các lựa chọn cục bộ theo tiêu chí phù hợp có thể dẫn tới một lời giải toàn cục tối ưu. Không phải cứ “chọn tốt nhất trước” là sẽ đúng.

#### Phản ví dụ với đổi tiền

Giả sử có các mệnh giá `1`, `3`, `4` và cần đổi số tiền `6` bằng ít đồng nhất.

Nếu luôn chọn đồng lớn nhất trước:

```text
6 → chọn 4, còn 2 → chọn 1, còn 1 → chọn 1
Số đồng: 3
```

Nhưng cách tốt hơn là:

```text
6 → chọn 3 và 3
Số đồng: 2
```

Vậy quy tắc “luôn chọn mệnh giá lớn nhất” **không phải lúc nào cũng đúng**. Đây là một phản ví dụ: một trường hợp nhỏ đủ để bác bỏ một quy tắc tổng quát.

#### Ba câu hỏi kiểm tra một ý tưởng tham lam

Trước khi code, em hãy hỏi:

1. Mục tiêu là tối đa, tối thiểu hay chỉ kiểm tra khả năng?
2. Tiêu chí chọn hiện tại có liên quan trực tiếp đến mục tiêu không?
3. Em có thể giải thích hoặc chứng minh vì sao lựa chọn đó không làm mất đáp án tốt nhất không?

Nếu chưa trả lời được câu thứ ba, đừng vội gọi thuật toán là đúng.

#### Tự kiểm tra

1. Lựa chọn cục bộ khác lời giải toàn cục ở điểm nào?
2. Trong ví dụ mệnh giá `1, 3, 4`, vì sao chọn `4` trước lại không tối ưu cho số tiền `6`?
3. Một phản ví dụ có tác dụng gì?
4. Tham lam có phải là thử mọi cách rồi chọn kết quả tốt nhất không?

#### Luyện tập ngắn

- Tạo một bộ mệnh giá khác mà chiến lược chọn đồng lớn nhất trước bị sai.
- Với mệnh giá `1, 5, 10, 25`, hãy thử số tiền `30` và kiểm tra xem chiến lược tham lam có cho kết quả tốt không. Chưa cần chứng minh cho mọi số tiền.
- Viết bằng lời một tình huống trong đó chọn phương án kết thúc sớm có thể hữu ích hơn chọn phương án bắt đầu sớm.

#### Tóm tắt bài

Tham lam là cách xây dựng lời giải bằng các quyết định từng bước. **Tiêu chí chọn phải được giải thích và kiểm tra**, vì một quy tắc hợp lý trong vài ví dụ chưa đủ để bảo đảm đúng trong mọi trường hợp.

---

### Bài 2.2 — Chọn nhiều hoạt động không giao nhau

#### Mục tiêu bài

Sau Bài 2.2, em có thể mô hình hóa bài toán lịch hoạt động, hiểu điều kiện hai hoạt động không giao nhau và mô phỏng việc chọn nhiều hoạt động bằng tay.

#### Bài toán

Một phòng học chỉ phục vụ được một hoạt động tại một thời điểm. Hoạt động thứ `i` bắt đầu tại `start[i]` và kết thúc tại `finish[i]`. Trong các ví dụ của chương, ta giả sử `0 <= start[i] < finish[i]`. Hai hoạt động được xem là không giao nhau nếu hoạt động sau bắt đầu khi hoạt động trước đã kết thúc.

Hãy chọn **nhiều hoạt động nhất** sao cho không có hai hoạt động được chọn nào giao nhau.

Nếu hoạt động A kết thúc lúc `5` và hoạt động B bắt đầu lúc `5`, ta cho phép chọn cả hai. Điều kiện tương ứng là:

```text
start của hoạt động mới >= finish của hoạt động vừa chọn
```

#### Ví dụ bằng tay

Cho các hoạt động:

| Hoạt động | Bắt đầu | Kết thúc |
|---|---:|---:|
| A | 1 | 4 |
| B | 3 | 5 |
| C | 0 | 6 |
| D | 5 | 7 |
| E | 3 | 8 |
| F | 5 | 9 |
| G | 6 | 10 |
| H | 8 | 11 |
| I | 8 | 12 |
| J | 2 | 13 |
| K | 12 | 14 |

Một lựa chọn tốt là:

```text
A: [1, 4] → D: [5, 7] → H: [8, 11] → K: [12, 14]
```

Ta chọn được `4` hoạt động. Nhưng vì sao không chọn C trước? C kết thúc lúc `6`, làm mất cơ hội chọn A và D.

#### Quan sát quan trọng

Trong mục tiêu chọn **nhiều hoạt động nhất**, hoạt động kết thúc sớm để lại nhiều thời gian còn lại hơn. Đây là dấu hiệu để thử tiêu chí:

> **Ưu tiên hoạt động có thời điểm kết thúc nhỏ nhất.**

Tiêu chí này khác với:

- bắt đầu sớm nhất;
- có thời lượng ngắn nhất;
- có thời điểm bắt đầu muộn nhất;
- có tên hoặc số thứ tự nhỏ nhất.

Các tiêu chí trên có thể đúng trong một bài khác, nhưng không tự động đúng cho bài này.

#### Mô phỏng sau khi sắp xếp theo thời điểm kết thúc

Danh sách theo `finish` tăng dần:

```text
A(1,4), B(3,5), C(0,6), D(5,7), E(3,8), F(5,9), G(6,10), H(8,11), I(8,12), J(2,13), K(12,14)
```

Duyệt lần lượt:

| Hoạt động xét | Có hợp lệ không? | Hành động | Thời điểm kết thúc mới |
|---|---|---|---:|
| A(1,4) | Có, là hoạt động đầu tiên | Chọn | 4 |
| B(3,5) | Không, `3 < 4` | Bỏ qua | 4 |
| C(0,6) | Không, `0 < 4` | Bỏ qua | 4 |
| D(5,7) | Có, `5 >= 4` | Chọn | 7 |
| E(3,8) | Không, `3 < 7` | Bỏ qua | 7 |
| F(5,9) | Không, `5 < 7` | Bỏ qua | 7 |
| G(6,10) | Không, `6 < 7` | Bỏ qua | 7 |
| H(8,11) | Có, `8 >= 7` | Chọn | 11 |
| I(8,12) | Không, `8 < 11` | Bỏ qua | 11 |
| J(2,13) | Không, `2 < 11` | Bỏ qua | 11 |
| K(12,14) | Có, `12 >= 11` | Chọn | 14 |

Trạng thái cần nhớ chỉ là `lastFinish`: thời điểm kết thúc của hoạt động gần nhất đã chọn.

#### Tự kiểm tra

1. Hai hoạt động `[1, 4]` và `[4, 6]` có giao nhau theo quy ước của bài không?
2. Sau khi chọn `[1, 4]`, hoạt động `[3, 5]` có được chọn không? Vì sao?
3. Vì sao hoạt động kết thúc sớm để lại nhiều thời gian hơn?
4. Trong bảng trên, tại sao hoạt động `D(5,7)` được chọn sau `A(1,4)`?

#### Luyện tập ngắn

- Vẽ các đoạn thời gian của sáu hoạt động bất kỳ rồi tự chọn số hoạt động không giao nhau.
- Với các khoảng `[2,3]`, `[1,5]`, `[4,6]`, `[6,8]`, `[5,7]`, hãy tìm một tập hoạt động lớn nhất.
- Thử chọn theo “bắt đầu sớm nhất” và so sánh với chọn theo “kết thúc sớm nhất”. Tìm một input làm hai cách cho kết quả khác nhau.

#### Tóm tắt bài

Bài toán chọn hoạt động yêu cầu tối đa số khoảng không giao nhau. Khi một hoạt động được chọn, phần còn lại chỉ phụ thuộc vào thời điểm kết thúc của hoạt động đó. Đây là nền tảng để dùng tiêu chí **kết thúc sớm nhất**.

---

### Bài 2.3 — Sắp xếp theo thời điểm kết thúc và viết code

#### Mục tiêu bài

Sau Bài 2.3, em có thể chuyển ý tưởng chọn hoạt động thành code C++17, viết comparator theo thời điểm kết thúc và duyệt các hoạt động hợp lệ.

#### Từ ý tưởng đến pseudocode

```text
Đọc N hoạt động
Sắp xếp hoạt động theo thời điểm kết thúc tăng dần
answer = 0
lastFinish = thời điểm nhỏ hơn mọi thời điểm bắt đầu

Với mỗi hoạt động:
    nếu start >= lastFinish:
        chọn hoạt động
        answer tăng 1
        lastFinish = finish

In answer
```

Mỗi lần chọn, ta cập nhật `lastFinish`. Các hoạt động bắt đầu trước `lastFinish` chắc chắn giao với hoạt động vừa chọn nên bị bỏ qua.

#### Gom hai mốc thời gian bằng vector lồng nhau (`vector<vector<int>>`)

Mỗi hoạt động gồm hai thông tin đi liền nhau: thời điểm bắt đầu (`start`) và thời điểm kết thúc (`finish`). Học sinh đã quen với mảng 2 chiều; trong C++, ta lưu danh sách hoạt động dưới dạng một `vector<vector<int>>`, trong đó mỗi phần tử là một vector 2 số nguyên `{finish, start}`:

```cpp
vector<int> activity = {finish, start};
```

Khi đặt `finish` ở vị trí `0` và `start` ở vị trí `1`, hàm `sort()` mặc định của C++ sẽ **tự động sắp xếp tăng dần theo cột 0 (`finish`)**; nếu hai hoạt động có cùng thời điểm kết thúc, `sort()` sẽ tự động so sánh tiếp cột 1 (`start`).

Cách làm này hoàn toàn dựa trên kiểu dữ liệu `vector` quen thuộc, không cần học thêm cú pháp mới.

#### Code đầy đủ

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    // Lưu từng hoạt động dưới dạng vector 2 phần tử: {finish, start}
    vector<vector<int>> activities(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        int start, finish;
        cin >> start >> finish;
        activities[i] = {finish, start};
    }

    // sort() mặc định tự động sắp xếp tăng dần theo cột 0 (finish)
    sort(activities.begin(), activities.end());

    int answer = 0;
    int lastFinish = -1;

    for (int i = 0; i < n; i++) {
        int finish = activities[i][0];
        int start = activities[i][1];

        if (start >= lastFinish) {
            answer++;
            lastFinish = finish;
        }
    }

    cout << answer << '\n';
    return 0;
}
```

Với input:

```text
4
1 3
2 5
3 9
6 8
```

chương trình chọn được `2` hoạt động, chẳng hạn `[1,3]` và `[6,8]`.

#### Theo dõi biến khi debug

Với mỗi hoạt động, em có thể kiểm tra ba thông tin:

| Biến | Câu hỏi cần trả lời |
|---|---|
| `start` (`activities[i][1]`) | Hoạt động này bắt đầu lúc nào? |
| `finish` (`activities[i][0]`) | Hoạt động này kết thúc lúc nào? |
| `lastFinish` | Lựa chọn gần nhất kết thúc lúc nào? |

Nếu chương trình chọn hai hoạt động giao nhau, hãy kiểm tra điều kiện `start >= lastFinish`. Nếu số lượng thấp bất thường, hãy kiểm tra comparator có thật sự sắp xếp theo `finish` hay không.

#### Tự kiểm tra

1. Vì sao phải sắp xếp trước khi duyệt?
2. `lastFinish` được cập nhật vào lúc nào?
3. Nếu dùng `start > lastFinish` thay vì `>=`, chương trình sẽ sai ở trường hợp nào?
4. Vì sao comparator không được sắp xếp theo `start` trong bài này?
5. Với `n = 0`, chương trình in gì? Nếu đề bảo đảm `n >= 1`, điều này có ảnh hưởng không?

#### Luyện tập ngắn

- Viết lại comparator chỉ dùng tiêu chí `finish`.
- Sửa chương trình để in ra số thứ tự của các hoạt động được chọn, không chỉ in số lượng.
- Tự tạo input có hai hoạt động cùng thời điểm kết thúc và quan sát kết quả.

#### Tóm tắt bài

Code Greedy của bài chọn hoạt động có ba bước chính: **sort theo thời điểm kết thúc, kiểm tra điều kiện hợp lệ, cập nhật trạng thái**. Khi đã xác định được tiêu chí đúng, phần duyệt chỉ cần một biến `lastFinish`.

---

### Bài 2.4 — Vì sao lựa chọn kết thúc sớm là đúng?

#### Mục tiêu bài

Sau Bài 2.4, em có thể trình bày lập luận đổi chỗ và hiểu vì sao code đúng, thay vì chỉ nhớ một comparator.

#### Vì sao cần chứng minh?

Một chương trình có thể chạy đúng trên nhiều ví dụ nhưng vẫn sai ở một input khác. Với Greedy, phần khó thường không nằm ở vòng lặp mà nằm ở việc chứng minh **tiêu chí chọn là an toàn**.

Trong bài này, tiêu chí là chọn hoạt động kết thúc sớm nhất trong các hoạt động còn hợp lệ.

#### Lập luận đổi chỗ

Gọi `A` là hoạt động hợp lệ có thời điểm kết thúc sớm nhất. Giả sử có một lời giải tối ưu bắt đầu bằng hoạt động `B`.

Vì `A` kết thúc không muộn hơn `B`, ta có:

```text
finish(A) <= finish(B)
```

Nếu thay `B` bằng `A`, mọi hoạt động đứng sau `B` trong lời giải cũ vẫn bắt đầu sau hoặc đúng lúc `finish(B)`. Do `finish(A)` sớm hơn hoặc bằng `finish(B)`, các hoạt động đó cũng vẫn không giao với `A`.

Vậy ta có thể thay `B` bằng `A` mà không làm giảm số hoạt động được chọn. Điều này cho thấy tồn tại một lời giải tối ưu bắt đầu bằng hoạt động kết thúc sớm nhất.

Sau khi chọn `A`, bài toán còn lại có cùng dạng nhưng chỉ xét các hoạt động bắt đầu từ `finish(A)` trở đi. Lặp lại lập luận này cho phần còn lại, ta thu được thuật toán tham lam đúng.

#### Invariant khi duyệt

Trong lúc chương trình chạy, ta giữ **bất biến (invariant)**, tức là điều luôn đúng sau mỗi bước:

> Sau khi xử lý một đoạn đầu của danh sách đã sắp xếp, `lastFinish` là thời điểm kết thúc của hoạt động cuối cùng trong lời giải tham lam; các hoạt động đã chọn không giao nhau.

Khi gặp hoạt động mới:

- nếu `start < lastFinish`, hoạt động mới giao với lựa chọn trước nên bỏ qua;
- nếu `start >= lastFinish`, hoạt động mới hợp lệ và được chọn;
- vì danh sách đã sắp xếp theo `finish`, lựa chọn mới là hoạt động kết thúc sớm nhất trong các ứng viên đang xét.

#### Không cần thử mọi khả năng

Nếu có `N` hoạt động, thử mọi tập con có thể cần xét đến rất nhiều khả năng. Thuật toán tham lam tránh việc đó bằng cách cố định một lựa chọn an toàn ở mỗi bước. Đây là lý do Greedy thường có code ngắn, nhưng phần lập luận phải rõ.

#### Tự kiểm tra

1. Trong lập luận đổi chỗ, vì sao `finish(A) <= finish(B)` là điều quan trọng?
2. Sau khi thay `B` bằng `A`, tại sao các hoạt động phía sau vẫn hợp lệ?
3. Invariant của vòng duyệt nói điều gì?
4. Nếu chỉ cho biết code chạy đúng trên ba ví dụ, ta đã có chứng minh chưa?

#### Luyện tập ngắn

- Viết lại lập luận đổi chỗ bằng bốn câu của riêng em.
- Chỉ ra trạng thái được cập nhật sau mỗi lần chọn hoạt động.
- Vẽ một input trong đó lựa chọn đầu tiên kết thúc muộn làm số hoạt động tối đa giảm.

#### Tóm tắt bài

Greedy không đúng vì “trông có vẻ hợp lý”. Bài chọn hoạt động đúng vì ta có thể đổi lựa chọn đầu tiên của một lời giải tối ưu thành hoạt động kết thúc sớm nhất mà không làm mất các lựa chọn còn lại.

---

### Bài 2.5 — Khi nào tham lam thất bại?

#### Mục tiêu bài

Sau Bài 2.5, em có thể dùng phản ví dụ để bác bỏ một chiến lược tham lam sai và biết khi nào cần xem xét phương pháp khác.

#### Một số quy tắc dễ nhầm

Trong bài chọn hoạt động, các quy tắc sau không luôn tối ưu:

| Quy tắc | Vì sao có thể sai? |
|---|---|
| Chọn hoạt động bắt đầu sớm nhất | Có thể chọn một hoạt động kéo dài quá lâu |
| Chọn hoạt động ngắn nhất | Một hoạt động ngắn ở giữa vẫn có thể chặn hai hoạt động khác |
| Chọn hoạt động có ít xung đột nhất | Cần biết ảnh hưởng của nhiều hoạt động về sau |
| Chọn hoạt động có số thứ tự nhỏ nhất | Số thứ tự không liên quan mục tiêu |
| Chọn hoạt động kết thúc sớm nhất | Đây là tiêu chí phù hợp cho mục tiêu tối đa số hoạt động không giao nhau |

Không được dùng bảng này như một danh sách học thuộc. Hãy luôn quay lại mục tiêu và tìm phản ví dụ cho quy tắc đang định dùng.

#### Phản ví dụ cho “bắt đầu sớm nhất”

Cho các hoạt động:

```text
A = [0, 10]
B = [1, 2]
C = [2, 3]
D = [3, 4]
E = [4, 5]
```

Nếu chọn bắt đầu sớm nhất, ta chọn `A` và chỉ được `1` hoạt động. Nếu chọn kết thúc sớm nhất, ta chọn `B, C, D, E` và được `4` hoạt động.

#### Khi cần cân nhắc DP hoặc tìm kiếm

Nếu một lựa chọn hiện tại có nhiều trạng thái tương lai khác nhau và chưa thể chứng minh việc chọn sớm là an toàn, ta **chưa đủ cơ sở để dùng Greedy**. Khi đó cần phân tích thêm mục tiêu, trạng thái và các lựa chọn; có thể cân nhắc:

- **quy hoạch động**, nếu bài toán có các bài toán con lặp lại;
- **quay lui hoặc tìm kiếm**, nếu cần thử các lựa chọn trong phạm vi nhỏ;
- **sắp xếp kết hợp cấu trúc dữ liệu**, nếu quyết định phụ thuộc nhiều trạng thái đang hoạt động;
- một tiêu chí khác, nếu mục tiêu của bài đã thay đổi.

Ví dụ đổi tiền với mệnh giá `1, 3, 4` cho thấy cùng một ý tưởng “chọn đồng lớn nhất trước” có thể thất bại. Không nên lấy một Greedy đúng ở bài này áp dụng nguyên xi cho bài khác.

#### Phân biệt “tối đa số lượng” và “tối đa giá trị”

Bài chọn hoạt động tối đa **số lượng** hoạt động. Nếu mỗi hoạt động có thêm điểm thưởng và ta muốn tối đa **tổng điểm**, việc chọn kết thúc sớm nhất có thể không còn đủ. Mục tiêu mới thường đòi hỏi phân tích khác.

Thay đổi một từ trong đề — “nhiều hoạt động nhất” thành “tổng lợi ích lớn nhất” — có thể làm thay đổi hoàn toàn thuật toán.

#### Tự kiểm tra

1. Hãy dùng phản ví dụ để giải thích vì sao không chọn hoạt động bắt đầu sớm nhất.
2. “Ngắn nhất” và “kết thúc sớm nhất” có giống nhau không?
3. Nếu mỗi hoạt động có điểm thưởng, thông tin mới này có thể ảnh hưởng tiêu chí chọn như thế nào?
4. Vì sao không được kết luận “bài tối ưu nào cũng dùng Greedy”?

#### Luyện tập ngắn

- Tạo phản ví dụ cho quy tắc chọn hoạt động ngắn nhất.
- Cho một bộ mệnh giá và một số tiền, kiểm tra bằng tay xem chọn mệnh giá lớn nhất trước có tối ưu không.
- Viết hai đề bài gần giống nhau nhưng một bài tối đa số lượng, một bài tối đa tổng điểm. Nêu vì sao không nên dùng cùng một lập luận.

#### Tóm tắt bài

Một chiến lược tham lam chỉ đáng tin khi có lập luận phù hợp với mục tiêu cụ thể. **Phản ví dụ nhỏ là công cụ nhanh nhất để phát hiện một quy tắc sai.**

---

### Bài 2.6 — Ôn tập và bài chuyển giao

#### Mục tiêu bài

Bài này kiểm tra em có thể nhận dạng chiến lược tham lam, triển khai bài chọn hoạt động và tự kiểm tra tính đúng đắn hay không.

#### Tầng A — Củng cố

##### Bài 2.6.1 — Mô phỏng chọn hoạt động

Cho các khoảng thời gian. Sắp xếp chúng theo thời điểm kết thúc tăng dần, sau đó ghi lại các khoảng được chọn.

- **Input:** Năm hoạt động `[1,4]`, `[3,5]`, `[0,6]`, `[5,7]`, `[8,9]`.
- **Output:** Danh sách hoạt động được chọn và số lượng hoạt động.
- **Ví dụ:** Một đáp án tối ưu là `[1,4]`, `[5,7]`, `[8,9]`, nên số lượng là `3`.
- **Expected evidence:** Bảng sắp xếp theo `finish`, các hoạt động được chọn theo thứ tự và lý do mỗi hoạt động bị bỏ qua.

##### Bài 2.6.2 — Kiểm tra hai hoạt động

Cho hai hoạt động `[s1, f1]` và `[s2, f2]`. In `YES` nếu có thể chọn cả hai theo đúng thứ tự đã cho, tức là hoạt động thứ hai bắt đầu không sớm hơn thời điểm kết thúc của hoạt động thứ nhất; ngược lại in `NO`.

- **Input:** Một dòng gồm `s1 f1 s2 f2`, với `0 <= s1 < f1` và `0 <= s2 < f2`.
- **Output:** In `YES` hoặc `NO`.
- **Ví dụ:** `[2,5]` rồi `[5,8]` cho `YES`; `[2,5]` rồi `[4,8]` cho `NO`.
- **Expected evidence:** Dùng đúng điều kiện `s2 >= f1`, đặc biệt không loại trường hợp hai hoạt động nối tiếp tại cùng một mốc.

##### Bài 2.6.3 — Chọn hoạt động từ danh sách đã sắp xếp

Cho danh sách đã được sắp xếp theo thời điểm kết thúc. Viết vòng lặp duyệt danh sách và đếm số hoạt động được chọn.

- **Input:** `N`, sau đó là `N` cặp `start finish` đã được sắp xếp.
- **Output:** Số hoạt động không giao nhau được chọn.
- **Lưu ý:** Bài này tập trung vào điều kiện `start >= lastFinish`, chưa cần tự viết `sort`.

##### Bài 2.6.4 — Viết comparator

Viết comparator để sắp xếp các hoạt động theo `finish` tăng dần; nếu bằng nhau, sắp xếp theo `start` tăng dần.

Hãy kiểm tra comparator bằng ít nhất ba cặp hoạt động, trong đó có hai hoạt động cùng thời điểm kết thúc.

#### Tầng B — Vận dụng mẫu

##### Bài 2.6.5 — Lịch phòng học

Có `N` lớp học, mỗi lớp cần dùng một phòng trong khoảng `[start, finish]`. Chỉ có một phòng. Tìm số lớp lớn nhất có thể xếp vào phòng mà không trùng thời gian.

- **Input:** `N` và `N` cặp thời gian, với `0 <= start < finish`.
- **Output:** Số lớp lớn nhất.
- **Ví dụ:** Với `4` khoảng `[1,3]`, `[2,5]`, `[3,4]`, `[4,6]`, kết quả là `3`.

##### Bài 2.6.6 — Chọn chuyến bay

Có `N` chuyến bay sử dụng một đường băng duy nhất. Giả sử các mốc thời gian không âm và `start < finish`. Hai chuyến bay có thể nối tiếp nếu chuyến sau bắt đầu tại hoặc sau thời điểm chuyến trước kết thúc. Tìm số chuyến bay tối đa.

- **Input:** `N`, sau đó là `N` cặp `start finish`.
- **Output:** Số chuyến bay tối đa.
- **Ví dụ:** Với `[1,3]`, `[2,5]`, `[3,9]`, `[6,8]`, kết quả là `2`.

##### Bài 2.6.7 — In danh sách được chọn

Từ bài chọn hoạt động, không chỉ in số lượng mà còn in các hoạt động được chọn theo thứ tự thời gian.

- **Input:** `N` và `N` cặp `start finish`, với `0 <= start < finish`.
- **Output:** Dòng đầu là số hoạt động được chọn; dòng sau in các cặp `start finish` theo thứ tự đã chọn.
- **Yêu cầu:** Các hoạt động được in ra không giao nhau và giữ nguyên dữ liệu của từng hoạt động.
- **Expected evidence:** Có sort theo `finish`, điều kiện chọn đúng và danh sách in ra có thể kiểm tra được bằng mắt.

##### Bài 2.6.8 — Tìm phản ví dụ

Viết một input có ít nhất bốn hoạt động để chứng minh quy tắc “chọn hoạt động bắt đầu sớm nhất” không luôn cho số lượng lớn nhất.

Bài làm cần có ba phần: input, kết quả của quy tắc sai và một lời giải tốt hơn. **Expected evidence:** Em chỉ ra được số lượng của hai cách và giải thích vì sao input đó đủ để bác bỏ quy tắc sai.

#### Tầng C — Chuyển giao

##### Bài 2.6.9 — Lập lịch có điểm thưởng

Mỗi hoạt động có thêm một điểm thưởng. Mục tiêu là chọn các hoạt động không giao nhau để tổng điểm lớn nhất. Đây là **bài thảo luận có hướng dẫn**, chưa yêu cầu viết lời giải tối ưu hoàn chỉnh.

- **Dữ liệu mẫu:** `A = [1,4]` có điểm `5`, `B = [4,7]` có điểm `5`, `C = [1,7]` có điểm `12`.
- **Nhiệm vụ:** So sánh lựa chọn theo thời điểm kết thúc sớm với lựa chọn có tổng điểm lớn hơn.
- **Expected evidence:** Em chỉ ra được rằng `A + B` có tổng điểm `10`, còn `C` có điểm `12`, từ đó giải thích vì sao tiêu chí của bài chọn nhiều hoạt động không thể áp dụng nguyên xi.

##### Bài 2.6.10 — Đổi tiền và phản ví dụ

Cho các mệnh giá và số tiền cần đổi, với mục tiêu dùng **ít đồng nhất cho input đang xét**. Kiểm tra chiến lược chọn mệnh giá lớn nhất trước. Nếu chiến lược sai trên input đó, đưa ra một cách đổi tốt hơn và giải thích vì sao đây là phản ví dụ; không kết luận về mọi hệ mệnh giá từ một input duy nhất.

- **Ví dụ:** Mệnh giá `1, 3, 4`, số tiền `6`: Greedy cho `4+1+1`, nhưng đáp án tốt hơn là `3+3`.
- **Expected evidence:** Nêu rõ mục tiêu, dãy lựa chọn của Greedy, cách đổi tốt hơn và số đồng của mỗi cách.

##### Bài 2.6.11 — Chọn việc theo thời hạn

Mỗi công việc cần đúng một đơn vị thời gian và có thời hạn hoàn thành. Trong mỗi thời điểm `1, 2, .., D`, ta chỉ làm được một công việc; công việc có deadline `d` phải được thực hiện không muộn hơn thời điểm `d`. Hãy thử xây dựng chiến lược tham lam để thực hiện nhiều công việc nhất.

- **Dữ liệu mẫu:** Có năm công việc với deadline `1, 1, 2, 2, 3`.
- **Expected evidence:** Em giải thích được vì sao tối đa có thể làm `3` công việc trong ba vị trí thời gian, đồng thời nêu tiêu chí sắp xếp hoặc câu hỏi cần kiểm tra trước khi code.
- **Giới hạn:** Đây là bài mở rộng có hướng dẫn; chưa yêu cầu học thuộc một công thức mới hay triển khai priority queue.

##### Bài 2.6.12 — Nói rõ vì sao

Với mỗi mô tả, hãy trả lời `DÙNG GREEDY`, `CẦN KIỂM TRA THÊM` hoặc `KHÔNG ĐỦ THÔNG TIN`, rồi giải thích:

1. Chọn nhiều hoạt động không giao nhau nhất.
2. Đổi tiền bằng các mệnh giá `1, 3, 4`, số tiền `6`, với mục tiêu dùng ít đồng nhất.
3. Chọn dãy có tổng điểm lớn nhất nhưng các phần tử có thể xung đột.
4. Chọn các đoạn không giao nhau nhưng muốn tổng độ dài lớn nhất.
5. Chọn một số lượng lớn nhất trong một lần duyệt.

Điểm quan trọng là em phải nêu mục tiêu và lý do, không chỉ ghi tên thuật toán.

**Rubric cho Bài 2.6.12:** Mỗi câu được xem là đạt khi em nêu được mục tiêu của bài, chỉ ra tiêu chí hoặc thông tin còn thiếu, và đưa ra lý do/ phản ví dụ phù hợp. Một câu chỉ ghi tên thuật toán mà không có giải thích chưa được tính là hoàn thành.

#### Phiếu tự đánh giá

| Năng lực | Chưa chắc | Làm khi có gợi ý | Tự làm được |
|---|:---:|:---:|:---:|
| Giải thích tham lam bằng ví dụ |  |  |  |
| Phân biệt cục bộ và toàn cục |  |  |  |
| Chọn hoạt động kết thúc sớm nhất |  |  |  |
| Viết comparator theo `finish` |  |  |  |
| Duyệt và cập nhật `lastFinish` |  |  |  |
| Mô phỏng lời giải bằng tay |  |  |  |
| Viết phản ví dụ cho quy tắc sai |  |  |  |
| Trình bày lập luận đổi chỗ |  |  |  |
| Phân tích `O(N log N)` |  |  |  |
| Nhận biết khi cần kiểm tra phương pháp khác |  |  |  |

#### Tiêu chí hoàn thành chương

Em có thể xem mình đã nắm chương khi có thể trả lời rõ:

> **Tiêu chí tham lam của em là gì, vì sao lựa chọn đó an toàn, và có phản ví dụ nào làm nó thất bại không?**

Ngoài ra, em cần biên dịch được chương trình chọn hoạt động, chạy đúng ví dụ, thử ít nhất ba test tự tạo và giải thích được ý nghĩa của `lastFinish`.

#### Rubric hoàn thành chương

| Bằng chứng | Đạt khi |
|---|---|
| Mô phỏng | Chọn đúng các hoạt động hợp lệ và cập nhật đúng `lastFinish` |
| Code | Sort theo `finish`, dùng điều kiện `start >= lastFinish`, không chọn hai hoạt động giao nhau |
| Chứng minh | Nêu được ý nghĩa của `finish(A) <= finish(B)` trong lập luận đổi chỗ |
| Phản ví dụ | Tạo được input làm một tiêu chí sai cho kết quả kém hơn |
| Phân tích | Tách được chi phí sort `O(N log N)` và duyệt `O(N)` |
| Chuyển giao | Nhận ra khi mục tiêu đổi từ số lượng sang tổng giá trị thì cần phân tích lại |

---

### Tổng kết chương

> **Tham lam không phải là chọn tùy ý phương án tốt nhất trước mắt. Tham lam là chọn từng bước theo một tiêu chí có thể bảo vệ bằng lập luận.**

| Cần nhớ | Nội dung |
|---|---|
| Khái niệm | Xây dựng lời giải bằng lựa chọn cục bộ từng bước |
| Bài mẫu | Chọn nhiều hoạt động không giao nhau nhất |
| Tiêu chí | Sắp xếp theo thời điểm kết thúc tăng dần |
| Trạng thái | `lastFinish` của hoạt động gần nhất đã chọn |
| Điều kiện chọn | `start >= lastFinish` |
| Chứng minh | Lập luận đổi chỗ: kết thúc sớm không làm mất phần còn lại |
| Phản ví dụ | Dùng để bác bỏ quy tắc tham lam không đúng |
| Cẩn thận | “Lớn nhất”, “nhỏ nhất”, “ngắn nhất” chưa đủ để kết luận |
| Độ phức tạp | `O(N log N)` do sắp xếp và `O(N)` do duyệt |
| Câu hỏi chính | Chọn gì, vì sao an toàn, và khi nào thất bại? |

#### Những lỗi thường gặp

| Lỗi | Cách tự kiểm tra |
|---|---|
| Sắp xếp theo thời điểm bắt đầu | Nhắc lại mục tiêu là tối đa số hoạt động |
| Dùng `>` thay cho `>=` | Kiểm tra hai hoạt động nối tiếp tại cùng một thời điểm |
| Quên cập nhật `lastFinish` | Theo dõi trạng thái sau mỗi lần chọn |
| Comparator không theo `finish` | In danh sách sau sort để kiểm tra |
| Tin rằng mọi bài tối ưu đều tham lam | Tìm phản ví dụ nhỏ |
| Chỉ code mà không chứng minh | Viết lập luận đổi chỗ bằng lời |
| Quên hoạt động cuối danh sách | Kiểm tra vòng lặp chạy đến `n - 1` |
| Nhầm số lượng với tổng giá trị | Đọc kỹ mục tiêu trong đề |

#### Code tham chiếu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    // Lưu từng hoạt động dưới dạng vector 2 phần tử: {finish, start}
    vector<vector<int>> activities(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        int start, finish;
        cin >> start >> finish;
        activities[i] = {finish, start};
    }

    // sort() mặc định tự động sắp xếp tăng dần theo cột 0 (finish)
    sort(activities.begin(), activities.end());

    int answer = 0;
    int lastFinish = -1;

    for (int i = 0; i < n; i++) {
        int finish = activities[i][0];
        int start = activities[i][1];

        if (start >= lastFinish) {
            answer++;
            lastFinish = finish;
        }
    }

    cout << answer << '\n';
    return 0;
}
```

Với input:

```text
4
1 3
2 5
3 9
6 8
```

output là:

```text
2
```

---

## Ghi chú mở rộng cho giáo viên

Các chủ đề như lập lịch công việc có thời hạn, ba lô phân số, Kruskal hoặc chia tải bằng hàng đợi ưu tiên đều có thể dùng Greedy, nhưng không nên đưa tất cả vào bài đầu tiên. Trước hết, học sinh cần nắm vững bốn năng lực: nhận ra mục tiêu tối ưu, viết tiêu chí lựa chọn, mô phỏng trạng thái và bảo vệ lựa chọn bằng lập luận hoặc kiểm tra phản ví dụ.

## Ma trận alignment nội bộ

| Outcome | Evidence chính | Tiêu chí đạt |
|---|---|---|
| ,  — Giải thích Greedy và phân biệt cục bộ/toàn cục | Bài 2.1, Bài 2.6.12 | Nêu được mục tiêu, lựa chọn và lý do không chọn tùy tiện |
| ,  — Nhận biết interval scheduling và mô phỏng trạng thái | Bài 2.2, Bài 2.6.1, 2.6.5, 2.6.6 | Mô hình hóa đúng khoảng, điều kiện nối tiếp và `lastFinish` |
|  — Viết lời giải chọn hoạt động | Bài 2.3, Bài 2.6.3–2.6.7 | Sort theo `finish`, kiểm tra `start >= lastFinish`, cập nhật trạng thái |
| ,  — Giải thích tính đúng đắn và phần bài toán còn lại | Bài 2.4, rubric chương | Trình bày được lập luận đổi chỗ và bất biến (invariant) |
|  — Tìm giới hạn/phản ví dụ | Bài 2.1, Bài 2.5, Bài 2.6.8–2.6.10 | Tạo hoặc phân tích được phản ví dụ có mục tiêu rõ |
|  — Phân tích độ phức tạp | Bài 2.3, rubric chương | Tách được chi phí sort và chi phí duyệt |
|  — Chuyển giao sang bài biến thể | Bài 2.6.9–2.6.12 | Nhận ra khi mục tiêu/điều kiện đổi thì tiêu chí Greedy phải được kiểm tra lại |

Ma trận này là ghi chú biên soạn, không đồng bộ vào bản in học sinh.
