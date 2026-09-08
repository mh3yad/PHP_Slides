# -*- coding: utf-8 -*-
import os
import json

TARGET_DIR = "/home/m/projects/slides/logharitm-slides-source/lectures/lecture-06"
os.makedirs(TARGET_DIR, exist_ok=True)
TOTAL_SLIDES = 28

def pad(n):
    return f"{n:02d}"

def make_slide(index, title, eyebrow, slide_title, slide_text, body_content, notes_title, notes_script, notes_list, is_cover=False, is_divider=False):
    curr_num = index + 1
    file_name = f"slide-{pad(curr_num)}.html"
    prev_file = f"slide-{pad(curr_num - 1)}.html" if curr_num > 1 else None
    next_file = f"slide-{pad(curr_num + 1)}.html" if curr_num < TOTAL_SLIDES else None
    progress_pct = round((curr_num / TOTAL_SLIDES) * 100, 1)

    body_attrs = []
    if next_file:
        body_attrs.append(f'data-next="{next_file}"')
    if prev_file:
        body_attrs.append(f'data-prev="{prev_file}"')
    body_attr_str = " " + " ".join(body_attrs) if body_attrs else ""

    dots_html = []
    for i in range(1, TOTAL_SLIDES + 1):
        active_cls = " active" if i == curr_num else ""
        dots_html.append(f'<span class="slide-nav-dot{active_cls}" onclick="window.location.href=\'slide-{pad(i)}.html\'"></span>')
    nav_dots_str = "\n".join(dots_html)

    if next_file:
        next_btn = f'''<button class="nav-btn" onclick="window.location.href='{next_file}'">
      التالي
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>
    </button>'''
    else:
        next_btn = f'''<button class="nav-btn" disabled>
      التالي
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>
    </button>'''

    if prev_file:
        prev_btn = f'''<button class="nav-btn" onclick="window.location.href='{prev_file}'">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
      السابق
    </button>'''
    else:
        prev_btn = f'''<button class="nav-btn" disabled>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
      السابق
    </button>'''

    counter_str = f'<span class="counter">{pad(curr_num)} / {TOTAL_SLIDES}</span>'

    notes_json = json.dumps({
        "title": notes_title,
        "script": notes_script,
        "notes": notes_list
    }, ensure_ascii=False, indent=2)

    if is_cover:
        slide_cls = "slide active slide-cover"
    elif is_divider:
        slide_cls = "slide active slide-divider"
    else:
        slide_cls = "slide active"

    html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>المحاضرة 06 &middot; {title} &mdash; شريحة {pad(curr_num)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800;900&family=Fira+Code:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body{body_attr_str}>
<div class="deck">
  <div class="progress-bar"><div class="progress-fill" style="width:{progress_pct}%"></div></div>
  <div class="brand-logo"><img src="logo.jpg" alt="الشعار"></div>
  <section class="{slide_cls}">
    <span class="slide-index-badge">{pad(curr_num)} / {TOTAL_SLIDES}</span>
    <div class="slide-content">
{f'      <div class="cover-logo"><img src="logo.jpg" alt="الشعار"></div>' if is_cover else ''}
{f'      <div class="eyebrow">{eyebrow}</div>' if eyebrow else ''}
{f'      <h1 class="slide-title">{slide_title}</h1>' if slide_title else ''}
{f'      <p class="slide-text">{slide_text}</p>' if slide_text else ''}
      {body_content}
    </div>
  </section>
  <div class="nav-dots">
    {nav_dots_str}
  </div>
  <div class="nav-controls">
    {next_btn}
    {counter_str}
    {prev_btn}
  </div>
</div>
<script src="script.js"></script>
<script class="slide-notes" type="application/json">
{notes_json}
</script>
</body>
</html>
'''
    target_path = os.path.join(TARGET_DIR, file_name)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_name}")

