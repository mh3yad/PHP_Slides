# -*- coding: utf-8 -*-
"""
Generator script for Lecture 05:
Arrays in PHP & Essential Array Functions (Manipulation, Search/Check, Sorting)
29 Slides Total.
"""
from build_lecture_05 import make_slide

# ==========================================
# Slide 01: Cover
# ==========================================
make_slide(
    index=0,
    title="الـ Arrays ودوالها الأساسية في PHP",
    eyebrow="أساسيات PHP &middot; المحاضرة 05",
    slide_title="الـ Arrays في PHP ودوالها الأساسية",
    slide_text="سنتعلم كيفية تخزين وإدارة مجموعات البيانات في متغيّر واحد: من الـ Indexed Arrays والـ Associative Arrays إلى الـ Multidimensional Arrays، وصولاً لأهم 10 دوال أساسية للمعالجة، البحث، والـ Sort.",
    body_content='''<div class="cover-mark">
        <div><div class="num">06</div><div class="lbl">محاور كبرى</div></div>
        <div><div class="num">10</div><div class="lbl">دوال أساسية</div></div>
        <div><div class="num">29</div><div class="lbl">شريحة تفاعلية</div></div>
      </div>''',
    notes_title="المحاضرة 05: الـ Arrays في PHP",
    notes_script="أهلاً بكم في المحاضرة الخامسة المخصصة لهياكل الـ Arrays وأهم دوالها في PHP. سنغطي الأنواع الثلاثة ثم ننتقل لعشر دوال حيوية لا غنى عنها في أي مشروع حقيقي.",
    notes_list=["مفهوم الـ Array وتخزين البيانات", "الأنواع: Indexed و Associative و Multidimensional", "عشر دوال أساسية في PHP", "أفضل الممارسات والأخطاء الشائعة"],
    is_cover=True
)

# ==========================================
# Slide 02: Roadmap
# ==========================================
make_slide(
    index=1,
    title="خريطة المحاضرة 05",
    eyebrow="نظرة عامة &middot; محتويات المحاضرة",
    slide_title="خريطة المحاضرة 05",
    slide_text="خريطة طريق شاملة تغطي أنواع الـ Arrays وعشر دوال أساسية مقسمة حسب وظائفها:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">أنواع الـ Arrays الثلاثة</div>
            <div class="topic-desc">الـ Indexed، الـ Associative، والـ Multidimensional</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">دوال التعديل (Manipulation)</div>
            <div class="topic-desc">array_push للإضافة، array_pop للاستخراج، array_merge للدمج، و unset للحذف</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">دوال البحث والفحص (Search & Check)</div>
            <div class="topic-desc">in_array للتحقق من القيم، array_key_exists للمفاتيح، و count لحساب الحجم</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">دوال الترتيب والـ Sort (Sorting)</div>
            <div class="topic-desc">sort لإعادة الترقيم، asort للـ Sort مع حفظ المفاتيح، و ksort لـ Sort المفاتيح</div>
          </div>
        </div>
      </div>''',
    notes_title="خريطة المحاضرة 05",
    notes_script="قسمنا المحاضرة إلى قسمين رئيسيين: في البداية نراجع سريعاً الأنواع الثلاثة للـ Arrays، ثم نتوسع بعمق في الدوال العشر الأساسية المصنفة إلى معالجة، وبحث، و Sort.",
    notes_list=["الـ Arrays وأنواعها الأساسية", "دوال التعديل Manipulation", "دوال البحث والفحص Search & Check", "دوال الـ Sort"]
)

# ==========================================
# Slide 03: Indexed Arrays
# ==========================================
make_slide(
    index=2,
    title="الـ Indexed Arrays",
    eyebrow="أنواع الـ Arrays &middot; 1",
    slide_title="الـ Indexed Arrays",
    slide_text="الـ Indexed Array تخزن مجموعة قيم مرتبة، وكل قيمة تمتلك مؤشراً رقمياً (Index) يبدأ تلقائياً من الصفر:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>الفهرسة الصفرية (Zero-indexed):</strong> العنصر الأول مكانه دائماً <code>0</code>، والثاني <code>1</code>، وهكذا.</li>
          <li><strong>صيغة الأقواس المربعة:</strong> ننشئ الـ Array باستخدام <code>$arr = ["a", "b", "c"];</code> وهي الصيغة الحديثة والمفضلة.</li>
          <li><strong>الوصول للعناصر:</strong> نصل لأي قيمة بكتابة اسم المتغير متبوعاً بالـ index بين قوسين: <code>$arr[0]</code>.</li>
          <li><strong>إضافة عنصر جديد:</strong> ببساطة نكتب <code>$arr[] = "new";</code> فيضاف تلقائياً في نهاية الـ Array.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">indexed_arrays.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// إنشاء Indexed Array</span>
<span class="tok-var">$colors</span> = [<span class="tok-str">"أحمر"</span>, <span class="tok-str">"أخضر"</span>, <span class="tok-str">"أزرق"</span>];

<span class="tok-cmt">// قراءة العنصر الأول والثالث</span>
<span class="tok-kw">echo</span> <span class="tok-var">$colors</span>[<span class="tok-num">0</span>]; <span class="tok-cmt">// أحمر</span>
<span class="tok-kw">echo</span> <span class="tok-var">$colors</span>[<span class="tok-num">2</span>]; <span class="tok-cmt">// أزرق</span>

<span class="tok-cmt">// إضافة عنصر جديد في آخر الـ Array</span>
<span class="tok-var">$colors</span>[] = <span class="tok-str">"أصفر"</span>; <span class="tok-cmt">// index رقم 3</span></pre>
        </div>
      </div>''',
    notes_title="الـ Indexed Arrays",
    notes_script="الـ Indexed Array مثل درج بأقسام تبدأ فهارسها من 0. تذكر دائماً: الـ Index يبدأ من 0 وليس من 1.",
    notes_list=["فهرسة صفرية تبدأ من 0", "الإنشاء بالأقواس المربعة []", "الوصول بالرقم $arr[0]", "الإضافة بـ [] في النهاية"]
)

# ==========================================
# Slide 04: Indexed Array Example 1
# ==========================================
make_slide(
    index=3,
    title="مثال 1: قراءة عناصر Indexed Array",
    eyebrow="Indexed Arrays &middot; مثال 1",
    slide_title="مثال 1: قراءة عناصر Indexed Array",
    slide_text="استخراج قيم محددة من Array فواكه وعرضها في المتصفح بالتسلسل الصحيح:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب البرمجي</div>
          <p>أنشئ Array فواكه تحتوي على 3 عناصر، واطبع العنصر الأول والثالث، ولاحظ ما يحدث عند طلب فهرس غير موجود.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">fruits.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$fruits</span> = [<span class="tok-str">"تفاح"</span>, <span class="tok-str">"موز"</span>, <span class="tok-str">"برتقال"</span>];

<span class="tok-kw">echo</span> <span class="tok-str">"الأول: "</span> . <span class="tok-var">$fruits</span>[<span class="tok-num">0</span>] . <span class="tok-str">"&lt;br&gt;"</span>;
<span class="tok-kw">echo</span> <span class="tok-str">"الثالث: "</span> . <span class="tok-var">$fruits</span>[<span class="tok-num">2</span>];</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/fruits.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.95rem;">
الأول: تفاح
الثالث: برتقال
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال 1: قراءة Indexed Array",
    notes_script="لاحظ أن العنصر الثالث يقع في الفهرس 2 لأن الترقيم بدأ من 0. إذا حاولنا طلب $fruits[5] سيظهر تحذير Undefined array key.",
    notes_list=["الفهرس 0 هو الأول", "الفهرس 2 هو الثالث", "تجنب طلب مفتاح غير موجود"]
)

