"""
TRANSLATOR: PYTHON AST -> AUTHENTIC SCRATCH 3.0 SCRIPTS & STEPS (V3 MASTER)
Xử lý triệt để:
1. Loại bỏ các đoạn boilerplate input().split() / len() >= 2 của Python, chuyển thành khối 'hỏi [Nhập ...] và đợi'
2. Chuyển hàm max(a, b) / min(a, b) thành logic gán biến và so sánh nếu-thì
3. Chuyển print(*a) thành vòng lặp nói từng phần tử
4. Chuyển ' '.join(...) thành vòng lặp nối chuỗi chuẩn Scratch
5. Chuyển hàm len(s) thành khối (độ dài của (s))
6. Chuyển hàm round(x) thành khối [làm tròn v] của (x)
7. Chuyển f-string thành khối (kết hợp (...) (...))
"""

import ast
import re

class ScratchTranslator:
    def __init__(self):
        self.sb_lines = []
        self.text_steps = []
        self.indent = 0

    def translate(self, py_code: str):
        self.sb_lines = ["khi bấm vào @greenFlag :: events hat"]
        self.text_steps = ["khi bấm vào cờ xanh"]
        self.indent = 0
        
        try:
            tree = ast.parse(py_code)
        except Exception as e:
            return None, None

        # Tiền xử lý các statement: bỏ boilerplate đọc input phức tạp của Python
        cleaned_stmts = self.preprocess_statements(tree.body)
        self.visit_statements(cleaned_stmts)

        sb_clean = [l for l in self.sb_lines if l.strip()]
        steps_clean = [s for s in self.text_steps if s.strip()]
        return "\n".join(sb_clean), steps_clean

    def preprocess_statements(self, stmts):
        new_stmts = []
        for stmt in stmts:
            # Bỏ gán dòng input đọc xâu tạm: line = input().split() hoặc dong1 = input().split()
            if isinstance(stmt, ast.Assign) and isinstance(stmt.value, ast.Call):
                f = stmt.value.func
                if isinstance(f, ast.Attribute) and f.attr == 'split':
                    continue
            # Bỏ rẽ nhánh kiểm tra độ dài input: if len(line) >= 2: ... else: ...
            if isinstance(stmt, ast.If) and isinstance(stmt.test, ast.Compare):
                left = stmt.test.left
                if isinstance(left, ast.Call) and isinstance(left.func, ast.Name) and left.func.id == 'len':
                    # Lấy các biến được gán trong body chuyển thành lệnh gán input chuẩn
                    for b in stmt.body:
                        if isinstance(b, ast.Assign):
                            for t in b.targets:
                                if isinstance(t, ast.Name) and t.id not in ('line', 'dong1', 'parts'):
                                    # Tạo statement đơn giản var = int(input())
                                    fake_node = ast.Assign(
                                        targets=[t],
                                        value=ast.Call(func=ast.Name(id='int', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='input', ctx=ast.Load()), args=[], keywords=[])], keywords=[])
                                    )
                                    new_stmts.append(fake_node)
                    continue
            new_stmts.append(stmt)
        return new_stmts

    def emit(self, sb_line: str, step_text: str):
        pad = "  " * self.indent
        self.sb_lines.append(f"{pad}{sb_line}")
        if step_text:
            self.text_steps.append(f"{pad}{step_text}")

    def visit_statements(self, stmts):
        for stmt in stmts:
            self.visit_stmt(stmt)

    def visit_stmt(self, stmt):
        if isinstance(stmt, ast.Assign):
            self.handle_assign(stmt)
        elif isinstance(stmt, ast.AugAssign):
            self.handle_aug_assign(stmt)
        elif isinstance(stmt, ast.If):
            self.handle_if(stmt)
        elif isinstance(stmt, ast.For):
            self.handle_for(stmt)
        elif isinstance(stmt, ast.While):
            self.handle_while(stmt)
        elif isinstance(stmt, ast.Expr):
            self.handle_expr(stmt)
        elif isinstance(stmt, ast.Break):
            self.emit("dừng lại [kịch bản này v] :: control", "dừng kịch bản này")

    def handle_expr(self, stmt):
        val = stmt.value
        if isinstance(val, ast.Call) and isinstance(val.func, ast.Name) and val.func.id == 'print':
            self.handle_print(val)
        elif isinstance(val, ast.Call) and isinstance(val.func, ast.Attribute) and val.func.attr == 'append':
            list_name = val.func.value.id if isinstance(val.func.value, ast.Name) else 'danh_sach'
            arg_expr = self.trans_expr(val.args[0])
            arg_txt = self.trans_expr_text(val.args[0])
            self.emit(f"thêm ({arg_expr}) vào [{list_name} v] :: list", f"thêm ({arg_txt}) vào [{list_name}]")

    def handle_print(self, call_node):
        args = call_node.args
        if not args:
            self.emit("nói [] :: looks", "nói []")
            return

        # Case: print(max(a, b)) -> Rẽ nhánh nói số lớn hơn
        if len(args) == 1 and isinstance(args[0], ast.Call) and isinstance(args[0].func, ast.Name) and args[0].func.id in ('max', 'min'):
            fn = args[0].func.id
            m_args = args[0].args
            if len(m_args) == 2:
                a_sb = self.trans_expr(m_args[0])
                b_sb = self.trans_expr(m_args[1])
                cmp_op = ">" if fn == 'max' else "<"
                cmp_txt = "lớn hơn" if fn == 'max' else "nhỏ hơn"
                self.emit(f"nếu <({a_sb}) {cmp_op} ({b_sb})> thì {{", f"nếu <{self.trans_expr_text(m_args[0])} {cmp_op} {self.trans_expr_text(m_args[1])}> thì:")
                self.indent += 1
                self.emit(f"nói ({a_sb}) :: looks", f"nói ({self.trans_expr_text(m_args[0])})")
                self.indent -= 1
                self.emit(f"}} nếu không {{", "nếu không thì:")
                self.indent += 1
                self.emit(f"nói ({b_sb}) :: looks", f"nói ({self.trans_expr_text(m_args[1])})")
                self.indent -= 1
                self.emit(f"}} :: control", "")
                return
            elif len(m_args) >= 3:
                # max(a, b, c)
                self.emit(f"đặt [max_val v] thành ({self.trans_expr(m_args[0])}) :: variables", f"đặt [max_val] thành ({self.trans_expr_text(m_args[0])})")
                for item in m_args[1:]:
                    i_sb = self.trans_expr(item)
                    i_txt = self.trans_expr_text(item)
                    cmp_op = ">" if fn == 'max' else "<"
                    self.emit(f"nếu <({i_sb}) {cmp_op} (max_val :: variables)> thì {{", f"nếu <{i_txt} {cmp_op} max_val> thì:")
                    self.indent += 1
                    self.emit(f"đặt [max_val v] thành ({i_sb}) :: variables", f"đặt [max_val] thành ({i_txt})")
                    self.indent -= 1
                    self.emit(f"}} :: control", "")
                self.emit(f"nói (max_val :: variables) :: looks", "nói (max_val)")
                return

        # Case: print(' '.join(str(i) for i in range(1, n + 1))) -> Vòng lặp nối chuỗi và nói
        if len(args) == 1 and isinstance(args[0], ast.Call) and isinstance(args[0].func, ast.Attribute) and args[0].func.attr == 'join':
            join_arg = args[0].args[0]
            if isinstance(join_arg, ast.GeneratorExp):
                self.emit(f"đặt [ket_qua v] thành [] :: variables", "đặt [ket_qua] thành rỗng")
                self.emit(f"đặt [i v] thành (1) :: variables", "đặt [i] thành 1")
                self.emit(f"lặp lại (n) lần {{", "lặp lại (n) lần:")
                self.indent += 1
                self.emit(f"đặt [ket_qua v] thành (kết hợp (ket_qua :: variables) (kết hợp (i :: variables) [ ] :: operators) :: operators) :: variables", "đặt [ket_qua] thành kết hợp ket_qua và i và dấu cách")
                self.emit(f"thay đổi [i v] một lượng (1) :: variables", "thay đổi [i] một lượng 1")
                self.indent -= 1
                self.emit(f"}} :: control", "")
                self.emit(f"nói (ket_qua :: variables) :: looks", "nói (ket_qua)")
                return
            elif isinstance(join_arg, ast.Name):
                self.emit(f"nói ({join_arg.id} :: variables) :: looks", f"nói ({join_arg.id})")
                return

        # Case: print(*a) -> In toàn bộ danh sách bằng vòng lặp nối chuỗi
        if any(isinstance(a, ast.Starred) for a in args):
            star_arg = [a for a in args if isinstance(a, ast.Starred)][0]
            l_name = star_arg.value.id if isinstance(star_arg.value, ast.Name) else 'danh_sach'
            self.emit(f"đặt [ket_qua v] thành [] :: variables", "đặt [ket_qua] thành rỗng")
            self.emit(f"đặt [i v] thành (1) :: variables", "đặt [i] thành 1")
            self.emit(f"lặp lại (kích thước của [{l_name} v] :: list) lần {{", f"lặp lại (kích thước của [{l_name}]) lần:")
            self.indent += 1
            self.emit(f"đặt [ket_qua v] thành (kết hợp (ket_qua :: variables) (kết hợp (phần tử (i) của [{l_name} v] :: list) [ ] :: operators) :: operators) :: variables", f"đặt [ket_qua] thành kết hợp ket_qua và phần tử i và dấu cách")
            self.emit(f"thay đổi [i v] một lượng (1) :: variables", "thay đổi [i] một lượng 1")
            self.indent -= 1
            self.emit(f"}} :: control", "")
            self.emit(f"nói (ket_qua :: variables) :: looks", "nói (ket_qua)")
            return

        # Single arg
        if len(args) == 1:
            expr_code = self.trans_expr(args[0])
            expr_txt = self.trans_expr_text(args[0])
            self.emit(f"nói ({expr_code}) :: looks", f"nói ({expr_txt})")
            return

        # Multiple args: print(a, b, ...) -> kết hợp (...) (kết hợp [ ] (...))
        combined_sb = self.trans_expr(args[0])
        combined_txt = self.trans_expr_text(args[0])
        for a in args[1:]:
            arg_sb = self.trans_expr(a)
            arg_txt = self.trans_expr_text(a)
            combined_sb = f"(kết hợp ({combined_sb}) (kết hợp [ ] ({arg_sb}) :: operators) :: operators)"
            combined_txt = f"{combined_txt} và ' ' và {arg_txt}"
        
        self.emit(f"nói {combined_sb} :: looks", f"nói (kết hợp {combined_txt})")

    def handle_assign(self, stmt):
        target = stmt.targets[0]
        val = stmt.value

        # Multiple assignment: a, b = map(int, input().split())
        if isinstance(target, ast.Tuple):
            var_names = [t.id for t in target.elts if isinstance(t, ast.Name)]
            if isinstance(val, ast.Call) and isinstance(val.func, ast.Name) and val.func.id == 'map':
                for v in var_names:
                    self.emit(f"hỏi [Nhập {v}:] và đợi :: sensing", f"hỏi [Nhập {v}:] và đợi")
                    self.emit(f"đặt [{v} v] thành (câu trả lời :: sensing) :: variables", f"đặt [{v}] thành (câu trả lời)")
                return
            elif isinstance(val, ast.Tuple):
                for v, e in zip(var_names, val.elts):
                    e_sb = self.trans_expr(e)
                    e_txt = self.trans_expr_text(e)
                    self.emit(f"đặt [{v} v] thành ({e_sb}) :: variables", f"đặt [{v}] thành ({e_txt})")
                return

        if not isinstance(target, ast.Name):
            return

        var_name = target.id

        # Case 1: input() or int(input())
        if self.is_input_call(val):
            self.emit(f"hỏi [Nhập {var_name}:] và đợi :: sensing", f"hỏi [Nhập {var_name}:] và đợi")
            self.emit(f"đặt [{var_name} v] thành (câu trả lời :: sensing) :: variables", f"đặt [{var_name}] thành (câu trả lời)")
            return

        # Case 2: list input: a = list(map(int, input().split()))
        if self.is_list_input(val):
            self.emit(f"xóa tất cả của [{var_name} v] :: list", f"xóa tất cả của danh sách [{var_name}]")
            self.emit(f"đặt [i v] thành (1) :: variables", f"đặt [i] thành 1")
            self.emit(f"lặp lại (n) lần {{", f"lặp lại (n) lần:")
            self.indent += 1
            self.emit(f"hỏi [Nhập phần tử:] và đợi :: sensing", f"hỏi [Nhập phần tử:] và đợi")
            self.emit(f"thêm (câu trả lời :: sensing) vào [{var_name} v] :: list", f"thêm (câu trả lời) vào [{var_name}]")
            self.emit(f"thay đổi [i v] một lượng (1) :: variables", f"thay đổi [i] một lượng 1")
            self.indent -= 1
            self.emit(f"}} :: control", "")
            return

        # Case 3: empty list a = []
        if isinstance(val, ast.List) and len(val.elts) == 0:
            self.emit(f"xóa tất cả của [{var_name} v] :: list", f"xóa tất cả của [{var_name}]")
            return

        # General expression assign
        expr_sb = self.trans_expr(val)
        expr_txt = self.trans_expr_text(val)
        self.emit(f"đặt [{var_name} v] thành ({expr_sb}) :: variables", f"đặt [{var_name}] thành ({expr_txt})")

    def handle_aug_assign(self, stmt):
        var_name = stmt.target.id if isinstance(stmt.target, ast.Name) else 'x'
        op = stmt.op
        val = stmt.value
        
        # +=
        if isinstance(op, ast.Add):
            val_sb = self.trans_expr(val)
            val_txt = self.trans_expr_text(val)
            self.emit(f"thay đổi [{var_name} v] một lượng ({val_sb}) :: variables", f"thay đổi [{var_name}] một lượng ({val_txt})")
        # -=
        elif isinstance(op, ast.Sub):
            val_sb = self.trans_expr(val)
            val_txt = self.trans_expr_text(val)
            self.emit(f"thay đổi [{var_name} v] một lượng ((0) - ({val_sb}) :: operators) :: variables", f"thay đổi [{var_name}] một lượng (-{val_txt})")
        else:
            full_sb = self.trans_binop_raw(ast.Name(id=var_name, ctx=ast.Load()), op, val)
            full_txt = f"{var_name} {self.op_to_txt(op)} {self.trans_expr_text(val)}"
            self.emit(f"đặt [{var_name} v] thành ({full_sb}) :: variables", f"đặt [{var_name}] thành ({full_txt})")

    def handle_if(self, stmt):
        cond_sb = self.trans_cond(stmt.test)
        cond_txt = self.trans_cond_text(stmt.test)
        has_else = len(stmt.orelse) > 0

        if has_else:
            self.emit(f"nếu <{cond_sb}> thì {{", f"nếu <{cond_txt}> thì:")
            self.indent += 1
            self.visit_statements(stmt.body)
            self.indent -= 1
            self.emit(f"}} nếu không {{", f"nếu không thì:")
            self.indent += 1
            self.visit_statements(stmt.orelse)
            self.indent -= 1
            self.emit(f"}} :: control", "")
        else:
            self.emit(f"nếu <{cond_sb}> thì {{", f"nếu <{cond_txt}> thì:")
            self.indent += 1
            self.visit_statements(stmt.body)
            self.indent -= 1
            self.emit(f"}} :: control", "")

    def handle_for(self, stmt):
        target = stmt.target
        var_name = target.id if isinstance(target, ast.Name) else 'i'
        iter_node = stmt.iter

        # for i in range(...)
        if isinstance(iter_node, ast.Call) and isinstance(iter_node.func, ast.Name) and iter_node.func.id == 'range':
            r_args = iter_node.args
            if len(r_args) == 1:
                start_sb, start_txt = "0", "0"
                count_sb = self.trans_expr(r_args[0])
                count_txt = self.trans_expr_text(r_args[0])
            elif len(r_args) == 2:
                start_sb = self.trans_expr(r_args[0])
                start_txt = self.trans_expr_text(r_args[0])
                r_stop = r_args[1]
                if (isinstance(r_args[0], ast.Constant) and r_args[0].value == 1 and
                    isinstance(r_stop, ast.BinOp) and isinstance(r_stop.op, ast.Add) and
                    isinstance(r_stop.right, ast.Constant) and r_stop.right.value == 1):
                    count_sb = self.trans_expr(r_stop.left)
                    count_txt = self.trans_expr_text(r_stop.left)
                else:
                    count_sb = f"(({self.trans_expr(r_args[1])}) - ({start_sb}) :: operators)"
                    count_txt = f"{self.trans_expr_text(r_args[1])} - {start_txt}"
            else:
                start_sb = self.trans_expr(r_args[0])
                start_txt = self.trans_expr_text(r_args[0])
                count_sb = self.trans_expr(r_args[1])
                count_txt = self.trans_expr_text(r_args[1])

            self.emit(f"đặt [{var_name} v] thành ({start_sb}) :: variables", f"đặt [{var_name}] thành ({start_txt})")
            self.emit(f"lặp lại ({count_sb}) lần {{", f"lặp lại ({count_txt}) lần:")
            self.indent += 1
            self.visit_statements(stmt.body)
            self.emit(f"thay đổi [{var_name} v] một lượng (1) :: variables", f"thay đổi [{var_name}] một lượng 1")
            self.indent -= 1
            self.emit(f"}} :: control", "")
        else:
            iter_sb = self.trans_expr(iter_node)
            iter_txt = self.trans_expr_text(iter_node)
            self.emit(f"đặt [vi_tri v] thành (1) :: variables", "đặt [vi_tri] thành 1")
            self.emit(f"lặp lại (kích thước của [{iter_txt} v] :: list) lần {{", f"lặp lại (kích thước của {iter_txt}) lần:")
            self.indent += 1
            self.emit(f"đặt [{var_name} v] thành (phần tử (vi_tri) của [{iter_txt} v] :: list) :: variables", f"đặt [{var_name}] thành phần tử thứ (vi_tri)")
            self.visit_statements(stmt.body)
            self.emit(f"thay đổi [vi_tri v] một lượng (1) :: variables", "thay đổi [vi_tri] một lượng 1")
            self.indent -= 1
            self.emit(f"}} :: control", "")

    def handle_while(self, stmt):
        cond_sb = self.trans_cond(stmt.test)
        cond_txt = self.trans_cond_text(stmt.test)
        
        if isinstance(stmt.test, ast.Compare) and len(stmt.test.ops) == 1 and isinstance(stmt.test.ops[0], ast.Gt):
            left = self.trans_expr(stmt.test.left)
            right = self.trans_expr(stmt.test.comparators[0])
            self.emit(f"lặp lại cho đến khi <({left}) = ({right})> {{", f"lặp lại cho đến khi <{self.trans_expr_text(stmt.test.left)} = {self.trans_expr_text(stmt.test.comparators[0])}>:")
        else:
            self.emit(f"lặp lại cho đến khi <không <{cond_sb}> :: operators> {{", f"lặp lại cho đến khi không còn <{cond_txt}>:")

        self.indent += 1
        self.visit_statements(stmt.body)
        self.indent -= 1
        self.emit(f"}} :: control", "")

    def is_input_call(self, node):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ('input', 'int', 'float', 'str'):
                if node.func.id == 'input': return True
                if node.args and isinstance(node.args[0], ast.Call):
                    f = node.args[0].func
                    if isinstance(f, ast.Name) and f.id == 'input': return True
                    if isinstance(f, ast.Attribute) and f.attr in ('strip', 'split'): return True
        return False

    def is_list_input(self, node):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
            return True
        return False

    def trans_expr(self, node):
        if isinstance(node, ast.Constant):
            val = node.value
            return str(val) if val is not None else ""
        elif isinstance(node, ast.Name):
            return f"({node.id} :: variables)"
        elif isinstance(node, ast.BinOp):
            return self.trans_binop(node)
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return f"((0) - ({self.trans_expr(node.operand)}) :: operators)"
        elif isinstance(node, ast.Call):
            return self.trans_call(node)
        elif isinstance(node, ast.Subscript):
            val = node.value.id if isinstance(node.value, ast.Name) else 'danh_sach'
            idx = node.slice
            if isinstance(idx, ast.Constant):
                num = idx.value + 1 if isinstance(idx.value, int) and idx.value >= 0 else 1
                return f"(phần tử ({num}) của [{val} v] :: list)"
            elif isinstance(idx, ast.UnaryOp) and isinstance(idx.op, ast.USub):
                return f"(phần tử [cuối cùng v] của [{val} v] :: list)"
            else:
                idx_expr = self.trans_expr(idx)
                return f"(phần tử (({idx_expr}) + (1) :: operators) của [{val} v] :: list)"
        elif isinstance(node, ast.JoinedStr):
            # Format string f"{a} {b}"
            parts = []
            for v in node.values:
                if isinstance(v, ast.FormattedValue):
                    parts.append(self.trans_expr(v.value))
                elif isinstance(v, ast.Constant):
                    parts.append(f"[{v.value}]")
            if not parts: return "[]"
            res = parts[0]
            for p in parts[1:]:
                res = f"(kết hợp ({res}) ({p}) :: operators)"
            return res
        return "0"

    def trans_expr_text(self, node):
        if isinstance(node, ast.Constant):
            return str(node.value)
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.BinOp):
            l = self.trans_expr_text(node.left)
            r = self.trans_expr_text(node.right)
            op = self.op_to_txt(node.op)
            return f"{l} {op} {r}"
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return f"-{self.trans_expr_text(node.operand)}"
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                fid = node.func.id
                if fid == 'len' and node.args:
                    return f"độ dài của {self.trans_expr_text(node.args[0])}"
                return f"{fid}(...)"
        return "giá trị"

    def trans_binop(self, node):
        l = self.trans_expr(node.left)
        r = self.trans_expr(node.right)
        if isinstance(node.op, ast.Add):
            return f"(({l}) + ({r}) :: operators)"
        elif isinstance(node.op, ast.Sub):
            return f"(({l}) - ({r}) :: operators)"
        elif isinstance(node.op, ast.Mult):
            return f"(({l}) * ({r}) :: operators)"
        elif isinstance(node.op, ast.Div):
            return f"(({l}) / ({r}) :: operators)"
        elif isinstance(node.op, ast.FloorDiv):
            return f"([làm tròn xuống v] của (({l}) / ({r}) :: operators) :: operators)"
        elif isinstance(node.op, ast.Mod):
            return f"(({l}) mod ({r}) :: operators)"
        elif isinstance(node.op, ast.Pow):
            return f"([lũy thừa v] của ({l}) ({r}) :: operators)"
        return f"(({l}) + ({r}) :: operators)"

    def trans_binop_raw(self, left, op, right):
        l = self.trans_expr(left)
        r = self.trans_expr(right)
        if isinstance(op, ast.Add): return f"(({l}) + ({r}) :: operators)"
        if isinstance(op, ast.Sub): return f"(({l}) - ({r}) :: operators)"
        if isinstance(op, ast.Mult): return f"(({l}) * ({r}) :: operators)"
        if isinstance(op, ast.FloorDiv): return f"([làm tròn xuống v] của (({l}) / ({r}) :: operators) :: operators)"
        if isinstance(op, ast.Mod): return f"(({l}) mod ({r}) :: operators)"
        return f"(({l}) + ({r}) :: operators)"

    def op_to_txt(self, op):
        if isinstance(op, ast.Add): return "+"
        if isinstance(op, ast.Sub): return "-"
        if isinstance(op, ast.Mult): return "*"
        if isinstance(op, ast.Div): return "/"
        if isinstance(op, ast.FloorDiv): return "chia nguyên"
        if isinstance(op, ast.Mod): return "mod"
        return "+"

    def trans_call(self, node):
        if isinstance(node.func, ast.Name):
            fid = node.func.id
            if fid == 'len' and len(node.args) == 1:
                arg_name = node.args[0].id if isinstance(node.args[0], ast.Name) else self.trans_expr(node.args[0])
                return f"(độ dài của ({arg_name}) :: operators)"
            elif fid == 'abs' and len(node.args) == 1:
                a = self.trans_expr(node.args[0])
                return f"([giá trị tuyệt đối v] của ({a}) :: operators)"
            elif fid == 'round' and len(node.args) >= 1:
                a = self.trans_expr(node.args[0])
                return f"([làm tròn v] của ({a}) :: operators)"
        elif isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            if attr == 'upper':
                return f"(chuyển chữ hoa của ({self.trans_expr(node.func.value)}) :: operators)"
            elif attr == 'lower':
                return f"(chuyển chữ thường của ({self.trans_expr(node.func.value)}) :: operators)"
            elif attr == 'count' and len(node.args) == 1:
                return f"(số lần xuất hiện của ({self.trans_expr(node.args[0])}) trong ({self.trans_expr(node.func.value)}) :: operators)"
        return "(0)"

    def trans_cond(self, node):
        if isinstance(node, ast.Compare):
            left = self.trans_expr(node.left)
            cmp = node.ops[0]
            right = self.trans_expr(node.comparators[0])
            if isinstance(cmp, ast.Eq):
                return f"({left}) = ({right})"
            elif isinstance(cmp, ast.Gt):
                return f"({left}) > ({right})"
            elif isinstance(cmp, ast.Lt):
                return f"({left}) < ({right})"
            elif isinstance(cmp, ast.GtE):
                return f"<({left}) > ({right})> hoặc <({left}) = ({right})> :: operators"
            elif isinstance(cmp, ast.LtE):
                return f"<({left}) < ({right})> hoặc <({left}) = ({right})> :: operators"
            elif isinstance(cmp, ast.NotEq):
                return f"không <({left}) = ({right})> :: operators"
        elif isinstance(node, ast.BoolOp):
            if isinstance(node.op, ast.And):
                parts = [f"<{self.trans_cond(v)}>" for v in node.values]
                res = parts[0]
                for p in parts[1:]:
                    res = f"{res} và {p} :: operators"
                return res
            elif isinstance(node.op, ast.Or):
                parts = [f"<{self.trans_cond(v)}>" for v in node.values]
                res = parts[0]
                for p in parts[1:]:
                    res = f"{res} hoặc {p} :: operators"
                return res
        return "(1) = (1)"

    def trans_cond_text(self, node):
        if isinstance(node, ast.Compare):
            l = self.trans_expr_text(node.left)
            r = self.trans_expr_text(node.comparators[0])
            cmp = node.ops[0]
            op_str = "="
            if isinstance(cmp, ast.Gt): op_str = ">"
            elif isinstance(cmp, ast.Lt): op_str = "<"
            elif isinstance(cmp, ast.GtE): op_str = ">="
            elif isinstance(cmp, ast.LtE): op_str = "<="
            elif isinstance(cmp, ast.NotEq): op_str = "!="
            return f"{l} {op_str} {r}"
        return "điều kiện"
