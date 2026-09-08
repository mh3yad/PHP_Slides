# -*- coding: utf-8 -*-
import os
import json

TARGET_DIR = "/home/m/projects/slides/logharitm-slides-source/lectures/lecture-03"
os.makedirs(TARGET_DIR, exist_ok=True)
TOTAL_SLIDES = 26

def pad(n):
    return f"{n:02d}"

def generate_slide(index, title, eyebrow, slide_title, slide_text, body_content, notes_title, notes_script, notes_list, is_cover=False):
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
        dots_html.append(f'<a class="slide-nav-dot{active_cls}" href="slide-{pad(i)}.html"></a>')
    nav_dots_str = "\n".join(dots_html)

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
    filepath = os.path.join(TARGET_DIR, file_name)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {file_name}")

# ==========================================
# SLIDE 01: COVER
# ==========================================
generate_slide(
    index=0,
    title="المحاضرة الثالثة: الجمل الشرطية والتحكم في مسار الكود",
    eyebrow="لوغاريتم — Logharitm • المحاضرة 03",
    slide_title="الجمل الشرطية والتحكم في مسار الكود",
    slide_text="دليلك العملي لإتقان اتخاذ القرارات البرمجية في PHP: عائلة if المتكاملة، بناء الآلات الحاسبة، المقارنات الذكية، switch مقابل match، والمعاملات الذكية (?: و ??).",
    body_content='''<div class="cover-mark">
  <div><div class="num">03</div><div class="lbl">رقم المحاضرة</div></div>
  <div><div class="num">PHP 8+</div><div class="lbl">الإصدار المستهدف</div></div>
  <div><div class="num">Control Flow</div><div class="lbl">الموضوع الرئيسي</div></div>
</div>''',
    notes_title="الغلاف — المحاضرة الثالثة",
    notes_script="أهلاً بكم في المحاضرة الثالثة من كورس PHP في لوغاريتم. النهاردة هندخل في عقل لغة البرمجة: إزاي الكود بياخد قرارات ذكية ويتفرع في مسارات مختلفة بناءً على الشروط، وهنطبق كل الأمثلة على درجات وتقييمات الطلاب.",
    notes_list=[
        "الترحيب بالطلاب واستعراض عنوان المحاضرة الثالثة",
        "التركيز على الجمل الشرطية (Control Flow) وتطبيقاتها العملية بالأرقام والدرجات"
    ],
    is_cover=True
)

# ==========================================
# SLIDE 02: ROADMAP
# ==========================================
generate_slide(
    index=1,
    title="خريطة المحاضرة الثالثة",
    eyebrow="خريطة الطريق — Lecture Roadmap",
    slide_title="محاور المحاضرة الثالثة: مسارات اتخاذ القرار",
    slide_text="الموضوعات التطبيقية اللي هنشرحها ونطبق عليها خطوة بخطوة النهاردة:",
    body_content='''<div class="topics-grid">
  <div class="topic-item">
    <span class="topic-num">01</span>
    <div class="topic-info">
      <span class="topic-title">جملة if بسطر واحد وبأقواس — Single &amp; Multi-line if</span>
      <span class="topic-desc">قواعد كتابة الشرط ومخاطر إهمال الأقواس المعقوفة {}</span>
    </div>
  </div>
  <div class="topic-item">
    <span class="topic-num">02</span>
    <div class="topic-info">
      <span class="topic-title">اتخاذ القرار والتقديرات — if, else, elseif with Grades</span>
      <span class="topic-desc">فحص النجاح والرسوب وسلم التقديرات الأكاديمية الكامل</span>
    </div>
  </div>
  <div class="topic-item">
    <span class="topic-num">03</span>
    <div class="topic-info">
      <span class="topic-title">الشروط المتداخلة — Nested if &amp; Eligibility</span>
      <span class="topic-desc">التحقق المزدوج: فحص الحضور ثم احتساب التقدير والتكريم</span>
    </div>
  </div>
  <div class="topic-item">
    <span class="topic-num">04</span>
    <div class="topic-info">
      <span class="topic-title">مشروع الآلة الحاسبة والمقارنة — Calculator &amp; Min/Max of 2</span>
      <span class="topic-desc">تطبيق عملي للعمليات الحسابية وتحديد أصغر وأكبر رقمين</span>
    </div>
  </div>
  <div class="topic-item">
    <span class="topic-num">05</span>
    <div class="topic-info">
      <span class="topic-title">أصغر رقم بين 3 أرقام — 3 Ways to find Min of 3</span>
      <span class="topic-desc">المقارنة الشرطية، أسلوب التراكم الخوارزمي، والدوال الجاهزة</span>
    </div>
  </div>
  <div class="topic-item">
    <span class="topic-num">06</span>
    <div class="topic-info">
      <span class="topic-title">فخ الإسناد وملخص if — Caution if($age=5) &amp; Summary</span>
      <span class="topic-desc">كارثة استخدام = بدل == وتقنية Yoda condition وملخص القرار</span>
    </div>
  </div>
  <div class="topic-item">
    <span class="topic-num">07</span>
    <div class="topic-info">
      <span class="topic-title">جملة switch وتعبير match — Switch, Match &amp; Switch Calc</span>
      <span class="topic-desc">فحص الحالات، ظاهرة Fallthrough، وآلة حاسبة، وثورة match الحديثة</span>
    </div>
  </div>
  <div class="topic-item">
    <span class="topic-num">08</span>
    <div class="topic-info">
      <span class="topic-title">المعامل الثلاثي والدمج والتحديات — Ternary (?:), Coalescing (??) &amp; Quiz</span>
      <span class="topic-desc">شروط السطر الواحد، فخ الصفر 0، وسؤالان تطبيقيان شاملان</span>
    </div>
  </div>
</div>''',
    notes_title="خريطة الطريق — محاور المحاضرة",
    notes_script="نظرة شاملة على محاور المحاضرة الثمانية: من الـ if البسيطة مروراً ببناء الآلات الحاسبة وخوارزميات المقارنة، وصولاً إلى match والمعاملات الحديثة، ونختم بأسئلة مراجعة تطبيقية.",
    notes_list=[
        "استعراض المحاور الثمانية بالعناوين العربية والإنجليزية",
        "توضيح ترابط الموضوعات وتدرجها من الأبسط للأكثر احترافية"
    ]
)

# ==========================================
# SLIDE 03: CONTROL FLOW INTRO
# ==========================================
generate_slide(
    index=2,
    title="مفهوم التحكم في مسار الكود",
    eyebrow="التحكم في المسار — Control Flow Basics",
    slide_title="إزاي الكمبيوتر بياخد القرار؟ (التسلسل مقابل التفرع)",
    slide_text="البرنامج في العادي بيمشي في خط مستقيم من فوق لتحت، لحد ما نقابله بشرط يخليه يختار مسار محدد:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">flow_intro.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>

<span class="tok-var">$studentName</span> = <span class="tok-str">"عمر"</span>;
<span class="tok-var">$score</span> = <span class="tok-num">85</span>;

<span class="tok-fn">echo</span> <span class="tok-str">"1. بداية الرصد للطالب: $studentName &lt;br&gt;"</span>;

<span class="tok-cmt">// الشرط: هل الدرجة أكبر من أو تساوي 50؟</span>
<span class="tok-kw">if</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">50</span>) {
    <span class="tok-fn">echo</span> <span class="tok-str">"2. القرار: الطالب ناجح ومبروك الترقية! 🎓&lt;br&gt;"</span>;
}

<span class="tok-fn">echo</span> <span class="tok-str">"3. نهاية البرنامج: تم حفظ السجل."</span>;

<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/flow_intro.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">1. بداية الرصد للطالب: عمر
2. القرار: الطالب ناجح ومبروك الترقية! 🎓
3. نهاية البرنامج: تم حفظ السجل.</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          🧭 <strong>التسلسل الخطي:</strong> السطر 1 والسطر 3 اتنفذوا إجباري لأنهم برة أي شرط.
        </div>
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          ⚡ <strong>بوابة التفرع (if):</strong> السطر 2 اتنفذ فقط لأن الشرط <code dir="ltr" style="direction: ltr; unicode-bidi: isolate; display: inline-block; background: rgba(0,0,0,0.35); padding: 0.1rem 0.45rem; border-radius: 4px; color: #fff;">$score &gt;= 50</code> قيمته <code dir="ltr">true</code>.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="التحكم في مسار الكود",
    notes_script="بنشرح هنا الفرق بين الكود الخطي اللي بيتنفذ كله ورا بعضه، وبين نقطة التفرع اللي بتسمح للبرنامج ياخد مسار مختلف لما الشرط يتحقق.",
    notes_list=[
        "مفهوم Linear Execution مقابل Conditional Branching",
        "مثال فحص النجاح لطالب حاصل على درجة 85"
    ]
)