# ==========================================
# Slide 05: Indexed Array Example 2: Append & Modify
# ==========================================
make_slide(
    index=4,
    title="مثال 2: تعديل وإلحاق العناصر بالـ Array",
    eyebrow="Indexed Arrays &middot; مثال 2",
    slide_title="مثال 2: تعديل وإلحاق العناصر بالـ Array",
    slide_text="تغيير قيمة عنصر قائم وإضافة عناصر جديدة إلى نهاية الـ Array بسهولة:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب البرمجي</div>
          <p>قم بإنشاء Array أرقام، وعدّل العنصر الثاني، ثم أضف رقماً في النهاية واطبع المحتوى بواسطة <code>print_r</code>.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">modify_array.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$numbers</span> = [<span class="tok-num">10</span>, <span class="tok-num">20</span>, <span class="tok-num">30</span>];

<span class="tok-cmt">// تعديل العنصر الثاني (index 1)</span>
<span class="tok-var">$numbers</span>[<span class="tok-num">1</span>] = <span class="tok-num">25</span>;

<span class="tok-cmt">// إضافة عنصر جديد في نهاية الـ Array</span>
<span class="tok-var">$numbers</span>[] = <span class="tok-num">40</span>;

<span class="tok-fn">print_r</span>(<span class="tok-var">$numbers</span>);</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/modify_array.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:ltr;text-align:start;padding:0.75rem;font-size:0.88rem;font-family:monospace;">
Array
(
    [0] => 10
    [1] => 25
    [2] => 30
    [3] => 40
)
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال 2: تعديل وإلحاق عناصر الـ Array",
    notes_script="لتعديل قيمة نذكر رقم الفهرس مباشرة. ولإلحاق قيمة جديدة في النهاية نترك الأقواس المربعة فارغة.",
    notes_list=["تعديل قيمة بفهرس محدد", "إلحاق عنصر جديد بالأقواس الفارغة []", "استعراض الهيكل كاملاً بـ print_r"]
)

# ==========================================
# Slide 06: Associative Arrays
# ==========================================
make_slide(
    index=5,
    title="الـ Associative Arrays",
    eyebrow="أنواع الـ Arrays &middot; 2",
    slide_title="الـ Associative Arrays",
    slide_text="بدلاً من استخدام أرقام مجردة، ترتبط كل قيمة بمفتاح نصي ذي دلالة (Key => Value) يوضح معناها بوضوح:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>مفهوم Key => Value:</strong> المفتاح يكون نصاً معبراً (مثل <code>"name"</code> أو <code>"email"</code>) يرتبط بقيمته بسهم <code>=&gt;</code>.</li>
          <li><strong>وضوح الكود ومقروئيته:</strong> بدلاً من التخمين عما يعنيه <code>$user[2]</code>، نكتب <code>$user['age']</code> فيتضح المعنى فوراً.</li>
          <li><strong>الوصول والتعديل:</strong> نصل للقيمة عبر مفتاحها: <code>$student['score']</code>.</li>
          <li><strong>إضافة مفتاح جديد:</strong> نحدد اسم المفتاح الجديد وقيمته: <code>$user['city'] = "القاهرة";</code>.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">associative.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// Associative Array لبيانات طالب</span>
<span class="tok-var">$student</span> = [
    <span class="tok-str">"name"</span>  =&gt; <span class="tok-str">"أحمد محمد"</span>,
    <span class="tok-str">"age"</span>   =&gt; <span class="tok-num">21</span>,
    <span class="tok-str">"track"</span> =&gt; <span class="tok-str">"PHP & Laravel"</span>
];

<span class="tok-cmt">// قراءة القيم بمفتاحها</span>
<span class="tok-kw">echo</span> <span class="tok-var">$student</span>[<span class="tok-str">"name"</span>]; <span class="tok-cmt">// أحمد محمد</span>

<span class="tok-cmt">// إضافة مفتاح جديد</span>
<span class="tok-var">$student</span>[<span class="tok-str">"grade"</span>] = <span class="tok-str">"ممتاز"</span>;</pre>
        </div>
      </div>''',
    notes_title="الـ Associative Arrays",
    notes_script="الـ Associative Array تشبه القاموس: لكل كلمة معنى. في PHP نستخدم المفاتيح النصية لتمثيل السجلات مثل المستخدمين والمنتجات والخيارات.",
    notes_list=["ربط المفتاح بالقيمة بـ =>", "الوصول بالاسم $arr['key']", "كود نظيف وواضح الدلالة"]
)

# ==========================================
# Slide 07: Associative Example 1
# ==========================================
make_slide(
    index=6,
    title="مثال 1: Array مواصفات منتج",
    eyebrow="Associative Arrays &middot; مثال 1",
    slide_title="مثال 1: Array مواصفات منتج إلكتروني",
    slide_text="تمثيل منتج في متجر إلكتروني بمفاتيحه الأساسية: العنوان، السعر، وحالة التوفر:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب البرمجي</div>
          <p>أنشئ Array باسم <code>$product</code> واطبع اسم المنتج وسعره مع إضافة ضريبة 14% على السعر المعروض.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">product.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$product</span> = [
    <span class="tok-str">"title"</span> =&gt; <span class="tok-str">"لابتوب ديل"</span>,
    <span class="tok-str">"price"</span> =&gt; <span class="tok-num">15000</span>,
    <span class="tok-str">"in_stock"</span> =&gt; <span class="tok-kw">true</span>
];

<span class="tok-var">$tax</span> = <span class="tok-var">$product</span>[<span class="tok-str">"price"</span>] * <span class="tok-num">0.14</span>;
<span class="tok-var">$total</span> = <span class="tok-var">$product</span>[<span class="tok-str">"price"</span>] + <span class="tok-var">$tax</span>;

<span class="tok-kw">echo</span> <span class="tok-str">"المنتج: {$product['title']}&lt;br&gt;"</span>;
<span class="tok-kw">echo</span> <span class="tok-str">"الإجمالي بعد الضريبة: {$total} ج.م"</span>;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/product.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.95rem;">
المنتج: لابتوب ديل
الإجمالي بعد الضريبة: 17100 ج.م
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال 1: Array منتج",
    notes_script="لاحظ كيف يمكننا إجراء عمليات حسابية على القيم المستخرجة من الـ Associative Array ودمجها في النصوص.",
    notes_list=["استخراج القيم النصية والعددية", "إجراء العمليات الحسابية", "الدمج المعقد داخل النصوص"]
)

# ==========================================
# Slide 08: Associative Example 2: Update & Add Keys
# ==========================================
make_slide(
    index=7,
    title="مثال 2: تحديث بيانات مستخدم في الـ Array",
    eyebrow="Associative Arrays &middot; مثال 2",
    slide_title="مثال 2: تحديث المفاتيح وإضافة خصائص جديدة",
    slide_text="تعديل مفتاح قائم وإضافة حقول إضافية لـ Array إعدادات حساب المستخدم:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب البرمجي</div>
          <p>حدّث البريد الإلكتروني للمستخدم، وأضف خاصية <code>role</code> بقيمة <code>admin</code> ثم اعرض النتيجة.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">user_update.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$user</span> = [
    <span class="tok-str">"username"</span> =&gt; <span class="tok-str">"mahmoud_99"</span>,
    <span class="tok-str">"email"</span>    =&gt; <span class="tok-str">"old@test.com"</span>
];

<span class="tok-cmt">// تحديث البريد الإلكتروني</span>
<span class="tok-var">$user</span>[<span class="tok-str">"email"</span>] = <span class="tok-str">"new_email@gmail.com"</span>;

<span class="tok-cmt">// إضافة مفتاح الرتبة</span>
<span class="tok-var">$user</span>[<span class="tok-str">"role"</span>] = <span class="tok-str">"مدير النظام"</span>;

<span class="tok-kw">echo</span> <span class="tok-str">"المستخدم: {$user['username']} | الرتبة: {$user['role']}"</span>;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/user_update.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.95rem;">
المستخدم: mahmoud_99 | الرتبة: مدير النظام
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال 2: تحديث بيانات مستخدم",
    notes_script="إذا كان المفتاح موجوداً مسبقاً، سيتم استبدال قيمته؛ وإذا لم يكن موجوداً، سيتم إنشاؤه تلقائياً.",
    notes_list=["تحديث المفاتيح الحالية", "إنشاء مفاتيح جديدة بسهولة", "مرونة الـ Arrays في PHP"]
)

# ==========================================
# Slide 09: Multidimensional Arrays
# ==========================================
make_slide(
    index=8,
    title="الـ Multidimensional Arrays",
    eyebrow="أنواع الـ Arrays &middot; 3",
    slide_title="الـ Multidimensional Arrays",
    slide_text="Array تحتوي بداخلها على Arrays أخرى؛ لتمثيل الجداول والصفوف وقواعد البيانات المعقدة:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>Array داخل Array:</strong> كل عنصر في الـ Array الرئيسية يمكن أن يكون Array أخرى مستقلة.</li>
          <li><strong>تمثيل الجداول (Rows & Columns):</strong> البعد الأول يمثل الصف (Row)، والبعد الثاني يمثل العمود (Column).</li>
          <li><strong>طريقة الوصول المزدوج:</strong> نستخدم قوسين متتاليين للوصول: <code>$matrix[0][1]</code> أو <code>$users[1]['name']</code>.</li>
          <li><strong>الاستخدام الشائع:</strong> نتائج استعلامات قواعد البيانات، وسجلات المنتجات، وجداول الدرجات.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">matrix.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// Array أرقام ثنائية الأبعاد (جدول)</span>
<span class="tok-var">$matrix</span> = [
    [<span class="tok-num">1</span>, <span class="tok-num">2</span>, <span class="tok-num">3</span>],  <span class="tok-cmt">// الصف 0</span>
    [<span class="tok-num">4</span>, <span class="tok-num">5</span>, <span class="tok-num">6</span>],  <span class="tok-cmt">// الصف 1</span>
    [<span class="tok-num">7</span>, <span class="tok-num">8</span>, <span class="tok-num">9</span>]   <span class="tok-cmt">// الصف 2</span>
];

<span class="tok-cmt">// الوصول للرقم 6 (الصف 1، العمود 2)</span>
<span class="tok-kw">echo</span> <span class="tok-var">$matrix</span>[<span class="tok-num">1</span>][<span class="tok-num">2</span>]; <span class="tok-cmt">// 6</span></pre>
        </div>
      </div>''',
    notes_title="الـ Multidimensional Arrays",
    notes_script="فكر في الـ Multidimensional Array كجدول إكسل: البعد الأول يحدد رقم السطر، والبعد الثاني يحدد رقم العمود.",
    notes_list=["Array عناصرها Arrays", "البعد الأول للصفوف والبعد الثاني للأعمدة", "الوصول بالقوس المزدوج [0][1]"]
)

