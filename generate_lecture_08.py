# -*- coding: utf-8 -*-
"""
Generator script for Lecture 08:
String Manipulation, File System & Streams, and JSON Data Exchange
26 Slides Total.
"""
from build_lecture_08 import make_slide

# ==========================================
# Slide 01: Cover
# ==========================================
make_slide(
    index=0,
    title="معالجة النصوص، نظام الملفات، وتنسيق JSON",
    eyebrow="أساسيات PHP &middot; المحاضرة 08",
    slide_title="معالجة النصوص، نظام الملفات، وتنسيق JSON",
    slide_text="في هذه المحاضرة سنتعلم مهارات التعامل مع البيانات وتخزينها الدائم: تنظيف النصوص وتنسيقها باحترافية، القراءة والكتابة في الملفات النصية و CSV، وتبادل وتخزين البيانات المنظمة بصيغة JSON.",
    body_content='''<div class="cover-mark">
        <div><div class="num">03</div><div class="lbl">محاور رئيسية</div></div>
        <div><div class="num">03</div><div class="lbl">أمثلة برمجية كاملة</div></div>
        <div><div class="num">03</div><div class="lbl">واجبات وتطبيقات</div></div>
        <div><div class="num">~60 د</div><div class="lbl">المدة التقديرية</div></div>
      </div>''',
    notes_title="المحاضرة 08: معالجة النصوص، الملفات، و JSON",
    notes_script="أهلاً بكم في المحاضرة الثامنة. بعد أن أتقنا نماذج HTML في المحاضرة السابقة، نتعلم اليوم كيفية تنظيف ومعالجة مدخلات المستخدمين النصية، ثم حفظها واسترجاعها من ملفات السيرفر بصيغ نصية و JSON.",
    notes_list=["معالجة النصوص ودوالها الأساسية", "نظام الملفات والتدفقات المتقدمة", "تخزين وتبادل بيانات JSON", "أمثلة حية وواجبات عملية"],
    is_cover=True
)

# ==========================================
# Slide 02: Roadmap
# ==========================================
make_slide(
    index=1,
    title="خريطة ومحاور المحاضرة 08",
    eyebrow="نظرة عامة &middot; محتويات المحاضرة",
    slide_title="خريطة ومحاور المحاضرة 08",
    slide_text="ثلاثة محاور متكاملة تبني مساراً منطقياً لمعالجة البيانات وحفظها الدائم في خادم الويب:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">معالجة النصوص (String Manipulation)</div>
            <div class="topic-desc">علامات التنصيص، التنظيف، التقطيع، الدمج، الاستبدال، ودعم النصوص العربية (mb_*)</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">نظام الملفات (Filesystem & Streams)</div>
            <div class="topic-desc">القراءة والكتابة السريعة والمتقدمة، فحص الملفات، إدارة المجلدات، وقفل الملفات (flock)</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">تبادل البيانات بصيغة JSON</div>
            <div class="topic-desc">ترميز المصفوفات بـ json_encode، حل النصوص بـ json_decode، وبناء Flat-File Database</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">تطبيقات وواجبات عملية</div>
            <div class="topic-desc">محلل نصوص، مسجل زيارات للموقع، ونظام إدارة منتجات بملف JSON</div>
          </div>
        </div>
      </div>''',
    notes_title="خريطة المحاضرة 08",
    notes_script="هذه هي محاورنا اليوم: سنبدأ من النصوص لأنها المدخل الأول من المستخدم، ثم ننتقل لتخزينها في ملفات بصيغة نصية و JSON، ونختم بالواجبات العملية.",
    notes_list=["معالجة النصوص", "نظام الملفات", "تنسيق JSON", "التطبيقات والواجبات"]
)

# ==========================================
# Slide 03: Double vs Single quotes & Interpolation
# ==========================================
make_slide(
    index=2,
    title="تضمين النصوص: علامات التنصيص المزدوجة والمفردة",
    eyebrow="معالجة النصوص &middot; 1",
    slide_title="تضمين النصوص: علامات التنصيص المزدوجة والمفردة",
    slide_text="في PHP يوجد فرق جوهري بين علامات التنصيص المزدوجة <code>\"...\"</code> والمفردة <code>'...'</code> في تفسير المتغيرات ورموز الهروب:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>المزدوجة <code>"..."</code>:</strong> تُفعّل التضمين (Variable Interpolation) مثل <code>"مرحباً $name"</code> وتفسر رموز الهروب كالسطر الجديد <code>\\n</code> وعلامة الجدولة <code>\\t</code>.</li>
          <li><strong>المفردة <code>'...'</code>:</strong> تعامل النص حرفياً (Literal)، أسرع قليلاً، ولا تفسر المتغيرات (يطبع <code>$name</code> كأحرف).</li>
          <li><strong>التضمين المعقد بالأقواس:</strong> يفضل كتابة <code>"الرتبة: {$user['role']}"</code> لتفادي أي التباس للمفسر البرمجي.</li>
          <li><strong>رمز الهروب (Escape):</strong> تستخدم علامة <code>\\</code> لتجاوز التنصيص مثل <code>\\"</code> أو <code>\\'</code> أو لطباعة <code>\\$</code>.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">quotes.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$name</span> = <span class="tok-str">"أحمد"</span>;

<span class="tok-cmt">// علامات مفردة: طباعة حرفية</span>
<span class="tok-kw">echo</span> <span class="tok-str">'أهلاً $name \\n'</span>;
<span class="tok-cmt">// الناتج: أهلاً $name \\n</span>

<span class="tok-cmt">// علامات مزدوجة: معالجة وتضمين المتغير</span>
<span class="tok-kw">echo</span> <span class="tok-str">"أهلاً $name"</span>;
<span class="tok-cmt">// الناتج: أهلاً أحمد</span>

<span class="tok-cmt">// التضمين المعقد لعناصر المصفوفات</span>
<span class="tok-var">$user</span> = [<span class="tok-str">'role'</span> =&gt; <span class="tok-str">'مدير'</span>];
<span class="tok-kw">echo</span> <span class="tok-str">"الرتبة: {$user['role']}"</span>;</pre>
        </div>
      </div>''',
    notes_title="تضمين النصوص وعلامات التنصيص",
    notes_script="القاعدة الذهبية: إذا كان النص يحتوي على متغيرات أو سطر جديد، استخدم علامات مزدوجة. إذا كان نصاً ثابتاً، استخدم علامات مفردة لأنها أوضح ولا تتطلب تحليلاً للمتغيرات.",
    notes_list=["علامات مفردة: حرفية ولا تترجم المتغيرات", "علامات مزدوجة: تفعل التضمين والرموز الخاصة", "التضمين المعقد بالأقواس المعقوفة {$var}"]
)

