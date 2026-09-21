const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

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

const APPENDIX_BLOCKS = {
  "phu_luc_a_setup_pen": `
khi bấm vào @greenFlag :: events hat
xóa tất cả :: pen
nhấc bút :: pen
đi tới điểm x: (0) y: (0) :: motion
đặt hướng bằng (90) :: motion
chọn màu vẽ [#0055ff] :: pen
đặt kích thước bút vẽ bằng (3) :: pen
đặt bút :: pen
`,
  "phu_luc_a_tach_chu_so": `
đặt [tong v] thành (0) :: variables
lặp lại cho đến khi <(N :: variables) = (0)> {
  đặt [chu_so v] thành ((N :: variables) mod (10) :: operators) :: variables
  thay đổi [tong v] một lượng (chu_so :: variables) :: variables
  đặt [N v] thành ([làm tròn xuống v] của ((N :: variables) / (10) :: operators) :: operators) :: variables
} :: control
nói (tong :: variables) :: looks
`,
  "phu_luc_a_so_nguyen_to": `
đặt [la_nguyen_to v] thành (1) :: variables
nếu <(N :: variables) < (2)> thì {
  đặt [la_nguyen_to v] thành (0) :: variables
} nếu không thì {
  đặt [i v] thành (2) :: variables
  lặp lại cho đến khi <<((i :: variables) * (i :: variables) :: operators) > (N :: variables)> hoặc <(la_nguyen_to :: variables) = (0)>> {
    nếu <((N :: variables) mod (i :: variables) :: operators) = (0)> thì {
      đặt [la_nguyen_to v] thành (0) :: variables
    } :: control
    thay đổi [i v] một lượng (1) :: variables
  } :: control
} :: control
`,
  "phu_luc_a_max_list": `
đặt [max_val v] thành (phần tử (1) của [danh_sach v] :: list) :: variables
đặt [i v] thành (2) :: variables
lặp lại ((kích thước của [danh_sach v] :: list) - (1) :: operators) lần {
  nếu <(phần tử (i :: variables) của [danh_sach v] :: list) > (max_val :: variables)> thì {
    đặt [max_val v] thành (phần tử (i :: variables) của [danh_sach v] :: list) :: variables
  } :: control
  thay đổi [i v] một lượng (1) :: variables
} :: control
nói (max_val :: variables) :: looks
`,
  "phu_luc_a_dao_chuoi": `
đặt [chuoi_nguoc v] thành [] :: variables
đặt [i v] thành (độ dài của (chuoi_goc :: variables) :: operators) :: variables
lặp lại (độ dài của (chuoi_goc :: variables) :: operators) lần {
  đặt [chuoi_nguoc v] thành (kết hợp (chuoi_nguoc :: variables) (ký tự (i :: variables) của (chuoi_goc :: variables) :: operators) :: operators) :: variables
  thay đổi [i v] một lượng (-1) :: variables
} :: control
nói (chuoi_nguoc :: variables) :: looks
`
};

const outDir = path.join(__dirname, '../assets/rendered_blocks');
for (const [name, script] of Object.entries(APPENDIX_BLOCKS)) {
  const outSvg = path.join(outDir, `${name}.svg`);
  const outPng = path.join(outDir, `${name}.png`);
  renderToSvgAndPng(script.trim(), outSvg, outPng);
  console.log(`Rendered ${name}.png successfully`);
}