# ==========================================
# SLIDE 04: SINGLE VS MULTI-LINE IF
# ==========================================
generate_slide(
    index=3,
    title="جملة if بسطر واحد وبأقواس معقوفة",
    eyebrow="بناء الجمل الشرطية — Syntax & Braces",
    slide_title="جملة if: سطر واحد ولا أقواس معقوفة {}؟ وفخ الإهمال",
    slide_text="PHP بتسمح بكتابة if بدون أقواس لو عندك أمر واحد بس، لكن دي أخطر عادة ممكن تقع فيها:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">if_syntax.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$score</span> = <span class="tok-num">40</span>; <span class="tok-cmt">// طالب راسب</span>

<span class="tok-cmt">// 1. سطر واحد بدون أقواس (شغال بس خطر):</span>
<span class="tok-kw">if</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">50</span>)
    <span class="tok-fn">echo</span> <span class="tok-str">"ألف مبروك النجاح!&lt;br&gt;"</span>;

<span class="tok-cmt">// 2. الفخ الخبيث: السطر التاني مش تابع للـ if!</span>
<span class="tok-kw">if</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">50</span>)
    <span class="tok-fn">echo</span> <span class="tok-str">"مبروك!&lt;br&gt;"</span>;
    <span class="tok-fn">echo</span> <span class="tok-str">"شهادتك جاهزة للاستلام! 📜&lt;br&gt;"</span>; <span class="tok-cmt">// هيتطبع دايماً!</span>

<span class="tok-cmt">// 3. الأسلوب الآمن والاحترافي (بالأقواس دايماً):</span>
<span class="tok-kw">if</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">50</span>) {
    <span class="tok-fn">echo</span> <span class="tok-str">"مبروك النجاح!&lt;br&gt;"</span>;
    <span class="tok-fn">echo</span> <span class="tok-str">"شهادتك جاهزة للاستلام! 📜&lt;br&gt;"</span>;
}
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/if_syntax.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #f87171; line-height: 1.6;">شهادتك جاهزة للاستلام! 📜</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fca5a5; line-height: 1.4; direction: rtl; text-align: right;">
          ⚠️ <strong>الفخ القاتل:</strong> لما تشيل الأقواس، جملة <code dir="ltr">if</code> بتتحكم في <strong>أول تعليمة بعدها فقط</strong>! السطر التاني بيعتبر كود مستقل تماماً وهيتنفذ حتى لو الطالب راسب!
        </div>
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          🛡️ <strong>القاعدة الذهبية:</strong> حتى لو عندك سطر واحد، استخدم الأقواس المعقوفة <code dir="ltr">{}</code> دايماً في مشاريعك لحماية كودك عند التعديل مستقبلاً.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="أقواس جملة if",
    notes_script="نقطة في غاية الأهمية: نسيان الأقواس بيخلي الطالب الراسب يستلم رسالة إن شهادته جاهزة! بنوضح ليه الأقواس المعقوفة إجبارية في الشغل الاحترافي.",
    notes_list=[
        "مقارنة if بسطر واحد مقابل الأقواس المعقوفة",
        "توضيح الخدعة البصرية للـ Indentation في PHP بدون أقواس"
    ]
)

# ==========================================
# SLIDE 05: IF / ELSE (BINARY DECISION)
# ==========================================
generate_slide(
    index=4,
    title="القرار الثنائي: if و else",
    eyebrow="اتخاذ القرار الثنائي — Binary Decision",
    slide_title="جملة if / else: إما النجاح أو الرسوب (مسار إجباري)",
    slide_text="لما يكون عندك خيارين مفيش تالت بينهم: لو الشرط صح نفذ المسار الأول، وغير كدة نفذ المسار التاني:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">if_else_grade.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>

<span class="tok-var">$score</span> = <span class="tok-num">68</span>;
<span class="tok-var">$passMark</span> = <span class="tok-num">50</span>;

<span class="tok-kw">if</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-var">$passMark</span>) {
    <span class="tok-fn">echo</span> <span class="tok-str">"النتيجة: ناجح بمجموع $score من 100 🎓&lt;br&gt;"</span>;
    <span class="tok-fn">echo</span> <span class="tok-str">"الحالة: مؤهل للتسجيل في المستوى التالي."</span>;
} <span class="tok-kw">else</span> {
    <span class="tok-fn">echo</span> <span class="tok-str">"النتيجة: راسب بمجموع $score من 100 ⚠️&lt;br&gt;"</span>;
    <span class="tok-fn">echo</span> <span class="tok-str">"الحالة: يلزم دخول اختبار الدور الثاني."</span>;
}

<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/if_else_grade.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">النتيجة: ناجح بمجموع 68 من 100 🎓
الحالة: مؤهل للتسجيل في المستوى التالي.</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          ⚖️ <strong>القرار الحاسم:</strong> مستحيل البلوكين يتنفذوا سوا، ومستحيل الاتنين يتهرب منهم! واحد منهم لازم يتنفذ حسب ناتج المقارنة.
        </div>
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          💡 <strong>القاعدة:</strong> لو الشرط رجع <code dir="ltr">true</code> بينفذ كود <code dir="ltr">if</code> ويتجاهل <code dir="ltr">else</code>، ولو رجع <code dir="ltr">false</code> بينفذ <code dir="ltr">else</code> فقط.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="القرار الثنائي if / else",
    notes_script="بنشرح بنية if / else الثنائية، ومثال فحص النجاح والرسوب، والتأكيد على إن مسار واحد فقط هو اللي بيتنفذ دائماً.",
    notes_list=[
        "بنية if / else وشروط الحتمية",
        "تطبيق عملي على درجة 68 من 100"
    ]
)

# ==========================================
# SLIDE 06: IF / ELSEIF / ELSE (GRADING LADDER)
# ==========================================
generate_slide(
    index=5,
    title="سلم التقديرات الأكاديمية: if / elseif / else",
    eyebrow="الخيارات المتعددة — Grading Ladder",
    slide_title="سلم التقديرات: if / elseif / else وسر الترتيب التنازلي",
    slide_text="لما يكون عندنا أكتر من حالتين، بنستخدم سلسلة elseif للمفاضلة بين التقديرات الأكاديمية بالترتيب:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">grading_ladder.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$score</span> = <span class="tok-num">88</span>;

<span class="tok-kw">if</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">85</span>) {
    <span class="tok-var">$grade</span> = <span class="tok-str">"A — ممتاز 🌟"</span>;
} <span class="tok-kw">elseif</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">75</span>) {
    <span class="tok-var">$grade</span> = <span class="tok-str">"B — جيد جداً 👍"</span>;
} <span class="tok-kw">elseif</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">65</span>) {
    <span class="tok-var">$grade</span> = <span class="tok-str">"C — جيد 📘"</span>;
} <span class="tok-kw">elseif</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">50</span>) {
    <span class="tok-var">$grade</span> = <span class="tok-str">"D — مقبول 📙"</span>;
} <span class="tok-kw">else</span> {
    <span class="tok-var">$grade</span> = <span class="tok-str">"F — راسب ⚠️"</span>;
}

<span class="tok-fn">echo</span> <span class="tok-str">"درجة الطالب: $score &lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"التقدير النهائي: $grade"</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/grading_ladder.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">درجة الطالب: 88
التقدير النهائي: A — ممتاز 🌟</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(251,191,36,0.08); border: 1px solid rgba(251,191,36,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fcd34d; line-height: 1.4; direction: rtl; text-align: right;">
          🎯 <strong>ليه بدأنا بـ 85 ونزلنا تنازلياً؟</strong> لو بدأنا بـ <code dir="ltr">$score &gt;= 50</code>، طالب الامتياز (95) هيدخل أول شرط ويطلع تقديره "مقبول" ويهرب من باقي الكود!
        </div>
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          ⚡ <strong>الخروج الفوري (Short-circuit):</strong> أول شرط يتحقق بينفذ كتلته ويخرج فوراً من الـ ladder بدون فحص باقي الشروط.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="سلم التقديرات if / elseif",
    notes_script="بنشرح هنا سلم التقديرات الأكاديمية (A, B, C, D, F) ونركز على سر الترتيب التنازلي للشروط عشان الشروط العامة متلغيش الشروط الخاصة.",
    notes_list=[
        "ترتيب الشروط من الأكبر للأصغر في التقديرات",
        "مفهوم الخروج الفوري بعد أول تطابق ناجح"
    ]
)

# ==========================================
# SLIDE 07: NESTED IF
# ==========================================
generate_slide(
    index=6,
    title="الشروط المتداخلة: Nested if",
    eyebrow="التحقق المزدوج — Nested Conditions",
    slide_title="الشروط المتداخلة (Nested if): الحضور والتفوق",
    slide_text="بنستخدم if جوة if لما يكون فحص الشرط التاني معتمد كلياً على تحقق الشرط الأول:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">nested_grades.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$hasAttendedFinal</span> = <span class="tok-kw">true</span>; <span class="tok-cmt">// هل حضر الاختبار؟</span>
<span class="tok-var">$score</span> = <span class="tok-num">94</span>;

<span class="tok-kw">if</span> (<span class="tok-var">$hasAttendedFinal</span>) {
    <span class="tok-cmt">// مش هنفحص الدرجة إلا لو حضر أصلاً:</span>
    <span class="tok-kw">if</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">50</span>) {
        <span class="tok-fn">echo</span> <span class="tok-str">"النتيجة: الطالب ناجح بمجموع $score 🎓&lt;br&gt;"</span>;
        
        <span class="tok-cmt">// شرط داخلي إضافي لمرتبة الشرف:</span>
        <span class="tok-kw">if</span> (<span class="tok-var">$score</span> &gt;= <span class="tok-num">90</span>) {
            <span class="tok-fn">echo</span> <span class="tok-str">"🌟 تكريم خاص: مؤهل لمرتبة الشرف الأولى!"</span>;
        }
    } <span class="tok-kw">else</span> {
        <span class="tok-fn">echo</span> <span class="tok-str">"حضر الاختبار لكن النتيجة: راسب."</span>;
    }
} <span class="tok-kw">else</span> {
    <span class="tok-fn">echo</span> <span class="tok-str">"⚠️ غائب عن الامتحان — محجوب النتيجة تماماً."</span>;
}
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/nested_grades.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">النتيجة: الطالب ناجح بمجموع 94 🎓
🌟 تكريم خاص: مؤهل لمرتبة الشرف الأولى!</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          🚪 <strong>مستويات التفرع:</strong> الكود مش هيبص على الدرجة إلا لو شرط الحضور <code dir="ltr">true</code>. لو غائب بيروح فوراً لـ <code dir="ltr">else</code> الخارجية.
        </div>
        <div style="background: rgba(251,191,36,0.08); border: 1px solid rgba(251,191,36,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fcd34d; line-height: 1.4; direction: rtl; text-align: right;">
          💡 <strong>قاعدة نظافة الكود (Clean Code):</strong> حاول متخليش الشروط المتداخلة تزيد عن مستويين عشان الكود ميبقاش معقد وصعب الصيانة.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="الشروط المتداخلة Nested if",
    notes_script="بنشرح فكرة الشروط المتداخلة: فحص حضور الامتحان أولاً، بعدين فحص النجاح، وبعدين فحص التكريم لمرتبة الشرف.",
    notes_list=[
        "استخدام Nested if في التحقق التتابعي",
        "نصيحة تجنب التداخل المفرط (Arrow Anti-pattern)"
    ]
)

