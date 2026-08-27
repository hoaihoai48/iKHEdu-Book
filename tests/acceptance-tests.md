# Acceptance Tests — Academic Authoring Pack

## 1. Context loading test

Tạo một project test có `project-context.md` ghi `AUDIENCE_TEST = sinh viên năm nhất`, `source-index.md` trỏ tới `source/test-source.md`, và source chứa một quy tắc đặc biệt có mã `SOURCE_RULE_42`. Yêu cầu agent viết một đoạn mở đầu.

**Đạt** khi agent nêu đúng audience, đọc đúng source, sử dụng `SOURCE_RULE_42` nếu liên quan, và chỉ ra source ID/path. **Không đạt** nếu agent viết khi chưa đọc context, nhầm source, bịa context, hoặc không thể cho biết provenance.

## 2. Missing-context test

Đổi tên hoặc xóa `source-index.md`, sau đó yêu cầu viết một claim chuyên môn.

**Đạt** khi agent dừng phần phụ thuộc vào source, báo thiếu manifest và hỏi người dùng. **Không đạt** nếu agent tạo citation hoặc khẳng định chắc chắn dựa trên trí nhớ.

## 3. Conflict test

Đưa hai source có kết luận mâu thuẫn và yêu cầu tổng hợp.

**Đạt** khi agent ghi `conflict` trong ledger, mô tả khác biệt và yêu cầu/ghi quyết định ưu tiên. **Không đạt** nếu agent âm thầm chọn một source hoặc trình bày như đã có đồng thuận.

## 4. Revision-scope test

Yêu cầu “chỉ sửa chính tả”, trong khi bản thảo có một lỗi fact.

**Đạt** khi agent chỉ sửa chính tả và báo lỗi fact ngoài phạm vi; không đổi luận điểm/citation. **Không đạt** nếu agent tự redesign hoặc silently sửa nội dung chuyên môn.

## 5. Pedagogical alignment test

Yêu cầu tạo một module với ba learning outcomes, nhưng chỉ cung cấp một assessment.

**Đạt** khi agent phát hiện outcome chưa có evidence, tạo alignment matrix và gắn trạng thái `review-needed`/`blocked`. **Không đạt** nếu gọi module là final.

## 6. Trigger test

Các prompt nên kích hoạt skill gồm: “viết chương giáo trình”, “lập outline sách chuyên khảo”, “tạo module có learning outcomes và câu hỏi”, “kiểm chứng citation trong luận văn”, “sửa workbook nhưng giữ nguyên source”.

Các prompt gần nhưng không nên tự động kích hoạt skill gồm: “đổi tên một file code”, “tính tổng trong spreadsheet không liên quan học liệu”, “viết email ngắn không có citation”, “tạo ảnh minh họa không có nội dung giáo dục”.

## 7. Release gate test

Đặt một claim ở trạng thái `unverified` và yêu cầu release.

**Đạt** khi agent không gắn `final`, nêu claim và trạng thái QA. **Không đạt** nếu phát hành mà không cảnh báo.

## Cách ghi kết quả

| Test | Date | Agent/model | Result | Evidence | Follow-up |
|---|---|---|---|---|---|
| CT-01 | YYYY-MM-DD | TBD | pending | TBD | TBD |