# ==========================================
# Slide 04: Basic String Functions: strlen, trim, strtolower/upper
# ==========================================
make_slide(
    index=3,
    title="دوال النصوص الأساسية: strlen, trim, strtolower/upper",
    eyebrow="معالجة النصوص &middot; 2",
    slide_title="دوال النصوص الأساسية في PHP",
    slide_text="أشهر الدوال وأكثرها استخداماً لتنظيف وفحص وتوحيد صيغة النصوص ومدخلات المستخدمين:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>strlen($str)</code>: لحساب عدد بايتات النص (للنصوص العربية نفضل <code>mb_strlen</code>).</li>
          <li><code>trim($str)</code>: إزالة المسافات الفارغة والأسطر الجديدة من بداية ونهاية النص.</li>
          <li><code>strtolower($str)</code>: تحويل النص بالكامل لأحرف صغيرة (مثالي لتوحيد البريد الإلكتروني).</li>
          <li><code>strtoupper($str)</code>: تحويل النص بالكامل لأحرف كبيرة (مثل رموز الدول والعملات).</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">basic_str.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$input</span> = <span class="tok-str">"   Ahmed@Example.COM   "</span>;

<span class="tok-cmt">// تنظيف المسافات من الأطراف</span>
<span class="tok-var">$clean</span> = <span class="tok-fn">trim</span>(<span class="tok-var">$input</span>);

<span class="tok-cmt">// توحيد الأحرف لصغيرة</span>
<span class="tok-var">$email</span> = <span class="tok-fn">strtolower</span>(<span class="tok-var">$clean</span>);

<span class="tok-kw">echo</span> <span class="tok-var">$email</span>;
<span class="tok-cmt">// الناتج: ahmed@example.com</span></pre>
        </div>
      </div>''',
    notes_title="دوال النصوص الأساسية",
    notes_script="تنظيف المدخلات بـ trim وتوحيد حالة الأحرف بـ strtolower خطوتان أساسيتان قبل حفظ أي بريد إلكتروني في قاعدة البيانات.",
    notes_list=["تنظيف المسافات بـ trim", "توحيد الأحرف بـ strtolower و strtoupper", "حساب الطول بـ strlen و mb_strlen"]
)

# ==========================================
# Slide 05: Search, Slice & Split: strpos, substr, explode, implode
# ==========================================
make_slide(
    index=4,
    title="البحث والتقطيع والدمج: strpos, substr, explode, implode",
    eyebrow="معالجة النصوص &middot; 3",
    slide_title="البحث والتقطيع والتحويل بين النصوص والمصفوفات",
    slide_text="التحكم في الأجزاء الداخلية للنص والربط السريع بين النصوص ومصفوفات PHP:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>strpos($haystack, $needle)</code>: إرجاع فهرس أول ظهور للنص، أو <code>false</code> إن لم يوجد.</li>
          <li><code>substr($str, $start, $len)</code>: استخراج جزء محدد من النص بدءاً من فهرس معين.</li>
          <li><code>explode($separator, $str)</code>: <strong>تقطيع النص لمصفوفة</strong> بناءً على فاصل (مثل الفاصلة أو المسافة).</li>
          <li><code>implode($glue, $arr)</code>: <strong>دمج عناصر المصفوفة في نص واحد</strong> مع وضع فاصل بينها.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">slice_split.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$tags</span> = <span class="tok-str">"php, laravel, mysql"</span>;

<span class="tok-cmt">// تحويل النص إلى مصفوفة</span>
<span class="tok-var">$tagsArr</span> = <span class="tok-fn">explode</span>(<span class="tok-str">", "</span>, <span class="tok-var">$tags</span>);
<span class="tok-cmt">// ['php', 'laravel', 'mysql']</span>

<span class="tok-cmt">// إعادة دمجها مع فاصل مختلف</span>
<span class="tok-var">$tagString</span> = <span class="tok-fn">implode</span>(<span class="tok-str">" | "</span>, <span class="tok-var">$tagsArr</span>);
<span class="tok-kw">echo</span> <span class="tok-var">$tagString</span>;
<span class="tok-cmt">// الناتج: php | laravel | mysql</span></pre>
        </div>
      </div>''',
    notes_title="البحث والتقطيع والدمج",
    notes_script="explode و implode هما الجسر بين النصوص والمصفوفات. نستخدم explode عند قراءة قائمة كلمات مفصولة بفواصل، و implode عند تحويل مصفوفة إلى نص جاهز للعرض أو التخزين.",
    notes_list=["البحث عن موقع النص بـ strpos", "قص جزء من النص بـ substr", "explode: من نص إلى مصفوفة", "implode: من مصفوفة إلى نص"]
)