# ==========================================
# Slide 10: Multidimensional Example: Associative inside Indexed
# ==========================================
make_slide(
    index=9,
    title="مثال واقعي: قائمة مستخدمين (Associative جوه Indexed)",
    eyebrow="Multidimensional &middot; مثال واقعي",
    slide_title="قائمة مستخدمين: Associative Arrays داخل Indexed Array",
    slide_text="هذا النمط هو الأكثر استخداماً في تطوير الويب لمحاكاة البيانات القادمة من قواعد البيانات ومنافذ API:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب البرمجي</div>
          <p>قم بتعريف قائمة طلاب تحتوي على طالبين، واطبع اسم وعمر الطالب الثاني مع تعديل درجته.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">students_db.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$students</span> = [
    [<span class="tok-str">"name"</span> =&gt; <span class="tok-str">"علي"</span>,  <span class="tok-str">"age"</span> =&gt; <span class="tok-num">20</span>, <span class="tok-str">"grade"</span> =&gt; <span class="tok-num">88</span>],
    [<span class="tok-str">"name"</span> =&gt; <span class="tok-str">"سارة"</span>, <span class="tok-str">"age"</span> =&gt; <span class="tok-num">22</span>, <span class="tok-str">"grade"</span> =&gt; <span class="tok-num">95</span>]
];

<span class="tok-cmt">// قراءة بيانات الطالبة الثانية (index 1)</span>
<span class="tok-kw">echo</span> <span class="tok-str">"الاسم: "</span> . <span class="tok-var">$students</span>[<span class="tok-num">1</span>][<span class="tok-str">"name"</span>] . <span class="tok-str">"&lt;br&gt;"</span>;
<span class="tok-kw">echo</span> <span class="tok-str">"العمر: "</span> . <span class="tok-var">$students</span>[<span class="tok-num">1</span>][<span class="tok-str">"age"</span>];</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/students_db.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.95rem;">
الاسم: سارة
العمر: 22
            </div>
          </div>
        </div>
      </div>''',
    notes_title="سجلات واقعية: Arrays مدمجة",
    notes_script="هذا النمط سيتكرر معكم في 99% من مشاريع PHP: Indexed Array من السجلات، وكل سجل عبارة عن Associative Array من الخصائص.",
    notes_list=["نمط سجلات قواعد البيانات", "الفهرس الأول للسطر والفهرس الثاني للخاصية", "أهم هيكل بيانات في تطوير الويب"]
)

# ==========================================
# Slide 11: Section Divider: Essential Array Functions
# ==========================================
make_slide(
    index=10,
    title="دوال الـ Arrays الأساسية (Essential Array Functions)",
    eyebrow="القسم الثاني",
    slide_title="دوال الـ Arrays الأساسية في PHP",
    slide_text="تحتوي PHP على مكتبة دوال غنية وسريعة لإنجاز كل ما تحتاجه على الـ Arrays دون كتابة كود مكرر:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">01. التعديل (Manipulation): push, pop, merge, unset</span>
        <span class="pill-badge">02. البحث والفحص (Search/Check): in_array, key_exists, count</span>
        <span class="pill-badge">03. الترتيب والـ Sort (Sorting): sort, asort, ksort</span>
      </div>''',
    notes_title="فاصل دوال الـ Arrays الأساسية",
    notes_script="ننتقل الآن إلى القلب النابض للمحاضرة: الدوال الأساسية العشر. رتبناها في 3 مجموعات واضحة لسهولة الحفظ والتطبيق.",
    notes_list=["مجموعة التعديل والمعالجة", "مجموعة البحث والتحقق", "مجموعة الترتيب والـ Sort"],
    is_divider=True
)

