# -*- coding: utf-8 -*-
from build_lecture_06 import make_slide

# Slide 01: Cover
make_slide(
    index=0,
    title="الدوال في PHP",
    eyebrow="أساسيات PHP &middot; المحاضرة 06",
    slide_title="الدوال في PHP (Functions)",
    slide_text="هنتعلم إزاي ننظم كودنا ونمنع التكرار (DRY) باستخدام الدوال &mdash; من تمرير المعاملات وإرجاع القيم، للمعاملات الافتراضية، ونطاق المتغيرات (Scope)، وصولاً للدوال المجهولة والسهمية في PHP الحديثة.",
    body_content='''<div class="cover-mark">
        <div><div class="num">05</div><div class="lbl">مواضيع رئيسية</div></div>
        <div><div class="num">03</div><div class="lbl">تمارين برمجية</div></div>
        <div><div class="num">~50 د</div><div class="lbl">المدة التقديرية</div></div>
      </div>''',
    notes_title="المحاضرة 06: الدوال في PHP",
    notes_script="أهلاً بكم في المحاضرة السادسة من دورة PHP. موضوعنا اليوم من أهم الموضوعات البرمجية وهو الدوال؛ الأداة الأساسية لتنظيم الكود ومنع التكرار وبناء تطبيقات قابلة للتوسع.",
    notes_list=["مفهوم الدوال ومبدأ DRY", "المعاملات والإرجاع وتصريح الأنواع", "المعاملات الافتراضية ونطاق المتغيرات", "الدوال المجهولة ودوال السهم"],
    is_cover=True
)

# Slide 02: Roadmap
make_slide(
    index=1,
    title="خريطة المحاضرة 06",
    eyebrow="نظرة عامة &middot; محتويات المحاضرة",
    slide_title="خريطة المحاضرة 06",
    slide_text="خمسة محاور رئيسية سنتعلمها اليوم لاحتراف الدوال في لغة PHP بالتطبيق العملي:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">المعاملات والإرجاع (Args &amp; Return)</div>
            <div class="topic-desc">تمرير المعاملات وجملة return المتعددة</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">تحديد الأنواع الصارمة (Type Declarations)</div>
            <div class="topic-desc">أنواع المدخلات والمخرجات في PHP 7+</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">المعاملات الافتراضية (Default Parameters)</div>
            <div class="topic-desc">القيم الافتراضية وترتيب المعاملات الاختيارية</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">نطاق المتغيرات (Variable Scope)</div>
            <div class="topic-desc">النطاق المحلي والعام واستخدام global و static</div>
          </div>
        </div>
        <div class="topic-item" style="grid-column: span 2;">
          <div class="topic-num">05</div>
          <div class="topic-info">
            <div class="topic-title">الدوال المجهولة والسهمية (Anonymous &amp; Arrow Functions)</div>
            <div class="topic-desc">الدوال بدون اسم، إسنادها لمتغيرات، استخدامها كـ Callback، وصياغة fn()</div>
          </div>
        </div>
      </div>''',
    notes_title="خريطة المحاضرة",
    notes_script="هذه هي محاورنا الخمسة الأساسية لليوم. سنبدأ بالتعريف وتمرير البيانات، ثم ننتقل للميزات الأحدث مثل تحديد الأنواع، المعاملات الافتراضية، إدارة النطاقات، وأخيراً الدوال المجهولة.",
    notes_list=["المعاملات والإرجاع", "تصريح الأنواع في PHP 7+", "المعاملات الافتراضية", "نطاق المتغيرات Local و Global و Static", "الدوال المجهولة والسهمية"]
)

# Slide 03: Functions Concept & DRY
make_slide(
    index=2,
    title="ما هي الدالة؟ ومبدأ DRY",
    eyebrow="الدوال في PHP &middot; 1",
    slide_title="ما هي الدالة؟ ومبدأ DRY",
    slide_text="الدالة (Function) هي كتلة برمجية مستقلة لها اسم، تُكتب مرة واحدة ويمكن استدعاؤها في أي مكان عدة مرات لمنع تكرار الكود (Don't Repeat Yourself).",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>تُعرّف بالكلمة المفتاحية <code>function</code> متبوعة بالاسم</li>
          <li>أسماء الدوال تتبع عادةً أسلوب <strong>camelCase</strong></li>
          <li>الأقواس <code>()</code> تلي اسم الدالة وتُستخدم لتمرير البيانات</li>
          <li>جسم الدالة محاط بأقواس معقوفة <code>{ ... }</code></li>
          <li>الكود داخل الدالة <strong>لا يُنفّذ</strong> إلا عند استدعائها باسمها</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">define.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// 1. تعريف الدالة</span>
<span class="tok-kw">function</span> <span class="tok-fn">sayHello</span>() {
    <span class="tok-kw">echo</span> <span class="tok-str">"أهلاً بكم في كورس PHP!&lt;br&gt;"</span>;
}

<span class="tok-cmt">// 2. استدعاء الدالة</span>
<span class="tok-fn">sayHello</span>();
<span class="tok-fn">sayHello</span>(); <span class="tok-cmt">// يمكن تكرارها بسهولة</span></pre>
        </div>
      </div>''',
    notes_title="مفهوم الدالة ومبدأ DRY",
    notes_script="تخيل لو احتجت تكتب نفس كود حساب الفاتورة في 10 صفحات مختلفة، ثم أردت تعديل نسبة الضريبة! الدوال تحل هذه المعضلة: نكتب الكود مرة واحدة ونناديه في أي مكان.",
    notes_list=["مبدأ DRY: Don't Repeat Yourself", "الصياغة الأساسية function name() {}", "الكود خامل حتى يتم استدعاء الدالة"]
)