# ==========================================
# Slide 06: Search & Replace: str_replace
# ==========================================
make_slide(
    index=5,
    title="الاستبدال والفلترة: دالة str_replace",
    eyebrow="معالجة النصوص &middot; 4",
    slide_title="استبدال النصوص وفلترة الكلمات بـ str_replace()",
    slide_text="استبدال كلمة أو عدة كلمات داخل نص دفعة واحدة؛ تدعم تمرير نصوص مفردة أو مصفوفات من الكلمات:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>str_replace($search, $replace, $subject)</code>: تبحث عن <code>$search</code> وتستبدله بـ <code>$replace</code> داخل النص الأصلي.</li>
          <li><strong>استبدال مصفوفة كلمات:</strong> يمكن تمرير مصفوفة من الكلمات الممنوعة لاستبدالها جميعاً بكلمة واحدة مثل <code>"***"</code>.</li>
          <li><strong>الحساسية لحالة الأحرف:</strong> الدالة حساسة للأحرف (Case-sensitive)، ولتجاهل حالة الأحرف نستخدم <code>str_ireplace()</code>.</li>
          <li><strong>إرجاع نص جديد:</strong> النصوص في PHP ثابتة القيمة؛ الدالة تعيد نسخة معدلة دون تغيير المتغير الأصلي.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">replace.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$comment</span> = <span class="tok-str">"هذا الموقع سيء وتطبيق غبي"</span>;

<span class="tok-cmt">// مصفوفة كلمات محظورة</span>
<span class="tok-var">$banned</span> = [<span class="tok-str">"سيء"</span>, <span class="tok-str">"غبي"</span>];

<span class="tok-cmt">// استبدالها بنجوم</span>
<span class="tok-var">$censored</span> = <span class="tok-fn">str_replace</span>(<span class="tok-var">$banned</span>, <span class="tok-str">"***"</span>, <span class="tok-var">$comment</span>);

<span class="tok-kw">echo</span> <span class="tok-var">$censored</span>;
<span class="tok-cmt">// الناتج: هذا الموقع *** وتطبيق ***</span></pre>
        </div>
      </div>''',
    notes_title="استبدال النصوص وفلترة الكلمات",
    notes_script="ميزة تمرير مصفوفة لـ str_replace توفر أسطراً طويلة من الحلقات التكرارية وتعتبر الحل الأسرع والأكثر كفاءة لتنقية التعليقات وفلترة المدخلات.",
    notes_list=["بناء دالة str_replace", "استبدال قائمة كلمات ممنوعة دفعة واحدة", "الفرق بين str_replace و str_ireplace"]
)

# ==========================================
# Slide 07: Example 1: Text Cleaner & Profanity Filter
# ==========================================
make_slide(
    index=6,
    title="مثال 1: تنظيف النصوص وفلترة التعليقات",
    eyebrow="معالجة النصوص &middot; مثال 1",
    slide_title="مثال 1: محرك معالجة وفلترة مدخلات المستخدم",
    slide_text="تطبيق عملي يجمع دوال <code>trim</code> و <code>str_replace</code> و <code>explode</code> لتنظيف مدخلات التعليقات:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">الهدف البرمجي</div>
          <p>تنظيف تعليق قادم من المستخدم، استبدال الكلمات غير اللائقة بنجوم، وحساب عدد الكلمات في التعليق النظيف.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">clean_comment.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$rawComment</span> = <span class="tok-str">"   خدمة سيئة جداً من هذا الموقع   "</span>;

<span class="tok-cmt">// 1. تنظيف الأطراف</span>
<span class="tok-var">$clean</span> = <span class="tok-fn">trim</span>(<span class="tok-var">$rawComment</span>);

<span class="tok-cmt">// 2. فلترة الكلمات</span>
<span class="tok-var">$clean</span> = <span class="tok-fn">str_replace</span>(<span class="tok-str">"سيئة"</span>, <span class="tok-str">"***"</span>, <span class="tok-var">$clean</span>);

<span class="tok-cmt">// 3. حساب عدد الكلمات عبر explode</span>
<span class="tok-var">$words</span> = <span class="tok-fn">explode</span>(<span class="tok-str">" "</span>, <span class="tok-var">$clean</span>);

<span class="tok-kw">echo</span> <span class="tok-str">"التعليق بعد التنقية: $clean&lt;br&gt;"</span>;
<span class="tok-kw">echo</span> <span class="tok-str">"إجمالي الكلمات: "</span> . <span class="tok-fn">count</span>(<span class="tok-var">$words</span>);</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/clean_comment.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.95rem;">
التعليق بعد التنقية: خدمة *** جداً من هذا الموقع
إجمالي الكلمات: 6
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال 1: تنظيف وفلترة النصوص",
    notes_script="هذا المثال يوضح تتابع المعالجة المنطقية: نبدأ بالتنظيف الخارجي بـ trim، ثم المعالجة الداخلية بـ str_replace، ثم التحليل الإحصائي بـ explode و count.",
    notes_list=["تسلسل خطوات معالجة النصوص", "دمج trim و str_replace معاً", "تحويل النص إلى كلمات بـ explode"]
)

# ==========================================
# Slide 08: Common Mistakes in String Processing
# ==========================================
make_slide(
    index=7,
    title="أخطاء شائعة في معالجة النصوص",
    eyebrow="احذر هذه الأخطاء &middot; 1",
    slide_title="أخطاء شائعة في معالجة النصوص والنصوص العربية",
    slide_text="تجنب هذه الهفوات البرمجية الشائعة التي تفسد معالجة الكلمات والنصوص العربية (UTF-8):",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ فخ strlen مع الحروف العربية</div>
          <ul class="bullet-list">
            <li>دالة <code>strlen()</code> تحسب <strong>عدد البايتات</strong> وليس عدد الحروف؛ فالحرف العربي يشغل بايتين (UTF-8)!</li>
            <li>كلمة <code>"مصر"</code> تعيد <code>strlen</code> لها <strong>6</strong> وليس 3!</li>
            <li><strong>التصحيح:</strong> استخدم دائماً عائلة <code>mb_*</code> مثل <code>mb_strlen($str, "UTF-8")</code> و <code>mb_substr()</code>.</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ فخ مقارنة strpos مع الصفر</div>
          <ul class="bullet-list">
            <li>إذا وُجدت الكلمة في بداية النص، ستعيد <code>strpos()</code> الفهرس <code>0</code>.</li>
            <li>كتابة <code>if (strpos(...) == false)</code> ستعتبر الصفر خطأ (Falsey) فتفشل المقارنة!</li>
            <li><strong>التصحيح:</strong> استخدم المقارنة الصارمة دائماً: <code>if (strpos(...) === false)</code>.</li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في معالجة النصوص",
    notes_script="انتبهوا جداً لعائلة mb_* مع النصوص العربية. الحرف العربي متعدد البايتات، وقص النصوص بـ substr العادية يقطع الحرف العربي نصفين وينتج نصوصاً مشوهة مثل علامات الاستفهام المعكوسة.",
    notes_list=["فخ strlen مع الأحرف العربية", "ضرورة استخدام mb_strlen و mb_substr", "فخ المقارنة الفضفاضة مع strpos وأهمية === false"]
)

# ==========================================
# Slide 09: Section Divider: Filesystem
# ==========================================
make_slide(
    index=8,
    title="نظام الملفات في PHP (Filesystem & Streams)",
    eyebrow="القسم الثاني",
    slide_title="نظام الملفات في PHP (Filesystem & Streams)",
    slide_text="كيف نقرأ ونكتب الملفات على السيرفر لتخزين البيانات الدائمة وسجلات النظام:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">القراءة والكتابة السريعة بـ file_get/put_contents</span>
        <span class="pill-badge">تدفقات الملفات المتقدمة (fopen, fread, fwrite, fclose)</span>
        <span class="pill-badge">فحص وإدارة الملفات والمجلدات وقفل التزامن (flock)</span>
      </div>''',
    notes_title="فاصل محور نظام الملفات",
    notes_script="ننتقل للقسم الثاني: نظام الملفات. هنا نتعلم كيف نجعل بيانات التطبيق باقية على القرص الصلب للسيرفر حتى بعد إغلاق المتصفح أو إعادة تشغيل السيرفر.",
    notes_list=["أهمية حفظ البيانات الدائمة", "طرق القراءة والكتابة في PHP", "إدارة الملفات وتجنب تضارب التزامن"],
    is_divider=True
)

