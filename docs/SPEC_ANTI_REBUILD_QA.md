# SCRATCH BẢNG A — REBUILD & CONTENT QA/FIX

## ROLE

Bạn đang làm việc trực tiếp trên repository iKHEdu Book.

Nhiệm vụ của bạn là **QA + rebuild/fix nội dung Scratch Bảng A**, không phải thiết kế lại khóa học từ đầu.

Repository:

`hoaihoai48/iKHEdu-Book`

Phạm vi chính:

`courses/scratch-bang-a/`

---

# 1. MỤC TIÊU

Review và sửa toàn bộ pipeline:

```text
Lesson Content
      ↓
Quiz
      ↓
Problems
      ↓
Images / rendered blocks
      ↓
Lesson ↔ Problem ↔ Quiz consistency
```

Mục tiêu cuối cùng:

> Scratch Bảng A – 16 lesson phải có nội dung đúng, quiz đúng, problem đúng scope, hình minh họa đúng và tất cả các thành phần phải nhất quán với nhau.

Không được chỉ sửa lỗi Markdown/path.

Phải kiểm tra **tính đúng đắn về mặt sư phạm và thuật toán**.

---

# 2. NGUYÊN TẮC QUAN TRỌNG

## KHÔNG được tự ý:

- đổi số lượng lesson
- đổi chapter structure
- đổi lesson order
- xóa hàng loạt problems
- viết lại toàn bộ curriculum
- thêm kiến thức ngoài scope Scratch Bảng A
- chuyển bài sang lesson khác chỉ vì cảm thấy “hay hơn”
- tăng số quiz chỉ để đạt một con số metadata cũ
- thêm hình chỉ để tăng số lượng hình
- thay đổi ID `sca_*`
- đổi tên problem nếu không cần thiết
- phá mapping hiện tại giữa lesson ↔ problem
- sửa source Python gốc.

Architecture hiện tại là baseline.

Nếu một problem hơi advanced nhưng vẫn có thể giữ:

```text
CORE
EXTENSION
CHALLENGE
```

hãy ưu tiên **phân tầng** thay vì xóa.

Chỉ MOVE/EXCLUDE khi thật sự không phù hợp.

---

# 3. SOURCE OF TRUTH

Trước khi sửa, phải đọc:

```text
courses/scratch-bang-a/
```

và xác định:

### Lesson

```text
lessons/*/LessonXX_Production_Content.md
```

### Lesson problems

```text
lessons/*/Bai_Tap.md
```

### Problem packages

```text
problems/sca_*/
```

Mỗi problem package hiện được kỳ vọng có:

```text
De_Bai.md
Huong_Dan_Giang_Day.md
solution_blocks_vi.png
solution_blocks_vi.svg
```

### Assets

```text
assets/
assets/rendered_blocks/
```

---

# 4. PHẢI AUDIT TRƯỚC KHI SỬA

Tạo một QA matrix nội bộ cho toàn bộ 16 lesson.

Mỗi lesson phải kiểm:

```text
Lesson
├── Concept/content
├── Examples
├── Dry-run
├── Images
├── Quiz
├── Problems
└── Scope progression
```

Mỗi problem phải kiểm:

```text
Problem
├── Lesson alignment
├── Algorithm correctness
├── Scratch feasibility
├── Difficulty
├── Problem statement
├── Teaching guide
├── Solution image
└── P-level / CORE-EXTENSION-CHALLENGE
```

Mỗi quiz phải kiểm:

```text
Quiz
├── Question correctness
├── Correct answer
├── Distractors
├── Lesson alignment
├── Difficulty
├── Duplicate/redundancy
├── Visual opportunity
└── Image reference if applicable
```

---

# 5. CÁC LỖI ĐÃ XÁC NHẬN — PHẢI FIX

## P0 — L02 geometry

Kiểm tra và sửa logic vẽ đường tròn/cung tròn.

Đặc biệt kiểm tra đoạn:

```text
đi R bước
→ xoay
→ vẽ
→ quay về tâm
```

Không được dùng:

```text
di chuyển (-R)
```

nếu hướng hiện tại khiến thao tác đó đi sai hướng.

Phải đảm bảo:

```text
position
+
direction
+
rotation
+
movement
```

nhất quán.

Kiểm tra lại tất cả:

- explanation
- example
- dry-run
- image
- quiz
- related Pen problems.

Đặc biệt kiểm tra Quiz L02 về thao tác quay về tâm.

---

# 6. P0 — L15 DRY RUN

Có một lỗi đã xác nhận.

Lesson 15 có ví dụ:

```text
SCRATCH
L = 2
R = 4
```