# ==========================================
# Slide 12: Overview of 3 Essential Groups
# ==========================================
make_slide(
    index=11,
    title="تصنيف الدوال الأساسية الـ 10 للـ Arrays",
    eyebrow="دوال الـ Arrays &middot; نظرة شاملة",
    slide_title="الدوال الأساسية الـ 10 مقسمة حسب وظيفتها",
    slide_text="خريطة ذهنية واضحة لأهم الدوال التي لا يخلو منها أي تطبيق PHP احترافي:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">المعالجة والتعديل (Manipulation)</div>
            <div class="topic-desc"><code>array_push</code> (إضافة بالآخر)، <code>array_pop</code> (حذف من الآخر)، <code>array_merge</code> (دمج)، و <code>unset</code> (حذف مخصص)</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">البحث والتحقق والعد (Search & Check)</div>
            <div class="topic-desc"><code>count</code> (إجمالي الحجم)، <code>in_array</code> (فحص وجود قيمة)، و <code>array_key_exists</code> (فحص وجود مفتاح)</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">الترتيب والـ Sort (Sorting)</div>
            <div class="topic-desc"><code>sort</code> (تصاعدي مع مسح المفاتيح)، <code>asort</code> (تصاعدي بالقيم مع حفظ المفاتيح)، و <code>ksort</code> (تصاعدي بالمفاتيح)</div>
          </div>
        </div>
      </div>''',
    notes_title="تصنيف دوال الـ Arrays الـ 10",
    notes_script="تصنيف الدوال يسهل تذكرها: عندما تريد تعديل الـ Array تتذكر Manipulation، وعندما تبحث تتذكر Search، وعند الترتيب تتذكر Sort.",
    notes_list=["تصنيف دقيق وشامل", "4 دوال معالجة وتعديل", "3 دوال بحث وتحقق", "3 دوال ترتيب و Sort"]
)

# ==========================================
# Slide 13: Manipulation: array_push & array_pop
# ==========================================
make_slide(
    index=12,
    title="دوال التعديل: array_push و array_pop",
    eyebrow="دوال التعديل &middot; 1",
    slide_title="الإضافة والحذف من النهاية: array_push و array_pop",
    slide_text="التعامل مع الـ Array كبنية مكدس (Stack - LIFO) عبر إضافة عناصر لنهايتها واستخراج آخر عنصر منها:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>array_push(&$arr, ...$vals)</code>: تضيف عنصراً أو أكثر لنهاية الـ Array وتعيد <strong>العدد الجديد</strong> للعناصر.</li>
          <li><code>array_pop(&$arr)</code>: تستخرج وتحذف <strong>آخر عنصر</strong> من الـ Array وتعيد قيمته للمتغير، أو <code>null</code> إن كانت فارغة.</li>
          <li><strong>تعديل بالمرجع (In-Place):</strong> كلاهما يعدل على الـ Array الأصلية مباشرة دون الحاجة لإعادة تعيينها.</li>
          <li><strong>بديل سريع:</strong> استخدام <code>$arr[] = $val</code> أسرع في الأداء من <code>array_push</code> إذا كنت تضيف عنصراً واحداً فقط.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">push_pop.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$stack</span> = [<span class="tok-str">"A"</span>, <span class="tok-str">"B"</span>];

<span class="tok-cmt">// 1. إضافة عناصر بالآخر</span>
<span class="tok-fn">array_push</span>(<span class="tok-var">$stack</span>, <span class="tok-str">"C"</span>, <span class="tok-str">"D"</span>);
<span class="tok-cmt">// $stack أصبح: ["A", "B", "C", "D"]</span>

<span class="tok-cmt">// 2. استخراج وحذف آخر عنصر</span>
<span class="tok-var">$last</span> = <span class="tok-fn">array_pop</span>(<span class="tok-var">$stack</span>);

<span class="tok-kw">echo</span> <span class="tok-str">"العنصر المستخرج: "</span> . <span class="tok-var">$last</span> . <span class="tok-str">"&lt;br&gt;"</span>; <span class="tok-cmt">// D</span>
<span class="tok-kw">echo</span> <span class="tok-str">"المتبقي بالكدس: "</span> . <span class="tok-fn">implode</span>(<span class="tok-str">"-"</span>, <span class="tok-var">$stack</span>); <span class="tok-cmt">// A-B-C</span></pre>
        </div>
      </div>''',
    notes_title="array_push و array_pop",
    notes_script="array_push تضع في القمة، و array_pop تسحب من القمة. هذا مفهوم الـ Stack الكلاسيكي في علوم الحاسب.",
    notes_list=["push تضيف عنصر أو أكثر لنهاية الـ Array", "pop تحذف آخر عنصر وتعيد قيمته", "تعديل مباشر على الـ Array الأصلية"]
)

# ==========================================
# Slide 14: Manipulation: array_merge & unset
# ==========================================
make_slide(
    index=13,
    title="دوال التعديل: array_merge و unset",
    eyebrow="دوال التعديل &middot; 2",
    slide_title="الدمج والحذف المباشر: array_merge و unset",
    slide_text="دمج عدة Arrays في Array واحدة، وحذف عناصر محددة بواسطة مفاتيحها:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>array_merge($arr1, $arr2, ...)</code>: تدمج 2 Arrays أو أكثر وتنشئ Array جديدة بالكامل دون المساس بالأصلية.</li>
          <li><strong>سلوك المفاتيح في الدمج:</strong>
            المفاتيح العددية يُعاد ترقيمها تلقائياً من 0؛ أما المفاتيح النصية المتشابهة فيقوم الأخير باستبدال الأول.</li>
          <li><code>unset($arr[key])</code>: تعليمة لحذف عنصر محدد (بفهرس رقمي أو مفتاح نصي) من الذاكرة فوراً.</li>
          <li><strong>ملاحظة هامة:</strong> <code>unset</code> لا تعيد ترتيب المفاتيح العددية؛ قد تترك فجوة في الترقيم.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">merge_unset.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$a</span> = [<span class="tok-str">"PHP"</span>, <span class="tok-str">"Laravel"</span>];
<span class="tok-var">$b</span> = [<span class="tok-str">"MySQL"</span>, <span class="tok-str">"Vue"</span>];

<span class="tok-cmt">// دمج الـ 2 Arrays</span>
<span class="tok-var">$fullStack</span> = <span class="tok-fn">array_merge</span>(<span class="tok-var">$a</span>, <span class="tok-var">$b</span>);
<span class="tok-cmt">// ["PHP", "Laravel", "MySQL", "Vue"]</span>

<span class="tok-cmt">// حذف عنصر معين بواسطة المفتاح</span>
<span class="tok-kw">unset</span>(<span class="tok-var">$fullStack</span>[<span class="tok-num">1</span>]); <span class="tok-cmt">// حذف Laravel</span>

<span class="tok-fn">print_r</span>(<span class="tok-var">$fullStack</span>);</pre>
        </div>
      </div>''',
    notes_title="array_merge و unset",
    notes_script="array_merge تجمع Arrays وتنتج Array جديدة. unset تدمر عنصراً محدداً من الـ Array الحالية مباشرة.",
    notes_list=["array_merge تعيد Array مدمجة جديدة", "إعادة ترقيم المفاتيح العددية في الدمج", "unset تحذف العنصر فوراً دون إعادة ترقيم"]
)

# ==========================================
# Slide 15: Search & Check: count & in_array
# ==========================================
make_slide(
    index=14,
    title="دوال البحث والتحقق: count و in_array",
    eyebrow="البحث والتحقق &middot; 1",
    slide_title="عد العناصر وفحص القيم: count و in_array",
    slide_text="معرفة حجم الـ Array والتحقق مما إذا كانت قيمة معينة موجودة بداخلها أم لا:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>count($arr)</code>: تعيد إجمالي عدد العناصر في الـ Array كـ Integer.</li>
          <li><code>in_array($val, $arr, $strict = false)</code>: تبحث عن <strong>القيمة</strong> داخل عناصر الـ Array وتعيد <code>true</code> أو <code>false</code>.</li>
          <li><strong>المعامل الصارم (Strict Mode):</strong> يفضل دائماً تمرير <code>true</code> كمعامل ثالث لمقارنة النوع والقيمة بدقة (مماثلة لـ <code>===</code>).</li>
          <li><strong>فخ التحويل التلقائي:</strong> بدون المعامل الصارم، قد تتطابق <code>"apple"</code> مع الرقم <code>0</code> في إصدارات PHP القديمة!</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">count_in_array.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$roles</span> = [<span class="tok-str">"admin"</span>, <span class="tok-str">"editor"</span>, <span class="tok-str">"author"</span>];

<span class="tok-cmt">// 1. حساب عدد العناصر في الـ Array</span>
<span class="tok-kw">echo</span> <span class="tok-str">"العدد: "</span> . <span class="tok-fn">count</span>(<span class="tok-var">$roles</span>); <span class="tok-cmt">// 3</span>

<span class="tok-cmt">// 2. التحقق من وجود قيمة معينة بصرامة</span>
<span class="tok-kw">if</span> (<span class="tok-fn">in_array</span>(<span class="tok-str">"admin"</span>, <span class="tok-var">$roles</span>, <span class="tok-kw">true</span>)) {
    <span class="tok-kw">echo</span> <span class="tok-str">"صلاحية مدير مؤكدة!"</span>;
} <span class="tok-kw">else</span> {
    <span class="tok-kw">echo</span> <span class="tok-str">"غير مصرح له"</span>;
}</pre>
        </div>
      </div>''',
    notes_title="count و in_array",
    notes_script="count أساسية للـ loops وحساب عناصر الـ Array. in_array ممتازة لفحص الصلاحيات والخيارات المتاحة، والوضع الصارم يضمن سلامة المقارنة.",
    notes_list=["count لحساب عدد العناصر", "in_array تبحث عن القيمة وتعيد boolean", "أهمية تفعيل الوضع الصارم true"]
)