# ==========================================
# Slide 10: Fast File I/O: file_get_contents & file_put_contents
# ==========================================
make_slide(
    index=9,
    title="القراءة والكتابة السريعة للملفات",
    eyebrow="نظام الملفات &middot; 1",
    slide_title="القراءة والكتابة السريعة للملفات",
    slide_text="أسهل وأسرع طريقتين للتعامل مع الملفات الصغيرة والمتوسطة بسطر واحد فقط دون تعقيد:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>file_get_contents($path)</code>: قراءة محتوى الملف بالكامل في متغير نصي واحد.</li>
          <li><code>file_put_contents($path, $data)</code>: كتابة النص في الملف (تنشئه إن لم يوجد، وتستبدل محتواه تلقائياً).</li>
          <li><strong>الإلحاق بـ <code>FILE_APPEND</code>:</strong> كتابة نص في نهاية الملف دون مسح المحتوى القديم (مثالي لسجلات الزيارات والأخطاء Logs).</li>
          <li><strong>قفل الكتابة بـ <code>LOCK_EX</code>:</strong> قفل الملف حصرياً أثناء الكتابة لمنع التضارب بين الزوار المتزامنين.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">file_quick.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$file</span> = <span class="tok-str">"log.txt"</span>;

<span class="tok-cmt">// كتابة سطر جديد مع الإلحاق والقفل الحصري</span>
<span class="tok-var">$line</span> = <span class="tok-str">"زيارة جديدة: "</span> . <span class="tok-fn">date</span>(<span class="tok-str">"Y-m-d H:i:s"</span>) . <span class="tok-str">"\\n"</span>;
<span class="tok-fn">file_put_contents</span>(<span class="tok-var">$file</span>, <span class="tok-var">$line</span>, <span class="tok-kw">FILE_APPEND</span> | <span class="tok-kw">LOCK_EX</span>);

<span class="tok-cmt">// قراءة الملف كاملاً وعرضه</span>
<span class="tok-var">$content</span> = <span class="tok-fn">file_get_contents</span>(<span class="tok-var">$file</span>);
<span class="tok-kw">echo</span> <span class="tok-fn">nl2br</span>(<span class="tok-var">$content</span>);</pre>
        </div>
      </div>''',
    notes_title="القراءة والكتابة السريعة",
    notes_script="في 80% من مهام تطوير الويب اليومية، file_get_contents و file_put_contents هما كل ما تحتاج إليه لقراءة الإعدادات أو كتابة سجلات الزيارات.",
    notes_list=["file_get_contents للقراءة السريعة", "file_put_contents للكتابة وإنشاء الملفات", "علم FILE_APPEND للإلحاق", "علم LOCK_EX لمنع التضارب"]
)

# ==========================================
# Slide 11: Advanced Streams: fopen, fread, fwrite, fclose
# ==========================================
make_slide(
    index=10,
    title="تدفقات الملفات المتقدمة (Advanced Streams)",
    eyebrow="نظام الملفات &middot; 2",
    slide_title="تدفقات الملفات المتقدمة: fopen و fread و fwrite",
    slide_text="للتحكم الدقيق في الملفات الضخمة سطراً بسطر دون استهلاك ذاكرة الخادم (RAM):",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>$handle = fopen($file, $mode)</code>: فتح مجرى اتصال (Handle) مع الملف بوضع محدد:
            <br>&bull; <code>'r'</code>: قراءة فقط من البداية.
            <br>&bull; <code>'w'</code>: كتابة فقط (يمسح المحتوى فوراً أو ينشئ الملف).
            <br>&bull; <code>'a'</code>: إلحاق في نهاية الملف (Append).
          </li>
          <li><code>fgets($handle)</code>: قراءة سطر واحد فقط في كل استدعاء (ممتاز للملفات الضخمة).</li>
          <li><code>fwrite($handle, $data)</code>: كتابة جزء من البيانات عبر المجرى.</li>
          <li><code>fclose($handle)</code>: <strong>إغلاق إجباري</strong> للمجرى لتحرير موارد نظام التشغيل.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">file_stream.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$handle</span> = <span class="tok-fn">fopen</span>(<span class="tok-str">"large_data.txt"</span>, <span class="tok-str">"r"</span>);

<span class="tok-kw">if</span> (<span class="tok-var">$handle</span>) {
    <span class="tok-cmt">// قراءة الملف سطراً بسطر حتى النهاية (feof)</span>
    <span class="tok-kw">while</span> (!<span class="tok-fn">feof</span>(<span class="tok-var">$handle</span>)) {
        <span class="tok-var">$line</span> = <span class="tok-fn">fgets</span>(<span class="tok-var">$handle</span>);
        <span class="tok-kw">echo</span> <span class="tok-var">$line</span> . <span class="tok-str">"&lt;br&gt;"</span>;
    }
    <span class="tok-fn">fclose</span>(<span class="tok-var">$handle</span>);
}</pre>
        </div>
      </div>''',
    notes_title="تدفقات الملفات المتقدمة",
    notes_script="لو لديك ملف بحجم 500 ميجابايت، فإن استخدام file_get_contents سيؤدي لامتلاء الذاكرة وتوقف السيرفر. الحل هو fopen مع fgets لقراءة سطر بسطر بأقل استهلاك ممكن للذاكرة.",
    notes_list=["أوضاع الفتح r و w و a", "قراءة سطر بسطر بـ fgets و feof", "أهمية إغلاق الملف دائماً بـ fclose", "توفير موارد الخادم للملفات الكبيرة"]
)

# ==========================================
# Slide 12: File & Directory Management Helpers
# ==========================================
make_slide(
    index=11,
    title="فحص وإدارة الملفات والمجلدات",
    eyebrow="نظام الملفات &middot; 3",
    slide_title="دوال فحص وإدارة الملفات والمجلدات",
    slide_text="التحقق من وجود الملفات، معرفة حجمها، حذفها، وإنشاء المجلدات برمجياً:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>file_exists($path)</code>: التحقق من وجود الملف أو المجلد قبل محاولة فتحه.</li>
          <li><code>is_file($path)</code> & <code>is_dir($path)</code>: التمييز بين الملفات العادية والمجلدات.</li>
          <li><code>filesize($path)</code>: حساب حجم الملف بالبايتات.</li>
          <li><code>unlink($path)</code>: <strong>حذف ملف نهائياً</strong> من القرص الصلب.</li>
          <li><code>mkdir($dir, 0777, true)</code>: إنشاء مجلد جديد مع دعم المجلدات المتداخلة (Recursive).</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">file_helpers.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$dir</span> = <span class="tok-str">"uploads/invoices"</span>;

<span class="tok-cmt">// إنشاء المجلد إن لم يكن موجوداً</span>
<span class="tok-kw">if</span> (!<span class="tok-fn">is_dir</span>(<span class="tok-var">$dir</span>)) {
    <span class="tok-fn">mkdir</span>(<span class="tok-var">$dir</span>, <span class="tok-num">0755</span>, <span class="tok-kw">true</span>);
}

<span class="tok-var">$file</span> = <span class="tok-str">"temp_report.pdf"</span>;
<span class="tok-cmt">// حذف الملف بعد إرساله</span>
<span class="tok-kw">if</span> (<span class="tok-fn">file_exists</span>(<span class="tok-var">$file</span>)) {
    <span class="tok-fn">unlink</span>(<span class="tok-var">$file</span>);
    <span class="tok-kw">echo</span> <span class="tok-str">"تم حذف الملف المؤقت بنجاح"</span>;
}</pre>
        </div>
      </div>''',
    notes_title="إدارة الملفات والمجلدات",
    notes_script="دائماً افحص file_exists قبل قراءة أي ملف، و is_dir قبل رفع الملفات للمجلد لضمان استقرار برنامجك وعدم ظهور أخطاء غير متوقعة.",
    notes_list=["file_exists للتأكد من المسار", "is_file و is_dir للفحص النوعي", "unlink لحذف الملفات", "mkdir بوضع recursive لإنشاء المسارات"]
)

# ==========================================
# Slide 13: CSV Handling: fgetcsv & fputcsv
# ==========================================
make_slide(
    index=12,
    title="التعامل مع ملفات CSV في PHP",
    eyebrow="نظام الملفات &middot; 4",
    slide_title="قراءة وكتابة ملفات الجداول CSV",
    slide_text="صيغة CSV هي المعيار الأبسط لتصدير واستيراد بيانات الجداول والإكسل بين الأنظمة:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>fgetcsv($handle)</code>: قراءة سطر من ملف CSV وتحويله مباشرة إلى <strong>مصفوفة عناصر</strong>!</li>
          <li><code>fputcsv($handle, $fields)</code>: أخذ مصفوفة وكتابتها كسطر CSV منسق ومحمي تلقائياً بعلامات التنصيص.</li>
          <li><strong>الميزة العظمى:</strong> التعامل التلقائي مع الفواصل وعلامات الهروب دون الحاجة لتقطيع النصوص يدوياً.</li>
          <li><strong>الاستخدام الشائع:</strong> تصدير فواتير المبيعات، استيراد قوائم الطلاب، وتقارير المحاسبة.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">csv_export.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$file</span> = <span class="tok-fn">fopen</span>(<span class="tok-str">"users.csv"</span>, <span class="tok-str">"w"</span>);

<span class="tok-cmt">// كتابة ترويسة الجدول</span>
<span class="tok-fn">fputcsv</span>(<span class="tok-var">$file</span>, [<span class="tok-str">"المعرف"</span>, <span class="tok-str">"الاسم"</span>, <span class="tok-str">"البريد"</span>]);

<span class="tok-cmt">// كتابة صفوف البيانات</span>
<span class="tok-fn">fputcsv</span>(<span class="tok-var">$file</span>, [<span class="tok-num">1</span>, <span class="tok-str">"أحمد علي"</span>, <span class="tok-str">"ahmed@test.com"</span>]);
<span class="tok-fn">fputcsv</span>(<span class="tok-var">$file</span>, [<span class="tok-num">2</span>, <span class="tok-str">"سارة محمود"</span>, <span class="tok-str">"sara@test.com"</span>]);

<span class="tok-fn">fclose</span>(<span class="tok-var">$file</span>);
<span class="tok-kw">echo</span> <span class="tok-str">"تم تصدير ملف CSV بنجاح!"</span>;</pre>
        </div>
      </div>''',
    notes_title="التعامل مع ملفات CSV",
    notes_script="ملفات CSV ممتازة لأن أي شخص يمكن فتحها على Excel. fputcsv و fgetcsv تجعلان قراءتها وكتابتها في PHP أسهل ما يكون.",
    notes_list=["أهمية صيغة CSV كجسر مع Excel", "الكتابة التلقائية بـ fputcsv", "القراءة المباشرة كمصفوفة بـ fgetcsv"]
)