# Slide 04: Arguments & Return
make_slide(
    index=3,
    title="تمرير المعاملات وإرجاع القيم",
    eyebrow="الدوال في PHP &middot; 1",
    slide_title="تمرير المعاملات وجملة return",
    slide_text="المعاملات (Parameters) هي مدخلات الدالة، وجملة <code>return</code> هي المخرج الذي تعيده الدالة إلى مكان الاستدعاء لتكتمل دورة المعالجة.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>المعامل (Parameter):</strong> متغير نضعه في تعريف الدالة كمدخل</li>
          <li><strong>الوسيط (Argument):</strong> القيمة الفعلية الممررة عند الاستدعاء</li>
          <li>يمكن للدالة استقبال <strong>معامل واحد أو عدة معاملات</strong> مفصولة بفاصلة <code>,</code></li>
          <li>جملة <code>return</code> ترجع القيمة وتوقف تنفيذ الدالة فوراً</li>
          <li>القيمة المرجعة يمكن تخزينها في متغير أو طباعتها مباشرة</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">return.php</span>
          </div>
          <pre class="code-body"><span class="tok-kw">function</span> <span class="tok-fn">calcTax</span>(<span class="tok-var">$price</span>, <span class="tok-var">$rate</span>) {
    <span class="tok-var">$total</span> = <span class="tok-var">$price</span> + (<span class="tok-var">$price</span> * <span class="tok-var">$rate</span>);
    <span class="tok-kw">return</span> <span class="tok-var">$total</span>; <span class="tok-cmt">// إرجاع النتيجة</span>
}

<span class="tok-var">$invoice</span> = <span class="tok-fn">calcTax</span>(<span class="tok-num">100</span>, <span class="tok-num">0.14</span>);
<span class="tok-kw">echo</span> <span class="tok-var">$invoice</span>; <span class="tok-cmt">// الناتج: 114</span></pre>
        </div>
      </div>''',
    notes_title="المعاملات وقيمة return",
    notes_script="مهم جداً نوضح للطلاب الفرق بين الطباعة داخل الدالة بـ echo وبين إرجاع القيمة بـ return. الدالة الاحترافية لا تطبع بنفسها، بل ترجع القيمة لمن طلبها.",
    notes_list=["الفرق بين Parameter و Argument", "إمكانية استقبال معاملات متعددة", "return تنهي الدالة وترجع النتيجة"]
)

# Slide 05: Type Declarations PHP 7+
make_slide(
    index=4,
    title="تصريح أنواع البيانات (PHP 7+)",
    eyebrow="الدوال في PHP &middot; 1",
    slide_title="تصريح أنواع البيانات (Type Declarations)",
    slide_text="بدءاً من PHP 7، يمكننا تحديد نوع كل معامل ونوع القيمة التي ترجعها الدالة لضمان جودة الكود واكتشاف الأخطاء مبكراً (Type Safety).",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>نوع المعامل يسبق اسمه: <code>int $a</code>, <code>string $b</code>, <code>float $c</code></li>
          <li>نوع الإرجاع يُكتب بعد النقطتين بعد الأقواس: <code>: int</code></li>
          <li>الدالة التي لا تعيد قيمة نحدد لها نوع <code>: void</code></li>
          <li>يدعم: <code>int</code>, <code>float</code>, <code>string</code>, <code>bool</code>, <code>array</code></li>
          <li>يمنع تمرير بيانات غير متوقعة ويسهل قراءة الكود وفهمه</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">types.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// دالة تقبل عددين وترجع int</span>
<span class="tok-kw">function</span> <span class="tok-fn">getTotal</span>(<span class="tok-kw">int</span> <span class="tok-var">$count</span>, <span class="tok-kw">int</span> <span class="tok-var">$price</span>): <span class="tok-kw">int</span> {
    <span class="tok-kw">return</span> <span class="tok-var">$count</span> * <span class="tok-var">$price</span>;
}

<span class="tok-kw">echo</span> <span class="tok-fn">getTotal</span>(<span class="tok-num">5</span>, <span class="tok-num">20</span>); <span class="tok-cmt">// الناتج: 100</span></pre>
        </div>
      </div>''',
    notes_title="تصريح أنواع البيانات في PHP الحديثة",
    notes_script="تحديد الأنواع ميزة نقلت PHP لمستوى لغات الـ Enterprise مثل Java و TypeScript. هذا يمنع أخطاء شائعة مثل تمرير نص لدالة حسابية.",
    notes_list=["Type Hinting للمدخلات والمخرجات", "أنواع البيانات المدعومة", "تحديد void للدوال التي لا ترجع بيانات"]
)

# Slide 06: Example 1: add($a, $b)
make_slide(
    index=5,
    title="مثال 1: دالة الجمع add()",
    eyebrow="الدوال والمعاملات &middot; مثال 1",
    slide_title="مثال 1: دالة الجمع add($a, $b)",
    slide_text="تعريف دالة تقبل معاملين وترجع حاصل جمعهما، ثم استدعاؤها وطباعة الناتج.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>عرّف دالة باسم <code>add($a, $b)</code> ترجع حاصل جمع a و b. استدعِ الدالة بالقيمتين 5 و 3 واطبع النتيجة في المتصفح.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">add.php</span>
          </div>
          <pre class="code-body"><span class="tok-kw">function</span> <span class="tok-fn">add</span>(<span class="tok-var">$a</span>, <span class="tok-var">$b</span>) {
    <span class="tok-kw">return</span> <span class="tok-var">$a</span> + <span class="tok-var">$b</span>;
}

<span class="tok-var">$sum</span> = <span class="tok-fn">add</span>(<span class="tok-num">5</span>, <span class="tok-num">3</span>);
<span class="tok-kw">echo</span> <span class="tok-var">$sum</span>;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/add.php</div>
          </div>
          <div class="browser-viewport">
            <pre class="output-ascii">8</pre>
          </div>
        </div>
      </div>''',
    notes_title="مثال دالة الجمع add()",
    notes_script="مثال مباشر وواضح على استقبال معاملين واستخدام return مع تخزين القيمة في متغير ثم طباعتها.",
    notes_list=["استقبال المعاملين $a و $b", "استخدام return لإرجاع الجمع", "طباعة الناتج 8"]
)

# Slide 07: Example 2: multiply($x, $y)
make_slide(
    index=6,
    title="مثال 2: دالة الضرب multiply()",
    eyebrow="الدوال والمعاملات &middot; مثال 2",
    slide_title="مثال 2: دالة الضرب multiply($x, $y)",
    slide_text="تعريف دالة تقبل معاملين وترجع حاصل ضربهما، ثم استدعاؤها بالقيمتين 4 و 6.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>عرّف دالة باسم <code>multiply($x, $y)</code> ترجع حاصل ضرب x * y. استدعِ الدالة بالقيمتين 4 و 6 واطبع النتيجة مباشرة.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">multiply.php</span>
          </div>
          <pre class="code-body"><span class="tok-kw">function</span> <span class="tok-fn">multiply</span>(<span class="tok-var">$x</span>, <span class="tok-var">$y</span>) {
    <span class="tok-kw">return</span> <span class="tok-var">$x</span> * <span class="tok-var">$y</span>;
}

<span class="tok-kw">echo</span> <span class="tok-fn">multiply</span>(<span class="tok-num">4</span>, <span class="tok-num">6</span>);</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/multiply.php</div>
          </div>
          <div class="browser-viewport">
            <pre class="output-ascii">24</pre>
          </div>
        </div>
      </div>''',
    notes_title="مثال دالة الضرب multiply()",
    notes_script="في هذا المثال قمنا بالطباعة مباشرة عبر تمرير استدعاء الدالة لـ echo بدون الحاجة لمتغير وسيط.",
    notes_list=["استدعاء الدالة مباشرة مع echo", "حساب 4 * 6", "المخرج 24"]
)