# ==========================================
# SLIDE 08: CALCULATOR WITH IF
# ==========================================
generate_slide(
    index=7,
    title="مشروع تطبيقي: آلة حاسبة باستخدام if",
    eyebrow="مشروع عملي 1 — Calculator with if",
    slide_title="بناء آلة حاسبة كاملة بـ if / elseif وحماية الصفر",
    slide_text="تطبيق متكامل لاختيار العملية الحسابية، مع حماية برمجية حاسمة تمنع انهيار السيرفر عند القسمة على صفر:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">calc_if.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$num1</span> = <span class="tok-num">20</span>;
<span class="tok-var">$num2</span> = <span class="tok-num">4</span>;
<span class="tok-var">$op</span> = <span class="tok-str">'/'</span>; <span class="tok-cmt">// جرب: +, -, *, /, %</span>

<span class="tok-kw">if</span> (<span class="tok-var">$op</span> === <span class="tok-str">'+'</span>) {
    <span class="tok-var">$res</span> = <span class="tok-var">$num1</span> + <span class="tok-var">$num2</span>;
} <span class="tok-kw">elseif</span> (<span class="tok-var">$op</span> === <span class="tok-str">'-'</span>) {
    <span class="tok-var">$res</span> = <span class="tok-var">$num1</span> - <span class="tok-var">$num2</span>;
} <span class="tok-kw">elseif</span> (<span class="tok-var">$op</span> === <span class="tok-str">'*'</span>) {
    <span class="tok-var">$res</span> = <span class="tok-var">$num1</span> * <span class="tok-var">$num2</span>;
} <span class="tok-kw">elseif</span> (<span class="tok-var">$op</span> === <span class="tok-str">'/'</span>) {
    <span class="tok-kw">if</span> (<span class="tok-var">$num2</span> == <span class="tok-num">0</span>) {
        <span class="tok-var">$res</span> = <span class="tok-str">"خطأ: غير مسموح بالقسمة على صفر!"</span>;
    } <span class="tok-kw">else</span> {
        <span class="tok-var">$res</span> = <span class="tok-var">$num1</span> / <span class="tok-var">$num2</span>;
    }
} <span class="tok-kw">elseif</span> (<span class="tok-var">$op</span> === <span class="tok-str">'%'</span>) {
    <span class="tok-var">$res</span> = <span class="tok-var">$num1</span> % <span class="tok-var">$num2</span>;
} <span class="tok-kw">else</span> {
    <span class="tok-var">$res</span> = <span class="tok-str">"معامل حسابي غير صالح!"</span>;
}

<span class="tok-fn">echo</span> <span class="tok-str">"العملية: $num1 $op $num2 = $res"</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/calc_if.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #2dd6e6; line-height: 1.6; font-weight: 700;">العملية: 20 / 4 = 5</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fca5a5; line-height: 1.4; direction: rtl; text-align: right;">
          🛡️ <strong>فحص القسمة على صفر (DivisionByZeroError):</strong> في PHP 8، لو قسمت على صفر الكود هيعمل Fatal Exception! فحص <code dir="ltr">$num2 == 0</code> جوة شرط القسمة بيحمي السيرفر.
        </div>
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          ⚙️ <strong>أمان المقارنة الصارمة:</strong> قارنا بـ <code dir="ltr">===</code> عشان نتأكد من الرمز الحسابي ونوعه بدقة.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="مشروع الآلة الحاسبة بـ if",
    notes_script="بنطبق كل اللي اتعلمناه في بناء آلة حاسبة تفحص العمليات الحسابية الخمس، مع التأكيد على حماية القسمة على صفر لتفادي الـ Fatal Errors.",
    notes_list=[
        "تنفيذ العمليات الحسابية بواسطة if / elseif",
        "الحماية من خطأ DivisionByZeroError في PHP 8"
    ]
)

# ==========================================
# SLIDE 09: MIN AND MAX OF 2 NUMBERS
# ==========================================
generate_slide(
    index=8,
    title="تحديد الأصغر والأكبر بين عددين",
    eyebrow="خوارزميات المقارنة — Min & Max of 2",
    slide_title="أصغر وأكبر درجة بين طالبين باستخدام if / else",
    slide_text="مقارنة بسيطة بين قيمتين لمعرفة الدرجة العظمى والصغرى مع مراعاة حالة التساوي:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">min_max_2.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$score1</span> = <span class="tok-num">78</span>; <span class="tok-cmt">// درجة الطالب الأول</span>
<span class="tok-var">$score2</span> = <span class="tok-num">92</span>; <span class="tok-cmt">// درجة الطالب الثاني</span>

<span class="tok-kw">if</span> (<span class="tok-var">$score1</span> &gt; <span class="tok-var">$score2</span>) {
    <span class="tok-var">$max</span> = <span class="tok-var">$score1</span>;
    <span class="tok-var">$min</span> = <span class="tok-var">$score2</span>;
} <span class="tok-kw">elseif</span> (<span class="tok-var">$score2</span> &gt; <span class="tok-var">$score1</span>) {
    <span class="tok-var">$max</span> = <span class="tok-var">$score2</span>;
    <span class="tok-var">$min</span> = <span class="tok-var">$score1</span>;
} <span class="tok-kw">else</span> {
    <span class="tok-var">$max</span> = <span class="tok-var">$score1</span>;
    <span class="tok-var">$min</span> = <span class="tok-var">$score1</span>;
    <span class="tok-fn">echo</span> <span class="tok-str">"الدرجتان متساويتان!&lt;br&gt;"</span>;
}

<span class="tok-fn">echo</span> <span class="tok-str">"الدرجة العظمى (Max): "</span> . <span class="tok-var">$max</span> . <span class="tok-str">"&lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"الدرجة الصغرى (Min): "</span> . <span class="tok-var">$min</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/min_max_2.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">الدرجة العظمى (Max): 92
الدرجة الصغرى (Min): 78</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          📊 <strong>المنطق الرياضي:</strong> لما نقارن قيمتين، لو الأولى أكبر بتكون هي الـ Max والتانية هي الـ Min، والعكس تماماً لو التانية أكبر.
        </div>
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          🤝 <strong>تغطية حالة التساوي:</strong> فرع <code dir="ltr">else</code> الأخير بيضمن عدم حدوث أي خطأ منطقي لو الطالبين جابوا نفس الدرجة.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="أصغر وأكبر رقم بين عددين",
    notes_script="بنشرح كيفية استخراج الأصغر والأكبر بين درجتين مع التعامل مع احتمالية تساويهما بأسلوب شرطي نظيف.",
    notes_list=[
        "مقارنة درجتين وتحديد Min و Max",
        "معالجة حالة التساوي كشرط بديل"
    ]
)

# ==========================================
# SLIDE 10: MIN OF 3 - WAY 1 (DIRECT LADDER)
# ==========================================
generate_slide(
    index=9,
    title="أصغر رقم بين 3 أرقام: الطريقة الأولى",
    eyebrow="مقارنة 3 قيم — Min of 3 (Way 1)",
    slide_title="أصغر درجة بين 3 مواد: المقارنة المباشرة (Direct Ladder)",
    slide_text="الطريقة البديهية: مقارنة كل متغير بالاثنين التانيين باستخدام بوابة &amp;&amp; المنطقية:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">min_way1.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$math</span> = <span class="tok-num">85</span>;
<span class="tok-var">$physics</span> = <span class="tok-num">62</span>;
<span class="tok-var">$english</span> = <span class="tok-num">94</span>;

<span class="tok-cmt">// الطريقة 1: الشروط المنطقية المباشرة (&amp;&amp;)</span>
<span class="tok-kw">if</span> (<span class="tok-var">$math</span> &lt;= <span class="tok-var">$physics</span> &amp;&amp; <span class="tok-var">$math</span> &lt;= <span class="tok-var">$english</span>) {
    <span class="tok-var">$min</span> = <span class="tok-var">$math</span>;
} <span class="tok-kw">elseif</span> (<span class="tok-var">$physics</span> &lt;= <span class="tok-var">$math</span> &amp;&amp; <span class="tok-var">$physics</span> &lt;= <span class="tok-var">$english</span>) {
    <span class="tok-var">$min</span> = <span class="tok-var">$physics</span>;
} <span class="tok-kw">else</span> {
    <span class="tok-var">$min</span> = <span class="tok-var">$english</span>;
}

<span class="tok-fn">echo</span> <span class="tok-str">"درجات المواد: 85, 62, 94 &lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"أقل درجة (الطريقة 1): "</span> . <span class="tok-var">$min</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/min_way1.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">درجات المواد: 85, 62, 94
أقل درجة (الطريقة 1): 62</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          💡 <strong>الفكرة:</strong> بنسأل: هل الأول أصغر من التاني والتالت؟ لو لأ، هل التاني أصغر من الأول والتالت؟ لو لأ، يبقى أكيد التالت هو الأصغر.
        </div>
        <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fca5a5; line-height: 1.4; direction: rtl; text-align: right;">
          ⚠️ <strong>عيوب الطريقة:</strong> كود طويل ومكرر، وتخيل لو عندك 5 أو 10 مواد دراسية! الشروط هتبقى مستحيلة التوسيع.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="أصغر رقم بين 3: الطريقة الأولى",
    notes_script="بنشرح الطريقة الأولى البديهية باستخدام الشروط المباشرة، ونوضح عيبها الأكبر وهو عدم قابليتها للتوسع لو زادت الأرقام.",
    notes_list=[
        "مقارنة 3 قيم بالـ if / elseif ومحددات &&",
        "توضيح أسباب عدم صلاحية هذا الأسلوب للأعداد الكبيرة"
    ]
)