Với indexing:

```text
1 S
2 C
3 R
4 A
5 T
6 C
7 H
```

kết quả phải là:

```text
CRA
```

Không phải:

```text
YTH
```

Sửa:

- dry-run table
- explanation
- related image nếu image chứa kết quả sai
- quiz nếu có liên quan
- problem/example nếu copy cùng logic.

Sau khi sửa phải grep toàn repo để tìm các phiên bản sai tương tự.

---

# 7. P0 — PROBLEM ALIGNMENT

Không được chỉ kiểm tra problem tồn tại.

Phải kiểm tra:

> Problem này có thật sự sử dụng kiến thức mà lesson đã dạy không?

Ví dụ đã phát hiện:

### L04

Lesson chủ yếu dạy:

```text
+
-
*
/
expression
formula
operator
```

Nhưng một số problem đang dùng:

```text
mod
integer division
digit extraction
reverse number
power
```

Trong đó một số kiến thức thuộc L05/L10.

Không nhất thiết xóa.

Phải phân loại:

```text
CORE
EXTENSION
CHALLENGE
```

Nếu problem thực sự yêu cầu kiến thức chưa được dạy và không thể coi là extension hợp lý:

```text
MOVE_TO_LATER
```

Nhưng **không được tự ý thay đổi ID**.

---

# 8. P1 — L03

Review lại Lesson 03.

Mục tiêu:

```text
input
→ variable
→ process
→ output
```

Không nên giải thích Scratch bằng cách phụ thuộc vào:

```text
RAM
CPU
memory address
```

hoặc wording kỹ thuật không cần thiết cho học sinh.

Nếu nói về kiểu dữ liệu, phải đảm bảo nội dung thực sự dạy điều đó.

Không được gọi lesson là “kiểu dữ liệu” rồi chỉ nói về variable/input/output.

---

# 9. P1 — L07

Tên hiện tại:

```text
Vòng lặp for và hàm range
```

Scratch không có native:

```text
for
range()
```

Không được khiến học sinh hiểu Scratch có `range()`.

Có thể giữ liên hệ Python nhưng phải diễn đạt rõ:

```text
Python:
for i in range(...)


Scratch:
repeat (...) + biến đếm
```

Nếu cần, đổi title thành hướng:

```text
Vòng lặp biết trước số lần và biến đếm
```

hoặc tương đương.

Phần liên hệ Python vẫn có thể giữ.

---

# 10. P1 — L08 / Collatz

Không được trình bày Collatz như một định lý đã được chứng minh.

Không viết theo cách ngầm khẳng định:

```text
mọi số nguyên dương đều chắc chắn về 1
```

Nên framing là:

```text
mô phỏng dãy Collatz
```

hoặc:

```text
với ví dụ được cho, ta quan sát quá trình...
```

Nếu Collatz là extension/challenge thì thể hiện rõ.

Không cần xóa chỉ vì advanced.

---

# 11. P1 — L11/L12/L14/L15/L16

Review problem scope.

Các problem nâng cao có thể giữ, nhưng phải phân tầng.

Ví dụ:

```text
CORE
EXTENSION
CHALLENGE
```

Những bài như:

```text
GCD/LCM
super prime
prime factorization
merge sorted arrays
greedy
longest palindromic substring
Caesar cipher
anagram
Run Length Encoding
word frequency
```

không nên mặc nhiên được xem là CORE nếu lesson chưa xây dựng đầy đủ kiến thức cho chúng.

Không xóa tự động.

---

# 12. P1 — L16 STRING

Review toàn bộ Lesson 16.

Mục tiêu chính phải vẫn là:

```text
duyệt chuỗi
→ đọc từng ký tự
→ kiểm tra ký tự
→ đếm
→ biến đổi
→ tách dữ liệu
```

Không để lesson trở thành một “String Algorithms advanced course”.

Đặc biệt review:

```text
uppercase/lowercase
ASCII
Caesar
RLE
anagram
word frequency
```

Mỗi nội dung phải được phân loại:

```text
CORE
EXTENSION
CHALLENGE
```

Nếu cần prerequisite chưa tồn tại trong lesson thì phải ghi rõ.

---

# 13. CASE-SENSITIVE STRING

Review các bài như:

```text
đếm chữ thường
đếm chữ hoa
phân biệt A/a
```

Scratch comparison có hạn chế về hoa/thường.

Không được đưa ra giải pháp mơ hồ.

Nếu dùng:

```text
costume name
ASCII / Unicode-like mapping
```

thì phải giải thích chính xác cơ chế Scratch thực sự có thể làm được.