# ==========================================
# Slide 16: Search & Check: array_key_exists vs isset
# ==========================================
make_slide(
    index=15,
    title="فحص وجود المفاتيح: array_key_exists",
    eyebrow="البحث والتحقق &middot; 2",
    slide_title="التحقق من وجود المفاتيح: array_key_exists",
    slide_text="فحص وجود مفتاح معين داخل Associative Array، والفرق الجوهري بينها وبين دالة <code>isset()</code>:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>array_key_exists($key, $arr)</code>: تعيد <code>true</code> إذا كان <strong>المفتاح</strong> موجوداً في الـ Array، حتى وإن كانت قيمته <code>null</code>!</li>
          <li><strong>الفرق الحاسم مع <code>isset()</code>:</strong>
            دالة <code>isset($arr['key'])</code> تعيد <code>false</code> إذا كانت قيمة المفتاح تساوي <code>null</code> مع أنه موجود بالفعل في الـ Array!</li>
          <li><strong>الأداء:</strong> <code>isset</code> أسرع قليلاً، لكن <code>array_key_exists</code> أدق لمعرفة بنية البيانات الحقيقية.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">key_exists.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$user</span> = [
    <span class="tok-str">"name"</span>  =&gt; <span class="tok-str">"سارة"</span>,
    <span class="tok-str">"phone"</span> =&gt; <span class="tok-kw">null</span> <span class="tok-cmt">// المفتاح موجود لكن قيمته فارغة</span>
];

<span class="tok-cmt">// array_key_exists ترى المفتاح بنجاح!</span>
<span class="tok-fn">var_dump</span>(<span class="tok-fn">array_key_exists</span>(<span class="tok-str">"phone"</span>, <span class="tok-var">$user</span>));
<span class="tok-cmt">// bool(true)</span>

<span class="tok-cmt">// isset تعيد false بسبب قيمة null!</span>
<span class="tok-fn">var_dump</span>(<span class="tok-kw">isset</span>(<span class="tok-var">$user</span>[<span class="tok-str">"phone"</span>]));
<span class="tok-cmt">// bool(false)</span></pre>
        </div>
      </div>''',
    notes_title="array_key_exists مقابل isset",
    notes_script="سؤال كلاسيكي في مقابلات العمل: ما الفرق بين array_key_exists و isset؟ الإجابة: إذا كان المفتاح موجوداً وقيمته null، فإن isset تعيد false بينما array_key_exists تعيد true.",
    notes_list=["array_key_exists تفحص وجود المفتاح بغض النظر عن القيمة", "isset تعيد false إذا كانت القيمة null", "سؤال مفضل في المقابلات التقنية"]
)

# ==========================================
# Slide 17: Sorting: Overview of Sorting in PHP
# ==========================================
make_slide(
    index=16,
    title="دوال الـ Sort والترتيب (Sorting Functions)",
    eyebrow="الـ Sort والترتيب &middot; نظرة شاملة",
    slide_title="دوال الـ Sort والترتيب في PHP",
    slide_text="في PHP تختلف دوال الـ Sort بناءً على معيارين رئيسيين يحددان النتيجة تماماً:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">1. هل نعمل Sort حسب المفاتيح أم القيم؟</div>
          <ul class="bullet-list">
            <li><strong>الترتيب حسب القيم (Values):</strong> مثل عمل Sort لقائمة أسعار من الأرخص للأغلى أو أسماء الطلاب أبجدياً.</li>
            <li><strong>الترتيب حسب المفاتيح (Keys):</strong> مثل عمل Sort لـ Array تواريخ أو رموز الدول (EG, SA, US) أبجدياً بمفاتيحها.</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">2. هل نحافظ على ارتباط المفتاح أم نعيد الترقيم؟</div>
          <ul class="bullet-list">
            <li><strong>إعادة الترقيم (Reset Indexes):</strong> مسح المفاتيح السابقة وترقيم العناصر <code>0, 1, 2...</code> (دالة <code>sort</code>).</li>
            <li><strong>الحفاظ على المفاتيح (Preserve Keys):</strong> يبقى كل عنصر مرتبطاً بمفتاحه الأصلي دون تغيير (حرف <strong>a</strong> في <code>asort</code> اختصار لـ Associative).</li>
          </ul>
        </div>
      </div>''',
    notes_title="مفهوم الـ Sort في PHP",
    notes_script="قاعدة ذهبية: حرف k يعني Key (مفتاح)، وحرف a يعني Associative (حفظ الارتباط). ودوال الـ Sort تعدل الـ Array في مكانها دون إرجاع Array جديدة.",
    notes_list=["الـ Sort بالقيم مقابل المفاتيح", "إعادة الترقيم مقابل حفظ الارتباط", "دلالة الحروف k و a في أسماء الدوال"]
)