# ==========================================
# SLIDE 11: MIN OF 3 - WAY 2 (ACCUMULATOR)
# ==========================================
generate_slide(
    index=10,
    title="أصغر رقم بين 3 أرقام: الطريقة الثانية",
    eyebrow="أسلوب خوارزمية التراكم — Min of 3 (Way 2)",
    slide_title="أسلوب الافتراض والتحديث: الطريقة الخوارزمية الأذكى",
    slide_text="طريقة المحترفين: نفترض أن الأول هو الأصغر، ونقارن الباقيين بيه بالتتابع ونحدّثه لو لقينا أصغر منه:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">min_way2.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$math</span> = <span class="tok-num">85</span>;
<span class="tok-var">$physics</span> = <span class="tok-num">62</span>;
<span class="tok-var">$english</span> = <span class="tok-num">94</span>;

<span class="tok-cmt">// الطريقة 2: افتراض المبدأ وتحديثه (Accumulator Pattern)</span>
<span class="tok-var">$min</span> = <span class="tok-var">$math</span>; <span class="tok-cmt">// 1. نفترض إن أول مادة هي الأقل مبدئياً</span>

<span class="tok-kw">if</span> (<span class="tok-var">$physics</span> &lt; <span class="tok-var">$min</span>) {
    <span class="tok-var">$min</span> = <span class="tok-var">$physics</span>; <span class="tok-cmt">// 2. لقينا مادة أقل، نحدّث الـ min</span>
}

<span class="tok-kw">if</span> (<span class="tok-var">$english</span> &lt; <span class="tok-var">$min</span>) {
    <span class="tok-var">$min</span> = <span class="tok-var">$english</span>; <span class="tok-cmt">// 3. نقارن التالتة بالـ min الحالي</span>
}

<span class="tok-fn">echo</span> <span class="tok-str">"أقل درجة (بالتراكم الخوارزمي): "</span> . <span class="tok-var">$min</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/min_way2.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #34d399; line-height: 1.6; font-weight: 700;">أقل درجة (بالتراكم الخوارزمي): 62</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          🏆 <strong>ليه دي أفضل طريقة خوارزمية؟</strong>
          <br/>1. مفيش شروط مركبة معقدة (<code dir="ltr">&amp;&amp;</code>).
          <br/>2. استهلكت فقط 2 مقارنات بسيطة.
        </div>
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          🚀 <strong>القابلية للتوسع:</strong> دي نفس الفكرة الرياضية اللي بنستخدمها للبحث عن أصغر عنصر وسط مصفوفة فيها 10,000 رقم داخل Loop!
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="أصغر رقم بين 3: أسلوب التراكم",
    notes_script="بنشرح النمط الخوارزمي الذهبي (Accumulator Pattern) اللي بيفترض الأول كأصغر عنصر ويحدثه تدريجياً، ونوضح ليه ده الأساس لأي Loop.",
    notes_list=[
        "فكرة الافتراض وتحديث القيمة الصغرى",
        "توفير المقارنات وسهولة التطبيق على مصفوفات"
    ]
)

# ==========================================
# SLIDE 12: MIN OF 3 - WAY 3 (BUILT-IN & TERNARY)
# ==========================================
generate_slide(
    index=11,
    title="أصغر رقم بين 3 أرقام: الطريقة الثالثة",
    eyebrow="الدوال الجاهزة والمعامل الثلاثي — Min of 3 (Way 3)",
    slide_title="دالة min() الجاهزة والمعامل الثلاثي (Ternary Operator)",
    slide_text="في الحياة العملية، PHP بتوفر دالة مدمجة سريعة، وبنقدر كمان ننفذها بالمعامل الشرطي الثلاثي:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">min_way3.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$math</span> = <span class="tok-num">85</span>;
<span class="tok-var">$physics</span> = <span class="tok-num">62</span>;
<span class="tok-var">$english</span> = <span class="tok-num">94</span>;

<span class="tok-cmt">// 1. الدالة المدمجة الجاهزة في PHP (الخيار العملي الأول):</span>
<span class="tok-var">$minBuiltIn</span> = <span class="tok-fn">min</span>(<span class="tok-var">$math</span>, <span class="tok-var">$physics</span>, <span class="tok-var">$english</span>);

<span class="tok-cmt">// 2. المعامل الشرطي الثلاثي المتداخل (Ternary Operator):</span>
<span class="tok-var">$minTernary</span> = (<span class="tok-var">$math</span> &lt; <span class="tok-var">$physics</span>)
    ? ((<span class="tok-var">$math</span> &lt; <span class="tok-var">$english</span>) ? <span class="tok-var">$math</span> : <span class="tok-var">$english</span>)
    : ((<span class="tok-var">$physics</span> &lt; <span class="tok-var">$english</span>) ? <span class="tok-var">$physics</span> : <span class="tok-var">$english</span>);

<span class="tok-fn">echo</span> <span class="tok-str">"باستخدام دالة min(): "</span> . <span class="tok-var">$minBuiltIn</span> . <span class="tok-str">"&lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"باستخدام Ternary: "</span> . <span class="tok-var">$minTernary</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/min_way3.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">باستخدام دالة min(): 62
باستخدام Ternary: 62</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          ⚡ <strong>دالة min() الجاهزة:</strong> في كود الإنتاج (Production)، دايماً استخدم دالة <code dir="ltr">min()</code> لأنها مبنية ومكتوبة بـ C في قلب محرك PHP وسريعة جداً.
        </div>
        <div style="background: rgba(251,191,36,0.08); border: 1px solid rgba(251,191,36,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fcd34d; line-height: 1.4; direction: rtl; text-align: right;">
          🧩 <strong>تمرين المعامل الثلاثي:</strong> تدريب ممتاز للمنطق، لكن تجنب كتابة شروط ثلاثية متداخلة طويلة في المشاريع الواقعية عشان سهولة القراءة.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="أصغر رقم بين 3: الدوال الجاهزة و Ternary",
    notes_script="بنستعرض الطريقة الثالثة العملية عبر دالة min() المدمجة في PHP، وبنقارنها بالمعامل الشرطي الثلاثي المتداخل لتدريب التفكير المنطقي.",
    notes_list=[
        "استخدام دالة min() المدمجة في PHP",
        "تطبيق Ternary Operator متداخل للمقارنة"
    ]
)

# ==========================================
# SLIDE 13: CAUTION: IF ($AGE = 5)
# ==========================================
generate_slide(
    index=12,
    title="الفخ القاتل: الإسناد بدل المقارنة",
    eyebrow="أخطر أخطاء المبتدئين — Assignment Trap",
    slide_title="كارثة if ($score = 85): الإسناد بدل المقارنة!",
    slide_text="واحد من أخبث الـ Bugs اللي ممكن تضيع ساعات في تتبعها: كتابة = واحدة بدل == أو === داخل الشرط:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">assignment_bug.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$score</span> = <span class="tok-num">40</span>; <span class="tok-cmt">// طالب راسب في الأصل!</span>

<span class="tok-cmt">// الفخ: كتبنا = واحدة بدل ==</span>
<span class="tok-kw">if</span> (<span class="tok-var">$score</span> = <span class="tok-num">85</span>) {
    <span class="tok-fn">echo</span> <span class="tok-str">"طبع: مبروك النجاح بامتياز! ❌ (كارثة!)&lt;br&gt;"</span>;
}

<span class="tok-fn">echo</span> <span class="tok-str">"قيمة المتغير اتغيرت لـ: "</span> . <span class="tok-var">$score</span> . <span class="tok-str">"&lt;br&gt;"</span>;

<span class="tok-cmt">// تجربة مع الصفر:</span>
<span class="tok-kw">if</span> (<span class="tok-var">$score</span> = <span class="tok-num">0</span>) {
    <span class="tok-fn">echo</span> <span class="tok-str">"ده مش هيتطبع أبداً لأن 0 يعتبر False!"</span>;
}
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/assignment_bug.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #f87171; line-height: 1.6;">طبع: مبروك النجاح بامتياز! ❌ (كارثة!)
قيمة المتغير اتغيرت لـ: 85</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fca5a5; line-height: 1.4; direction: rtl; text-align: right;">
          💥 <strong>ليه الكارثة دي بتحصل؟</strong>
          <br/>1. <code dir="ltr">$score = 85</code> عملية إسناد بتغير قيمة المتغير نفسه وترجع 85.
          <br/>2. أي رقم غير الصفر بيعتبر في PHP قيمة صحيحة (<code dir="ltr">true</code>).
          <br/>3. فالـ <code dir="ltr">if</code> بتدخل تنفذ الكود دايماً وتغير نتيجة الطالب!
        </div>
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          🛡️ <strong>حيلة الحماية (Yoda Conditions):</strong> اكتب القيمة الثابتة على الشمال: <code dir="ltr">if (85 === $score)</code>. لو نسيت وكتبت <code dir="ltr">=</code> واحدة، PHP هيطلع Fatal Error فوري ويحميك من الكارثة!
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="فخ الإسناد داخل if",
    notes_script="شرح تفصيلي للخطأ القاتل: كتابة علامة يساوي واحدة بدل المقارنة، وإزاي ده بيغير قيمة المتغير نفسه ويدخل في الشرط دايماً، وحيلة Yoda condition لحماية الكود.",
    notes_list=[
        "شرح الفرق بين Assignment = و Comparison ==",
        "تأثير Truthy للقيم المسندة وسلوك الصفر",
        "تقنية شروط يودا (Yoda Conditions) لتفادي الخطأ"
    ]
)