Không được giả định Scratch có native:

```text
isUpper()
isLower()
ASCII()
```

nếu không có block tương ứng.

Nếu solution hiện tại quá phức tạp so với Bảng A:

```text
CHALLENGE
```

hoặc điều chỉnh.

---

# 14. QUIZ QA

Không chỉ kiểm số lượng.

Mỗi lesson hiện có khoảng 10 quiz.

Giữ nguyên khoảng này trừ khi có lý do nội dung rõ ràng.

Không thêm quiz chỉ để khớp README cũ.

Mỗi quiz phải kiểm:

### Correctness

- đáp án đúng?
- calculation đúng?
- Scratch block đúng?
- dry-run đúng?

### Distractors

Đáp án sai phải là lỗi học sinh thực sự có thể mắc.

Không tạo distractor vô lý.

### Variety

Ưu tiên phối hợp:

```text
Concept
Block recognition
Dry-run
Output prediction
Bug finding
Algorithm choice
Visual reasoning
```

Không để cả 10 câu chỉ là:

```text
“X là gì?”
```

---

# 15. QUIZ IMAGE

Trong:

```text
assets/rendered_blocks/
```

đã có nhiều asset dạng:

```text
quiz_lXX_qYY.png
quiz_lXX_qYY.svg
```

Phải kiểm tra từng lesson:

```text
ảnh nào đã tồn tại
ảnh nào thực sự được quiz sử dụng
ảnh nào có thể sử dụng tốt
ảnh nào render sai / outdated
```

Không bắt buộc đưa toàn bộ ảnh vào quiz.

Chỉ dùng ảnh khi:

> hình ảnh giúp câu hỏi tốt hơn text.

Mục tiêu khoảng:

```text
3–5 visual quiz / lesson
```

chỉ là guideline, không phải quota bắt buộc.

---

# 16. IMAGE QA

Không được đánh giá hình theo số lượng đơn thuần.

Mỗi image phải trả lời:

> “Hình này giúp học sinh hiểu điều gì?”

Phân loại:

```text
CONCEPT
BLOCK
RESULT
DRY_RUN
BUG
QUIZ
EXAMPLE
```

Kiểm:

```text
block đúng?
text đúng?
result đúng?
direction đúng?
number đúng?
variable đúng?
label đúng?
```

Đặc biệt các hình geometry phải kiểm tra:

```text
position
direction
rotation
movement
```

Các hình algorithm phải kiểm tra:

```text
input
state
iteration
output
```

---

# 17. IMAGE PATH

Fix toàn bộ relative paths bị sai.

Từ lesson:

```text
lessons/lesson-XX-.../
```

asset chung phải reference đúng relative path:

```text
../../assets/...
```

Không sửa path bằng cách copy duplicate assets vào từng lesson.

Sau khi sửa:

- grep toàn bộ Markdown
- kiểm tra tất cả image references
- không còn broken relative links.

---

# 18. PROBLEM PACKAGE

Không phá cấu trúc hiện tại:

```text
De_Bai.md
Huong_Dan_Giang_Day.md
solution_blocks_vi.png
solution_blocks_vi.svg
```

Tất cả problem phải tiếp tục có đủ các file.

Nếu sửa problem statement:

phải kiểm tra đồng thời:

```text
De_Bai.md
Huong_Dan_Giang_Day.md
solution image
solution SVG
lesson reference
```

Không được để:

```text
statement ≠ solution
```

---

# 19. P-LEVEL / DIFFICULTY

L01 và L02 hiện có mismatch giữa heading và detail.

Không được đoán.

Trước khi sửa:

1. tìm definition/spec về P-level trong repo
2. xác định field nào là canonical
3. áp dụng một nguồn duy nhất.

Sau đó kiểm tra:

```text
heading
detail
problem metadata
lesson listing
```

phải nhất quán.

---

# 20. KHÔNG REBUILD MÙ

Trước khi sửa một problem, phải xác định:

```text
lesson concept
problem requirement
required blocks
required algorithm
difficulty
```

Nếu problem yêu cầu kiến thức chưa học:

```text
CORE → không phù hợp
EXTENSION → có thể giữ
CHALLENGE → có thể giữ
MOVE_TO_LATER → xem xét
```

Không được xóa hàng loạt problem chỉ vì problem khó.

---

# 21. VALIDATION SAU KHI SỬA

Bắt buộc chạy các kiểm tra:

## Lesson

```text
16 lesson tồn tại
16 Production_Content.md tồn tại
16 Bai_Tap.md tồn tại
```

## Problems