# Slide 08: Common Mistakes in Return & Arguments
make_slide(
    index=7,
    title="أخطاء شائعة: الإرجاع والمعاملات",
    eyebrow="احذر هذه الأخطاء &middot; 1",
    slide_title="أخطاء شائعة: الإرجاع والمعاملات",
    slide_text="خطآن يقع فيهما الكثير من المبرمجين المبتدئين عند التعامل مع المعاملات وقيم الإرجاع:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ نسيان جملة return</div>
          <ul class="bullet-list">
            <li>الدالة تنفذ العملية ولكن <strong>لا تعيد أي قيمة</strong> للمستدعي</li>
            <li>في PHP، الدالة التي تنتهي بدون return تُرجع تلقائياً <code>null</code></li>
            <li>كود خاطئ:
              <pre class="code-body" style="padding:0.4rem 0.6rem;font-size:0.75rem;"><span class="tok-kw">function</span> <span class="tok-fn">calc</span>(<span class="tok-var">$a</span>, <span class="tok-var">$b</span>) {
    <span class="tok-var">$a</span> + <span class="tok-var">$b</span>; <span class="tok-cmt">// نسيان return!</span>
}
<span class="tok-kw">echo</span> <span class="tok-fn">calc</span>(<span class="tok-num">2</span>, <span class="tok-num">3</span>); <span class="tok-cmt">// لن يطبع شيئاً (null)</span></pre>
            </li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ تمرير عدد معاملات غير مطابق</div>
          <ul class="bullet-list">
            <li>إذا طلبت الدالة معاملين واستدعيتها بمعامل واحد فقط:</li>
            <li>تُلقي PHP خطأً قاتلاً فورياً (Fatal Error):
              <br><code>ArgumentCountError: Too few arguments</code>
            </li>
            <li>كود مسبب للخطأ:
              <pre class="code-body" style="padding:0.4rem 0.6rem;font-size:0.75rem;"><span class="tok-kw">function</span> <span class="tok-fn">sub</span>(<span class="tok-var">$a</span>, <span class="tok-var">$b</span>) { <span class="tok-kw">return</span> <span class="tok-var">$a</span> - <span class="tok-var">$b</span>; }
<span class="tok-fn">sub</span>(<span class="tok-num">10</span>); <span class="tok-cmt">// Fatal Error!</span></pre>
            </li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في الإرجاع والمعاملات",
    notes_script="ركز على أن نسيان return لا يظهر خطأ صريحاً في الـ Syntax ولكنه خطأ منطقي (Logical Bug) يرجع null. أما نقص المعاملات في PHP الحديثة فيوقف تنفيذ البرنامج تماماً بـ ArgumentCountError.",
    notes_list=["نسيان return ينتج null صامتاً", "عدم تطابق عدد المعاملات يسبب ArgumentCountError"]
)

# Slide 09: Default and Optional Parameters Concept
make_slide(
    index=8,
    title="المعاملات الافتراضية والاختيارية",
    eyebrow="المعاملات الافتراضية &middot; 2",
    slide_title="المعاملات الافتراضية (Default Parameters)",
    slide_text="تتيح PHP تعيين قيمة مسبقة للمعامل داخل تعريف الدالة، فتصبح القيمة اختيارية عند الاستدعاء.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>تحديد القيمة الافتراضية باستخدام <code>=</code> في سطر التعريف</li>
          <li>إذا استدعينا الدالة بدون هذا المعامل، تُستخدم القيمة الافتراضية</li>
          <li>إذا مرّرنا قيمة، يتم استخدام القيمة الممررة وإهمال الافتراضية</li>
          <li><strong>قاعدة ذهبية:</strong> المعاملات الاختيارية توضع <strong>بعد</strong> المعاملات الإلزامية دائماً</li>
          <li>تساعد في تقليل عدد الدوال وجعل استدعائها أكثر مرونة</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">default_demo.php</span>
          </div>
          <pre class="code-body"><span class="tok-kw">function</span> <span class="tok-fn">sayHi</span>(<span class="tok-var">$user</span> = <span class="tok-str">"Guest"</span>) {
    <span class="tok-kw">echo</span> <span class="tok-str">"Welcome, "</span> . <span class="tok-var">$user</span>;
}

<span class="tok-fn">sayHi</span>(<span class="tok-str">"Sara"</span>); <span class="tok-cmt">// Welcome, Sara</span>
<span class="tok-fn">sayHi</span>();       <span class="tok-cmt">// Welcome, Guest</span></pre>
        </div>
      </div>''',
    notes_title="مفهوم المعاملات الافتراضية",
    notes_script="المعاملات الافتراضية تجعل الدالة متعددة الاستخدامات بدون الحاجة لكتابة دوال إضافية. تذكروا دائماً: الإلزامي أولاً ثم الاختياري في النهاية.",
    notes_list=["تعيين القيمة بـ =", "الاستدعاء مع أو بدون الوسيط", "ترتيب المعاملات: الإلزامي أولاً"]
)

# Slide 10: Example 1: greet($name = "Guest")
make_slide(
    index=9,
    title="مثال 1: دالة التحية greet()",
    eyebrow="المعاملات الافتراضية &middot; مثال 1",
    slide_title="مثال 1: دالة التحية greet($name = \"Guest\")",
    slide_text="دالة ترحيب بقيمة افتراضية لمعامل الاسم عند عدم تمريره من المستدعي.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>عرّف دالة <code>greet($name = "Guest")</code> تطبع "Hello $name". استدعِها بالاسم "Ali" ثم استدعِها مرة ثانية بدون أي معاملات واعرض الناتجين.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">greet.php</span>
          </div>
          <pre class="code-body"><span class="tok-kw">function</span> <span class="tok-fn">greet</span>(<span class="tok-var">$name</span> = <span class="tok-str">"Guest"</span>) {
    <span class="tok-kw">echo</span> <span class="tok-str">"Hello "</span> . <span class="tok-var">$name</span> . <span class="tok-str">"&lt;br&gt;"</span>;
}

<span class="tok-fn">greet</span>(<span class="tok-str">"Ali"</span>);
<span class="tok-fn">greet</span>();</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/greet.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:ltr;text-align:start;">Hello Ali
Hello Guest</div>
          </div>
        </div>
      </div>''',
    notes_title="مثال دالة التحية greet()",
    notes_script="لاحظ كيف تعاملت الدالة بذكاء في المرتين: في الأولى استبدلت Guest بـ Ali، وفي الثانية استخدمت القيمة الافتراضية بسلاسة.",
    notes_list=["تمرير Ali ينتج Hello Ali", "عدم التمرير ينتج Hello Guest"]
)