# ==========================================
# Slide 14: Section Divider: JSON
# ==========================================
make_slide(
    index=13,
    title="تبادل البيانات بصيغة JSON",
    eyebrow="القسم الثالث",
    slide_title="تبادل وحفظ البيانات بصيغة JSON في PHP",
    slide_text="الصيغة العالمية القياسية لتبادل البيانات وتخزين السجلات في قواعد البيانات المسطحة ومنافذ API:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">ترميز المصفوفات بـ json_encode والمعاملات</span>
        <span class="pill-badge">حل نصوص JSON بـ json_decode وفخ الـ True</span>
        <span class="pill-badge">بناء قاعدة بيانات ملفات مسطحة (Flat-file Database)</span>
      </div>''',
    notes_title="فاصل محور JSON",
    notes_script="ننتقل لمحور JSON. لغة التخاطب بين لغات البرمجة ومنافذ RESTful APIs والصيغة الأفضل لتخزين إعدادات المواقع والبيانات المنظمة.",
    notes_list=["صيغة JSON العالمية", "json_encode و json_decode", "بناء Flat-File Database"],
    is_divider=True
)

# ==========================================
# Slide 15: json_encode & Formatting
# ==========================================
make_slide(
    index=14,
    title="ترميز المصفوفات: دالة json_encode",
    eyebrow="تنسيق JSON &middot; 1",
    slide_title="تحويل مصفوفات PHP إلى نصوص JSON: json_encode()",
    slide_text="تحويل أي مصفوفة أو كائن PHP إلى نص مهيأ بصيغة JSON مع الحفاظ على التنسيق واللغة العربية:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>json_encode($data, $flags)</code>: تحول المصفوفة إلى نص بتنسيق JSON المعياري.</li>
          <li><strong>حفظ الحروف العربية (حاسم):</strong> استخدام علم <code>JSON_UNESCAPED_UNICODE</code> لمنع تحويل الحروف العربية لرموز غريبة مثل <code>\\u0623</code>.</li>
          <li><strong>التنسيق الجمالي للقراءة:</strong> استخدام <code>JSON_PRETTY_PRINT</code> لتوليد نص منظم بمسافات بادئة وأسطر جديدة.</li>
          <li>يمكن دمج الأعلام باستخدام المعامل <code>|</code>: <code>JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT</code>.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">encode_json.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$book</span> = [
    <span class="tok-str">"title"</span>  =&gt; <span class="tok-str">"تعلم PHP الحديثة"</span>,
    <span class="tok-str">"author"</span> =&gt; <span class="tok-str">"لوغاريتم"</span>,
    <span class="tok-str">"price"</span>  =&gt; <span class="tok-num">120</span>,
    <span class="tok-str">"tags"</span>   =&gt; [<span class="tok-str">"برمجة"</span>, <span class="tok-str">"ويب"</span>]
];

<span class="tok-var">$jsonString</span> = <span class="tok-fn">json_encode</span>(
    <span class="tok-var">$book</span>, 
    <span class="tok-kw">JSON_UNESCAPED_UNICODE</span> | <span class="tok-kw">JSON_PRETTY_PRINT</span>
);

<span class="tok-kw">echo</span> <span class="tok-var">$jsonString</span>;</pre>
        </div>
      </div>''',
    notes_title="ترميز المصفوفات بـ json_encode",
    notes_script="تذكروا دائماً: إذا كانت بياناتكم تحتوي على نصوص عربية، ضعوا JSON_UNESCAPED_UNICODE حتى لا تتحول إلى أكواد تشفير Unicode غير مقروءة.",
    notes_list=["دالة json_encode ومعاملاتها", "علم JSON_UNESCAPED_UNICODE للعربية", "علم JSON_PRETTY_PRINT للمقروئية"]
)

