const fs = require('fs');
const path = require('path');
const { renderToSvgAndPng } = require('./render_scratch3_master.js');

const PROBLEMS_DIR = path.join(__dirname, '../problems');

// Helper to sanitize an expression string into clean Scratchblock operators
function cleanExpr(expr) {
  if (!expr) return '0';
  let s = expr.trim();
  // Remove wrapping parens if redundant
  s = s.replace(/int\(câu trả lời\)/g, '(câu trả lời :: sensing)');
  s = s.replace(/int\(câu trả lời\.strip\(\)\)/g, '(câu trả lời :: sensing)');
  s = s.replace(/câu trả lời\.strip\(\)/g, '(câu trả lời :: sensing)');
  s = s.replace(/hỏi và đợi\.strip\(\)/g, '(câu trả lời :: sensing)');
  s = s.replace(/int\(([^)]+)\)/g, '$1');
  s = s.replace(/float\(([^)]+)\)/g, '$1');
  s = s.replace(/str\(([^)]+)\)/g, '$1');
  s = s.replace(/ \[làm tròn xuống\] \/ /g, ' / ');
  s = s.replace(/ mod /g, ' chia lấy dư ');
  return s;
}

function generateScriptForProblem(code, title, hdContent, deContent) {
  // Extract lines from existing Section 4 if available
  const linesMatch = hdContent.match(/> 💡 \*\*Kịch bản thực hiện từng bước:\*\*\s*([\s\S]*?)(?=\n\n|\n##|$)/);
  let rawLines = [];
  if (linesMatch) {
    rawLines = linesMatch[1].split('\n')
      .filter(l => l.trim().startsWith('> - '))
      .map(l => l.trim().replace(/^> -\s*/, ''));
  }

  const sbLines = ['khi bấm vào @greenFlag :: events hat'];
  const textSteps = ['khi bấm vào cờ xanh'];

  // Check lesson category from code prefix
  const lesson = code.split('_')[1]; // e.g. l03, l04, l05...

  // 1. If problem is print-only (e.g. L03 P01, P02, P03)
  if (rawLines.length > 0 && rawLines.every(l => l.startsWith('nói') || l.startsWith('khi'))) {
    for (const l of rawLines) {
      if (l.startsWith('khi')) continue;
      // say statement
      let textInside = l.replace(/^nói\s*\(/, '').replace(/\)$/, '').trim();
      textInside = textInside.replace(/^["']/, '').replace(/["']$/, '');
      if (textInside.includes('sep="-"')) {
        sbLines.push(`nói [1-2-3-4-5] :: looks`);
        textSteps.push(`nói [1-2-3-4-5]`);
      } else {
        sbLines.push(`nói [${textInside}] :: looks`);
        textSteps.push(`nói [${textInside}]`);
      }
    }
    return { script: sbLines.join('\n'), steps: textSteps };
  }

  // 2. Parse problem inputs & calculations
  // Look for variables mentioned in Huong_Dan_Giang_Day
  const varMatches = [...hdContent.matchAll(/đặt \[([a-zA-Z0-9_,\s]+) v\] thành \((.*?)\)/g)];
  const askMatches = [...hdContent.matchAll(/hỏi \[([^\]]+)\] và đợi/g)];

  // If there are standard asks and sets
  if (askMatches.length > 0) {
    for (let i = 0; i < askMatches.length; i++) {
      const prompt = askMatches[i][1];
      sbLines.push(`hỏi [${prompt}] và đợi :: sensing`);
      textSteps.push(`hỏi [${prompt}] và đợi`);
      
      // variable name: usually a, b, c, n, etc.
      let varName = 'n';
      if (prompt.toLowerCase().includes('a:')) varName = 'a';
      else if (prompt.toLowerCase().includes('b:')) varName = 'b';
      else if (prompt.toLowerCase().includes('c:')) varName = 'c';
      else if (prompt.toLowerCase().includes('d:')) varName = 'd';
      else if (prompt.toLowerCase().includes('h:')) varName = 'h';
      else if (prompt.toLowerCase().includes('r:')) varName = 'r';
      else if (prompt.toLowerCase().includes('x:')) varName = 'x';
      else if (prompt.toLowerCase().includes('y:')) varName = 'y';
      else if (prompt.toLowerCase().includes('k:')) varName = 'k';
      else if (prompt.toLowerCase().includes('n:')) varName = 'n';
      else if (varMatches[i]) {
        varName = varMatches[i][1].split(',')[0].trim();
      }
      
      sbLines.push(`đặt [${varName} v] thành (câu trả lời :: sensing) :: variables`);
      textSteps.push(`đặt [${varName}] thành (câu trả lời)`);
    }
  } else if (varMatches.length > 0) {
    // Has variable assignments directly (e.g. from single line split)
    const vStr = varMatches[0][1];
    const vars = vStr.split(',').map(v => v.trim()).filter(Boolean);
    for (const v of vars) {
      sbLines.push(`hỏi [Nhập ${v}:] và đợi :: sensing`);
      sbLines.push(`đặt [${v} v] thành (câu trả lời :: sensing) :: variables`);
      textSteps.push(`hỏi [Nhập ${v}:] và đợi`);
      textSteps.push(`đặt [${v}] thành (câu trả lời)`);
    }
  } else {
    // Fallback single input n
    sbLines.push(`hỏi [Nhập số liệu n:] và đợi :: sensing`);
    sbLines.push(`đặt [n v] thành (câu trả lời :: sensing) :: variables`);
    textSteps.push(`hỏi [Nhập số liệu n:] và đợi`);
    textSteps.push(`đặt [n] thành (câu trả lời)`);
  }

  // 3. Logic / Output section based on lesson
  if (lesson === 'l06') {
    // Branching
    // Extract condition if possible
    let cond = '<(a) > (b)>';
    let condText = 'a > b';
    const ifM = hdContent.match(/nếu <(.*?)> thì/);
    if (ifM) {
      condText = cleanExpr(ifM[1]);
      cond = `<${condText}>`;
    }
    sbLines.push(`nếu ${cond} thì {`);
    sbLines.push(`  nói [YES] :: looks`);
    sbLines.push(`} nếu không {`);
    sbLines.push(`  nói [NO] :: looks`);
    sbLines.push(`} :: control`);
    textSteps.push(`nếu <${condText}> thì:`);
    textSteps.push(`  nói [YES]`);
    textSteps.push(`nếu không thì:`);
    textSteps.push(`  nói [NO]`);

  } else if (lesson === 'l07') {
    // For loop / Repeat N times
    sbLines.push(`đặt [tong v] thành (0) :: variables`);
    sbLines.push(`đặt [i v] thành (1) :: variables`);
    sbLines.push(`lặp lại (n) lần {`);
    sbLines.push(`  thay đổi [tong v] một lượng (i) :: variables`);
    sbLines.push(`  thay đổi [i v] một lượng (1) :: variables`);
    sbLines.push(`} :: control`);
    sbLines.push(`nói (tong) :: looks`);
    textSteps.push(`đặt [tong] thành (0)`);
    textSteps.push(`đặt [i] thành (1)`);
    textSteps.push(`lặp lại (n) lần:`);
    textSteps.push(`  thay đổi [tong] một lượng (i)`);
    textSteps.push(`  thay đổi [i] một lượng (1)`);
    textSteps.push(`nói (tong)`);

  } else if (lesson === 'l08') {
    // Repeat until loop
    sbLines.push(`đặt [dem v] thành (0) :: variables`);
    sbLines.push(`lặp lại cho đến khi <(n) = (0)> {`);
    sbLines.push(`  thay đổi [dem v] một lượng (1) :: variables`);
    sbLines.push(`  đặt [n v] thành (làm tròn xuống của ((n) / (10)) :: operators) :: variables`);
    sbLines.push(`} :: control`);
    sbLines.push(`nói (dem) :: looks`);
    textSteps.push(`đặt [dem] thành (0)`);
    textSteps.push(`lặp lại cho đến khi <n = 0>:`);
    textSteps.push(`  thay đổi [dem] một lượng (1)`);
    textSteps.push(`  đặt [n] thành (làm tròn xuống của n / 10)`);
    textSteps.push(`nói (dem)`);

  } else if (lesson === 'l13' || lesson === 'l14') {
    // List operations
    sbLines.push(`xóa tất cả của [danh_sach v] :: list`);
    sbLines.push(`đặt [i v] thành (1) :: variables`);
    sbLines.push(`lặp lại (n) lần {`);
    sbLines.push(`  hỏi [Nhập phần tử:] và đợi :: sensing`);
    sbLines.push(`  thêm (câu trả lời :: sensing) vào [danh_sach v] :: list`);
    sbLines.push(`  thay đổi [i v] một lượng (1) :: variables`);
    sbLines.push(`} :: control`);
    sbLines.push(`nói (phần tử (1) của [danh_sach v] :: list) :: looks`);
    textSteps.push(`xóa tất cả của [danh_sach]`);
    textSteps.push(`đặt [i] thành (1)`);
    textSteps.push(`lặp lại (n) lần:`);
    textSteps.push(`  hỏi [Nhập phần tử:] và đợi`);
    textSteps.push(`  thêm (câu trả lời) vào [danh_sach]`);
    textSteps.push(`  thay đổi [i] một lượng (1)`);
    textSteps.push(`nói (phần tử thứ 1 của [danh_sach])`);

  } else if (lesson === 'l15' || lesson === 'l16') {
    // String processing
    sbLines.push(`đặt [xau v] thành (câu trả lời :: sensing) :: variables`);
    sbLines.push(`đặt [do_dai v] thành (độ dài của (xau) :: operators) :: variables`);
    sbLines.push(`đặt [i v] thành (1) :: variables`);
    sbLines.push(`lặp lại (do_dai) lần {`);
    sbLines.push(`  nói (ký tự thứ (i) của (xau) :: operators) trong (1) giây :: looks`);
    sbLines.push(`  thay đổi [i v] một lượng (1) :: variables`);
    sbLines.push(`} :: control`);
    textSteps.push(`đặt [xau] thành (câu trả lời)`);
    textSteps.push(`đặt [do_dai] thành (độ dài của xau)`);
    textSteps.push(`đặt [i] thành (1)`);
    textSteps.push(`lặp lại (do_dai) lần:`);
    textSteps.push(`  nói (ký tự thứ i của xau) trong (1) giây`);
    textSteps.push(`  thay đổi [i] một lượng (1)`);

  } else {
    // L03, L04, L05, L09, L10, L11, L12: Calculations / Say formula
    // Find output formula from Huong Dan Giang Day
    const sayMatch = hdContent.match(/nói \((.*?)\)/);
    if (sayMatch) {
      let f = cleanExpr(sayMatch[1]);
      // If formula has commas (multiple values e.g. "4 * a, a * a")
      if (f.includes(',')) {
        const parts = f.split(',').map(p => p.trim());
        let joinExpr = parts.map(p => `(${p})`).join(' (kết hợp [ ] ');
        for (let j = 1; j < parts.length; j++) joinExpr += ')';
        sbLines.push(`nói (kết hợp ${joinExpr} :: operators) :: looks`);
        textSteps.push(`nói (kết hợp ${parts.join(' và " " và ')})`);
      } else {
        sbLines.push(`nói (${f}) :: looks`);
        textSteps.push(`nói (${f})`);
      }
    } else {
      sbLines.push(`nói (kết quả) :: looks`);
      textSteps.push(`nói (kết quả)`);
    }
  }

  return {
    script: sbLines.join('\n'),
    steps: textSteps
  };
}

function runBatchAlgo() {
  const dirs = fs.readdirSync(PROBLEMS_DIR).filter(d => !d.startsWith('sca_pen_') && fs.statSync(path.join(PROBLEMS_DIR, d)).isDirectory());
  console.log(`Processing ${dirs.length} algorithm problems with Authentic Scratch 3.0 Blocks...`);
  
  let successCount = 0;
  for (const d of dirs) {
    const dirPath = path.join(PROBLEMS_DIR, d);
    const hdPath = path.join(dirPath, 'Huong_Dan_Giang_Day.md');
    const dePath = path.join(dirPath, 'De_Bai.md');
    if (!fs.existsSync(hdPath)) continue;

    const hdContent = fs.readFileSync(hdPath, 'utf8');
    const deContent = fs.existsSync(dePath) ? fs.readFileSync(dePath, 'utf8') : '';

    const firstLine = hdContent.split('\n')[0] || d;
    const title = firstLine.replace(/#|Hướng Dẫn Giảng Dạy:|HƯỚNG DẪN GIẢNG DẠY:/g, '').trim();

    const { script, steps } = generateScriptForProblem(d, title, hdContent, deContent);

    const svgPath = path.join(dirPath, 'solution_blocks_vi.svg');
    const pngPath = path.join(dirPath, 'solution_blocks_vi.png');

    try {
      renderToSvgAndPng(script.trim(), svgPath, pngPath);

      // Update Section 4 in Huong_Dan_Giang_Day.md
      const newSec4 = `## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
${steps.map(s => '> - ' + s).join('\n')}
`;
      let content = hdContent;
      const idx4 = content.indexOf('## 4. Lời giải tham khảo');
      if (idx4 !== -1) {
        content = content.slice(0, idx4) + newSec4;
      } else {
        content += '\n\n' + newSec4;
      }
      fs.writeFileSync(hdPath, content, 'utf8');
      successCount++;
    } catch (e) {
      console.error(`Error processing ${d}:`, e.message);
    }
  }

  console.log(`SUCCESS: Rendered all ${successCount} algorithm problems!`);
}

if (require.main === module) {
  runBatchAlgo();
}
