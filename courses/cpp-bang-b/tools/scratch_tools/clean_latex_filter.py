import re

def clean_latex(text: str) -> str:
    # 1. Phân số: \frac{a}{b} -> a / b
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 / \2', text)
    # 2. Xóa các ký hiệu toán phổ biến
    text = text.replace(r'\le', '≤').replace(r'\ge', '≥')
    text = text.replace(r'\ne', '≠').replace(r'\times', '×')
    text = text.replace(r'\dots', '...').replace(r'\cdots', '...')
    text = text.replace(r'\%', '%')
    text = text.replace(r'\approx', '≈').replace(r'\infty', '∞')
    text = re.sub(r'\\text\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\mathcal\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\mathbf\{([^}]+)\}', r'\1', text)
    # 3. Bỏ dấu $ bao quanh công thức đơn
    text = re.sub(r'\$([^\$]+)\$', r'\1', text)
    return text

print("Test clean_latex:")
print(clean_latex(r"Điểm trung bình cộng: $\frac{24}{3} = 8.00$."))
print(clean_latex(r"Giới hạn: $1 \le a, b \le 10^9$, thời gian $1.0\text{s}$."))