# ==========================================
# Slide 18: Sorting 1: sort()
# ==========================================
make_slide(
    index=17,
    title="دوال الـ Sort: دالة sort للـ Indexed Arrays",
    eyebrow="دوال الـ Sort &middot; 1",
    slide_title="ترتيب القيم وإعادة الترقيم: دالة sort()",
    slide_text="ترتيب عناصر الـ Array تصاعدياً من الأصغر للأكبر (أرقام أو نصوص أبجدية) مع إعادة ترقيم فهارسها من الصفر:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>sort(&$arr)</code>: ترتب العناصر تصاعدياً (A-Z أو 0-9).</li>
          <li><strong>تعديل بالمرجع:</strong> تقوم بعمل Sort للـ Array الأصلية في مكانها (In-Place) وتعيد قيمة <code>true</code> أو <code>false</code>.</li>
          <li><strong>إعادة تعيين الفهارس:</strong> تمسح أي مفاتيح سابقة وتضع فهارس رقمية جديدة تبدأ من <code>0</code>.</li>
          <li><strong>الاستخدام المثالي:</strong> مخصصة للـ Indexed Arrays عندما لا تهتم بالمؤشر السابق.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">sort_example.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$numbers</span> = [<span class="tok-num">40</span>, <span class="tok-num">10</span>, <span class="tok-num">30</span>, <span class="tok-num">20</span>];

<span class="tok-cmt">// Sort تصاعدي للقيم</span>
<span class="tok-fn">sort</span>(<span class="tok-var">$numbers</span>);

<span class="tok-cmt">// النتيجة: [10, 20, 30, 40]</span>
<span class="tok-fn">print_r</span>(<span class="tok-var">$numbers</span>);

<span class="tok-var">$names</span> = [<span class="tok-str">"سارة"</span>, <span class="tok-str">"أحمد"</span>, <span class="tok-str">"محمود"</span>];
<span class="tok-fn">sort</span>(<span class="tok-var">$names</span>);
<span class="tok-cmt">// النتيجة: ["أحمد", "سارة", "محمود"]</span></pre>
        </div>
      </div>''',
    notes_title="دالة sort",
    notes_script="تذكر أن sort ترتب القيم وتعيد ترقيم المفاتيح من 0. لا تستخدمها مع الـ Associative Arrays إذا كنت تريد الحفاظ على مفاتيحك!",
    notes_list=["Sort تصاعدي للأرقام والنصوص", "إعادة ترقيم الفهارس من 0", "تعديل الـ Array الأصلية مباشرة"]
)

# ==========================================
# Slide 19: Sorting 2: asort() vs ksort()
# ==========================================
make_slide(
    index=18,
    title="دوال الـ Sort: دالتا asort و ksort للـ Associative Arrays",
    eyebrow="دوال الـ Sort &middot; 2",
    slide_title="عمل Sort للـ Associative Arrays: asort() مقابل ksort()",
    slide_text="الـ Sort مع الحفاظ الكامل على ارتباط كل مفتاح بقيمته الأصلية:",
    body_content='''<div class="compare-card">
        <div class="compare-header">
          <span class="badge-echo">asort() &mdash; Sort بالقيم (Values)</span>
          <span class="vs-badge">VS</span>
          <span class="badge-print">ksort() &mdash; Sort بالمفاتيح (Keys)</span>
        </div>
        <div class="compare-rows">
          <div class="compare-row">
            <div class="compare-item">تعمل Sort حسب <strong>القيم</strong> تصاعدياً</div>
            <div class="compare-feature">أساس الـ Sort</div>
            <div class="compare-item">تعمل Sort حسب <strong>المفاتيح</strong> تصاعدياً</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">نعم، المفتاح يبقى مرتبطاً بقيمته</div>
            <div class="compare-feature">حفظ الارتباط</div>
            <div class="compare-item">نعم، المفتاح يحتفظ بقيمته دون تغيير</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">ترتيب درجات الطلاب، أسعار المنتجات</div>
            <div class="compare-feature">أفضل استخدام</div>
            <div class="compare-item">ترتيب الحقول أبجدياً، قواميس المعاني</div>
          </div>
        </div>
      </div>''',
    notes_title="مقارنة asort مقابل ksort",
    notes_script="asort تعمل Sort بالقيم مع حفظ المفاتيح (مثال: ترتيب درجات الطلاب من الأصغر للأكبر مع بقاء اسم كل طالب مرتبطاً بدرجته). ksort تعمل Sort بالمفاتيح (مثال: ترتيب أسماء الطلاب أبجدياً).",
    notes_list=["asort: عمل Sort بالقيم مع حفظ المفاتيح", "ksort: عمل Sort بالمفاتيح أبجدياً أو عددياً", "ضرورية جداً للـ Associative Arrays"]
)

# ==========================================
# Slide 20: Code comparison: asort vs ksort
# ==========================================
make_slide(
    index=19,
    title="تطبيق عملي: مقارنة asort و ksort بالكود",
    eyebrow="دوال الـ Sort &middot; تطبيق",
    slide_title="مقارنة عملية بالكود بين asort() و ksort()",
    slide_text="تطبيق الدالتين على نفس الـ Array لملاحظة الفارق الدقيق في النتيجة:",
    body_content='''<div class="grid-2">
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">asort_values.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$prices</span> = [
    <span class="tok-str">"شاشة"</span>  =&gt; <span class="tok-num">5000</span>,
    <span class="tok-str">"ماوس"</span>   =&gt; <span class="tok-num">300</span>,
    <span class="tok-str">"كيبورد"</span> =&gt; <span class="tok-num">800</span>
];

<span class="tok-cmt">// Sort بالقيم تصاعدياً (من الأرخص للأغلى)</span>
<span class="tok-fn">asort</span>(<span class="tok-var">$prices</span>);

<span class="tok-cmt">/* الناتج:
ماوس   => 300
كيبورد => 800
شاشة   => 5000
*/</span></pre>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">ksort_keys.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$codes</span> = [
    <span class="tok-str">"US"</span> =&gt; <span class="tok-str">"أمريكا"</span>,
    <span class="tok-str">"EG"</span> =&gt; <span class="tok-str">"مصر"</span>,
    <span class="tok-str">"SA"</span> =&gt; <span class="tok-str">"السعودية"</span>
];

<span class="tok-cmt">// Sort بالمفاتيح تصاعدياً (أبجدياً EG, SA, US)</span>
<span class="tok-fn">ksort</span>(<span class="tok-var">$codes</span>);

<span class="tok-cmt">/* الناتج:
EG => مصر
SA => السعودية
US => أمريكا
*/</span></pre>
        </div>
      </div>''',
    notes_title="مقارنة عملية بالكود",
    notes_script="لاحظ كيف رتبت asort المنتجات بالسعر مع بقاء اسم المنتج، بينما رتبت ksort الدول حسب رمز الدولة EG ثم SA ثم US.",
    notes_list=["asort عملت Sort بالسعر (القيم)", "ksort عملت Sort برمز الدولة (المفاتيح)", "حفظ الارتباط كامل في الحالتين"]
)

# ==========================================
# Slide 21: Comprehensive Comparison Table
# ==========================================
make_slide(
    index=20,
    title="جدول المقارنة الشامل لدوال الـ Arrays الـ 10 الأساسية",
    eyebrow="ملخص الدوال &middot; مرجع سريع",
    slide_title="جدول المقارنة الشامل لدوال الـ Arrays الأساسية",
    slide_text="مرجع سريع يلخص وظيفة كل دالة ونوع تعديلها والقيمة التي تعيدها:",
    body_content='''<div class="flow-steps">
        <div class="flow-step">
          <div class="flow-icon">🛠️</div>
          <div class="flow-title">المعالجة (Manipulation)</div>
          <div class="flow-desc">
            <code>array_push</code>: إضافة بالنهاية<br>
            <code>array_pop</code>: استخراج من النهاية<br>
            <code>array_merge</code>: دمج Arrays<br>
            <code>unset</code>: حذف عنصر محدد
          </div>
        </div>
        <div class="flow-step">
          <div class="flow-icon">🔍</div>
          <div class="flow-title">البحث والفحص (Search/Check)</div>
          <div class="flow-desc">
            <code>count</code>: حساب إجمالي العناصر<br>
            <code>in_array</code>: فحص وجود قيمة (True/False)<br>
            <code>array_key_exists</code>: فحص وجود مفتاح
          </div>
        </div>
        <div class="flow-step">
          <div class="flow-icon">⚡</div>
          <div class="flow-title">الترتيب والـ Sort (Sorting)</div>
          <div class="flow-desc">
            <code>sort</code>: عمل Sort للقيم مع إعادة الفهارس<br>
            <code>asort</code>: عمل Sort للقيم مع حفظ المفاتيح<br>
            <code>ksort</code>: عمل Sort حسب المفاتيح
          </div>
        </div>
      </div>''',
    notes_title="الجدول الشامل لدوال الـ Arrays",
    notes_script="هذه الشريحة تلخص كل شيء في صفحة واحدة كمرجع سريع للطلاب قبل الانتقال للتمارين.",
    notes_list=["ملخص عائلة المعالجة", "ملخص عائلة البحث والتحقق", "ملخص عائلة الترتيب والـ Sort"]
)

# ==========================================
# Slide 22: Common Pitfalls & Mistakes
# ==========================================
make_slide(
    index=21,
    title="أخطاء وفخاخ شائعة في دوال الـ Arrays",
    eyebrow="احذر هذه الأخطاء &middot; فخاخ برمجية",
    slide_title="أخطاء شائعة في التعامل مع دوال الـ Arrays",
    slide_text="تجنب هذه المشكلات التي يقع فيها أغلب المطورين في بداية رحلتهم:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ فخ 1: كتابة $arr = sort($arr)</div>
          <ul class="bullet-list">
            <li>دوال الـ Sort (<code>sort</code>, <code>asort</code>, <code>ksort</code>) تعدل الـ Array بالمرجع وتعيد <code>true</code>!</li>
            <li>كتابة <code>$arr = sort($arr);</code> ستمسح الـ Array الخاصة بك وتجعل المتغير يساوي <code>true</code> (boolean)!</li>
            <li><strong>التصحيح:</strong> استدعِ الدالة وحدها: <code>sort($arr);</code> ثم تعامل مع <code>$arr</code> كالمعتاد.</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ فخ 2: فجوات unset وإهمال strict</div>
          <ul class="bullet-list">
            <li>حذف عنصر بـ <code>unset($arr[1])</code> يترك فجوة في الفهارس؛ الترقيم لن يعاد تلقائياً من 0 إلا بـ <code>array_values()</code>.</li>
            <li>استدعاء <code>in_array()</code> بدون المعامل الصارم <code>true</code> قد يسبب أخطاء أمنية مع المقارنة الفضفاضة.</li>
            <li>استخدام <code>sort</code> بالخطأ مع Associative Array يمسح جميع مفاتيحها النصية للأبد!</li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء وفخاخ شائعة",
    notes_script="أشهر خطأ على الإطلاق هو $arr = sort($arr). الطلاب ينسون أن دوال الـ Sort تعيد boolean وتعدل الـ Array الأصلية بالمرجع.",
    notes_list=["خطأ تعيين ناتج دالة sort لمتغير", "فهم سلوك unset والفهارس", "أهمية الوضع الصارم في in_array", "تجنب استخدام sort مع الـ Associative Arrays"]
)

# ==========================================
# Slide 23: Section Divider: Exercises
# ==========================================
make_slide(
    index=22,
    title="تمارين وتطبيقات عملية",
    eyebrow="التطبيق العملي",
    slide_title="تمارين وتطبيقات عملية على الـ Arrays",
    slide_text="حان وقت اختبار مهاراتك البرمجية من خلال 3 تمارين تطبيقية متنوعة:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">تمرين 1: مكدس المهام بـ Push و Pop و Merge</span>
        <span class="pill-badge">تمرين 2: فحص الصلاحيات بـ in_array و array_key_exists</span>
        <span class="pill-badge">تمرين 3: عمل Sort لقائمة منتجات المتجر بـ asort و ksort</span>
      </div>''',
    notes_title="فاصل التمارين العملية",
    notes_script="التمارين مصممة لتغطي المجموعات الثلاث: المعالجة، والبحث، والـ Sort.",
    notes_list=["تمرين 1: معالجة", "تمرين 2: بحث وتحقق", "تمرين 3: Sort وترتيب"],
    is_divider=True
)