# Slide 11: Example 2: power($base, $exponent = 2)
make_slide(
    index=10,
    title="مثال 2: دالة الأس power()",
    eyebrow="المعاملات الافتراضية &middot; مثال 2",
    slide_title="مثال 2: دالة الأس power($base, $exponent = 2)",
    slide_text="معامل الأساس إلزامي، والأس افتراضياً 2 (تربيع) مع إمكانية تحديده عند الحاجة.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>عرّف دالة <code>power($base, $exponent = 2)</code> ترجع الأساس مرفوعاً للأس. استدعِها بـ 3 فقط (3² = 9)، ثم بالقيمتين 2 و 3 (2³ = 8).</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">power.php</span>
          </div>
          <pre class="code-body"><span class="tok-kw">function</span> <span class="tok-fn">power</span>(<span class="tok-var">$base</span>, <span class="tok-var">$exponent</span> = <span class="tok-num">2</span>) {
    <span class="tok-kw">return</span> <span class="tok-var">$base</span> ** <span class="tok-var">$exponent</span>;
}

<span class="tok-kw">echo</span> <span class="tok-fn">power</span>(<span class="tok-num">3</span>) . <span class="tok-str">"&lt;br&gt;"</span>;    <span class="tok-cmt">// 3^2 = 9</span>
<span class="tok-kw">echo</span> <span class="tok-fn">power</span>(<span class="tok-num">2</span>, <span class="tok-num">3</span>);         <span class="tok-cmt">// 2^3 = 8</span></pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/power.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:ltr;text-align:start;">9
8</div>
          </div>
        </div>
      </div>''',
    notes_title="مثال دالة الأس power()",
    notes_script="هذا المثال يوضح فائدة المعامل الافتراضي كـ Default Behavior: إذا أردت التربيع فقط تمرر رقماً واحداً، وإذا أردت قوة أخرى تمرر المعاملين.",
    notes_list=["power(3) -> 9", "power(2, 3) -> 8", "المعامل الإلزامي أولاً والاختياري ثانياً"]
)

# Slide 12: Common Mistakes in Default Parameters
make_slide(
    index=11,
    title="أخطاء شائعة في المعاملات الافتراضية",
    eyebrow="احذر هذه الأخطاء &middot; 2",
    slide_title="أخطاء شائعة في المعاملات الافتراضية",
    slide_text="قواعد حاسمة في PHP حول مكان المعاملات الافتراضية وسلوك استدعائها:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ وضع الاختياري قبل الإلزامي</div>
          <ul class="bullet-list">
            <li>وضع المعامل ذو القيمة الافتراضية في الأول يربك ترتيب الوسائط</li>
            <li>كود خاطئ في PHP 8+:
              <pre class="code-body" style="padding:0.4rem 0.6rem;font-size:0.75rem;"><span class="tok-kw">function</span> <span class="tok-fn">login</span>(<span class="tok-var">$role</span> = <span class="tok-str">"admin"</span>, <span class="tok-var">$user</span>) { ... }
<span class="tok-cmt">// Deprecated: Optional parameter before required</span></pre>
            </li>
            <li><strong>التصحيح:</strong> الإلزامي أولاً: <code>($user, $role = "admin")</code></li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">💡 متى تُستخدم القيمة الافتراضية؟</div>
          <ul class="bullet-list">
            <li>القيمة الافتراضية تُستخدم <strong>فقط عند عدم تمرير وسيط</strong></li>
            <li>إذا مرّرت <code>null</code> أو نصاً فارغاً <code>""</code>، ستأخذ الدالة <code>null</code> أو <code>""</code> ولن تعود للقيمة الافتراضية!</li>
            <li>تأكد من استدعاء الدالة بدون وسيط <code>func()</code> للاستفادة من الافتراضي</li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في المعاملات الافتراضية",
    notes_script="في PHP 8 أصبح وضع المعامل الافتراضي قبل الإلزامي يطلق رسالة Deprecation رسمية. دائماً رتب: المعاملات التي ليس لها افتراضي أولاً، ثم التي لها افتراضي أخيراً.",
    notes_list=["المعاملات الإلزامية تسبق الاختيارية", "الافتراضي يُستخدم فقط عند عدم التمرير"]
)

# Slide 13: Scope: Local vs Global
make_slide(
    index=12,
    title="نطاق المتغيرات: المحلي والعام",
    eyebrow="نطاق المتغيرات &middot; 3",
    slide_title="نطاق المتغيرات: المحلي والعام",
    slide_text="النطاق (Scope) يحدد أين يمكن رؤية المتغير واستخدامه في الكود. دوال PHP تتمتع بنطاق معزول تماماً عن المحيط الخارجي.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>النطاق المحلي (Local Scope):</strong> أي متغير يُنشأ داخل دالة، يعيش ويموت بداخلها فقط</li>
          <li><strong>النطاق العام (Global Scope):</strong> المتغيرات المعرفة خارج أي دالة</li>
          <li>الدالة في PHP <strong>لا تستطيع رؤية المتغيرات العامة</strong> تلقائياً</li>
          <li>لإتاحة متغير عام داخل الدالة، نستخدم الكلمة المفتاحية <code>global</code></li>
          <li>العزل التام يحمي المتغيرات من التعديل العشوائي غير المقصود</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">scope_intro.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$appName</span> = <span class="tok-str">"Logharitm"</span>; <span class="tok-cmt">// Global</span>

<span class="tok-kw">function</span> <span class="tok-fn">showApp</span>() {
    <span class="tok-cmt">// echo $appName; // خطأ: Undefined variable</span>
    <span class="tok-var">$version</span> = <span class="tok-str">"2.0"</span>;  <span class="tok-cmt">// Local</span>
}

<span class="tok-cmt">// echo $version; // خطأ: غير مرئي خارج الدالة!</span></pre>
        </div>
      </div>''',
    notes_title="نطاق المتغيرات Local و Global",
    notes_script="نطاق المتغيرات في PHP يختلف عن لغات أخرى مثل جافاسكريبت؛ فالدالة هنا جزيرة منعزلة تماماً، لا ترى ما بالخارج ولا يرى الخارج ما بداخلها إلا بإذن صريح.",
    notes_list=["النطاق المحلي خاص بالدالة فقط", "النطاق العام خارج الدوال", "عزل المتغيرات لحماية البيانات"]
)