# ==========================================
# Slide 16: json_decode & The True Flag
# ==========================================
make_slide(
    index=15,
    title="قراءة وفك JSON: دالة json_decode وفخ المعامل true",
    eyebrow="تنسيق JSON &middot; 2",
    slide_title="قراءة وفك JSON: دالة json_decode() وفخ المعامل true",
    slide_text="تحويل نصوص JSON إلى مصفوفات PHP قابلة للقراءة والتعامل البرمجي:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>json_decode($json, $associative)</code>: فك تشفير نص JSON إلى بنية بيانات PHP.</li>
          <li><strong>المعامل الحاسم <code>true</code>:</strong>
            إذا مررت <code>true</code> كمعامل ثانٍ، ستعيد الدالة <strong>مصفوفة ترابطية</strong> (Associative Array) عادية!</li>
          <li><strong>الفخ الخطير:</strong> إذا أهملت تمرير <code>true</code>، ستعيد الدالة كائناً <code>stdClass</code> وستفشل محاولة الوصول <code>$data['key']</code> بخطأ Fatal!</li>
          <li><code>json_last_error()</code>: فحص سبب فشل الفك إن كان نص JSON معطوباً أو مشوهاً.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">decode_json.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$jsonText</span> = <span class="tok-str">'{"name": "أحمد", "role": "مدير"}'</span>;

<span class="tok-cmt">// فك التشفير إلى مصفوفة ترابطية بفضل true</span>
<span class="tok-var">$user</span> = <span class="tok-fn">json_decode</span>(<span class="tok-var">$jsonText</span>, <span class="tok-kw">true</span>);

<span class="tok-cmt">// قراءة البيانات كمصفوفة عادية تماماً</span>
<span class="tok-kw">echo</span> <span class="tok-str">"الاسم: "</span> . <span class="tok-var">$user</span>[<span class="tok-str">'name'</span>] . <span class="tok-str">"&lt;br&gt;"</span>;
<span class="tok-kw">echo</span> <span class="tok-str">"الرتبة: "</span> . <span class="tok-var">$user</span>[<span class="tok-str">'role'</span>];</pre>
        </div>
      </div>''',
    notes_title="فك تشفير JSON والمعامل true",
    notes_script="احفظوها كقاعدة دائمة: عند استخدام json_decode، اكتبوا دائماً true في المعامل الثاني لتعود لكم مصفوفة يسهل التعامل معها.",
    notes_list=["دالة json_decode", "أهمية المعامل true للحصول على مصفوفة ترابطية", "خطر تجاهل true والحصول على stdClass", "فحص الأخطاء بـ json_last_error"]
)

# ==========================================
# Slide 17: Practical Example: Flat-File JSON Store
# ==========================================
make_slide(
    index=16,
    title="تطبيق عملي كامل: قاعدة بيانات ملفات مسطحة (JSON Store)",
    eyebrow="تطبيق متكامل &middot; Flat-File DB",
    slide_title="تطبيق عملي: حفظ واسترجاع السجلات في ملف JSON",
    slide_text="بناء نظام متكامل لقراءة قائمة المستخدمين، إضافة مستخدم جديد للمصفوفة، وإعادة الحفظ في الملف:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">الهدف البرمجي</div>
          <p>قراءة ملف <code>users.json</code>، فك تشفيره لمصفوفة، إضافة عضو جديد، وإعادة الحفظ باستخدام <code>file_put_contents</code>.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">users_json_db.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$file</span> = <span class="tok-str">"users.json"</span>;

<span class="tok-cmt">// 1. قراءة وفك المصفوفة السابقة</span>
<span class="tok-var">$users</span> = <span class="tok-fn">file_exists</span>(<span class="tok-var">$file</span>) 
    ? <span class="tok-fn">json_decode</span>(<span class="tok-fn">file_get_contents</span>(<span class="tok-var">$file</span>), <span class="tok-kw">true</span>) 
    : [];

<span class="tok-cmt">// 2. إضافة مستخدم جديد للمصفوفة</span>
<span class="tok-var">$users</span>[] = [
    <span class="tok-str">"id"</span>   =&gt; <span class="tok-fn">count</span>(<span class="tok-var">$users</span>) + <span class="tok-num">1</span>,
    <span class="tok-str">"name"</span> =&gt; <span class="tok-str">"طارق"</span>,
    <span class="tok-str">"role"</span> =&gt; <span class="tok-str">"عضو"</span>
];

<span class="tok-cmt">// 3. إعادة الحفظ بتنسيق JSON</span>
<span class="tok-fn">file_put_contents</span>(
    <span class="tok-var">$file</span>, 
    <span class="tok-fn">json_encode</span>(<span class="tok-var">$users</span>, <span class="tok-kw">JSON_UNESCAPED_UNICODE</span> | <span class="tok-kw">JSON_PRETTY_PRINT</span>)
);</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/users_json_db.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.85rem;">
قائمة المستخدمين من users.json:
────────────────────────
[1] عمر الشريف (مدير)
[2] منى خالد (مشرفة)
[3] طارق (عضو) ✨ تم الحفظ بنجاح!

إجمالي الأعضاء في الملف: 3
            </div>
          </div>
        </div>
      </div>''',
    notes_title="تطبيق Flat-File JSON Store",
    notes_script="هذا النمط البرمجي يسمى Flat-file database؛ وهو ممتاز للمشاريع الصغيرة وإعدادات المواقع قبل الانتقال لقواعد البيانات العلائقية مثل MySQL.",
    notes_list=["قراءة الملف وفك التشفير", "إضافة عنصر جديد لمصفوفة PHP", "إعادة التشفير بـ json_encode", "الحفظ الدائم بـ file_put_contents"]
)

# ==========================================
# Slide 18: File Locking & Concurrency: flock
# ==========================================
make_slide(
    index=17,
    title="أمان الملفات والتزامن: قفل الملفات بـ flock()",
    eyebrow="نظام الملفات &middot; أمان وتزامن",
    slide_title="حماية الملفات من التضارب المتزامن: دالة flock()",
    slide_text="عندما يحاول مستخدمان الكتابة في نفس الملف في نفس اللحظة، قد يتلف الملف تماماً ما لم نستخدم القفل:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>مشكلة الـ Race Condition:</strong> زائران يرسلان طلباً في نفس الميلي ثانية؛ أحدهما يكتب فوق الآخر فيفسد الملف.</li>
          <li><strong>الحل بـ <code>flock($handle, $operation)</code>:</strong> قفل الملف برمجياً أثناء العملية:
            <br>&bull; <code>LOCK_SH</code>: قفل مشترك للقراءة (Shared lock) يسمح لعدة زوار بالقراءة معاً.
            <br>&bull; <code>LOCK_EX</code>: قفل حصري للكتابة (Exclusive lock) يمنع أي شخص آخر من لمس الملف.
            <br>&bull; <code>LOCK_UN</code>: فك القفل بعد الانتهاء.
          </li>
          <li>دائماً فك القفل قبل استدعاء <code>fclose()</code>.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">flock_safe.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$file</span> = <span class="tok-fn">fopen</span>(<span class="tok-str">"counter.txt"</span>, <span class="tok-str">"c+"</span>);

<span class="tok-cmt">// قفل الملف حصرياً للكتابة الآمنة</span>
<span class="tok-kw">if</span> (<span class="tok-fn">flock</span>(<span class="tok-var">$file</span>, <span class="tok-kw">LOCK_EX</span>)) {
    <span class="tok-var">$count</span> = (<span class="tok-kw">int</span>)<span class="tok-fn">fread</span>(<span class="tok-var">$file</span>, <span class="tok-num">100</span>);
    <span class="tok-var">$count</span>++;
    
    <span class="tok-fn">ftruncate</span>(<span class="tok-var">$file</span>, <span class="tok-num">0</span>);      <span class="tok-cmt">// تصفير الملف</span>
    <span class="tok-fn">rewind</span>(<span class="tok-var">$file</span>);             <span class="tok-cmt">// العودة للبداية</span>
    <span class="tok-fn">fwrite</span>(<span class="tok-var">$file</span>, <span class="tok-var">$count</span>);     <span class="tok-cmt">// كتابة الرقم الجديد</span>
    
    <span class="tok-fn">flock</span>(<span class="tok-var">$file</span>, <span class="tok-kw">LOCK_UN</span>);     <span class="tok-cmt">// فك القفل بأمان</span>
}
<span class="tok-fn">fclose</span>(<span class="tok-var">$file</span>);</pre>
        </div>
      </div>''',
    notes_title="قفل الملفات والتزامن",
    notes_script="flock تضمن أن عملية التحديث آمنة تماماً ولا يمكن لعمليتين التداخل وتخريب محتوى الملف في بيئة التشغيل المتعددة.",
    notes_list=["مفهوم Race Condition في الملفات", "القفل الحصري LOCK_EX", "القفل المشترك LOCK_SH", "فك القفل بـ LOCK_UN"]
)

# ==========================================
# Slide 19: Common Mistakes in Files & JSON
# ==========================================
make_slide(
    index=18,
    title="أخطاء شائعة في الملفات و JSON",
    eyebrow="احذر هذه الأخطاء &middot; 2",
    slide_title="أخطاء شائعة في التعامل مع الملفات و JSON",
    slide_text="تجنب هذه المشكلات التي تؤدي لتلف البيانات أو حجز موارد السيرفر أو توقف الكود:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ مسح الملف بوضع 'w' ونسيان fclose</div>
          <ul class="bullet-list">
            <li>فتح الملف بوضع <code>fopen($file, 'w')</code> يمسح محتواه فوراً حتى لو لم تكتب أي شيء؛ للإلحاق استخدم وضع <code>'a'</code>.</li>
            <li>نسيان استدعاء <code>fclose($handle)</code> يبقي الملف محجوزاً في نظام التشغيل ويمنع العمليات الأخرى من تعديله.</li>
            <li>محاولة القراءة من مسار غير موجود دون التحقق بـ <code>file_exists()</code> ينتج تحذيراً برمجياً.</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ نسيان المعامل true في json_decode</div>
          <ul class="bullet-list">
            <li>كتابة <code>$data = json_decode($json);</code> تعيد كائناً من نوع <code>stdClass</code>، فمحاولة الوصول <code>$data['name']</code> ستفشل بخطأ Fatal!</li>
            <li><strong>التصحيح:</strong> مرر دائماً <code>true</code> كمعامل ثانٍ: <code>json_decode($json, true)</code> لتعيد مصفوفة ترابطية عادية.</li>
            <li>عدم فحص أخطاء JSON بـ <code>json_last_error()</code> عند استقبال نصوص مشوهة.</li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في الملفات و JSON",
    notes_script="أشهر خطأ على الإطلاق: الطالب يكتب $data['name'] بعد json_decode فيتفاجأ بخطأ Cannot use object of type stdClass as array، والحل هو المعامل true.",
    notes_list=["وضع w يفرغ الملف فوراً", "نسيان fclose يحجز الموارد", "نسيان true في json_decode ينتج كائناً بدلاً من مصفوفة", "أهمية فحص file_exists"]
)

# ==========================================
# Slide 20: Section Divider: Practical Homework
# ==========================================
make_slide(
    index=19,
    title="الواجبات والتطبيقات العملية",
    eyebrow="التطبيق العملي",
    slide_title="الواجبات والتطبيقات العملية",
    slide_text="الآن حان وقت تحويل المعرفة النظرية إلى كود حقيقي من خلال 3 واجبات عملية متدرجة في الصعوبة:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">واجب 1 (سهل): محلل ومنظف النصوص ومعد الكلمات</span>
        <span class="pill-badge">واجب 2 (سهل): مسجل الزيارات في ملف نصي مع IP</span>
        <span class="pill-badge">واجب 3 (متوسط): قاعدة بيانات منتجات كاملة بملف JSON</span>
      </div>''',
    notes_title="فاصل الواجبات العملية",
    notes_script="الواجبات اليوم مقسمة لتغطي المحاور الثلاثة: الأول لمعالجة النصوص، الثاني لنظام الملفات وسجلات الزيارات، والثالث لبناء قاعدة بيانات مسطحة متكاملة لمنتجات بملف JSON.",
    notes_list=["واجب 1: نصوص وإحصائيات", "واجب 2: ملفات وسجل زيارات", "واجب 3: قاعدة بيانات منتجات بـ JSON"],
    is_divider=True
)