# ==========================================
# Slide 24: Exercise 1: Manipulation
# ==========================================
make_slide(
    index=23,
    title="تمرين 1: معالجة قائمة مهام برمجية",
    eyebrow="تمارين تطبيقية &middot; 1",
    slide_title="تمرين 1: إدارة قائمة مهام (Push, Pop, Merge, Unset)",
    slide_text="قم بتنفيذ العمليات التالية على الـ Arrays ولاحظ التغييرات خطوة بخطوة:",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في التمرين 1</div>
          <ul class="bullet-list" style="margin-top:0.4rem;">
            <li>أنشئ Array مهام أولية: <code>["مراجعة الكود", "كتابة الاختبارات"]</code>.</li>
            <li>أضف مهمتين بالآخر بـ <code>array_push()</code>: "نشر المشروع" و "توثيق API".</li>
            <li>استخرج وأنهِ المهمة الأخيرة بـ <code>array_pop()</code> واطبع اسمها.</li>
            <li>ادمج معها Array مهام طارئة بـ <code>array_merge()</code>.</li>
            <li>احذف المهمة الأولى بـ <code>unset()</code> واطبع العدد المتبقي بـ <code>count()</code>.</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">exercise1_tasks.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$tasks</span> = [<span class="tok-str">"مراجعة الكود"</span>, <span class="tok-str">"كتابة الاختبارات"</span>];

<span class="tok-cmt">// 1. إضافة مهام جديدة</span>
<span class="tok-fn">array_push</span>(<span class="tok-var">$tasks</span>, <span class="tok-str">"نشر المشروع"</span>, <span class="tok-str">"توثيق API"</span>);

<span class="tok-cmt">// 2. سحب آخر مهمة</span>
<span class="tok-var">$done</span> = <span class="tok-fn">array_pop</span>(<span class="tok-var">$tasks</span>);

<span class="tok-cmt">// 3. دمج مهام طارئة</span>
<span class="tok-var">$urgent</span> = [<span class="tok-str">"إصلاح ثغرة"</span>];
<span class="tok-var">$tasks</span> = <span class="tok-fn">array_merge</span>(<span class="tok-var">$tasks</span>, <span class="tok-var">$urgent</span>);

<span class="tok-cmt">// 4. حذف وفحص العدد</span>
<span class="tok-kw">unset</span>(<span class="tok-var">$tasks</span>[<span class="tok-num">0</span>]);
<span class="tok-kw">echo</span> <span class="tok-str">"عدد المهام المتبقية: "</span> . <span class="tok-fn">count</span>(<span class="tok-var">$tasks</span>);</pre>
        </div>
      </div>''',
    notes_title="تمرين 1: معالجة الـ Arrays",
    notes_script="تمرين شامل يطبق الأربع دوال للمعالجة في سياق عملي حقيقي لإدارة المهام.",
    notes_list=["تطبيق push و pop", "تطبيق merge و unset", "حساب الناتج النهائي بـ count"]
)

# ==========================================
# Slide 25: Exercise 2: Search & Check
# ==========================================
make_slide(
    index=24,
    title="تمرين 2: نظام تحقق أمني وفحص صلاحيات",
    eyebrow="تمارين تطبيقية &middot; 2",
    slide_title="تمرين 2: فحص الصلاحيات (in_array & array_key_exists)",
    slide_text="بناء محرك تحقق يفحص رتبة المستخدم وحقول الملف الشخصي الإلزامية في الـ Array:",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في التمرين 2</div>
          <ul class="bullet-list" style="margin-top:0.4rem;">
            <li>لديك Array رتب مسموح لها بالنشر: <code>["admin", "manager", "publisher"]</code>.</li>
            <li>افحص باستخدام <code>in_array()</code> بوضع صارم إذا كانت رتبة الزائر <code>$userRole</code> مصرحاً لها.</li>
            <li>لديك Associative Array لبيانات مستخدم، تحقق باستخدام <code>array_key_exists()</code> من احتواء الـ Array على مفتاح <code>"email"</code> حتى وإن كان غير محدد.</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">exercise2_check.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$allowed</span> = [<span class="tok-str">"admin"</span>, <span class="tok-str">"manager"</span>, <span class="tok-str">"publisher"</span>];
<span class="tok-var">$userRole</span> = <span class="tok-str">"manager"</span>;

<span class="tok-cmt">// 1. فحص الصلاحية</span>
<span class="tok-kw">if</span> (<span class="tok-fn">in_array</span>(<span class="tok-var">$userRole</span>, <span class="tok-var">$allowed</span>, <span class="tok-kw">true</span>)) {
    <span class="tok-kw">echo</span> <span class="tok-str">"مسموح بالنشر &lt;br&gt;"</span>;
}

<span class="tok-var">$profile</span> = [<span class="tok-str">"name"</span> =&gt; <span class="tok-str">"أحمد"</span>, <span class="tok-str">"email"</span> =&gt; <span class="tok-kw">null</span>];

<span class="tok-cmt">// 2. فحص وجود الحقل</span>
<span class="tok-kw">if</span> (<span class="tok-fn">array_key_exists</span>(<span class="tok-str">"email"</span>, <span class="tok-var">$profile</span>)) {
    <span class="tok-kw">echo</span> <span class="tok-str">"حقل البريد موجود في النموذج."</span>;
}</pre>
        </div>
      </div>''',
    notes_title="تمرين 2: البحث والتحقق",
    notes_script="هذا التمرين يرسخ التفكير الأمني: فحص الصلاحية بصرامة، والتحقق من وجود المفاتيح في مدخلات المستخدم.",
    notes_list=["استخدام in_array مع الوضع الصارم true", "فحص وجود المفاتيح بـ array_key_exists", "التعامل مع القيم الفارغة null"]
)