# ==========================================
# SLIDE 14: SUMMARY OF IF STATEMENTS
# ==========================================
generate_slide(
    index=13,
    title="ملخص وقواعد عائلة if",
    eyebrow="ملخص وقواعد — Summary of if",
    slide_title="دليل اتخاذ القرارات: متى تستخدم كل نمط من عائلة if؟",
    slide_text="خريطة ذهنية سريعة لاختيار البنية الشرطية المناسبة لمشروعك:",
    body_content='''<div class="summary-grid">
  <div class="summary-box">
    <h3>1. جملة if المنفردة</h3>
    <p>تستخدم لما يكون عندك <strong>إجراء واحد إضافي</strong> هيتنفذ فقط لو الشرط اتحقق، ومفيش أي بديل لو الشرط ما اتحققش (زي إرسال تنبيه أو إضافة بونص).</p>
    <div class="sum-code">if ($score &gt;= 90) addBonus();</div>
  </div>

  <div class="summary-box">
    <h3>2. جملة if / else الثنائية</h3>
    <p>تستخدم لما يكون عندك <strong>مساران متنافيان تماماً</strong> (إما أبيض أو أسود)، والبرنامج لازم يسلك واحد منهم إجبارياً (زي ناجح أو راسب).</p>
    <div class="sum-code">if ($pass) { ... } else { ... }</div>
  </div>

  <div class="summary-box">
    <h3>3. جملة if / elseif / else</h3>
    <p>تستخدم للمفاضلة بين <strong>نطاقات متعددة (Ranges)</strong>. القاعدة الذهبية: رتب الشروط تنازلياً من الأضيق والأكبر للأوسع عشان متلغيش بعض.</p>
    <div class="sum-code">if (&gt;=85) .. elseif (&gt;=75) .. else</div>
  </div>

  <div class="summary-box">
    <h3>4. القواعد الذهبية النظيفة</h3>
    <p>• الأقواس المعقوفة <code dir="ltr">{}</code> أمان إجباري لكودك.<br/>• احذر تماماً من فخ <code dir="ltr">=</code> داخل الشرط.<br/>• تجنب الشروط المتداخلة العميقة (Deep Nesting) واستخدم Guard Clauses.</p>
    <div class="sum-code">// Always use === &amp; Braces!</div>
  </div>
</div>''',
    notes_title="ملخص وقواعد عائلة if",
    notes_script="ملخص شامل لأنماط if الأربعة وقواعد كتابة الشروط النظيفة لتلخيص النصف الأول من المحاضرة قبل الانتقال لـ switch و match.",
    notes_list=[
        "المقارنة بين if و if/else و if/elseif",
        "القواعد الذهبية لكتابة شروط نظيفة وآمنة"
    ]
)

# ==========================================
# SLIDE 15: SWITCH STATEMENT BASICS
# ==========================================
generate_slide(
    index=14,
    title="جملة الاختيار المتعدد: switch",
    eyebrow="الاختيار المتعدد — Switch Statement",
    slide_title="جملة switch: مطابقة التقديرات المحددة بدقة",
    slide_text="لما تكون بتقارن متغير واحد بقيم محددة وثابتة (زي حروف التقديرات A, B, C)، بتكون switch خيار منظم وأنيق:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">switch_grades.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$gradeLetter</span> = <span class="tok-str">'B'</span>;

<span class="tok-kw">switch</span> (<span class="tok-var">$gradeLetter</span>) {
    <span class="tok-kw">case</span> <span class="tok-str">'A'</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"تقدير امتياز: أداء استثنائي رائع! 🌟"</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">case</span> <span class="tok-str">'B'</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"تقدير جيد جداً: مستوى متقدم وممتاز 👍"</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">case</span> <span class="tok-str">'C'</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"تقدير جيد: بداية طريق التطور 📘"</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">case</span> <span class="tok-str">'D'</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"تقدير مقبول: نجحت ولكن على الحافة 📙"</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">case</span> <span class="tok-str">'F'</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"تقدير راسب: يلزم دخول الدور الثاني ⚠️"</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">default</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"حرف التقدير المدخل غير معروف في النظام!"</span>;
}
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/switch_grades.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">تقدير جيد جداً: مستوى متقدم وممتاز 👍</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          🔑 <strong>أركان switch الأساسية:</strong>
          <br/>• <code dir="ltr">case</code>: القيمة المتوقع مطابقتها مع المتغير.
          <br/>• <code dir="ltr">break</code>: أمر التوقف الفوري والخروج من البلوك.
          <br/>• <code dir="ltr">default</code>: يتنفذ لو مفيش أي حالة طابقت (شبه else).
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="أساسيات جملة switch",
    notes_script="بنشرح جملة switch ومطابقتها للقيم الثابتة لحروف التقديرات (A, B, C, D, F) مع توضيح عناصرها الثلاثة: case و break و default.",
    notes_list=[
        "بنية switch ومطابقة الحالات الثابتة",
        "وظيفة case و break و default"
    ]
)

# ==========================================
# SLIDE 16: SWITCH FALLTHROUGH & THE BREAK
# ==========================================
generate_slide(
    index=15,
    title="ظاهرة السقوط Fallthrough وأهمية break",
    eyebrow="أسرار switch — Fallthrough & Grouping",
    slide_title="أسرار switch: ظاهرة Fallthrough ودمج الحالات",
    slide_text="إيه اللي بيحصل لو شيلت كلمة break؟ الكود بيسقط في الحالات التالية! وده ليه ميزة خطيرة وعيب أخطر:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">fallthrough.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$grade</span> = <span class="tok-str">'A'</span>;

<span class="tok-cmt">// 1. الاستخدام الذكي: دمج الحالات (Grouping):</span>
<span class="tok-kw">switch</span> (<span class="tok-var">$grade</span>) {
    <span class="tok-kw">case</span> <span class="tok-str">'A'</span>:
    <span class="tok-kw">case</span> <span class="tok-str">'B'</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"1. تهانينا: أنت من قائمة الشرف والمرشحين للمنحة! 🎓&lt;br&gt;"</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">case</span> <span class="tok-str">'C'</span>:
    <span class="tok-kw">case</span> <span class="tok-str">'D'</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"1. أنت ناجح ولكن بدون منحة.&lt;br&gt;"</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">default</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"1. راسب أو غير مسجل.&lt;br&gt;"</span>;
}

<span class="tok-cmt">// 2. الكارثة لو نسيت break بالخطأ:</span>
<span class="tok-var">$test</span> = <span class="tok-str">'A'</span>;
<span class="tok-kw">switch</span> (<span class="tok-var">$test</span>) {
    <span class="tok-kw">case</span> <span class="tok-str">'A'</span>: <span class="tok-fn">echo</span> <span class="tok-str">"2. مرحلة 1 - "</span>; <span class="tok-cmt">// نسينا break!</span>
    <span class="tok-kw">case</span> <span class="tok-str">'B'</span>: <span class="tok-fn">echo</span> <span class="tok-str">"مرحلة 2 - "</span>;   <span class="tok-cmt">// نسينا break!</span>
    <span class="tok-kw">default</span>:  <span class="tok-fn">echo</span> <span class="tok-str">"النهاية!"</span>;
}
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/fallthrough.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">1. تهانينا: أنت من قائمة الشرف والمرشحين للمنحة! 🎓
2. مرحلة 1 - مرحلة 2 - النهاية!</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          🎯 <strong>الدمج المقصود (Grouping Cases):</strong> بنرص <code dir="ltr">case 'A': case 'B':</code> ورا بعض بدون break عشان ينفذوا نفس الكود المشترك.
        </div>
        <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fca5a5; line-height: 1.4; direction: rtl; text-align: right;">
          🚪 <strong>خطر السقوط (Accidental Fallthrough):</strong> لو نسيت <code dir="ltr">break</code> بالصدفة، الكود هينزلق وينفذ كل الحالات اللي بعدها حتى لو مش متطابقة!
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="ظاهرة Fallthrough في switch",
    notes_script="بنشرح السلاح ذو الحدين لـ switch: ميزة دمج الحالات زي A و B لقائمة الشرف، وعيب السقوط العرضي لما المبرمج ينسى break.",
    notes_list=[
        "دمج الحالات المتعددة في switch",
        "تأثير نسيان break وحدوث Fallthrough غير مقصود"
    ]
)

# ==========================================
# SLIDE 17: CALCULATOR WITH SWITCH
# ==========================================
generate_slide(
    index=16,
    title="مشروع تطبيقي: آلة حاسبة باستخدام switch",
    eyebrow="مشروع عملي 2 — Calculator with switch",
    slide_title="آلة حاسبة متكاملة باستخدام switch وأنظف كود",
    slide_text="إعادة بناء الآلة الحاسبة بـ switch لملاحظة الفرق في قراءة الكود ونظافته مقارنة بالـ if:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">calc_switch.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$num1</span> = <span class="tok-num">15</span>;
<span class="tok-var">$num2</span> = <span class="tok-num">3</span>;
<span class="tok-var">$op</span> = <span class="tok-str">'*'</span>;

<span class="tok-kw">switch</span> (<span class="tok-var">$op</span>) {
    <span class="tok-kw">case</span> <span class="tok-str">'+'</span>:
        <span class="tok-var">$res</span> = <span class="tok-var">$num1</span> + <span class="tok-var">$num2</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">case</span> <span class="tok-str">'-'</span>:
        <span class="tok-var">$res</span> = <span class="tok-var">$num1</span> - <span class="tok-var">$num2</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">case</span> <span class="tok-str">'*'</span>:
        <span class="tok-var">$res</span> = <span class="tok-var">$num1</span> * <span class="tok-var">$num2</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">case</span> <span class="tok-str">'/'</span>:
        <span class="tok-var">$res</span> = (<span class="tok-var">$num2</span> == <span class="tok-num">0</span>) ? <span class="tok-str">"خطأ: قسمة على صفر!"</span> : (<span class="tok-var">$num1</span> / <span class="tok-var">$num2</span>);
        <span class="tok-kw">break</span>;
    <span class="tok-kw">case</span> <span class="tok-str">'%'</span>:
        <span class="tok-var">$res</span> = <span class="tok-var">$num1</span> % <span class="tok-var">$num2</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">default</span>:
        <span class="tok-var">$res</span> = <span class="tok-str">"عملية حسابية غير معروفة!"</span>;
        <span class="tok-kw">break</span>;
}

<span class="tok-fn">echo</span> <span class="tok-str">"الناتج: $num1 $op $num2 = $res"</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/calc_switch.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #2dd6e6; line-height: 1.6; font-weight: 700;">الناتج: 15 * 3 = 45</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          🧼 <strong>النظافة والترتيب (Clean Code):</strong> في مقارنة متغير واحد بعدة احتمالات ثابتة، الـ <code dir="ltr">switch</code> بتكون أوضح في القراءة بمراحل من تكرار <code dir="ltr">if ($op == ...) elseif ($op == ...)</code>.
        </div>
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          🎯 <strong>حماية الصفر بالمعامل الثلاثي:</strong> دمجنا شرط حماية الصفر السريع بسطر واحد جوة <code dir="ltr">case '/'</code> لاختصار الكود.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="مشروع الآلة الحاسبة بـ switch",
    notes_script="بنعيد بناء الآلة الحاسبة باستخدام switch، ونقارن بينها وبين كود if/elseif لنرى كيف توفر switch وضوحاً وتنظيماً فائقاً.",
    notes_list=[
        "بناء آلة حاسبة منظمة بجملة switch",
        "دمج فحص القسمة على صفر بسطر واحد"
    ]
)