# Slide 14: Example 1: global keyword
make_slide(
    index=13,
    title="مثال 1: استخدام الكلمة المفتاحية global",
    eyebrow="نطاق المتغيرات &middot; مثال 1",
    slide_title="مثال 1: استخدام الكلمة المفتاحية global $x",
    slide_text="الوصول لمتغير عام معرف خارج الدالة باستخدام الكلمة المفتاحية <code>global</code>.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>عرّف المتغير <code>$x = 10</code> خارج دالة. داخل دالة باسم <code>printX()</code>، استخدم <code>global $x</code> للوصول إليه واطبعه في المتصفح.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">global.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$x</span> = <span class="tok-num">10</span>;

<span class="tok-kw">function</span> <span class="tok-fn">printX</span>() {
    <span class="tok-kw">global</span> <span class="tok-var">$x</span>;
    <span class="tok-kw">echo</span> <span class="tok-var">$x</span>;
}

<span class="tok-fn">printX</span>();</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/global.php</div>
          </div>
          <div class="browser-viewport">
            <pre class="output-ascii">10</pre>
          </div>
        </div>
      </div>''',
    notes_title="مثال الكلمة المفتاحية global",
    notes_script="بإضافة السطر global $x؛ أخبرنا PHP أن تربط المتغير داخل الدالة بالمتغير العام الموجود بالخارج، مما سمح بطباعته بنجاح.",
    notes_list=["تعريف $x خارج الدالة", "استدعاء global $x بداخلها", "طباعة القيمة 10"]
)

# Slide 15: Static Variables Concept
make_slide(
    index=14,
    title="المتغيرات الساكنة (Static Variables)",
    eyebrow="نطاق المتغيرات &middot; 3",
    slide_title="المتغيرات الساكنة (Static Variables)",
    slide_text="في الوضع العادي، يتم تدمير المتغيرات المحلية فور انتهاء الدالة. لكن الكلمة المفتاحية <code>static</code> تجعل المتغير يتذكر قيمته السابقة!",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>تُعرّف بـ <code>static $var = initial;</code> داخل الدالة</li>
          <li>التهيئة الابتدائية تحدث <strong>مرة واحدة فقط</strong> عند أول استدعاء</li>
          <li>عند تكرار استدعاء الدالة، يحتفظ المتغير بآخر قيمة وصل إليها</li>
          <li>يظل محلياً ومحمياً داخل الدالة ولا يمكن الوصول إليه من الخارج</li>
          <li>استخدام مثالي: العدادات (Counters)، التخزين المؤقت، وتتبع التكرار</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">static_diff.php</span>
          </div>
          <pre class="code-body"><span class="tok-kw">function</span> <span class="tok-fn">normalVar</span>() {
    <span class="tok-var">$a</span> = <span class="tok-num">0</span>; <span class="tok-var">$a</span>++; <span class="tok-kw">echo</span> <span class="tok-var">$a</span>; <span class="tok-cmt">// يطبع 1 دائماً</span>
}

<span class="tok-kw">function</span> <span class="tok-fn">staticVar</span>() {
    <span class="tok-kw">static</span> <span class="tok-var">$b</span> = <span class="tok-num">0</span>;
    <span class="tok-var">$b</span>++;
    <span class="tok-kw">echo</span> <span class="tok-var">$b</span>; <span class="tok-cmt">// يطبع 1 ثم 2 ثم 3...</span>
}</pre>
        </div>
      </div>''',
    notes_title="مفهوم المتغيرات الساكنة static",
    notes_script="المتغير static عبارة عن متغير محلي بذاكرة دائمة طوال فترة تشغيل السكربت. ممتاز لحساب عدد مرات الزيارة أو بناء عدادات داخلية.",
    notes_list=["التهيئة تحدث مرة واحدة فقط", "الاحتفاظ بالقيمة بين الاستدعاءات", "بقاء المتغير محمياً داخل النطاق المحلي"]
)