# ==========================================
# Slide 26: Exercise 3: Sorting
# ==========================================
make_slide(
    index=25,
    title="تمرين 3: عمل Sort لأسعار ورموز المنتجات",
    eyebrow="تمارين تطبيقية &middot; 3",
    slide_title="تمرين 3: عمل Sort وترتيب للمنتجات (asort مقابل ksort)",
    slide_text="عمل Sort لقائمة أسعار متجر إلكتروني تارة حسب السعر وتارة حسب كود المنتج:",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في التمرين 3</div>
          <ul class="bullet-list" style="margin-top:0.4rem;">
            <li>أنشئ Array منتجات: <code>["PROD-C" => 120, "PROD-A" => 450, "PROD-B" => 90]</code>.</li>
            <li>اعمل Sort للمنتجات من الأرخص للأغلى باستخدام <code>asort()</code> واطبع النتيجة.</li>
            <li>اعمل Sort للمنتجات أبجدياً حسب كود المنتج باستخدام <code>ksort()</code> واطبع النتيجة.</li>
            <li>تأكد من عدم استخدام <code>sort()</code> العادية حتى لا تفقد أكواد المنتجات!</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">exercise3_sort.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$items</span> = [
    <span class="tok-str">"PROD-C"</span> =&gt; <span class="tok-num">120</span>,
    <span class="tok-str">"PROD-A"</span> =&gt; <span class="tok-num">450</span>,
    <span class="tok-str">"PROD-B"</span> =&gt; <span class="tok-num">90</span>
];

<span class="tok-cmt">// 1. Sort بالسعر تصاعدياً (قيم)</span>
<span class="tok-fn">asort</span>(<span class="tok-var">$items</span>);
<span class="tok-cmt">// PROD-B (90), PROD-C (120), PROD-A (450)</span>

<span class="tok-cmt">// 2. Sort بكود المنتج تصاعدياً (مفاتيح)</span>
<span class="tok-fn">ksort</span>(<span class="tok-var">$items</span>);
<span class="tok-cmt">// PROD-A (450), PROD-B (90), PROD-C (120)</span></pre>
        </div>
      </div>''',
    notes_title="تمرين 3: الـ Sort والترتيب",
    notes_script="هذا التمرين يوضح عملياً متى نلجأ لـ asort (عمل Sort بالأسعار للمشتري) ومتى نلجأ لـ ksort (تنظيم بالمخزن حسب الرمز).",
    notes_list=["تطبيق asort على الأسعار", "تطبيق ksort على الأكواد", "حماية مفاتيح الـ Associative Array"]
)

# ==========================================
# Slide 27: Section Divider: Review Time
# ==========================================
make_slide(
    index=26,
    title="وقت المراجعة والتأمل السريع",
    eyebrow="نقاش ومراجعة",
    slide_title="وقت المراجعة والتأمل السريع",
    slide_text="اختبر فهمك للمفاهيم الأساسية التي تم تناولها اليوم:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">ماذا يحدث لمفاتيح الـ Associative Array إذا رتبتها بـ sort() بدلاً من asort()؟</span>
        <span class="pill-badge">متى تُفضل استخدام array_key_exists() على isset()؟</span>
        <span class="pill-badge">ما القيمة التي تعيدها دالة array_push() وما الفرق بينها وبين $arr[] = $val؟</span>
      </div>''',
    notes_title="فاصل المراجعة",
    notes_script="أسئلة تحفيزية تؤكد على الفروق الجوهرية التي تميز المطور المتقن عن غيره.",
    notes_list=["سؤال مصير المفاتيح مع sort", "سؤال الفرق بين array_key_exists و isset", "سؤال القيمة الراجعة لـ array_push"],
    is_divider=True
)

# ==========================================
# Slide 28: Summary: What We Learned Today
# ==========================================
make_slide(
    index=27,
    title="اللي اتعلمناه النهاردة",
    eyebrow="ملخص المحاضرة 05",
    slide_title="اللي اتعلمناه النهاردة في المحاضرة 05",
    slide_text="خلاصة شاملة لما تم إتقانه اليوم في عالم الـ Arrays في PHP:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">أنواع الـ Arrays</div>
            <div class="topic-desc">الـ Indexed بالفهارس 0..N، والـ Associative بمفاتيح Key=>Value، والـ Multidimensional للسجلات والجداول</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">دوال التعديل (Manipulation)</div>
            <div class="topic-desc">array_push للإلحاق، array_pop للاستخراج، array_merge للدمج، و unset للحذف المباشر</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">دوال البحث والفحص (Search/Check)</div>
            <div class="topic-desc">count لحساب الحجم، in_array للتحقق الصارم من القيم، و array_key_exists للمفاتيح</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">دوال الـ Sort</div>
            <div class="topic-desc">sort للترقيم الجديد، asort للـ Sort مع حفظ المفاتيح، و ksort لـ Sort المفاتيح ذاتها</div>
          </div>
        </div>
      </div>''',
    notes_title="ملخص المحاضرة 05",
    notes_script="أصبح لديكم الآن صندوق أدوات كامل للتعامل مع أي مجموعة بيانات في PHP: بناء، تعديل، بحث، و Sort.",
    notes_list=["إتقان أنواع الـ Arrays الثلاثة", "إتقان دوال المعالجة الـ 4", "إتقان دوال البحث والتحقق الـ 3", "إتقان دوال الـ Sort الـ 3"]
)

# ==========================================
# Slide 29: Conclusion & Thank You
# ==========================================
make_slide(
    index=28,
    title="شكرًا لكم &mdash; نهاية المحاضرة 05",
    eyebrow="الخاتمة &middot; المحاضرة 05",
    slide_title="شكرًا لكم! أبدعتم في إتقان الـ Arrays",
    slide_text="اليوم امتلكتم المهارة الأساسية لإدارة البيانات المعقدة في PHP. طبّقوا التمارين واستعدوا للخطوة التالية:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">Indexed &amp; Associative Arrays</span>
        <span class="pill-badge">Manipulation: push, pop, merge, unset</span>
        <span class="pill-badge">Search: in_array, key_exists, count</span>
        <span class="pill-badge">Sort: sort, asort, ksort</span>
        <span class="pill-badge">المحاضرة القادمة: الدوال في PHP (Functions) 🚀</span>
      </div>''',
    notes_title="خاتمة المحاضرة 05",
    notes_script="شكراً لكم على تركيزكم. في المحاضرة السادسة سنبني دوالنا الخاصة Functions ونتعلم مبادئ DRY وتنظيم الأكواد. نراكم على خير!",
    notes_list=["شكر وتشجيع الطلاب", "الحث على حل التمارين", "التمهيد للمحاضرة 06: الدوال Functions"],
    is_divider=True
)

print("All 29 slides generated successfully for Lecture 05!")