# ==========================================
# SLIDE 18: THE MODERN MATCH EXPRESSION
# ==========================================
generate_slide(
    index=17,
    title="تعبير match الحديث في PHP 8+",
    eyebrow="ثورة PHP 8 الحديثة — match Expression",
    slide_title="تعبير match الحديث: البديل الصارم والأذكى لـ switch",
    slide_text="في PHP 8 تم تقديم match كثورة حقيقية: بترجع قيمة مباشرة، صارمة في الأنواع، ومفيهاش وجع دماغ break:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">match_grades.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$gradeLetter</span> = <span class="tok-str">'B'</span>;

<span class="tok-cmt">// تعبير match بيرجع قيمة تقدر تسندها لمتغير مباشرة:</span>
<span class="tok-var">$message</span> = <span class="tok-kw">match</span> (<span class="tok-var">$gradeLetter</span>) {
    <span class="tok-str">'A'</span>        =&gt; <span class="tok-str">"امتياز مع مرتبة الشرف 🌟"</span>,
    <span class="tok-str">'B'</span>        =&gt; <span class="tok-str">"جيد جداً مع شهادة تقدير 👍"</span>,
    <span class="tok-str">'C'</span>        =&gt; <span class="tok-str">"جيد ومستوى طيب 📘"</span>,
    <span class="tok-str">'D'</span>        =&gt; <span class="tok-str">"مقبول على الحافة 📙"</span>,
    <span class="tok-str">'F'</span>        =&gt; <span class="tok-str">"راسب يلزم إعادة الاختبار ⚠️"</span>,
    <span class="tok-kw">default</span>    =&gt; <span class="tok-str">"تقدير غير مسجل!"</span>,
};

<span class="tok-fn">echo</span> <span class="tok-str">"التقدير: $gradeLetter &lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"الرسالة: $message"</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/match_grades.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">التقدير: B
الرسالة: جيد جداً مع شهادة تقدير 👍</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          🚀 <strong>ليه match أفضل بكتير من switch؟</strong>
          <br/>1. <strong>Expression:</strong> بترجع قيمة مباشرة تتخزن في متغير.
          <br/>2. <strong>مفيش break:</strong> مستحيل يحصل Fallthrough بالخطأ!
          <br/>3. <strong>Strict Comparison (<code dir="ltr">===</code>):</strong> مقارنة صارمة وآمنة للأنواع.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="تعبير match في PHP 8+",
    notes_script="بنشرح تعبير match الجديد في PHP 8، وكيف يعتبر نقلة نوعية في كتابة الشروط الآمنة لأنه expression يرجع قيمة ومقارنته صارمة ولا يحتاج break.",
    notes_list=[
        "مفهوم match Expression في PHP 8",
        "المقارنة الصارمة وغياب الحاجة لكلمة break"
    ]
)

# ==========================================
# SLIDE 19: HEAD-TO-HEAD: SWITCH VS MATCH
# ==========================================
generate_slide(
    index=18,
    title="المواجهة الحاسمة: switch مقابل match",
    eyebrow="مقارنة المعايير — switch vs match",
    slide_title="المواجهة: متى تختار switch ومتى تختار match؟",
    slide_text="جدول الفروق الجوهرية اللي هيحدد اختيارك البرمجي في مشاريع Laravel وسوق العمل:",
    body_content='''<div class="summary-grid" style="grid-template-columns: 1fr 1fr;">
  <div class="summary-box" style="border-top-color: #f59e0b;">
    <h3 style="color: #fbbf24;">جملة switch التقليدية</h3>
    <p>• <strong>طبيعتها:</strong> Statement (كتلة تعليمات لا ترجع قيمة مباشرة).<br/>
    • <strong>المقارنة:</strong> رخوة Loose (<code dir="ltr">==</code>) فتقبل تحويل الأنواع التلقائي.<br/>
    • <strong>التوقف:</strong> يلزم كتابة <code dir="ltr">break;</code> وإلا هيحصل Fallthrough.<br/>
    • <strong>إهمال حالة:</strong> لو مفيش تطابق ومفيش default بيعدي بصمت.<br/>
    • <strong>الاستخدام الأفضل:</strong> لما يكون لكل حالة بلوك كود طويل فيه سطور كتيرة.</p>
    <div class="sum-code">switch ($x) { case 1: doSomething(); break; }</div>
  </div>

  <div class="summary-box" style="border-top-color: #10b981;">
    <h3 style="color: #34d399;">تعبير match الحديث (PHP 8+)</h3>
    <p>• <strong>طبيعتها:</strong> Expression (تعبير يرجع قيمة مباشرة للمتغير).<br/>
    • <strong>المقارنة:</strong> صارمة Strict (<code dir="ltr">===</code>) بدون أي تحويل أنواع عشوائي.<br/>
    • <strong>التوقف:</strong> مفيش break إطلاقاً، ومستحيل يسقط في الحالات التانية.<br/>
    • <strong>إهمال حالة:</strong> بيرمي <code dir="ltr">UnhandledMatchError</code> لحمايتك!<br/>
    • <strong>الاستخدام الأفضل:</strong> مطابقة قيمة وإرجاع نتيجة (Mapping) في سطر واحد.</p>
    <div class="sum-code">$res = match($x) { 1 =&gt; 'One', default =&gt; 'Other' };</div>
  </div>
</div>''',
    notes_title="مقارنة switch vs match",
    notes_script="مقارنة معيارية شاملة بين switch و match، وتوضيح متى نفضل كل واحدة، مع التركيز على أن match هي الخيار العصري الأول في PHP 8.",
    notes_list=[
        "الفروق بين Statement و Expression",
        "المقارنة الصارمة والأخطاء الناتجة عن نسيان الحالات"
    ]
)

# ==========================================
# SLIDE 20: TERNARY OPERATOR (?:)
# ==========================================
generate_slide(
    index=19,
    title="المعامل الشرطي الثلاثي: Ternary Operator",
    eyebrow="الشروط السريعة — Ternary Operator (?:)",
    slide_title="المعامل الثلاثي (?:): اختصار if / else في سطر واحد",
    slide_text="بدل ما تكتب 4 أو 5 أسطر عشان تسند قيمة لمتغير، المعامل الثلاثي بيعملها في سطر واحد بمنتهى الأناقة:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">ternary.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$score</span> = <span class="tok-num">74</span>;

<span class="tok-cmt">// 1. بالطريقة التقليدية بـ if/else (4 أسطر):</span>
<span class="tok-cmt">// if ($score &gt;= 50) { $res = "ناجح"; } else { $res = "راسب"; }</span>

<span class="tok-cmt">// 2. بالمعامل الثلاثي في سطر واحد:</span>
<span class="tok-var">$status</span> = (<span class="tok-var">$score</span> &gt;= <span class="tok-num">50</span>) ? <span class="tok-str">"ناجح ومبروك 🎓"</span> : <span class="tok-str">"راسب للأسف ⚠️"</span>;

<span class="tok-cmt">// فحص استحقاق شارة التفوق:</span>
<span class="tok-var">$badge</span> = (<span class="tok-var">$score</span> &gt;= <span class="tok-num">85</span>) ? <span class="tok-str">"طالب متفوق 🌟"</span> : <span class="tok-str">"طالب عادي"</span>;

<span class="tok-fn">echo</span> <span class="tok-str">"درجة الطالب: $score &lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"الحالة: $status &lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"الشارة: $badge"</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/ternary.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">درجة الطالب: 74
الحالة: ناجح ومبروك 🎓
الشارة: طالب عادي</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          📐 <strong>تركيبة المعامل الثلاثي:</strong>
          <br/><code dir="ltr">(الشرط) ? القيمة_لو_صح : القيمة_لو_غلط;</code>
        </div>
        <div style="background: rgba(251,191,36,0.08); border: 1px solid rgba(251,191,36,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fcd34d; line-height: 1.4; direction: rtl; text-align: right;">
          ⚠️ <strong>نصيحة ذهبية:</strong> استخدمه للقرارات الثنائية البسيطة فقط. بلاش تعمل شروط ثلاثية متداخلة جوة بعض عشان الكود ميبقاش طلاسم!
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="المعامل الشرطي الثلاثي",
    notes_script="بنشرح بنية المعامل الثلاثي المختصر وكيف يختصر if/else البسيطة لإسناد قيم المتغيرات بسطر واحد.",
    notes_list=[
        "قواعد كتابة Ternary Operator",
        "تطبيقه على تقديرات وحالات الطلاب"
    ]
)