```text
324 problem hiện tại
không mất problem ngoài chủ ý
mọi sca_* reference đều resolve
```

## Package

```text
324/324 De_Bai.md
324/324 Huong_Dan_Giang_Day.md
324/324 solution_blocks_vi.png
324/324 solution_blocks_vi.svg
```

## Quiz

```text
quiz count chính xác theo source
không tự thêm quiz chỉ để đạt metadata cũ
```

## Images

```text
không còn broken relative image paths
```

## Content consistency

Search toàn repo cho các lỗi đã biết:

```text
YTH
di chuyển (-R)
for/range
RAM
Collatz
```

và các biến thể tương tự.

---

# 22. README / METADATA

Sau khi source đã ổn định mới cập nhật README.

Không lấy README làm source of truth.

README phải phản ánh source thực tế:

```text
324 problems
37 Pen
287 Algorithm
160 quizzes
```

và phân bổ L01/L02 thực tế:

```text
L01 = 16
L02 = 21
```

Không dùng số liệu cũ:

```text
308
190
22/15
21 Pen
```

---

# 23. KHÔNG TĂNG SỐ LƯỢNG HÌNH MÁY MÓC

Không có requirement:

```text
Lesson nào ít hình thì phải thêm X hình.
```

Thay vào đó:

Nếu một concept khó hiểu bằng text:

```text
→ thêm visual
```

Nếu concept đơn giản:

```text
→ không cần thêm visual
```

Ưu tiên:

```text
L04
L05
L06
L09
L10
L11
L12
L14
L16
```

nhưng chỉ thêm khi có giá trị sư phạm thực sự.

---

# 24. OUTPUT REPORT

Sau khi hoàn thành, tạo:

```text
courses/scratch-bang-a/SCRATCH_CONTENT_QA_REPORT.md
```

Report phải có:

## A. Summary

```text
Lessons reviewed: 16
Problems reviewed: 324
Quizzes reviewed: 160
Images reviewed: ...
```

## B. Fixed issues

Table:

```text
ID | Lesson | Type | Problem/Quiz/Image | Before | After
```

## C. Problems reclassified

```text
Problem
Old classification
New classification
Reason
```

## D. Quiz changes

```text
Lesson
Quiz
Issue
Fix
```

## E. Image changes

```text
Lesson
Image
Issue
Fix
```

## F. Remaining issues

Chỉ ghi những thứ thực sự chưa thể giải quyết.

---

# 25. GIT

Sau khi QA hoàn tất:

1. kiểm tra git diff
2. đảm bảo không có file ngoài scope bị thay đổi
3. kiểm tra không accidentally regenerate hàng loạt binary không cần thiết
4. commit thành một commit rõ ràng.

Commit message:

```text
fix(scratch): rebuild content quiz problems and visuals
```

Push lên branch hiện tại.

---

# 26. QUAN TRỌNG — KHÔNG ĐƯỢC “SÁNG TẠO LẠI CURRICULUM”

Đây là yêu cầu quan trọng nhất.

Bạn đang sửa một curriculum đã được thiết kế.

Không được biến task thành:

```text
design a new Scratch course
```

Task là:

```text
audit
→ fix factual errors
→ fix pedagogical inconsistencies
→ fix lesson/problem alignment
→ improve quiz
→ fix visual representation
→ validate
```

Architecture 16 lesson hiện tại là baseline.

---

# 27. DEFINITION OF DONE

Task chỉ được coi là hoàn thành khi:

```text
[ ] 16 lessons reviewed
[ ] lesson content reviewed
[ ] dry-runs verified
[ ] quiz questions verified
[ ] quiz answers verified
[ ] problem alignment verified
[ ] difficulty classification reviewed
[ ] image correctness verified
[ ] image paths fixed
[ ] L02 geometry verified
[ ] L15 SCRATCH example fixed
[ ] L16 string scope reviewed
[ ] L07 range wording reviewed
[ ] L08 Collatz wording reviewed
[ ] L03 wording reviewed
[ ] README synced
[ ] no broken image links
[ ] no broken problem references
[ ] no accidental problem deletion
[ ] QA report generated
[ ] git diff reviewed
[ ] commit created
[ ] pushed to remote
```

Sau khi hoàn thành, hãy trả về:

```text
1. Commit hash
2. Tổng số file changed
3. Tổng số lesson changed
4. Tổng số problem changed
5. Tổng số quiz changed
6. Tổng số image changed
7. Các issue P0/P1 đã fix
8. Các issue còn lại
9. Link đến QA report
```

Không chỉ nói:

> “Done.”

Phải báo cáo cụ thể những gì đã thực sự thay đổi.