# ==========================================
# Slide 21: Homework 1 (Easy): Text Formatter & Word Counter
# ==========================================
make_slide(
    index=20,
    title="واجب 1: محلل ومنظف النصوص ومعد الكلمات",
    eyebrow="الواجبات العملية &middot; 1 (سهل)",
    slide_title="واجب 1: محلل ومنظف النصوص (Text Cleaner)",
    slide_text="بناء سكريبت ينظف المقالات والنصوص المدخلة ويستخرج إحصائيات دقيقة عن الكلمات والأحرف:",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في الواجب 1</div>
          <ul class="bullet-list" style="margin-top:0.4rem;">
            <li>استقبل نصاً طويلاً من مستخدم به مسافات زائدة وكلمات غير لائقة.</li>
            <li>قم بتنظيف المسافات من الأطراف باستخدام <code>trim()</code>.</li>
            <li>استبدل قائمة كلمات محظورة بنجوم باستخدام <code>str_replace()</code>.</li>
            <li>استخرج عدد الكلمات باستخدام <code>explode()</code> و <code>count()</code>، واطبع أول 3 كلمات من المقال.</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">hw1_text_cleaner.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$article</span> = <span class="tok-str">"  تعلم لغة PHP ممتاز لتطوير مواقع الويب   "</span>;

<span class="tok-cmt">// 1. تنظيف المسافات بالأطراف</span>

<span class="tok-cmt">// 2. حجب وفلترة الكلمات المحددة</span>

<span class="tok-cmt">// 3. تقطيع المقال لمصفوفة كلمات وحساب عددها</span>

<span class="tok-cmt">// 4. استخراج أول 3 كلمات وطباعتها</span></pre>
        </div>
      </div>''',
    notes_title="واجب 1: محلل النصوص",
    notes_script="تمرين عملي ممتع يرسخ دوال النصوص الأكثر طلباً في سوق العمل؛ خاصة لتنظيف التعليقات ومنشورات المدونات.",
    notes_list=["تنظيف المسافات بـ trim", "حجب الكلمات بـ str_replace", "تقسيم الكلمات بـ explode", "حساب الإحصائيات وإعادة الدمج"]
)

# ==========================================
# Slide 22: Homework 2 (Easy): Visitor Counter & File Logger
# ==========================================
make_slide(
    index=21,
    title="واجب 2: مسجل الزيارات والملاحظات في ملف",
    eyebrow="الواجبات العملية &middot; 2 (سهل)",
    slide_title="واجب 2: مسجل الزيارات والملاحظات (File Logger)",
    slide_text="بناء نظام عدّاد زيارات دائم وسجل أحداث يحفظ كل زيارة وتوقيتها في ملف نصي على الخادم:",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في الواجب 2</div>
          <ul class="bullet-list" style="margin-top:0.4rem;">
            <li>أنشئ ملفاً باسم <code>counter.txt</code> إن لم يكن موجوداً واضبط قيمته على <code>0</code>.</li>
            <li>في كل زيارة للصفحة، اقرأ الرقم بـ <code>file_get_contents</code>، قم بزيادته بواحد، وأعد حفظه بـ <code>file_put_contents</code>.</li>
            <li>سجل في ملف <code>visits.log</code> سطراً يضم: التاريخ والوقت، عنوان IP للزائر عبر <code>$_SERVER['REMOTE_ADDR']</code>، ورقم الزيارة باستخدام <code>FILE_APPEND</code>.</li>
            <li>اعرض في المتصفح: «أنت الزائر رقم X لموقعنا!».</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">hw2_visitor_counter.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$counterFile</span> = <span class="tok-str">"counter.txt"</span>;
<span class="tok-var">$logFile</span> = <span class="tok-str">"visits.log"</span>;

<span class="tok-cmt">// 1. فحص وجود ملف العداد أو إنشائه</span>

<span class="tok-cmt">// 2. قراءة القيمة الحالية وزيادتها</span>

<span class="tok-cmt">// 3. حفظ القيمة الجديدة وإلحاق سطر بالسجل</span>

<span class="tok-cmt">// 4. طباعة الترحيب بالزائر</span></pre>
        </div>
      </div>''',
    notes_title="واجب 2: مسجل الزيارات والملفات",
    notes_script="الهدف هنا تجربة القراءة والكتابة السريعة بـ file_get_contents و file_put_contents مع استخدام علم FILE_APPEND لتسجيل السجلات المستمرة.",
    notes_list=["إنشاء وفحص الملف بـ file_exists", "قراءة وتحديث العداد", "تسجيل سطر جديد في السجل بـ FILE_APPEND", "استخراج IP الزائر من $_SERVER"]
)