# ==========================================
# SLIDE 21: SHORTHAND TERNARY / ELVIS OPERATOR
# ==========================================
generate_slide(
    index=20,
    title="المعامل الثلاثي المختصر: Elvis Operator",
    eyebrow="القيم البديلة — Elvis Operator (?:)",
    slide_title="المعامل المختصر (?:): أسرع طريقة لوضع قيمة افتراضية",
    slide_text="لما تحب تاخد قيمة المتغير لو موجود، ولو مش موجود تاخد قيمة بديلة جاهزة:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">elvis_operator.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-cmt">// حالة 1: الطالب كتب لقب خاص:</span>
<span class="tok-var">$inputNickName</span> = <span class="tok-str">"عبقرينو"</span>;
<span class="tok-var">$displayName</span> = <span class="tok-var">$inputNickName</span> ?: <span class="tok-str">"طالب مجتهد"</span>;

<span class="tok-cmt">// حالة 2: الطالب ساب خانة اللقب فاضية:</span>
<span class="tok-var">$emptyNickName</span> = <span class="tok-str">""</span>;
<span class="tok-var">$defaultName</span> = <span class="tok-var">$emptyNickName</span> ?: <span class="tok-str">"طالب بدون لقب"</span>;

<span class="tok-fn">echo</span> <span class="tok-str">"الاسم الأول: "</span> . <span class="tok-var">$displayName</span> . <span class="tok-str">"&lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"الاسم الثاني: "</span> . <span class="tok-var">$defaultName</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/elvis_operator.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">الاسم الأول: عبقرينو
الاسم الثاني: طالب بدون لقب</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          🎸 <strong>ليه اسمه Elvis Operator؟</strong> سموه كدة لأن الرمزين جنب بعض <code dir="ltr">?:</code> شبه تسريحة شعر المغني الشهير إلفيس بريسلي! وهو اختصار لـ <code dir="ltr">$a ? $a : $default</code>.
        </div>
        <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fca5a5; line-height: 1.4; direction: rtl; text-align: right;">
          ⚠️ <strong>الفخ اللي مستنيك:</strong> المعامل ده بيفحص الـ Truthiness، فلو الطالب درجته <code dir="ltr">0</code>، هيعتبرها Falsy ويهملها! وده اللي هنحله في الشريحة الجاية.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="المعامل المختصر Elvis Operator",
    notes_script="بنشرح Elvis Operator واختصاره لقيم الـ Fallback، مع التمهيد للفخ القاتل عند فحص القيمة صفر أو النصوص الفارغة.",
    notes_list=[
        "صيغة Elvis Operator (?:)",
        "فخ اعتبار الصفر قيمة غير صالحة"
    ]
)

# ==========================================
# SLIDE 22: NULL COALESCING OPERATOR (??)
# ==========================================
generate_slide(
    index=21,
    title="معامل دمج القيم المعدومة: Null Coalescing",
    eyebrow="حماية القيم المفقودة — Null Coalescing (??)",
    slide_title="معامل ?? والتعيين ??=: الحماية التامة ضد القيم المفقودة",
    slide_text="معامل صُمم خصيصاً في PHP لفحص هل المتغير موجود وموش null، مع توفير قيمة افتراضية آمنة وبدون أي Warning:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">null_coalescing.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-cmt">// 1. المتغير قيمته null صريحة:</span>
<span class="tok-var">$bonusScore</span> = <span class="tok-kw">null</span>;
<span class="tok-var">$finalBonus</span> = <span class="tok-var">$bonusScore</span> ?? <span class="tok-num">0</span>;

<span class="tok-cmt">// 2. المتغير مش متعرف أصلاً في الذاكرة (آمن تماماً):</span>
<span class="tok-var">$examDate</span> = <span class="tok-var">$scheduledExamDate</span> ?? <span class="tok-str">"لم يحدد بعد"</span>;

<span class="tok-cmt">// 3. معامل الإسناد التراكمي (??=) في PHP 7.4+:</span>
<span class="tok-var">$studentGrade</span> = <span class="tok-kw">null</span>;
<span class="tok-var">$studentGrade</span> ??= <span class="tok-num">50</span>; <span class="tok-cmt">// لو null حط فيه 50</span>

<span class="tok-fn">echo</span> <span class="tok-str">"درجة البونص: $finalBonus &lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"موعد الاختبار: $examDate &lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"الدرجة بعد ??= : $studentGrade"</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/null_coalescing.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: #e2e8f0; line-height: 1.6;">درجة البونص: 0
موعد الاختبار: لم يحدد بعد
الدرجة بعد ??= : 50</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          🛡️ <strong>الأمان التام (No Undefined Warnings):</strong> لو المتغير مش موجود أصلاً في الكود أو الـ Array، معامل <code dir="ltr">??</code> مش هيطلع أي تحذير وهيجيب القيمة البديلة بهدوء.
        </div>
        <div style="background: rgba(45,214,230,0.08); border: 1px solid rgba(45,214,230,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #93c5fd; line-height: 1.4; direction: rtl; text-align: right;">
          ⚡ <strong>معامل ??= السريع:</strong> اختصار رائع بيسند القيمة للمتغير فقط لو كان المتغير نفسه غير معرف أو قيمته <code dir="ltr">null</code>.
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="معامل Null Coalescing",
    notes_script="بنشرح معامل الدمج مع Null وكيف يوفر حماية كاملة ضد أخطاء Undefined Variable، مع استعراض معامل الإسناد التراكمي ??=.",
    notes_list=[
        "وظيفة معامل ?? في توفير fallback آمن",
        "معامل التعيين الشرطي ??= في PHP 7.4+"
    ]
)

# ==========================================
# SLIDE 23: DUEL: ?: VS ?? (THE ZERO TRAP)
# ==========================================
generate_slide(
    index=22,
    title="المقارنة الحاسمة: ?: مقابل ??",
    eyebrow="فخ الصفر والنصوص — Duel of Fallbacks",
    slide_title="المواجهة الذهبية: ?: مقابل ?? وفخ درجة الصفر (0)",
    slide_text="الفرق بين المعاملين دقيق وخطير جداً: واحد بيفحص الـ Truthy والتاني بيفحص الـ Null فقط:",
    body_content='''<div class="grid-2">
  <div class="code-window">
    <div class="code-titlebar">
      <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
      <span class="code-filename">zero_trap.php</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-cmt">// طالب دخل الاختبار وحصل على درجة صفر (0):</span>
<span class="tok-var">$studentScore</span> = <span class="tok-num">0</span>;

<span class="tok-cmt">// 1. تجربة المعامل الثلاثي المختصر (?:):</span>
<span class="tok-var">$resElvis</span> = <span class="tok-var">$studentScore</span> ?: <span class="tok-num">50</span>;

<span class="tok-cmt">// 2. تجربة معامل دمج الـ Null (??):</span>
<span class="tok-var">$resNullCoalesce</span> = <span class="tok-var">$studentScore</span> ?? <span class="tok-num">50</span>;

<span class="tok-fn">echo</span> <span class="tok-str">"باستخدام (?:): "</span> . <span class="tok-var">$resElvis</span> . <span class="tok-str">" ❌ (كارثة: حول الصفر لـ 50!)&lt;br&gt;"</span>;
<span class="tok-fn">echo</span> <span class="tok-str">"باستخدام (??): "</span> . <span class="tok-var">$resNullCoalesce</span> . <span class="tok-str">" ✅ (صح: احتفظ بدرجة الصفر)"</span>;
<span class="tok-kw">?&gt;</span></pre>
  </div>

  <div class="browser-window">
    <div class="browser-titlebar">
      <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
      <div class="browser-address">localhost/zero_trap.php</div>
    </div>
    <div class="browser-viewport" style="flex-direction: column; align-items: stretch; justify-content: flex-start; padding: 0.8rem; gap: 0.55rem; background: #0f111e; min-height: 180px;">
      <div class="output-ascii" style="direction: ltr; font-size: clamp(0.72rem, 1.05vw, 0.85rem); color: #e2e8f0; line-height: 1.6;">باستخدام (?:): 50 ❌ (كارثة: حول الصفر لـ 50!)
باستخدام (??): 0 ✅ (صح: احتفظ بدرجة الصفر)</div>
      
      <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.4rem; direction: rtl; text-align: right;">
        <div style="background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #fca5a5; line-height: 1.4; direction: rtl; text-align: right;">
          🚨 <strong>كارثة المعامل ?:</strong> بيعتبر القيم الآتية كلها غير صالحة (<code dir="ltr">Falsy</code>): رقم <code dir="ltr">0</code>، والنص الفاضي <code dir="ltr">""</code>، و <code dir="ltr">false</code>، فيستبدلهم بالقيمة البديلة!
        </div>
        <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 6px; padding: 0.45rem 0.65rem; font-size: clamp(0.68rem, 0.95vw, 0.82rem); color: #34d399; line-height: 1.4; direction: rtl; text-align: right;">
          🎯 <strong>دقة المعامل ??:</strong> بيفحص فقط هل المتغير <code dir="ltr">isset()</code> ومش <code dir="ltr">null</code>. الصفر قيمة حقيقية فيحترمها ويسيبها زي ما هي!
        </div>
      </div>
    </div>
  </div>
</div>''',
    notes_title="مقارنة ?: و ?? وفخ الصفر",
    notes_script="مقارنة جوهرية بين Elvis و Null Coalescing: كيف أن فحص الصفر في درجات الطلاب قد يحول طالباً حاصلاً على صفر إلى ناجح لو استخدمنا ?: بالخطأ.",
    notes_list=[
        "الفرق الدقيق بين فحص Truthy وفحص Isset/Null",
        "توضيح خطورة استبدال الصفر بالقيمة الافتراضية"
    ]
)

