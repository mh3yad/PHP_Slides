import os
import json

TARGET_DIR = "/home/m/projects/slides/logharitm-slides-source/lectures/lecture-03"
TOTAL_SLIDES = 26

slides_data = []

# Helper to format slide index
def pad(n):
    return f"{n:02d}"

# Common head & navigation generator
def generate_slide_html(index, title, eyebrow, slide_title, slide_text, body_content, notes_title, notes_script, notes_list, is_cover=False):
    curr_num = index + 1
    file_name = f"slide-{pad(curr_num)}.html"
    prev_file = f"slide-{pad(curr_num - 1)}.html" if curr_num > 1 else None
    next_file = f"slide-{pad(curr_num + 1)}.html" if curr_num < TOTAL_SLIDES else None
    progress_pct = round((curr_num / TOTAL_SLIDES) * 100, 1)

    # Body data attributes
    body_attrs = []
    if next_file:
        body_attrs.append(f'data-next="{next_file}"')
    if prev_file:
        body_attrs.append(f'data-prev="{prev_file}"')
    body_attr_str = " " + " ".join(body_attrs) if body_attrs else ""

    # Nav dots
    dots_html = []
    for i in range(1, TOTAL_SLIDES + 1):
        active_cls = " active" if i == curr_num else ""
        dots_html.append(f'<a class="slide-nav-dot{active_cls}" href="slide-{pad(i)}.html"></a>')
    nav_dots_str = "\n".join(dots_html)

    # Nav controls
    if next_file:
        next_btn = f'''<a class="nav-btn" href="{next_file}">
    التالي
    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4" viewbox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
</a>'''
    else:
        next_btn = f'''<span aria-disabled="true" class="nav-btn" style="opacity:.35;cursor:not-allowed;">
    التالي
    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4" viewbox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
</span>'''

    if prev_file:
        prev_btn = f'''<a class="nav-btn" href="{prev_file}">
<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4" viewbox="0 0 24 24"><polyline points="9 18 15 12 9 6" transform="rotate(180 12 12)"></polyline></svg>
    السابق
</a>'''
    else:
        prev_btn = f'''<span aria-disabled="true" class="nav-btn" style="opacity:.35;cursor:not-allowed;">
<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4" viewbox="0 0 24 24"><polyline points="9 18 15 12 9 6" transform="rotate(180 12 12)"></polyline></svg>
    السابق
</span>'''

    counter_str = f'<span class="counter">{curr_num} / {TOTAL_SLIDES}</span>'

    notes_json = json.dumps({
        "title": notes_title,
        "script": notes_script,
        "notes": notes_list
    }, ensure_ascii=False, indent=2)

    slide_cls = "slide active slide-cover" if is_cover else "slide active"

    html = f'''<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="html-slides v0.9.4 (custom RTL blueprint - multi-file)" name="generator"/>
<title>لوغاريتم — {title}</title>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&amp;family=Fira+Code:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="styles.css" rel="stylesheet"/>
</head>
<body{body_attr_str}>
<div class="brand-logo"><img alt="شعار لوغاريتم" src="assets/logo.jpg"/></div>
<div class="progress-bar"><div class="progress-fill" style="width:{progress_pct}%"></div></div>
<div class="deck" id="deck">
<div class="{slide_cls}" data-slide="{index}">
<div class="slide-index-badge">{pad(curr_num)} / {TOTAL_SLIDES}</div>
<div class="slide-content">
{f'<div class="cover-logo"><img alt="شعار لوغاريتم" src="assets/logo.jpg"/></div>' if is_cover else ''}
<div class="eyebrow">{eyebrow}</div>
<h1 class="slide-title">{slide_title}</h1>
{f'<p class="slide-text">{slide_text}</p>' if slide_text else ''}

{body_content}

</div>
</div>
</div>
<div class="nav-dots">
{nav_dots_str}
</div>
<div class="nav-controls">
{next_btn}
{counter_str}
{prev_btn}
</div>
<script src="script.js"></script>
<script class="slide-notes" type="application/json">
{notes_json}
</script>
</body>
</html>
'''
    return file_name, html

print("Helper defined successfully.")
