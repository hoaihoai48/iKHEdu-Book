const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

// 1. Khởi tạo headless DOM với scratchblocks
const dom = new JSDOM('<!DOCTYPE html><html><head></head><body></body></html>', { runScripts: 'dangerously' });
const scriptEl = dom.window.document.createElement('script');
scriptEl.textContent = fs.readFileSync(path.join(__dirname, '../node_modules/scratchblocks/build/scratchblocks.min.js'), 'utf8');
dom.window.document.body.appendChild(scriptEl);
const scratchblocks = dom.window.scratchblocks;

scratchblocks.appendStyles(dom.window.document, 'scratch3');
const styleTags = dom.window.document.querySelectorAll('style');
let allCss = '';
styleTags.forEach(s => allCss += s.textContent + '\n');

function renderToSvgAndPng(sbScript, outSvgPath, outPngPath) {
  const doc = scratchblocks.parse(sbScript, { languages: ['en'] });
  const svg = scratchblocks.render(doc, { style: 'scratch3' });
  const defs = svg.querySelector('defs') || svg.insertBefore(dom.window.document.createElementNS('http://www.w3.org/2000/svg', 'defs'), svg.firstChild);
  const svgStyle = dom.window.document.createElementNS('http://www.w3.org/2000/svg', 'style');
  svgStyle.textContent = allCss;
  defs.appendChild(svgStyle);

  fs.writeFileSync(outSvgPath, svg.outerHTML, 'utf8');
  execSync(`rsvg-convert -z 2.5 -f png "${outSvgPath}" -o "${outPngPath}"`);
}