# Slide 16: Example 2: counter() with static
make_slide(
    index=15,
    title="مثال 2: دالة العداد counter()",
    eyebrow="نطاق المتغيرات &middot; مثال 2",
    slide_title="مثال 2: دالة العداد counter() بمتغير static",
    slide_text="بناء دالة عداد تحتفظ بالقيمة وتزيد في كل استدعاء باستخدام متغير <code>static</code>.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>عرّف دالة <code>counter()</code> تستخدم <code>static $count = 0</code>. مع كل استدعاء، قم بزيادة $count واطبعه. استدعِ الدالة 3 مرات متتالية.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">counter.php</span>
          </div>
          <pre class="code-body"><span class="tok-kw">function</span> <span class="tok-fn">counter</span>() {
    <span class="tok-kw">static</span> <span class="tok-var">$count</span> = <span class="tok-num">0</span>;
    <span class="tok-var">$count</span>++;
    <span class="tok-kw">echo</span> <span class="tok-var">$count</span> . <span class="tok-str">" "</span>;
}

<span class="tok-fn">counter</span>();
<span class="tok-fn">counter</span>();
<span class="tok-fn">counter</span>();</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/counter.php</div>
          </div>
          <div class="browser-viewport">
            <pre class="output-ascii">1 2 3 </pre>
          </div>
        </div>
      </div>''',
    notes_title="مثال دالة counter() بالمتغير الساكن",
    notes_script="عند الاستدعاء الأول طبعت 1، وفي الثاني تذكرت الـ 1 وأصبحت 2، وفي الثالث أصبحت 3. النتيجة هي 1 2 3.",
    notes_list=["تعريف static $count = 0", "الزيادة التراكمية في كل استدعاء", "المخرجات 1 2 3"]
)

# Slide 17: Common Mistakes in Scope
make_slide(
    index=16,
    title="أخطاء شائعة في نطاق المتغيرات",
    eyebrow="احذر هذه الأخطاء &middot; 3",
    slide_title="أخطاء شائعة في نطاق المتغيرات",
    slide_text="تجنب هذين الخطأين الشائعين عند التعامل مع نطاقات المتغيرات في PHP:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ ظن أن المتغيرات الداخلية مرئية بالخارج</div>
          <ul class="bullet-list">
            <li>أي متغير ينشأ داخل الدالة يتم حذفه من الذاكرة فوراً بعد إغلاق الدالة</li>
            <li>محاولة الوصول إليه في الملف العام تطلق خطأ:
              <br><code>Undefined variable</code>
            </li>
            <li><strong>الحل السليم:</strong> إذا كنت بحاجة للقيمة خارج الدالة، أرجعها بـ <code>return</code> وخزنها في متغير خارجي</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ نسيان كلمة global</div>
          <ul class="bullet-list">
            <li>في لغات مثل JS المتغيرات الخارجية مرئية بالداخل، لكن في PHP <strong>لا</strong></li>
            <li>إذا كتبت كوداً يحاول قراءة متغير عام مباشرة، ستعطيك PHP خطأ <code>Undefined variable</code></li>
            <li>يجب كتابة <code>global $x;</code> داخل الدالة قبل استخدامها، أو الأفضل: تمريره كمعامل!</li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في Scope",
    notes_script="نؤكد دائماً أن الاعتماد المفرط على global يعد مضاداً للأنماط السليمة (Anti-pattern). الأفضل تمرير البيانات كـ Arguments وإرجاعها بـ return.",
    notes_list=["المتغير الداخلي يموت مع انتهاء الدالة", "نسيان global يمنع رؤية المتغير الخارجي"]
)

# Slide 18: Anonymous Functions & Arrow Functions
make_slide(
    index=17,
    title="الدوال المجهولة ودوال السهم",
    eyebrow="الدوال المتقدمة &middot; 4",
    slide_title="الدوال المجهولة ودوال السهم",
    slide_text="الدالة المجهولة (Anonymous Function / Closure) هي دالة بدون اسم يمكن إسنادها لمتغير أو تمريرها كوسيط لدالة أخرى.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>تُنشأ بدون كتابة اسم: <code>function($param) { ... }</code></li>
          <li>يمكن تخزينها في متغير واستدعاؤها كأي دالة عادية</li>
          <li><strong>ضرورة وضع فاصلة منقوطة <code>;</code></strong> بعد القوس المعقوف</li>
          <li><strong>دوال السهم <code>fn()</code> في PHP 7.4+:</strong> صياغة مقتضبة ترجع القيمة تلقائياً من سطر واحد</li>
          <li>تُستخدم بكثرة كـ <strong>Callbacks</strong> مع دوال الـ arrays</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">anonymous_syntax.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// 1. دالة مجهولة تقليدية</span>
<span class="tok-var">$greet</span> = <span class="tok-kw">function</span>(<span class="tok-var">$name</span>) {
    <span class="tok-kw">return</span> <span class="tok-str">"أهلاً "</span> . <span class="tok-var">$name</span>;
}; <span class="tok-cmt">// لاحظ الفاصلة المنقوطة!</span>

<span class="tok-cmt">// 2. دالة سهمية (Arrow Function)</span>
<span class="tok-var">$addTen</span> = <span class="tok-kw">fn</span>(<span class="tok-var">$n</span>) =&gt; <span class="tok-var">$n</span> + <span class="tok-num">10</span>;

<span class="tok-kw">echo</span> <span class="tok-var">$greet</span>(<span class="tok-str">"عمر"</span>);  <span class="tok-cmt">// أهلاً عمر</span>
<span class="tok-kw">echo</span> <span class="tok-var">$addTen</span>(<span class="tok-num">5</span>);     <span class="tok-cmt">// 15</span></pre>
        </div>
      </div>''',
    notes_title="الدوال المجهولة ودوال السهم في PHP",
    notes_script="الدوال المجهولة من الأدوات القوية جداً في أطر العمل مثل Laravel. نستخدمها لما نكون محتاجين دالة مؤقتة لمرة واحدة أو تمريرها كـ Callback.",
    notes_list=["تعريف دالة مجهولة بلا اسم", "ضرورة الفاصلة المنقوطة في نهاية جملة الإسناد", "صياغة fn() السهمية السريعة في PHP 7.4+"]
)

# Slide 19: Example 1: $double
make_slide(
    index=18,
    title="مثال 1: دالة المضاعفة $double",
    eyebrow="الدوال المجهولة &middot; مثال 1",
    slide_title="مثال 1: دالة مضاعفة الرقم $double",
    slide_text="إنشاء دالة مجهولة تأخذ رقماً وترجع ضعفه، وتخزينها في متغير واستدعائها.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>أنشئ دالة مجهولة تستقبل رقماً وترجع ضعفه (ضرب 2). أسندها للمتغير <code>$double</code>، ثم استدعِها بالرقم 5 واطبع الناتج.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">double.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$double</span> = <span class="tok-kw">function</span>(<span class="tok-var">$num</span>) {
    <span class="tok-kw">return</span> <span class="tok-var">$num</span> * <span class="tok-num">2</span>;
};

<span class="tok-kw">echo</span> <span class="tok-var">$double</span>(<span class="tok-num">5</span>);

<span class="tok-cmt">// بديل السهم في PHP 7.4+:</span>
<span class="tok-cmt">// $double = fn($num) =&gt; $num * 2;</span></pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/double.php</div>
          </div>
          <div class="browser-viewport">
            <pre class="output-ascii">10</pre>
          </div>
        </div>
      </div>''',
    notes_title="مثال دالة المضاعفة $double",
    notes_script="نلاحظ هنا إسناد الدالة للمتغير $double، ثم استدعاء المتغير مباشرة وكأنه دالة عادية بوضع الأقواس $double(5).",
    notes_list=["إنشاء دالة مجهولة وإسنادها لـ $double", "استدعاء $double(5)", "المخرج 10"]
)

# Slide 20: Example 2: array_map with anonymous function
make_slide(
    index=19,
    title="مثال 2: دالة مع array_map",
    eyebrow="الدوال المجهولة &middot; مثال 2",
    slide_title="مثال 2: استخدام دالة مجهولة مع array_map",
    slide_text="استخدام دالة مجهولة كـ Callback مع <code>array_map</code> لتربيع عناصر الـ array [1, 2, 3].",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>استخدم دالة <code>array_map</code> مع دالة مجهولة لحساب مربع كل رقم في الـ array [1, 2, 3] للحصول على [1, 4, 9]. اطبع الناتج بـ print_r.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">array_map.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$nums</span> = [<span class="tok-num">1</span>, <span class="tok-num">2</span>, <span class="tok-num">3</span>];

<span class="tok-var">$squared</span> = <span class="tok-fn">array_map</span>(<span class="tok-kw">function</span>(<span class="tok-var">$n</span>) {
    <span class="tok-kw">return</span> <span class="tok-var">$n</span> * <span class="tok-var">$n</span>;
}, <span class="tok-var">$nums</span>);

<span class="tok-fn">print_r</span>(<span class="tok-var">$squared</span>);</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/array_map.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:ltr;font-size:0.8rem;text-align:start;">Array
(
    [0] => 1
    [1] => 4
    [2] => 9
)</div>
          </div>
        </div>
      </div>''',
    notes_title="مثال استخدام الدالة المجهولة كـ Callback",
    notes_script="هذا الاستخدام الأهم والأكثر واقعية للدوال المجهولة؛ حيث نمررها مباشرة إلى array_map لتطبق العملية على كل عنصر من عناصر الـ array بدون كتابة loop يدوي.",
    notes_list=["دالة array_map تأخذ callback و array", "تربيع الأرقام 1, 2, 3", "المخرجات array [1, 4, 9]"]
)