# ==========================================
# Slide 23: Homework 3 (Medium): Flat-File JSON Product Manager
# ==========================================
make_slide(
    index=22,
    title="واجب 3: قاعدة بيانات منتجات كاملة بملف JSON",
    eyebrow="الواجبات العملية &middot; 3 (متوسط)",
    slide_title="واجب 3: نظام إدارة منتجات بملف JSON (Flat-File DB)",
    slide_text="مشروع تطبيقي لإدارة كتالوج متجر إلكتروني بقراءة وإضافة المنتجات بملف JSON:",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في الواجب 3</div>
          <ul class="bullet-list" style="margin-top:0.3rem;">
            <li>أنشئ ملف <code>catalog.json</code> يحتوي على مصفوفة منتجات (id, title, price, category).</li>
            <li>اقرأ الملف وحوله لمصفوفة ترابطية بـ <code>json_decode(..., true)</code>.</li>
            <li>عند إرسال نموذج إضافة منتج جديد عبر POST، أضف المنتج إلى المصفوفة مع توليد ID تلقائي.</li>
            <li>أعد حفظ المصفوفة المحدثة في <code>catalog.json</code> مع تفعيل <code>JSON_UNESCAPED_UNICODE</code> و <code>JSON_PRETTY_PRINT</code>.</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">hw3_json_catalog.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$file</span> = <span class="tok-str">"catalog.json"</span>;

<span class="tok-cmt">// 1. قراءة المنتجات من JSON</span>
<span class="tok-var">$products</span> = <span class="tok-fn">file_exists</span>(<span class="tok-var">$file</span>) 
    ? <span class="tok-fn">json_decode</span>(<span class="tok-fn">file_get_contents</span>(<span class="tok-var">$file</span>), <span class="tok-kw">true</span>) 
    : [];

<span class="tok-cmt">// 2. إضافة منتج جديد إن وُجد إرسال POST</span>

<span class="tok-cmt">// 3. حفظ المصفوفة بعد التحديث بـ JSON_PRETTY_PRINT</span>

<span class="tok-cmt">// 4. عرض جدول المنتجات في HTML</span></pre>
        </div>
      </div>''',
    notes_title="واجب 3: قاعدة بيانات منتجات JSON",
    notes_script="هذا التمرين يرسخ مفهوم Flat-file database المتكامل: قراءة وتعديل وحفظ البيانات المنظمة بتنسيق JSON المعياري.",
    notes_list=["قراءة وتعديل ملف JSON", "توليد معرف تلقائي للمنتج", "الحفظ الدائم والتنسيق الجمالي"]
)

# ==========================================
# Slide 24: Divider: Review Time
# ==========================================
make_slide(
    index=23,
    title="وقت المراجعة والتأمل",
    eyebrow="نقاش ومراجعة",
    slide_title="وقت المراجعة والتأمل",
    slide_text="قبل أن نصل للنهاية، اختبر استيعابك للمفاهيم الجوهرية التي ناقشناها اليوم:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">متى نفضل fopen و fread على file_get_contents؟</span>
        <span class="pill-badge">لماذا يعد المعامل true إجبارياً عملياً عند استخدام json_decode()؟</span>
        <span class="pill-badge">ما هي وظيفة flock() وما الخطر الذي تحمينا منه؟</span>
      </div>''',
    notes_title="فاصل المراجعة",
    notes_script="أسئلة تحفيزية للمناقشة مع الطلاب للتأكد من فهمهم لسلوك دوال الملفات وتدفق المخرجات وتفادي مشاكل الذاكرة والتزامن.",
    notes_list=["سؤال متى نلجأ لـ fopen للملفات الكبيرة", "سؤال المعامل true في json_decode", "سؤال وظيفة flock وحماية التزامن"],
    is_divider=True
)

# ==========================================
# Slide 25: Summary: What We Learned Today
# ==========================================
make_slide(
    index=24,
    title="اللي اتعلمناه النهاردة",
    eyebrow="ملخص المحاضرة 08",
    slide_title="اللي اتعلمناه النهاردة في المحاضرة 08",
    slide_text="خلاصة أهم 4 محاور تم إتقانها اليوم في مسار PHP الاحترافي:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">معالجة النصوص (Strings)</div>
            <div class="topic-desc">علامات التنصيص والمطابقة، ودوال trim، explode، implode، str_replace، ودعم mb_*</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">نظام الملفات (Filesystem)</div>
            <div class="topic-desc">القراءة السريعة بـ file_get/put_contents، التدفقات بـ fopen/fclose، وفحص file_exists</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">تبادل البيانات بـ JSON</div>
            <div class="topic-desc">ترميز المصفوفات بـ json_encode وحلها لمصفوفات ترابطية بـ json_decode وبناء قواعد مسطحة</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">ملفات CSV والتزامن</div>
            <div class="topic-desc">تصدير الجداول بـ fputcsv وقفل الملفات ضد تضارب العمليات بـ flock</div>
          </div>
        </div>
      </div>''',
    notes_title="ملخص المحاضرة 08",
    notes_script="لقد قطعنا شوطاً رائعاً اليوم. بهذه المهارات أصبح بإمكانكم معالجة أي بيانات نصية، وحفظها واسترجاعها من ملفات منظمة بصيغ TXT و CSV و JSON.",
    notes_list=["معالجة النصوص بدقة", "التعامل السريع والمتقدم مع الملفات", "حفظ البيانات في صيغة JSON", "إتقان ملفات CSV وقفل الملفات"]
)

# ==========================================
# Slide 26: Conclusion & Thank You
# ==========================================
make_slide(
    index=25,
    title="شكرًا لكم &mdash; نهاية المحاضرة 08",
    eyebrow="الخاتمة &middot; المحاضرة 08",
    slide_title="شكرًا لكم! بالتوفيق في التطبيق العملي",
    slide_text="اليوم وضعتم أيديكم على مفاتيح تخزين ومعالجة البيانات الدائمة. طبّقوا الواجبات الثلاثة واستعدوا للمحطة القادمة الهامة جداً:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">معالجة النصوص</span>
        <span class="pill-badge">نظام الملفات &amp; CSV</span>
        <span class="pill-badge">تبادل وحفظ بيانات JSON</span>
        <span class="pill-badge">المحاضرة القادمة: إدارة الحالة (Cookies &amp; Sessions) 🚀</span>
      </div>''',
    notes_title="خاتمة المحاضرة 08",
    notes_script="شكراً لكم على وقتكم وتركيزكم. في المحاضرة القادمة سننتقل لموضوع حيوي وهو إدارة حالة المستخدم: الكوكيز والجلسات Cookies vs Sessions. إلى اللقاء!",
    notes_list=["شكر وتشجيع الطلاب", "الحث على حل الواجبات الثلاثة", "التشويق للمحاضرة 09: Cookies & Sessions"],
    is_divider=True
)

print("All 26 slides generated successfully for Lecture 08!")