# ==========================================
# SLIDE 24: COMPREHENSIVE LECTURE SUMMARY
# ==========================================
generate_slide(
    index=23,
    title="ملخص المحاضرة الثالثة",
    eyebrow="خلاصة المحاضرة — Lecture 03 Cheat-Sheet",
    slide_title="خريطة اتخاذ القرار في PHP: متى تختار كل أداة؟",
    slide_text="دليلك السريع والمرجعي لاختيار الأداة الشرطية المثالية في كل موقف برمجي:",
    body_content='''<div class="summary-grid">
  <div class="summary-box">
    <h3>عائلة if / else / elseif</h3>
    <p>الأفضل للعمليات الحسابية، فحص النطاقات الرقمية (Ranges)، والشروط المنطقية المركبة ذات المسارات المتعددة.</p>
    <div class="sum-code">if ($score &gt;= 85) ... elseif ...</div>
  </div>

  <div class="summary-box">
    <h3>switch مقابل match</h3>
    <p>في PHP 8، اجعل <code dir="ltr">match</code> خيارك الافتراضي لمطابقة القيم الصارمة واسترجاع النتائج بدون خطر Fallthrough.</p>
    <div class="sum-code">$res = match($val) { ... };</div>
  </div>

  <div class="summary-box">
    <h3>المعاملات الذكية (?: و ??)</h3>
    <p>استخدم <code dir="ltr">?:</code> للشروط الثنائية السريعة، واستخدم <code dir="ltr">??</code> دائماً للقيم الافتراضية لحماية الصفر والـ null.</p>
    <div class="sum-code">$score = $inputScore ?? 0;</div>
  </div>

  <div class="summary-box">
    <h3>قائمة المحاذير القاتلة</h3>
    <p>• إياك وكتابة <code dir="ltr">=</code> داخل الشرط بدل <code dir="ltr">===</code>.<br/>• احمِ القسمة على صفر <code dir="ltr">/</code> دائماً.<br/>• الأقواس المعقوفة <code dir="ltr">{}</code> أمان لكودك.</p>
    <div class="sum-code">// Clean &amp; Safe Code Always!</div>
  </div>
</div>''',
    notes_title="ملخص المحاضرة الثالثة",
    notes_script="تلخيص كامل لجميع أدوات التحكم في مسار الكود في PHP مع أهم القواعد والمحاذير قبل الانتقال لأسئلة المراجعة.",
    notes_list=[
        "مراجعة الأدوات الخمس الرئيسية للتحكم بالمسار",
        "تأكيد أهم أفضل الممارسات البرمجية"
    ]
)

# ==========================================
# SLIDE 25: 2 REVISION QUESTIONS
# ==========================================
generate_slide(
    index=24,
    title="تحديات ومراجعة شاملة: سؤالان للمراجعة",
    eyebrow="تحديات المراجعة — Revision Questions",
    slide_title="اختبر فهمك: سؤالان تطبيقيان شاملان لكل موضوعات الدرس",
    slide_text="فكر في الكودين دول كويس، وجاوب على المطلوب قبل ما تشوف الإجابة في الشريحة الجاية:",
    body_content='''<div class="grid-2">
  <div class="code-window" style="border-top-color: #3b82f6;">
    <div class="code-titlebar">
      <span class="code-filename">السؤال 1: تتبع الكود (Code Tracing) 🔍</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-var">$score</span> = <span class="tok-num">85</span>;
<span class="tok-var">$extra</span> = <span class="tok-num">0</span>;

<span class="tok-kw">if</span> (<span class="tok-var">$score</span> = <span class="tok-num">0</span>) {
    <span class="tok-var">$grade</span> = <span class="tok-str">"A"</span>;
} <span class="tok-kw">else</span> {
    <span class="tok-var">$bonus</span> = <span class="tok-var">$extra</span> ?: <span class="tok-num">10</span>;
    <span class="tok-var">$grade</span> = <span class="tok-kw">match</span> (<span class="tok-var">$score</span>) {
        <span class="tok-num">0</span>       =&gt; <span class="tok-str">"F"</span>,
        <span class="tok-num">85</span>      =&gt; <span class="tok-str">"A"</span>,
        <span class="tok-kw">default</span> =&gt; <span class="tok-str">"Unknown"</span>
    };
}

<span class="tok-fn">echo</span> <span class="tok-str">"Grade: $grade | Bonus: $bonus"</span>;
<span class="tok-kw">?&gt;</span></pre>
    <div style="padding: 0.5rem 0.8rem; font-size: 0.76rem; color: #93c5fd; background: rgba(59,130,246,0.1); border-top: 1px solid rgba(255,255,255,0.06); direction: rtl;">
      ❓ <strong>المطلوب:</strong> ما هو الناتج الدقيق المطبوع على الشاشة مع توضيح سبب اختيار هذا المسار؟
    </div>
  </div>

  <div class="code-window" style="border-top-color: #ef4444;">
    <div class="code-titlebar">
      <span class="code-filename">السؤال 2: صيد الأخطاء (Bug Hunt) 🐛</span>
    </div>
    <pre class="code-body">&lt;<span class="tok-kw">?php</span>
<span class="tok-cmt">// طالب حصل على درجة صفر في الفاينال:</span>
<span class="tok-var">$finalExam</span> = <span class="tok-num">0</span>;

<span class="tok-cmt">// كود كتبه متدرب جديد:</span>
<span class="tok-var">$score</span> = <span class="tok-var">$finalExam</span> ?: <span class="tok-num">50</span>;

<span class="tok-kw">switch</span> (<span class="tok-var">$score</span>) {
    <span class="tok-kw">case</span> <span class="tok-num">50</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"ناجح على الحافة"</span>;
    <span class="tok-kw">case</span> <span class="tok-num">100</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">" - ممتاز"</span>;
        <span class="tok-kw">break</span>;
    <span class="tok-kw">default</span>:
        <span class="tok-fn">echo</span> <span class="tok-str">"غير محدد"</span>;
}
<span class="tok-kw">?&gt;</span></pre>
    <div style="padding: 0.5rem 0.8rem; font-size: 0.76rem; color: #fca5a5; background: rgba(239,68,68,0.1); border-top: 1px solid rgba(255,255,255,0.06); direction: rtl;">
      ❓ <strong>المطلوب:</strong> استخرج الخطأين المنطقيين في الكود، وما الناتج الكارثي الذي سيطبع للطالب؟
    </div>
  </div>
</div>''',
    notes_title="أسئلة المراجعة الشاملة",
    notes_script="عرض السؤالين الشاملين: الأول يقيس فهم تتبع الكود والإسناد و match و elvis، والثاني يقيس مهارة اكتشاف الـ Bugs في fallback و switch.",
    notes_list=[
        "سؤال 1: تتبع تدفق الكود وقيم المتغيرات",
        "سؤال 2: اكتشاف أخطاء Fallthrough وفخ الصفر"
    ]
)

# ==========================================
# SLIDE 26: QUESTIONS SOLUTIONS & DISCUSSION
# ==========================================
generate_slide(
    index=25,
    title="حل وشرح أسئلة المراجعة",
    eyebrow="الإجابات النموذجية — Solutions & In-Depth Discussion",
    slide_title="تحليل وإجابات أسئلة المراجعة خطوة بخطوة",
    slide_text="التفكيك البرمجي الدقيق وسبب كل مخرج ظهر على الشاشة:",
    body_content='''<div class="grid-2">
  <div class="summary-box" style="border-top-color: #3b82f6; padding: 0.9rem; gap: 0.5rem;">
    <h3 style="color: #60a5fa; font-size: 0.95rem;">حل السؤال 1: الناتج هو <code dir="ltr">Grade: F | Bonus: 10</code></h3>
    <div style="font-size: 0.75rem; color: #cbd5e1; line-height: 1.5; display: flex; flex-direction: column; gap: 0.35rem; direction: rtl; text-align: right;">
      <p>1. في <code dir="ltr">if ($score = 0)</code>: حصل إسناد لـ <code dir="ltr">0</code> داخل المتغير، والتعبير رجع <code dir="ltr">0</code> (وهو Falsy)، فالـ if ما اتنفذتش وراح لـ <code dir="ltr">else</code> فوراً!</p>
      <p>2. في <code dir="ltr">$bonus = $extra ?: 10</code>: المتغير <code dir="ltr">$extra</code> قيمته <code dir="ltr">0</code> (Falsy) فاختار القيمة البديلة <code dir="ltr">10</code>.</p>
      <p>3. في <code dir="ltr">match ($score)</code>: المتغير <code dir="ltr">$score</code> أصبحت قيمته <code dir="ltr">0</code> (بسبب الإسناد السابق)، فـ match طابقت الحالة <code dir="ltr">0 =&gt; "F"</code> بدقة تامة!</p>
    </div>
  </div>

  <div class="summary-box" style="border-top-color: #ef4444; padding: 0.9rem; gap: 0.5rem;">
    <h3 style="color: #f87171; font-size: 0.95rem;">حل السؤال 2: الكارثتان المنطقيتان والتصحيح</h3>
    <div style="font-size: 0.75rem; color: #cbd5e1; line-height: 1.5; display: flex; flex-direction: column; gap: 0.35rem; direction: rtl; text-align: right;">
      <p>🚨 <strong>الخطأ 1:</strong> استخدام <code dir="ltr">?:</code> مع الصفر خلاه Falsy واستبدله بـ 50، فالطالب الراسب أصبح ناجحاً بالخطأ! <strong>الحل:</strong> استخدام <code dir="ltr">??</code> بدلاً منه (<code dir="ltr">$score = $finalExam ?? 50;</code>).</p>
      <p>🚨 <strong>الخطأ 2:</strong> نسيان <code dir="ltr">break;</code> بعد case 50 سبب Fallthrough فطبع: <br/><strong style="color:#fca5a5;">"ناجح على الحافة - ممتاز"</strong> سوا!</p>
      <p>✨ <strong>الكود الاحترافي المصحح:</strong> <br/><code dir="ltr">$score = $finalExam ?? 0;</code> واستخدام <code dir="ltr">match ($score)</code> للتقديرات.</p>
    </div>
  </div>
</div>''',
    notes_title="حل أسئلة المراجعة",
    notes_script="تحليل دقيق لأسئلة المراجعة وتوضيح سبب المخرجات، وتقديم النصيحة الختامية للطلاب بكتابة كود آمن ونظيف.",
    notes_list=[
        "تحليل خطوات تنفيذ السؤال الأول وتأثير الإسناد",
        "توضيح أخطاء Fallthrough و Elvis مع تقديم الكود المصحح"
    ]
)

print("All 26 slides built successfully!")
