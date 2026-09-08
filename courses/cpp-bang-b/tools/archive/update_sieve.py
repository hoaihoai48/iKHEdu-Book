import re
from pathlib import Path

def update_sieve():
    svg_path = Path("courses/cpp-bang-b/lessons/lesson-07-uoc-boi-so-nguyen-to/assets/sieve_eratosthenes_simulation_vi.svg")
    with open(svg_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Defs and outer card
    text = re.sub(
        r'<defs>.*?</defs>',
        '''<defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8FAFC"/>
    </linearGradient>
  </defs>''',
        text,
        flags=re.DOTALL
    )
    text = text.replace('stroke="#334155" stroke-width="2"', 'stroke="#CBD5E1" stroke-width="2"')

    # 2. Title and subtitle
    text = text.replace('fill="#38bdf8"', 'fill="#0F172A"')
    text = text.replace('fill="#94a3b8" font-family="system-ui', 'fill="#475569" font-family="system-ui')

    # 3. Prime cards
    text = text.replace('fill="#064e3b" stroke="#10b981"', 'fill="#ECFDF5" stroke="#10B981"')
    text = text.replace('fill="#6ee7b7"', 'fill="#065F46"')
    text = text.replace('fill="#047857"', 'fill="#A7F3D0"')
    text = text.replace('fill="#ecfdf5" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">isPrime',
                        'fill="#065F46" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">isPrime')
    text = text.replace('fill="#a7f3d0" font-family="sans-serif" font-size="10" text-anchor="middle">Nguyên tố',
                        'fill="#047857" font-family="sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Nguyên tố')

    # 4. Crossed cards
    text = text.replace('fill="#1e293b" stroke="#475569"', 'fill="#F8FAFC" stroke="#CBD5E1"')
    text = text.replace('fill="#64748b" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle" text-decoration="line-through"',
                        'fill="#94A3B8" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle" text-decoration="line-through"')
    text = text.replace('fill="#334155"', 'fill="#FEE2E2"')
    text = text.replace('fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">false',
                        'fill="#991B1B" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">false')
    text = text.replace('fill="#f87171" font-family="sans-serif" font-size="10" text-anchor="middle">Bội của 2',
                        'fill="#DC2626" font-family="sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Bội của 2')
    text = text.replace('fill="#f59e0b" font-family="sans-serif" font-size="10" text-anchor="middle">Bội của 3',
                        'fill="#D97706" font-family="sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Bội của 3')

    # 5. Legend
    text = text.replace('fill="#0f172a" stroke="#334155"', 'fill="#F8FAFC" stroke="#CBD5E1"')
    text = text.replace('fill="#ecfdf5" font-family="sans-serif" font-size="12" font-weight="bold"',
                        'fill="#065F46" font-family="sans-serif" font-size="12.5" font-weight="bold"')
    text = text.replace('fill="#f87171" font-family="sans-serif" font-size="12"',
                        'fill="#991B1B" font-family="sans-serif" font-size="12.5" font-weight="600"')
    text = text.replace('fill="#fcd34d" font-family="sans-serif" font-size="12"',
                        'fill="#92400E" font-family="sans-serif" font-size="12.5" font-weight="600"')

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Sieve updated.")

update_sieve()