# Slide 21: Common Mistakes in Anonymous Functions
make_slide(
    index=20,
    title="أخطاء شائعة في الدوال المجهولة",
    eyebrow="احذر هذه الأخطاء &middot; 4",
    slide_title="أخطاء شائعة في الدوال المجهولة",
    slide_text="احذر هذين الخطأين أثناء كتابة الدوال المجهولة في PHP:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ نسيان الفاصلة المنقوطة ( ; )</div>
          <ul class="bullet-list">
            <li>لأن تعريف الدالة هنا هو جملة إسناد قيمة لمتغير:
              <br><code>$fn = function() { ... };</code>
            </li>
            <li>نسيان الفاصلة المنقوطة في النهاية يطلق خطأ قواعد (Syntax error) فوراً</li>
            <li>تذكر دائماً: أي دالة تُسند لمتغير تحتاج <code>;</code> عند القفل</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ عدم الإسناد لمتغير عند الرغبة في إعادة الاستخدام</div>
          <ul class="bullet-list">
            <li>الدالة المجهولة ليس لها اسم تستدعيها به لاحقاً</li>
            <li>إذا لم تسندها لمتغير أو تمررها مباشرة كـ Callback، فلن تستطيع استخدامها مطلقاً</li>
            <li>إذا كنت بحاجة لإعادة استدعائها في أماكن متعددة، يجب حفظها في متغير مثل <code>$calc = function()...</code></li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في الدوال المجهولة",
    notes_script="نلفت انتباه الطلاب إلى أن نهاية الدالة المجهولة ليست مجرد قوس معقوف، بل تنتهي بفاصلة منقوطة لأنها Assignment Statement.",
    notes_list=["نسيان الفاصلة المنقوطة خطأ نحوي يوقف الكود", "الدوال المجهولة تتطلب تخزينها في متغير لإعادة استدعائها"]
)

# Slide 22: Divider: Practical Exercises
make_slide(
    index=21,
    title="تمارين مكتوبة",
    eyebrow="تطبيقات عملية",
    slide_title="تمارين مكتوبة",
    slide_text="3 تمارين برمجية عملية لتطبيق وترسيخ كل المفاهيم التي درسناها اليوم في الدوال.",
    body_content='''<div class="badge-row">
        <span class="pill-badge">square() &amp; cube()</span>
        <span class="pill-badge">greetUser()</span>
        <span class="pill-badge">static counter()</span>
      </div>''',
    notes_title="فاصل التمارين المكتوبة",
    notes_script="الآن سنبدأ القسم العملي مع 3 تمارين مكتوبة يقيس كل منها فهماً لمفهوم محدد: الإرجاع والمعاملات، المعاملات الافتراضية، والمتغيرات الساكنة.",
    notes_list=["تمرين 1: دوال الحساب square و cube", "تمرين 2: المعاملات الافتراضية greetUser", "تمرين 3: العداد الساكن counter"],
    is_divider=True
)

# Slide 23: Problem 1: square() and cube()
make_slide(
    index=22,
    title="تمرين 1: دوال الحساب square و cube",
    eyebrow="تمارين مكتوبة &middot; 1",
    slide_title="تمرين 1: دوال الحساب square و cube",
    slide_text="عرّف دالة <code>square($num)</code> ترجع مربع الرقم. استدعِها بالرقم 4 واطبع الناتج. ثم عرّف دالة <code>cube($num)</code> ترجع المكعب، واستدعِها بالرقم 3 واطبع الناتج.",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب البرمجي</div>
          <p>استخدم الكلمة المفتاحية <code>function</code> و <code>return</code> لإنشاء دالتين مستقلتين، مع التأكد من طباعة الناتجين بشكل واضح في المتصفح.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">problem-1.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// 1. عرّف دالة square($num) لحساب المربع</span>

<span class="tok-cmt">// 2. استدعِ الدالة بالرقم 4 واطبع الناتج (16)</span>

<span class="tok-cmt">// 3. عرّف دالة cube($num) لحساب المكعب</span>

<span class="tok-cmt">// 4. استدعِ الدالة بالرقم 3 واطبع الناتج (27)</span></pre>
        </div>
      </div>''',
    notes_title="تمرين 1: square و cube",
    notes_script="اطلب من الطلاب كتابة الدالتين وتجربة استدعائهما والتأكد من استخدام return وليس echo داخل جسم الدالة.",
    notes_list=["تعريف square($num) بـ return $num * $num", "تعريف cube($num) بـ return $num ** 3", "طباعة 16 و 27"]
)

# Slide 24: Problem 2: greetUser($name = "Guest")
make_slide(
    index=23,
    title="تمرين 2: دالة greetUser الافتراضية",
    eyebrow="تمارين مكتوبة &middot; 2",
    slide_title="تمرين 2: دالة greetUser الافتراضية",
    slide_text="عرّف دالة <code>greetUser($name = \"Guest\")</code> تطبع \"Welcome, $name!\". استدعِها مع الاسم \"Ahmed\"، ثم استدعِها بدون أي معاملات، واطبع الناتجين.",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب البرمجي</div>
          <p>تطبيق فكرة المعاملات الافتراضية (Default Parameters)، والتأكد من إمكانية استدعاء الدالة بوجود وسيط أو غيابه بدون حدوث أي أخطاء.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">problem-2.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// 1. عرّف دالة greetUser بمعامل افتراضي قيمته "Guest"</span>

<span class="tok-cmt">// 2. استدعِ الدالة ومرر لها الاسم "Ahmed"</span>

<span class="tok-cmt">// 3. استدعِ الدالة مرة أخرى بدون أي معاملات</span>

<span class="tok-cmt">// المخرجات المتوقعة:</span>
<span class="tok-cmt">// Welcome, Ahmed!</span>
<span class="tok-cmt">// Welcome, Guest!</span></pre>
        </div>
      </div>''',
    notes_title="تمرين 2: المعاملات الافتراضية greetUser",
    notes_script="الهدف هو تعويد الطلاب على استخدام المعاملات الافتراضية والتحقق من المخرجين في المتصفح.",
    notes_list=["تعريف $name = 'Guest'", "الاستدعاء بـ 'Ahmed'", "الاستدعاء بدون وسيط"]
)