// 2. Danh mục 24 sơ đồ lý thuyết cho toàn bộ 16 bài học (Lesson 01 - 16)
const LESSON_THEORY_SCRIPTS = {
  // === Bài 01: Vẽ hình Pen & Repeat ===
  "l01_block_goto_vi": `
đi tới điểm x: (0) y: (0) :: motion
`,
  "l01_block_point_vi": `
đặt hướng bằng (90) :: motion
`,
  "l01_setup_pen_vi": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (90) :: motion
chọn màu vẽ [#0055ff] :: pen
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
`,
  "l01_hinh_vuong_vi": `
lặp lại (4) lần {
  di chuyển (100) bước :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
  "l01_tam_giac_deu_vi": `
lặp lại (3) lần {
  di chuyển (100) bước :: motion
  xoay phải @turnRight (120) độ :: motion
} :: control
`,
  "l01_luc_giac_deu_vi": `
lặp lại (6) lần {
  di chuyển (80) bước :: motion
  xoay phải @turnRight (60) độ :: motion
} :: control
`,
  "l01_myblock_dinh_nghia_vi": `
định nghĩa ve_hinh_vuong :: custom hat
lặp lại (4) lần {
  di chuyển (100) bước :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
  "l01_myblock_goi_vi": `
ve_hinh_vuong :: custom
`,

  // === Bài 02: Hình tròn & Cung tròn ===
  "l02_circle_360_vi": `
lặp lại (360) lần {
  di chuyển (1) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
`,
  "l02_cung_tron_vi": `
định nghĩa ve_cung_tron (goc) (buoc) :: custom hat
lặp lại (goc) lần {
  di chuyển (buoc) bước :: motion
  xoay phải @turnRight (1) độ :: motion
} :: control
`,
  "l02_canh_hoa_vi": `
định nghĩa ve_canh_hoa (buoc) :: custom hat
lặp lại (2) lần {
  ve_cung_tron (90) (buoc) :: custom
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
  "l02_bong_hoa_8_canh_vi": `
lặp lại (8) lần {
  ve_canh_hoa (1) :: custom
  xoay phải @turnRight (45) độ :: motion
} :: control
`,

  // === Bài 03: Nhập xuất & Biến số ===
  "l03_block_ask_vi": `
hỏi [Nhập số A:] và đợi :: sensing
`,
  "l03_block_set_vi": `
đặt [A v] thành (câu trả lời :: sensing) :: variables
`,
  "l03_block_say_join_vi": `
nói (kết hợp [Tổng là: ] (tong :: variables) :: operators) :: looks
`,
  "l03_block_swap_vi": `
đặt [tam v] thành (a :: variables) :: variables
đặt [a v] thành (b :: variables) :: variables
đặt [b v] thành (tam :: variables) :: variables
`,

  // === Bài 04: Toán tử & Biểu thức ===
  "l04_operators_vi": `
đặt [chu_vi v] thành (((dai :: variables) + (rong :: variables) :: operators) * (2) :: operators) :: variables
đặt [dien_tich v] thành ((dai :: variables) * (rong :: variables) :: operators) :: variables
đặt [hieu v] thành ((dai :: variables) - (rong :: variables) :: operators) :: variables
đặt [thuong v] thành ((dai :: variables) / (rong :: variables) :: operators) :: variables
`,

  // === Bài 05: Chia nguyên & Chia dư ===
  "l05_div_mod_vi": `
đặt [chia_du v] thành ((a :: variables) mod (b :: variables) :: operators) :: variables
đặt [chia_nguyen v] thành ([làm tròn xuống v] của ((a :: variables) / (b :: variables) :: operators) :: operators) :: variables
đặt [luy_thua v] thành ((kq :: variables) * (a :: variables) :: operators) :: variables
`,

  // === Bài 06: Cấu trúc rẽ nhánh ===
  "l06_branching_vi": `
nếu <(diem :: variables) > (5)> thì {
  nói [Đỗ rồi!] :: looks
} :: control
nếu <((n :: variables) mod (2) :: operators) = (0)> thì {
  nói [Số chẵn] :: looks
} nếu không thì {
  nói [Số lẻ] :: looks
} :: control
`,

  // === Bài 07: Vòng lặp đếm lần (i) ===
  "l07_repeat_counter_vi": `
đặt [i v] thành (1) :: variables
lặp lại (10) lần {
  thay đổi [tong v] một lượng (i :: variables) :: variables
  thay đổi [i v] một lượng (1) :: variables
} :: control
`,

  // === Bài 08: Vòng lặp cho đến khi ===
  "l08_repeat_until_vi": `
lặp lại cho đến khi <(so :: variables) = (0)> {
  thay đổi [dem v] một lượng (1) :: variables
  đặt [so v] thành ([làm tròn xuống v] của ((so :: variables) / (10) :: operators) :: operators) :: variables
} :: control
`,

  // === Bài 10: Tách chữ số ===
  "l10_digit_extraction_vi": `
đặt [chu_so v] thành ((N :: variables) mod (10) :: operators) :: variables
đặt [N v] thành ([làm tròn xuống v] của ((N :: variables) / (10) :: operators) :: operators) :: variables
`,

  // === Bài 13: Danh sách (List) ===
  "l13_list_operations_vi": `
thêm (câu trả lời :: sensing) vào [Dãy số v] :: list
xóa tất cả của [Dãy số v] :: list
đặt [x v] thành (phần tử (i :: variables) của [Dãy số v] :: list) :: variables
nói (kích thước của [Dãy số v] :: list) :: looks
`,

  // === Bài 15: Chuỗi ký tự (String) ===
  "l15_string_operations_vi": `
đặt [ky_tu v] thành (ký tự (i :: variables) của (chuỗi :: variables) :: operators) :: variables
đặt [dai v] thành (độ dài của (chuỗi :: variables) :: operators) :: operators
nói (kết hợp (tu_1 :: variables) (tu_2 :: variables) :: operators) :: looks
`,

  // === Pen Problem Sample References ===
  "sca_pen_p00_solution_vi": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (90) :: motion
chọn màu vẽ [#ff0000] :: pen
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
lặp lại (4) lần {
  di chuyển (50) bước :: motion
  di chuyển (-50) bước :: motion
  xoay phải @turnRight (90) độ :: motion
} :: control
`,
  "sca_pen_p01_tam_giac_vi": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (-50) y: (-30) :: motion
đặt hướng bằng (90) :: motion
chọn màu vẽ [#ff0000] :: pen
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
lặp lại (3) lần {
  di chuyển (100) bước :: motion
  xoay phải @turnRight (120) độ :: motion
} :: control
`
};

// 3. Tiến hành render toàn bộ danh mục sang assets/rendered_blocks/
const outDir = path.join(__dirname, '../assets/rendered_blocks');
let count = 0;

for (const [name, script] of Object.entries(LESSON_THEORY_SCRIPTS)) {
  const outSvg = path.join(outDir, `${name}.svg`);
  const outPng = path.join(outDir, `${name}.png`);
  try {
    renderToSvgAndPng(script.trim(), outSvg, outPng);
    console.log(`[OK] Re-rendered ${name}`);
    count++;
  } catch (err) {
    console.error(`[ERROR] ${name}:`, err.message);
  }
}

console.log(`\nHoàn tất re-render 100% (${count}/${Object.keys(LESSON_THEORY_SCRIPTS).length}) hình ảnh khối Scratch lý thuyết chuẩn Scratch 3.0!`);