# Slide 25: Problem 3: counter() with static 5 times
make_slide(
    index=24,
    title="تمرين 3: عداد الاستدعاء بـ static",
    eyebrow="تمارين مكتوبة &middot; 3",
    slide_title="تمرين 3: عداد الاستدعاء بـ static",
    slide_text="عرّف دالة <code>counter()</code> تستخدم متغيراً ساكناً لحساب عدد مرات استدعائها. استدعِها 5 مرات متتالية واطبع العدّاد في كل مرة ليظهر: 1 2 3 4 5.",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب البرمجي</div>
          <p>استخدام الكلمة المفتاحية <code>static</code> داخل الدالة لمنع إعادة تصفير المتغير عند كل استدعاء، واستدعاؤها 5 مرات متتالية.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">problem-3.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// 1. عرّف دالة counter وبداخلها متغير static بقيمة 0</span>

<span class="tok-cmt">// 2. قم بزيادة المتغير واطبعه يليه مسافة</span>

<span class="tok-cmt">// 3. استدعِ الدالة 5 مرات</span>

<span class="tok-cmt">// المخرجات المتوقعة:</span>
<span class="tok-cmt">// 1 2 3 4 5</span></pre>
        </div>
      </div>''',
    notes_title="تمرين 3: العداد الساكن counter",
    notes_script="هذا التمرين يختبر فهم الطلاب لمفهوم static وأنه يحتفظ بالقيمة بين الاستدعاءات الخمسة.",
    notes_list=["تعريف static $count = 0", "الاستدعاء 5 مرات متتالية", "النتيجة: 1 2 3 4 5"]
)

# Slide 26: Divider: وقت المراجعة
make_slide(
    index=25,
    title="وقت المراجعة",
    eyebrow="نقاش ومراجعة",
    slide_title="وقت المراجعة",
    slide_text="قبل أن نختم، فكّر في هذين السؤالين وتأكد من استيعابك الكامل لهما:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">ما الفرق بين المتغير المحلي والمتغير الساكن (static) داخل الدالة؟</span>
        <span class="pill-badge">لماذا يجب وضع المعاملات الاختيارية بعد الإلزامية دائماً؟</span>
      </div>''',
    notes_title="فاصل المراجعة",
    notes_script="أسئلة سريعة لإشراك الطلاب والتأكد من إدراكهم للفروق المفصلية بين المتغير المحلي والساكن، وقواعد ترتيب المعاملات.",
    notes_list=["سؤال الفرق بين Local و Static", "سؤال ترتيب المعاملات الافتراضية والإلزامية"],
    is_divider=True
)

# Slide 27: Summary
make_slide(
    index=26,
    title="اللي اتعلمناه النهاردة",
    eyebrow="ملخص المحاضرة",
    slide_title="اللي اتعلمناه النهاردة",
    slide_text="خلاصة أهم 4 ركائز أتقناها اليوم في التعامل مع الدوال في PHP:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">تعريف الدوال وقيم return</div>
            <div class="topic-desc">منع التكرار (DRY) وتحديد نوع الإرجاع (Type Safety)</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">المعاملات الافتراضية</div>
            <div class="topic-desc">مرونة الاستدعاء ووضع الاختياري بعد الإلزامي دائماً</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">نطاق المتغيرات (Scope)</div>
            <div class="topic-desc">عزل الدوال واستخدام global للعام و static للذاكرة</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">الدوال المجهولة والسهمية</div>
            <div class="topic-desc">استخدامها كـ Callbacks مع array_map وسرعة fn()</div>
          </div>
        </div>
      </div>''',
    notes_title="ملخص المحاضرة 06",
    notes_script="نراجع مع الطلاب النقاط الأربع الكبرى: الدوال الأساسية، المعاملات الافتراضية، إدارة النطاقات، والدوال المجهولة.",
    notes_list=["مبدأ DRY و Type Safety", "المعاملات الافتراضية", "نطاق المتغيرات global و static", "الدوال المجهولة والسهمية"]
)

# Slide 28: Ending / Thank You
make_slide(
    index=27,
    title="شكرًا لكم",
    eyebrow="نهاية المحاضرة 06",
    slide_title="شكرًا لكم",
    slide_text="الدوال هي اللبنة الأساسية لبناء أي تطبيق PHP احترافي وقاعدة الانطلاق نحو الـ Object-Oriented Programming (OOP) &mdash; واصلوا التدريب والتطبيق!",
    body_content='''<div class="badge-row">
        <span class="pill-badge">المحاضرة 06</span>
        <span class="pill-badge">الدوال في PHP</span>
        <span class="pill-badge">لوغاريتم للتدريب البرمجي</span>
      </div>''',
    notes_title="خاتمة المحاضرة 06",
    notes_script="شكر الطلاب على تركيزهم وتشجيعهم على حل التمارين المكتوبة بأيديهم على بيئة التطوير الخاصة بهم.",
    notes_list=["شكر وتقدير", "التشجيع على الممارسة المستمرة", "تمهيد للموضوع القادم"],
    is_divider=True
)

print("All 28 slides generated successfully!")
