# -*- coding: utf-8 -*-
"""
Generator script for Lecture 09:
State Management in Web Applications: Cookies & Sessions
29 Slides Total.
"""
from build_lecture_09 import make_slide

# ==========================================
# Slide 01: Cover
# ==========================================
make_slide(
    index=0,
    title="إدارة الحالة: الكوكيز والجلسات (Cookies & Sessions)",
    eyebrow="أساسيات PHP &middot; المحاضرة 09",
    slide_title="إدارة الحالة في PHP: الكوكيز والجلسات",
    slide_text="كيف نجعل تطبيقات الويب تتذكر المستخدمين وبياناتهم بين الطلبات: من فهم طبيعة بروتوكول HTTP عديم الحالة (Stateless)، إلى الكوكيز في متصفح العميل والجلسات المشفرة على الخادم، وصولاً لبناء أنظمة تسجيل الدخول وسلات التسوق.",
    body_content='''<div class="cover-mark">
        <div><div class="num">05</div><div class="lbl">محاور أساسية</div></div>
        <div><div class="num">04</div><div class="lbl">تطبيقات برمجية كاملة</div></div>
        <div><div class="num">03</div><div class="lbl">مشاريع وواجبات</div></div>
        <div><div class="num">~65 د</div><div class="lbl">المدة التقديرية</div></div>
      </div>''',
    notes_title="المحاضرة 09: إدارة الحالة (Cookies & Sessions)",
    notes_script="أهلاً بكم في المحاضرة التاسعة. بدون إدارة الحالة، لا يمكن بناء فيسبوك أو أمازون أو أي موقع يحتاج لتسجيل الدخول أو تذكر مشتريات السلة. اليوم سنتعلم كيف نحول الويب من نظام فاقد للذاكرة إلى تجربة تفاعلية تحتفظ بسياق المستخدم وأمانه.",
    notes_list=["طبيعة HTTP عديم الحالة Stateless", "الكوكيز Cookies وتخزين المتصفح", "الجلسات Sessions والتخزين الآمن بالخادم", "تطبيقات حية: تسجيل الدخول، تذكرني، وسلة المشتريات"],
    is_cover=True
)

# ==========================================
# Slide 02: Roadmap
# ==========================================
make_slide(
    index=1,
    title="خريطة ومحاور المحاضرة 09",
    eyebrow="نظرة عامة &middot; محتويات المحاضرة",
    slide_title="خريطة ومحاور المحاضرة 09",
    slide_text="مسار تعليمي متكامل ينقلك من الأساس النظري للبروتوكول إلى أحدث ممارسات الأمان وإدارة الجلسات:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">معضلة الويب عديم الحالة (Stateless HTTP)</div>
            <div class="topic-desc">لماذا ينسى الخادم المستخدم بعد كل طلب؟ والحاجة الماسة لمفهوم الـ State</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">الكوكيز (Cookies): تخزين المتصفح</div>
            <div class="topic-desc">ترويسات Set-Cookie، دالة setcookie()، ومعاملات الأمان (HttpOnly, Secure)</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">الجلسات (Sessions): أمان الخادم</div>
            <div class="topic-desc">معرف PHPSESSID، دالة session_start()، تخزين المصفوفة $_SESSION، وحماية التثبيت</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">المقارنة الشاملة ودليل القرار</div>
            <div class="topic-desc">مقارنة معمارية دقيقة: متى تختار Cookie ومتى تختار Session في الإنتاج؟</div>
          </div>
        </div>
      </div>''',
    notes_title="خريطة المحاضرة 09",
    notes_script="خريطتنا لليوم واضحة: نبدأ بفهم مشكلة بروتوكول HTTP، ثم نستكشف حل العميل عبر الكوكيز، ثم حل الخادم الآمن عبر الجلسات، ونقارن بينهما ونتوج المحاضرة بمشاريع وتطبيقات حية.",
    notes_list=["معضلة HTTP Stateless", "الكوكيز ودوالها وأمانها", "الجلسات وإدارتها بالخادم", "المقارنة والتطبيقات والواجبات"]
)

# ==========================================
# Slide 03: Stateless HTTP
# ==========================================
make_slide(
    index=2,
    title="معضلة الويب عديم الحالة (Stateless Protocol)",
    eyebrow="مفهوم الحالة &middot; 1",
    slide_title="معضلة الويب: بروتوكول HTTP عديم الحالة",
    slide_text="صُمم بروتوكول HTTP ليكون عديم الحالة (Stateless)؛ فكل طلب (Request) يُعامل كحدث مستقل تماماً عن أي طلب سابق:",
    body_content='''<div class="flow-steps">
        <div class="flow-step">
          <div class="flow-icon">🔑</div>
          <div class="flow-title">الطلب 1: تسجيل الدخول</div>
          <div class="flow-desc">المتصفح يرسل الاسم وكلمة المرور، ويتحقق السيرفر بنجاح ويعيد صفحة الترحيب</div>
        </div>
        <div class="flow-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
        <div class="flow-step">
          <div class="flow-icon">❓</div>
          <div class="flow-title">الطلب 2: لوحة التحكم</div>
          <div class="flow-desc">المتصفح يطلب صفحة الحساب، فيرد السيرفر: «من أنت؟ أنا لا أتذكر أي طلبات سابقة!»</div>
        </div>
        <div class="flow-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
        <div class="flow-step">
          <div class="flow-icon">💡</div>
          <div class="flow-title">الحل: بطاقة الهوية (State)</div>
          <div class="flow-desc">تزويد المتصفح ببطاقة هوية (Token / Cookie) يرسلها مع كل طلب قادم ليتعرف عليه الخادم</div>
        </div>
      </div>''',
    notes_title="طبيعة HTTP عديم الحالة",
    notes_script="تخيل أنك تدخل بنكاً وفي كل خطوة يسألك الموظف عن بطاقتك الشخصية من الصفر لأنه ينسى وجهك فور انتهاء الحديث. هذا تماماً هو سلوك HTTP، والحل هو إدارة الحالة State Management.",
    notes_list=["طبيعة HTTP المستقلة لكل طلب", "مشكلة نسيان سياق المستخدم", "أهمية تزويد المتصفح ببطاقة تعريفية للربط"]
)

# ==========================================
# Slide 04: Solution: State Management Architecture
# ==========================================
make_slide(
    index=3,
    title="الحل الهندسي: معمارية إدارة الحالة",
    eyebrow="مفهوم الحالة &middot; 2",
    slide_title="الحل الهندسي: تكامل العميل والخادم في إدارة الحالة",
    slide_text="للتغلب على معضلة الويب، توفر تقنيات الويب آليتين رئيسيتين متكاملتين تختلفان في مكان حفظ البيانات:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">🍪 جانب العميل: الكوكيز (Cookies)</div>
          <ul class="bullet-list">
            <li><strong>مكان التخزين:</strong> داخل متصفح المستخدم على جهازه الشخصي.</li>
            <li><strong>آلية الإرسال:</strong> يعيد المتصفح إرسالها تلقائياً في ترويسات HTTP مع كل طلب لنفس النطاق.</li>
            <li><strong>الاستخدام:</strong> تفضيلات العرض (Dark Mode)، اللغة المختارة، وتتبع المعرفات.</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">🔒 جانب الخادم: الجلسات (Sessions)</div>
          <ul class="bullet-list">
            <li><strong>مكان التخزين:</strong> ملفات آمنة أو ذاكرة مؤقتة على سيرفر الويب نفسه.</li>
            <li><strong>حلقة الوصل:</strong> يملك المتصفح فقط معرّف الجلسة العشوائي (Session ID) كرمز وصول.</li>
            <li><strong>الاستخدام:</strong> بيانات المصادقة الحساسة، الصلاحيات، وسلة المشتريات.</li>
          </ul>
        </div>
      </div>''',
    notes_title="معمارية إدارة الحالة",
    notes_script="الكوكيز في يد العميل، والجلسات في خزانة السيرفر. العميل لا يملك سوى مفتاح الخزانة Session ID، وبذلك نجمع بين سهولة تتبع العميل وأمان البيانات الحساسة بالخادم.",
    notes_list=["الكوكيز بالمتصفح Client-side", "الجلسات بالخادم Server-side", "Session ID كحلقة وصل آمنة"]
)

# ==========================================
# Slide 05: Section Divider: Cookies
# ==========================================
make_slide(
    index=4,
    title="الكوكيز (Cookies): التخزين في متصفح العميل",
    eyebrow="القسم الأول",
    slide_title="الكوكيز (Cookies): التخزين في متصفح العميل",
    slide_text="ملفات نصية خفيفة الوزن يرسلها الخادم لتُحفظ في المتصفح وترافق كل طلب قادم:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">كيف تعمل عبر ترويسات HTTP (Headers)</span>
        <span class="pill-badge">دالة setcookie() ومعاملات الأمان</span>
        <span class="pill-badge">القراءة والتعديل والحذف عبر $_COOKIE</span>
      </div>''',
    notes_title="فاصل محور الكوكيز",
    notes_script="نبدأ الآن بمحور الكوكيز. سنتعرف على آلية الترويسات وكيف يتم حفظ الكوكي في المتصفح ودوال إدارته في PHP.",
    notes_list=["ترويسات HTTP", "دالة setcookie", "مصفوفة $_COOKIE"],
    is_divider=True
)

# ==========================================
# Slide 06: Cookies: HTTP Headers & Mechanism
# ==========================================
make_slide(
    index=5,
    title="الكوكيز: آلية الترويسات (Set-Cookie & Cookie)",
    eyebrow="الكوكيز &middot; 1",
    slide_title="الكوكيز: كيف تنتقل بين المتصفح والخادم؟",
    slide_text="لا يتم تخزين الكوكيز عبر جسم الصفحة HTML، بل تنتقل عبر ترويسات بروتوكول HTTP في خلفية الاتصال:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>1. استجابة الخادم الأولى:</strong> يرسل الخادم ترويسة <code>Set-Cookie: theme=dark; Path=/</code> في المتصفح.</li>
          <li><strong>2. التخزين بالمتصفح:</strong> يفحص المتصفح النطاق والمسار وتاريخ الانتهاء، ويخزن الكوكي في قاعدة بياناته المحلية.</li>
          <li><strong>3. الطلبات اللاحقة:</strong> في كل زيارة لأي صفحة في نفس الموقع، يرفق المتصفح ترويسة <code>Cookie: theme=dark</code> تلقائياً!</li>
          <li><strong>4. قراءة PHP:</strong> يلتقط مفسر PHP الترويسة ويحللها تلقائياً داخل المصفوفة الفائقة <code>$_COOKIE</code>.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">HTTP Network Headers</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// استجابة الخادم عند إنشاء الكوكي:</span>
<span class="tok-kw">HTTP/1.1 200 OK</span>
<span class="tok-fn">Set-Cookie:</span> theme=dark; expires=Thu, 08-Oct-2026; path=/; HttpOnly

<span class="tok-cmt">// طلب المتصفح في الصفحات التالية:</span>
<span class="tok-kw">GET /dashboard.php HTTP/1.1</span>
<span class="tok-fn">Host:</span> localhost
<span class="tok-fn">Cookie:</span> theme=dark</pre>
        </div>
      </div>''',
    notes_title="آلية عمل الكوكيز",
    notes_script="فهم ترويسات HTTP يفسر كل سلوك الكوكيز: السيرفر يطلب من المتصفح حفظ الكوكي بـ Set-Cookie، والمتصفح يعيده مطيعاً في كل طلب لاحق بـ Cookie.",
    notes_list=["ترويسة Set-Cookie من السيرفر", "ترويسة Cookie من المتصفح", "تحليل PHP التلقائي في $_COOKIE"]
)

# ==========================================
# Slide 07: setcookie() function parameters
# ==========================================
make_slide(
    index=6,
    title="دالة setcookie() ومعاملاتها الأساسية والأمنية",
    eyebrow="الكوكيز &middot; 2",
    slide_title="دالة setcookie(): المعاملات وضوابط الأمان",
    slide_text="في PHP ننشئ الكوكيز باستخدام دالة <code>setcookie()</code> التي تقبل معاملات دقيقة تحدد سلوك الكوكي وأمانه:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>$name</code> & <code>$value</code>: اسم الكوكي وقيمته النصية.</li>
          <li><code>$expires_or_options</code>: وقت الانتهاء كختم زمني Unix timestamp (مثل <code>time() + 86400 * 30</code> لـ 30 يوماً). إن تركته <code>0</code> يُحذف فور إغلاق المتصفح (Session Cookie).</li>
          <li><code>$path</code>: المسار الذي يتاح فيه الكوكي؛ نستخدم <code>"/"</code> ليكون متاحاً في كافة مجلدات الموقع.</li>
          <li><code>$secure</code>: إذا كانت <code>true</code>، لن يُرسل الكوكي إلا عبر اتصال مشفر وآمن بـ HTTPS.</li>
          <li><code>$httponly</code>: إذا كانت <code>true</code>، يُمنع كود JavaScript من قراءة الكوكي (حماية حاسمة ضد هجمات XSS).</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">setcookie.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// طريقة حديثة واحترافية (PHP 7.3+)</span>
<span class="tok-fn">setcookie</span>(<span class="tok-str">"site_theme"</span>, <span class="tok-str">"dark"</span>, [
    <span class="tok-str">'expires'</span>  =&gt; <span class="tok-fn">time</span>() + (<span class="tok-num">86400</span> * <span class="tok-num">30</span>), <span class="tok-cmt">// 30 يوم</span>
    <span class="tok-str">'path'</span>     =&gt; <span class="tok-str">'/'</span>,
    <span class="tok-str">'secure'</span>   =&gt; <span class="tok-kw">false</span>, <span class="tok-cmt">// true في بيئة الإنتاج HTTPS</span>
    <span class="tok-str">'httponly'</span> =&gt; <span class="tok-kw">true</span>,  <span class="tok-cmt">// حماية من سرقة JS XSS</span>
    <span class="tok-str">'samesite'</span> =&gt; <span class="tok-str">'Lax'</span>  <span class="tok-cmt">// حماية من CSRF</span>
]);</pre>
        </div>
      </div>''',
    notes_title="معاملات دالة setcookie",
    notes_script="القاعدة الاحترافية: اجعل httponly دائماً true ما لم تكن بحاجة لقراءة الكوكي بواسطة JavaScript. واضبط path على / ليعمل الكوكي عبر كافة صفحات الموقع.",
    notes_list=["معاملات setcookie الأساسية والأمنية", "تحديد مدة الصلاحية بـ time()", "أهمية علم httponly لمنع XSS", "علم secure مع HTTPS"]
)

# ==========================================
# Slide 08: Reading, Modifying & Deleting Cookies
# ==========================================
make_slide(
    index=7,
    title="قراءة وتعديل وحذف الكوكيز في PHP",
    eyebrow="الكوكيز &middot; 3",
    slide_title="العمليات الثلاث: قراءة، تعديل، وحذف الكوكي",
    slide_text="التعامل الكامل مع دورة حياة الكوكي من القراءة بـ <code>$_COOKIE</code> إلى الحذف النهائي:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">قواعد العمليات الثلاث</div>
          <ul class="bullet-list" style="margin-top:0.3rem;">
            <li><strong>القراءة:</strong> فحص وجوده أولاً بـ <code>isset($_COOKIE['name'])</code> لتجنب أخطاء التحذير.</li>
            <li><strong>التعديل:</strong> إعادة استدعاء <code>setcookie</code> بنفس الاسم وقيمة جديدة.</li>
            <li><strong>الحذف:</strong> ضبط وقت الانتهاء في الماضي: <code>time() - 3600</code>، فيقوم المتصفح بإتلافه فوراً!</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">cookie_crud.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// 1. القراءة الآمنة مع قيمة افتراضية</span>
<span class="tok-var">$theme</span> = <span class="tok-var">$_COOKIE</span>[<span class="tok-str">'site_theme'</span>] ?? <span class="tok-str">'light'</span>;

<span class="tok-cmt">// 2. التعديل: إرسال قيمة جديدة</span>
<span class="tok-fn">setcookie</span>(<span class="tok-str">'site_theme'</span>, <span class="tok-str">'emerald'</span>, <span class="tok-fn">time</span>() + <span class="tok-num">86400</span>, <span class="tok-str">'/'</span>);

<span class="tok-cmt">// 3. الحذف: تعيين تاريخ ماضٍ</span>
<span class="tok-fn">setcookie</span>(<span class="tok-str">'site_theme'</span>, <span class="tok-str">''</span>, <span class="tok-fn">time</span>() - <span class="tok-num">3600</span>, <span class="tok-str">'/'</span>);
<span class="tok-kw">unset</span>(<span class="tok-var">$_COOKIE</span>[<span class="tok-str">'site_theme'</span>]);</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/cookie_crud.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.85rem;">
السمة الحالية: emerald
تم تعديل الكوكي وتعيين الصلاحية!
عند طلب الحذف: يتم إرسال تاريخ ماضٍ ويحذفه المتصفح فوراً.
            </div>
          </div>
        </div>
      </div>''',
    notes_title="قراءة وتعديل وحذف الكوكيز",
    notes_script="كيف نحذف كوكي؟ في PHP لا توجد دالة delete_cookie، بل نستخدم setcookie مع وقت سالب time() - 3600، فيعلم المتصفح أن صلاحيته انتهت ويحذفه.",
    notes_list=["القراءة مع مشغل ?? للقيمة الافتراضية", "التعديل بإعادة الإرسال", "الحذف بضبط وقت في الماضي time() - 3600", "حذف المتغير من $_COOKIE بـ unset"]
)

# ==========================================
# Slide 09: Cookies Limitations & Security Risks
# ==========================================
make_slide(
    index=8,
    title="قيود ومخاطر الكوكيز الأمنية",
    eyebrow="الكوكيز &middot; 4",
    slide_title="قيود ومخاطر الكوكيز الأمنية: ما لا يجب فعله",
    slide_text="الكوكيز أداة مفيدة لكنها محفوفة بمحاذير أمنية خطيرة يجب أن يعرفها كل مهندس برمجيات:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">🚫 محظورات أمنية مطلقة</div>
          <ul class="bullet-list">
            <li><strong>لا تخزن أبداً كلمات المرور</strong> أو أرقام البطاقات البنكية في الكوكي!</li>
            <li><strong>لا تخزن صلاحيات المستخدم</strong> مثل <code>is_admin=1</code>؛ يستطيع أي مستخدم فتح أدوات المطور (F12) وتغيير القيمة واختراق الموقع!</li>
            <li>الكوكي مكشوف تماماً للمستخدم ولأي برنامج على جهازه.</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ قيود فنية وتقنية</div>
          <ul class="bullet-list">
            <li><strong>سعة محدودة جداً:</strong> الحجم الأقصى للكوكي حوالي 4 كيلوبايت فقط لكل نطاق.</li>
            <li><strong>استهلاك الباندويث:</strong> بما أن الكوكي يُرسل مع كل طلب لصور وملفات الموقع، فإن كثرة الكوكيز تبطئ سرعة تحميل الصفحات.</li>
            <li>يمكن للمستخدم تعطيل الكوكيز بالكامل من إعدادات المتصفح.</li>
          </ul>
        </div>
      </div>''',
    notes_title="قيود ومخاطر الكوكيز",
    notes_script="القاعدة الذهبية للكوكيز: لا تثق أبداً في البيانات القادمة من الكوكي! المستخدم يستطيع تعديلها وتزييفها كما يشاء. استخدم الكوكيز للمعلومات غير الحساسة فقط.",
    notes_list=["حظر تخزين كلمات المرور والصلاحيات", "إمكانية تلاعب المستخدم بالكوكيز", "الحد الأقصى للحجم 4KB", "تأثير إرسال الكوكيز على أداء الموقع"]
)

# ==========================================
# Slide 10: Section Divider: Sessions
# ==========================================
make_slide(
    index=9,
    title="الجلسات (Sessions): التخزين الآمن على الخادم",
    eyebrow="القسم الثاني",
    slide_title="الجلسات (Sessions): التخزين الآمن على الخادم",
    slide_text="الحل الأمني الأمثل لتخزين بيانات المستخدم الحساسة بالكامل على خادم الويب المحمي:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">معرف الجلسة الفريد PHPSESSID</span>
        <span class="pill-badge">دالة session_start() والمصفوفة $_SESSION</span>
        <span class="pill-badge">إتلاف الجلسة والتسجيل الآمن للخروج (Logout)</span>
      </div>''',
    notes_title="فاصل محور الجلسات",
    notes_script="ننتقل للقسم الثاني: الجلسات Sessions. هنا تخزن البيانات الحقيقية بالخادم، ولا يرى المتصفح سوى معرف رقمي فريد يسمى Session ID.",
    notes_list=["مفهوم الجلسات بالخادم", "معرف PHPSESSID", "حماية البيانات الحساسة"],
    is_divider=True
)

# ==========================================
# Slide 11: Sessions Mechanism & PHPSESSID
# ==========================================
make_slide(
    index=10,
    title="الجلسات: آلية العمل الداخلية ومعرف PHPSESSID",
    eyebrow="الجلسات &middot; 1",
    slide_title="الجلسات: كيف تعمل وراء الكواليس؟",
    slide_text="الجلسة عبارة عن خزانة بيانات سرية في الخادم، والمفتاح الوحيد للوصول إليها هو معرّف مشفر يسمى <code>PHPSESSID</code>:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>1. إنشاء الجلسة:</strong> عند استدعاء <code>session_start()</code>، يولد الخادم سلسلة عشوائية مشفرة (Session ID) مكونة من 32 حرفاً فريداً.</li>
          <li><strong>2. ملف الخادم:</strong> ينشئ السيرفر ملفاً في مسار التخزين (مثل <code>sess_8a7f...</code>) لحفظ المتغيرات فيه.</li>
          <li><strong>3. تسليم المفتاح:</strong> يرسل السيرفر كوكي مؤقت للمتصفح يحمل اسم <code>PHPSESSID</code> وقيمته هي ذلك المعرف العشوائي.</li>
          <li><strong>4. الاستعادة الآمنة:</strong> في كل طلب، يقدم المتصفح كوكي <code>PHPSESSID</code>، فيفتح الخادم ملف الجلسة المطابق فوراً!</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">Session Architecture</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// بالمتصفح (العميل): كوكي يحمل المعرف فقط</span>
Cookie: PHPSESSID=d92b0f4a8e21c60f...

<span class="tok-cmt">// بالخادم (سيرفر الويب): ملف محمي بالكامل</span>
/tmp/sess_d92b0f4a8e21c60f
──────────────────────────────────────
user_id|i:42;
username|s:5:"ahmed";
role|s:5:"admin";
cart|a:2:{...}</pre>
        </div>
      </div>''',
    notes_title="آلية عمل الجلسات",
    notes_script="المتصفح لا يعلم ما بداخل الجلسة؛ هو فقط يحمل بطاقة برقم خزانته PHPSESSID. الخادم هو الوحيد القادر على فتح الخزانة وقراءة محتواها.",
    notes_list=["توليد Session ID عشوائي فريد", "حفظ البيانات في ملف آمن بالسيرفر", "المتصفح يملك المفتاح فقط", "أمان تام ضد تلاعب المستخدم"]
)

# ==========================================
# Slide 12: session_start() Rules
# ==========================================
make_slide(
    index=11,
    title="دالة session_start() وقواعد الاستدعاء الصارمة",
    eyebrow="الجلسات &middot; 2",
    slide_title="دالة session_start(): حجر الأساس لكل جلسة",
    slide_text="قبل أي تعامل مع الجلسة، يجب استدعاء <code>session_start()</code> مع الالتزام بقاعدتين برمجيتين حاسمتين:",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>القاعدة 1 (السطر الأول دائماً):</strong> يجب أن تُستدعى <code>session_start()</code> في أول سطر بالملف، <strong>قبل أي مخرجات نصية أو مسافات فارغة أو وسوم HTML</strong>، لأنها ترسل ترويسات HTTP.</li>
          <li><strong>القاعدة 2 (الاستدعاء في كل صفحة):</strong> يجب وضعها في كل ملف أو صفحة تحتاج لقراءة أو تعديل <code>$_SESSION</code>؛ وبدونها ستكون المصفوفة فارغة تماماً!</li>
          <li><strong>السلوك التلقائي:</strong> إذا كانت الجلسة موجودة مسبقاً تسترجعها؛ وإن لم تكن موجودة تنشئ جلسة جديدة تلقائياً.</li>
          <li><code>session_id()</code>: دالة تعيد معرّف الجلسة الحالي المستخدم للربط.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">start.php</span>
          </div>
          <pre class="code-body">&lt;?php
<span class="tok-cmt">// 1. أول تعليمة في الملف إجبارياً</span>
<span class="tok-fn">session_start</span>();

<span class="tok-cmt">// 2. طباعة معرف الجلسة للتأكد</span>
<span class="tok-kw">echo</span> <span class="tok-str">"معرف الجلسة: "</span> . <span class="tok-fn">session_id</span>();
?&gt;
&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;body&gt;
    &lt;h1&gt;مرحباً في الموقع&lt;/h1&gt;
  &lt;/body&gt;
&lt;/html&gt;</pre>
        </div>
      </div>''',
    notes_title="قواعد session_start",
    notes_script="إذا طبعت حرفاً واحداً أو مسافة قبل session_start()، سينفجر خطأ headers already sent الشهير. ضعها دائماً في أول سطر في ملفك أو في ملف التكوين الرئيسي.",
    notes_list=["استدعاء session_start() في بداية الملف قبل أي HTML", "ضرورة استدعائها في كل صفحة تستخدم الجلسة", "استخراج المعرف بـ session_id()"]
)

# ==========================================
# Slide 13: Using $_SESSION Superglobal
# ==========================================
make_slide(
    index=12,
    title="التعامل مع المصفوفة الفائقة $_SESSION",
    eyebrow="الجلسات &middot; 3",
    slide_title="التخزين والقراءة بـ المصفوفة الفائقة $_SESSION",
    slide_text="تتعامل مع <code>$_SESSION</code> كمصفوفة ترابطية عادية تماماً، ولكنها تحتفظ ببياناتها عبر كافة الصفحات والطلبات:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">خصائص $_SESSION</div>
          <ul class="bullet-list" style="margin-top:0.3rem;">
            <li><strong>تخزين أي نوع بيانات:</strong> نصوص، أرقام، مصفوفات متعددة الأبعاد، وكائنات!</li>
            <li><strong>استمرار البيانات:</strong> تبقى محفوظة طوال جلسة المستخدم ما دام المتصفح مفتوحاً.</li>
            <li><strong>الفحص الآمن:</strong> نستخدم <code>isset()</code> و <code>empty()</code> للتحقق من وجود المفاتيح قبل القراءة.</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">session_storage.php</span>
          </div>
          <pre class="code-body"><span class="tok-fn">session_start</span>();

<span class="tok-cmt">// تخزين بيانات مختلفة في الجلسة</span>
<span class="tok-var">$_SESSION</span>[<span class="tok-str">'user_id'</span>]  = <span class="tok-num">101</span>;
<span class="tok-var">$_SESSION</span>[<span class="tok-str">'username'</span>] = <span class="tok-str">"طارق"</span>;
<span class="tok-var">$_SESSION</span>[<span class="tok-str">'is_admin'</span>] = <span class="tok-kw">true</span>;
<span class="tok-var">$_SESSION</span>[<span class="tok-str">'cart'</span>]     = [<span class="tok-str">'item_1'</span>, <span class="tok-str">'item_2'</span>];

<span class="tok-cmt">// قراءة البيانات في صفحة أخرى</span>
<span class="tok-kw">if</span> (<span class="tok-var">$_SESSION</span>[<span class="tok-str">'is_admin'</span>] ?? <span class="tok-kw">false</span>) {
    <span class="tok-kw">echo</span> <span class="tok-str">"أهلاً بالقائد "</span> . <span class="tok-var">$_SESSION</span>[<span class="tok-str">'username'</span>];
}</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/profile.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.85rem;">
أهلاً بالقائد طارق
رقم المعرف: 101
عدد عناصر السلة المخزنة: 2
حالة الجلسة: نشطة ومحمية بالخادم
            </div>
          </div>
        </div>
      </div>''',
    notes_title="استخدام مصفوفة $_SESSION",
    notes_script="الجميل في $_SESSION أنها مصفوفة عادية في الكود، لكن PHP تتولى سراً تشفيرها وحفظها بالخادم واسترجاعها في كل طلب للمستخدم.",
    notes_list=["تخزين أنواع البيانات البسيطة والمركبة", "مشاركة البيانات بين كافة صفحات الموقع", "فحص المتغيرات بـ ?? أو isset"]
)

# ==========================================
# Slide 14: Session Lifecycle & Destruction (Logout)
# ==========================================
make_slide(
    index=13,
    title="إنهاء الجلسة وإتلافها (Logout)",
    eyebrow="الجلسات &middot; 4",
    slide_title="دورة حياة الجلسة وإتلافها: Logout الآمن",
    slide_text="الفرق الدقيق بين حذف متغير معين، تفريغ الذاكرة، وتدمير الجلسة بالكامل عند تسجيل الخروج:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">🔍 دوال إدارة دورة الحياة</div>
          <ul class="bullet-list">
            <li><code>unset($_SESSION['key'])</code>: حذف متغير واحد محدد (مثل تفريغ السلة مع بقاء تسجيل الدخول).</li>
            <li><code>session_unset()</code>: تفريغ كافة المتغيرات المسجلة في الجلسة الحالية من الذاكرة.</li>
            <li><code>session_destroy()</code>: تدمير الجلسة ومسح ملفها بالكامل من قرص السيرفر.</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">🛡️ بروتوكول تسجيل الخروج الكامل</div>
          <pre class="code-body" style="font-size:0.82rem;"><span class="tok-fn">session_start</span>();

<span class="tok-cmt">// 1. تفريغ المصفوفة من الذاكرة</span>
<span class="tok-var">$_SESSION</span> = [];
<span class="tok-fn">session_unset</span>();

<span class="tok-cmt">// 2. مسح كوكي الجلسة من المتصفح</span>
<span class="tok-kw">if</span> (<span class="tok-fn">ini_get</span>(<span class="tok-str">"session.use_cookies"</span>)) {
    <span class="tok-fn">setcookie</span>(<span class="tok-fn">session_name</span>(), <span class="tok-str">''</span>, <span class="tok-fn">time</span>() - <span class="tok-num">42000</span>, <span class="tok-str">'/'</span>);
}

<span class="tok-cmt">// 3. تدمير ملف الجلسة بالخادم</span>
<span class="tok-fn">session_destroy</span>();

<span class="tok-fn">header</span>(<span class="tok-str">"Location: login.php"</span>);
<span class="tok-kw">exit</span>;</pre>
        </div>
      </div>''',
    notes_title="إنهاء الجلسة وتسجيل الخروج",
    notes_script="تسجيل الخروج الآمن لا يقتصر على session_destroy()؛ الكود الاحترافي يفرغ المصفوفة ويمسح كوكي PHPSESSID من المتصفح ثم يحول المستخدم.",
    notes_list=["الفرق بين unset و session_unset و session_destroy", "بروتوكول تسجيل الخروج الاحترافي", "مسح كوكي الجلسة وإعادة التوجيه"]
)

# ==========================================
# Slide 15: Session Security: Fixation & Regeneration
# ==========================================
make_slide(
    index=14,
    title="أمان الجلسات: تجديد المعرف session_regenerate_id",
    eyebrow="أمان الجلسات &middot; 5",
    slide_title="حماية الجلسات من القرصنة: session_regenerate_id()",
    slide_text="أشهر هجومين على الجلسات هما تثبيت الجلسة (Session Fixation) وسرقتها (Session Hijacking):",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>هجوم تثبيت الجلسة (Fixation):</strong> يرسل المهاجم رابطاً يحتوي على معرف جلسة محدد مسبقاً، فإذا سجل الضحية دخوله أصبح المهاجم مسجلاً بنفس المعرف!</li>
          <li><strong>الحل السحري:</strong> استدعاء <code>session_regenerate_id(true);</code> <strong>فور نجاح تسجيل الدخول</strong>.</li>
          <li><strong>ماذا تفعل الدالة؟</strong> تستبدل معرف الجلسة القديم بمعرف جديد كلياً، وتحذف ملف الجلسة القديم فوراً (بفضل المعامل <code>true</code>).</li>
          <li><strong>فحص الهوية:</strong> تخزين بصمة المتصفح <code>$_SERVER['HTTP_USER_AGENT']</code> ومطابقتها في كل طلب لكشف سرقة الجلسة.</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">secure_login.php</span>
          </div>
          <pre class="code-body"><span class="tok-fn">session_start</span>();

<span class="tok-cmt">// بعد التحقق من صحة كلمة المرور</span>
<span class="tok-kw">if</span> (<span class="tok-var">$password_valid</span>) {
    <span class="tok-cmt">// تجديد معرف الجلسة وحذف القديم فوراً!</span>
    <span class="tok-fn">session_regenerate_id</span>(<span class="tok-kw">true</span>);

    <span class="tok-var">$_SESSION</span>[<span class="tok-str">'user_id'</span>] = <span class="tok-var">$user</span>[<span class="tok-str">'id'</span>];
    <span class="tok-var">$_SESSION</span>[<span class="tok-str">'agent'</span>]   = <span class="tok-var">$_SERVER</span>[<span class="tok-str">'HTTP_USER_AGENT'</span>];
    
    <span class="tok-fn">header</span>(<span class="tok-str">"Location: dashboard.php"</span>);
    <span class="tok-kw">exit</span>;
}</pre>
        </div>
      </div>''',
    notes_title="أمان الجلسات وتجديد المعرف",
    notes_script="قاعدة أمنية إلزامية في أي تطبيق إنتاجي: في اللحظة التي يسجل فيها المستخدم دخوله أو تتغير صلاحياته، استدعِ session_regenerate_id(true) لإبطال أي معرف سابق.",
    notes_list=["خطر هجوم Session Fixation", "الحل بـ session_regenerate_id(true)", "تخزين User-Agent للتحقق", "إلغاء المعرف القديم فور المصادقة"]
)

# ==========================================
# Slide 16: Comprehensive Comparison: Cookie vs Session
# ==========================================
make_slide(
    index=15,
    title="المقارنة المعمارية الشاملة: Cookie مقابل Session",
    eyebrow="المقارنة الشاملة &middot; 1",
    slide_title="المقارنة المعمارية الشاملة: Cookie مقابل Session",
    slide_text="جدول المعايير الهندسية الدقيقة للمقارنة بين الكوكيز والجلسات في مشاريع الويب الحقيقية:",
    body_content='''<div class="compare-card">
        <div class="compare-header">
          <span class="badge-echo">الكوكيز (Cookies)</span>
          <span class="vs-badge">VS</span>
          <span class="badge-print">الجلسات (Sessions)</span>
        </div>
        <div class="compare-rows">
          <div class="compare-row">
            <div class="compare-item">متصفح العميل (Client Browser)</div>
            <div class="compare-feature">مكان التخزين</div>
            <div class="compare-item">خادم الويب (Web Server)</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">محدودة جداً (~4 كيلوبايت)</div>
            <div class="compare-feature">سعة التخزين</div>
            <div class="compare-item">كبيرة (تعتمد على ذاكرة وقرص الخادم)</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">منخفض (مكشوف وقابل للتعديل والتلاعب)</div>
            <div class="compare-feature">مستوى الأمان</div>
            <div class="compare-item">عالي جداً (محمي ومخفي عن العميل)</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">طويلة الأجل (تستمر لأشهر وسنين بالتاريخ)</div>
            <div class="compare-feature">مدة الصلاحية</div>
            <div class="compare-item">مؤقتة (تنتهي بإغلاق المتصفح غالباً)</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">تفضيل المظهر، اللغة، تذكرني (Token)</div>
            <div class="compare-feature">أفضل استخدام</div>
            <div class="compare-item">تسجيل الدخول، الصلاحيات، سلة الشراء</div>
          </div>
        </div>
      </div>''',
    notes_title="مقارنة Cookie مقابل Session",
    notes_script="مقارنة جوهرية للمطورين: الكوكي للبيانات السطحية طويلة الأجل، والجلسة للبيانات الحساسة والمؤقتة.",
    notes_list=["مكان التخزين: العميل مقابل الخادم", "السعة: 4KB مقابل سعة الخادم", "الأمان: إمكانية التلاعب مقابل الحماية التامة", "الاستخدام المثالي لكل منهما"]
)

# ==========================================
# Slide 17: Decision Matrix: When to choose what?
# ==========================================
make_slide(
    index=16,
    title="شجرة القرار: متى تختار Cookie ومتى تختار Session؟",
    eyebrow="المقارنة الشاملة &middot; 2",
    slide_title="دليل القرار: متى تختار Cookie ومتى تختار Session؟",
    slide_text="قواعد قرار هندسية واضحة تساعدك على اختيار التقنية المناسبة لكل ميزة في مشروعك:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">استخدم Session حصراً إذا:</div>
            <div class="topic-desc">البيانات ترتبط بهوية المستخدم (ID, Email)، الصلاحيات، رصيد الحساب، أو أسرار الدفع</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">استخدم Cookie حصراً إذا:</div>
            <div class="topic-desc">المعلومة غير حساسة وتريدها أن تبقى بعد إغلاق الجهاز (Dark Mode، لغة الموقع، قبول الكوكيز)</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">ادمج الاثنين معاً في:</div>
            <div class="topic-desc">ميزة «تذكرني» (Remember Me): Session للدخول الحالي، وكوكي يحمل رمزاً عشوائياً مشفراً</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">قاعدة ذهبية للمهندس:</div>
            <div class="topic-desc">أي بيانات يؤدي تعديلها من المستخدم لكسب ميزة غير مستحقة يجب أن تسكن في Session!</div>
          </div>
        </div>
      </div>''',
    notes_title="شجرة القرار الهندسي",
    notes_script="السؤال الفاصل: لو عدل المستخدم هذه القيمة هل سيكتسب صلاحيات غير مصرح بها؟ إن كانت الإجابة نعم، فهي Session بدون أدنى تردد.",
    notes_list=["معايير اختيار Session", "معايير اختيار Cookie", "حالات دمج الاثنين معاً", "القاعدة الذهبية للأمان"]
)

# ==========================================
# Slide 18: Practical App 1: Auth System & Protected Dashboard
# ==========================================
make_slide(
    index=17,
    title="تطبيق عملي 1: نظام مصادقة وحماية الصفحات (Auth Guard)",
    eyebrow="تطبيقات عملية &middot; 1",
    slide_title="تطبيق 1: نظام تسجيل دخول وحماية الصفحات",
    slide_text="بناء جدار حماية (Auth Guard) يمنع الزوار غير المسجلين من دخول لوحة التحكم ويحولهم لصفحة الدخول:",
    body_content='''<div class="grid-2">
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">auth_guard.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// يتم تضمين هذا الملف في أول كل صفحة محمية</span>
<span class="tok-fn">session_start</span>();

<span class="tok-kw">if</span> (<span class="tok-kw">empty</span>(<span class="tok-var">$_SESSION</span>[<span class="tok-str">'logged_in'</span>])) {
    <span class="tok-cmt">// المستخدم غير مسجل، حوله لصفحة الدخول</span>
    <span class="tok-fn">header</span>(<span class="tok-str">"Location: login.php"</span>);
    <span class="tok-kw">exit</span>; <span class="tok-cmt">// ضروري لإيقاف تنفيذ الكود!</span>
}</pre>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">dashboard.php</span>
          </div>
          <pre class="code-body">&lt;?php
<span class="tok-kw">require</span> <span class="tok-str">'auth_guard.php'</span>;
?&gt;
&lt;h1&gt;لوحة تحكم المشرف&lt;/h1&gt;
&lt;p&gt;أهلاً &lt;?= <span class="tok-var">$_SESSION</span>[<span class="tok-str">'username'</span>] ?&gt;!&lt;/p&gt;
&lt;a href=<span class="tok-str">"logout.php"</span>&gt;تسجيل الخروج 🚪&lt;/a&gt;</pre>
        </div>
      </div>''',
    notes_title="تطبيق 1: جدار المصادقة",
    notes_script="لاحظ أمر exit بعد header(Location). دونه قد يستمر المتصفحات الخبيثة في قراءة محتوى الصفحة المحمية حتى لو أرسل السيرفر أمر التحويل.",
    notes_list=["إنشاء ملف حماية auth_guard.php", "فحص حالة الدخول في $_SESSION", "التحويل بـ header(Location)", "أهمية أمر exit بعد التحويل"]
)

# ==========================================
# Slide 19: Practical App 2: Remember Me Feature
# ==========================================
make_slide(
    index=18,
    title="تطبيق عملي 2: ميزة «تذكرني» (Remember Me)",
    eyebrow="تطبيقات عملية &middot; 2",
    slide_title="تطبيق 2: ميزة «تذكرني» بدمج الكوكيز مع الجلسات",
    slide_text="كيف تحتفظ بتسجيل دخول المستخدم لمدة 14 يوماً حتى بعد إغلاقه للمتصفح بالكامل:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">فكرة التطبيق الاحترافية</div>
          <p>عند تسجيل الدخول بنجاح مع اختيار «تذكرني»، نفتح جلسة فورية ونزرع كوكي باسم المستخدم مشفراً أو بمعرف دائم صالح لمدة أسبوعين.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">remember_login.php</span>
          </div>
          <pre class="code-body"><span class="tok-fn">session_start</span>();

<span class="tok-cmt">// 1. حفظ جلسة العمل الحالية</span>
<span class="tok-var">$_SESSION</span>[<span class="tok-str">'user'</span>] = <span class="tok-var">$username</span>;
<span class="tok-var">$_SESSION</span>[<span class="tok-str">'logged_in'</span>] = <span class="tok-kw">true</span>;

<span class="tok-cmt">// 2. فحص اختيار تذكرني</span>
<span class="tok-kw">if</span> (!<span class="tok-kw">empty</span>(<span class="tok-var">$_POST</span>[<span class="tok-str">'remember'</span>])) {
    <span class="tok-fn">setcookie</span>(
        <span class="tok-str">'remember_user'</span>, 
        <span class="tok-var">$username</span>, 
        <span class="tok-fn">time</span>() + (<span class="tok-num">86400</span> * <span class="tok-num">14</span>), <span class="tok-cmt">// أسبوعين</span>
        <span class="tok-str">'/'</span>, 
        <span class="tok-str">''</span>, 
        <span class="tok-kw">false</span>, 
        <span class="tok-kw">true</span> <span class="tok-cmt">// httponly</span>
    );
}</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/login.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.85rem;">
تسجيل الدخول ✅
اسم المستخدم: [ tarek_coder ] ← معبأ تلقائياً من الكوكي!
كلمة المرور: [ •••••••• ]
☑ تذكرني في هذا الجهاز لمدة أسبوعين
[ دخول ]
            </div>
          </div>
        </div>
      </div>''',
    notes_title="تطبيق 2: ميزة تذكرني",
    notes_script="نزرع الكوكي لمدة أسبوعين لملء النموذج أو تجديد الدخول، بينما بيانات الاعتماد النشطة تبقى في Session.",
    notes_list=["زرع كوكي طويل الأجل", "تأمين الكوكي بـ httponly", "تحسين تجربة المستخدم بإعادة ملء الحقول"]
)

# ==========================================
# Slide 20: Practical App 3: Shopping Cart System
# ==========================================
make_slide(
    index=19,
    title="تطبيق عملي 3: سلة مشتريات المتجر الإلكتروني",
    eyebrow="تطبيقات عملية &middot; 3",
    slide_title="تطبيق 3: بناء سلة تسوق متكاملة بـ $_SESSION",
    slide_text="إدارة عناصر السلة والكميات وتحديثها فورياً في جلسة الزائر عبر صفحات المتجر المختلفة:",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب البرمجي</div>
          <p>تهيئة مصفوفة <code>$_SESSION['cart']</code>، وإضافة منتج مع زيادة كميته إن كان موجوداً، وحساب إجمالي السلة.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">cart.php</span>
          </div>
          <pre class="code-body"><span class="tok-fn">session_start</span>();
<span class="tok-kw">if</span> (!<span class="tok-kw">isset</span>(<span class="tok-var">$_SESSION</span>[<span class="tok-str">'cart'</span>])) {
    <span class="tok-var">$_SESSION</span>[<span class="tok-str">'cart'</span>] = [];
}

<span class="tok-cmt">// إضافة منتج بالـ ID</span>
<span class="tok-var">$id</span> = <span class="tok-var">$_GET</span>[<span class="tok-str">'add'</span>] ?? <span class="tok-kw">null</span>;
<span class="tok-kw">if</span> (<span class="tok-var">$id</span>) {
    <span class="tok-kw">if</span> (<span class="tok-kw">isset</span>(<span class="tok-var">$_SESSION</span>[<span class="tok-str">'cart'</span>][<span class="tok-var">$id</span>])) {
        <span class="tok-var">$_SESSION</span>[<span class="tok-str">'cart'</span>][<span class="tok-var">$id</span>][<span class="tok-str">'qty'</span>]++;
    } <span class="tok-kw">else</span> {
        <span class="tok-var">$_SESSION</span>[<span class="tok-str">'cart'</span>][<span class="tok-var">$id</span>] = [<span class="tok-str">'title'</span> =&gt; <span class="tok-str">'ماوس'</span>, <span class="tok-str">'price'</span> =&gt; <span class="tok-num">300</span>, <span class="tok-str">'qty'</span> =&gt; <span class="tok-num">1</span>];
    }
}</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/cart.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.75rem;font-size:0.85rem;">
محتويات سلة المشتريات 🛒
────────────────────────
1. ماوس الألعاب | الكمية: 2 | السعر: 600 ج.م
2. لوحة مفاتيح ميكانيكية | الكمية: 1 | السعر: 800 ج.م

المجموع الإجمالي: 1400 ج.م
[ إتمام الشراء 💳 ]  [ تفريغ السلة 🗑️ ]
            </div>
          </div>
        </div>
      </div>''',
    notes_title="تطبيق 3: سلة المشتريات",
    notes_script="هذا النمط البرمجي هو أساس كل متاجر الويب؛ سلة الجلسة تبقى مع الزائر وهو يتنقل بين الأقسام حتى يقرر الشراء.",
    notes_list=["تهيئة مصفوفة السلة بالجلسة", "التحقق من وجود المنتج وزيادة كميته", "حساب الإجمالي النهائي"]
)

# ==========================================
# Slide 21: Practical App 4: Flash Messages
# ==========================================
make_slide(
    index=20,
    title="تطبيق عملي 4: رسائل التنبيه المؤقتة (Flash Messages)",
    eyebrow="تطبيقات عملية &middot; 4",
    slide_title="تطبيق 4: رسائل التنبيه لمرة واحدة (Flash Messages)",
    slide_text="إظهار رسالة تنبيه للمستخدم (مثل «تم حفظ البيانات بنجاح!») تختفي تلقائياً عند تحديث الصفحة أو الانتقال:",
    body_content='''<div class="grid-2">
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">save_action.php</span>
          </div>
          <pre class="code-body"><span class="tok-fn">session_start</span>();

<span class="tok-cmt">// تنفيذ عملية الحفظ بنجاح</span>
<span class="tok-var">$_SESSION</span>[<span class="tok-str">'flash_msg'</span>]  = <span class="tok-str">"تم حفظ التعديلات بنجاح! ✨"</span>;
<span class="tok-var">$_SESSION</span>[<span class="tok-str">'flash_type'</span>] = <span class="tok-str">"success"</span>;

<span class="tok-cmt">// إعادة توجيه لصفحة العرض</span>
<span class="tok-fn">header</span>(<span class="tok-str">"Location: view.php"</span>);
<span class="tok-kw">exit</span>;</pre>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">view.php</span>
          </div>
          <pre class="code-body">&lt;?php
<span class="tok-fn">session_start</span>();

<span class="tok-cmt">// عرض الرسالة ثم مسحها فوراً</span>
<span class="tok-kw">if</span> (<span class="tok-kw">isset</span>(<span class="tok-var">$_SESSION</span>[<span class="tok-str">'flash_msg'</span>])) {
    <span class="tok-kw">echo</span> <span class="tok-str">"&lt;div class='alert'&gt;{$_SESSION['flash_msg']}&lt;/div&gt;"</span>;
    
    <span class="tok-cmt">// مسح الرسالة لتختفي في التحديث القادم!</span>
    <span class="tok-kw">unset</span>(<span class="tok-var">$_SESSION</span>[<span class="tok-str">'flash_msg'</span>]);
}
?&gt;</pre>
        </div>
      </div>''',
    notes_title="تطبيق 4: رسائل Flash",
    notes_script="تقنية Flash Message مستخدمة في كل أطر العمل الكبرى مثل Laravel. الفكرة البسيطة: ضع الرسالة في Session، واعرضها في الطلب التالي مع استدعاء unset فوراً.",
    notes_list=["مفهوم رسائل Flash المؤقتة", "تخزين الرسالة قبل إعادة التوجيه", "عرض الرسالة وحذفها بـ unset فوراً"]
)

# ==========================================
# Slide 22: Common Pitfalls & Mistakes
# ==========================================
make_slide(
    index=21,
    title="أخطاء شائعة في الكوكيز والجلسات وكيفية حلها",
    eyebrow="احذر هذه الأخطاء &middot; فخاخ برمجية",
    slide_title="أخطاء وفخاخ شائعة في إدارة الحالة",
    slide_text="ثلاث مشكلات برمجية وأمنية شائعة يقع فيها المطورون وطرق حلها الاحترافية:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ خطأ Headers already sent</div>
          <ul class="bullet-list">
            <li><strong>السبب:</strong> استدعاء <code>session_start()</code> أو <code>setcookie()</code> بعد طباعة أي نص أو مسافة أو وسم HTML.</li>
            <li><strong>الحل:</strong> انقل الدالة لأول سطر، وتأكد من عدم وجود مسافات قبل وسم <code>&lt;?php</code>، أو فعّل <code>ob_start()</code> لتخزين المخرجات في بافر.</li>
            <li>نسيان <code>session_start()</code> في صفحة فرعية يجعل <code>$_SESSION</code> فارغة.</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ توهم وجود الكوكي فوراً ونسيان exit</div>
          <ul class="bullet-list">
            <li>الكوكي المنشأ بـ <code>setcookie</code> لا يظهر في مصفوفة <code>$_COOKIE</code> في نفس الطلب فوراً؛ بل يظهر في الطلب القادم بعد إعادة تحميل الصفحة.</li>
            <li>نسيان كتابة <code>exit;</code> بعد <code>header("Location: ...")</code> يجعل السيرفر يكمل قراءة باقي الكود الحساس!</li>
            <li>تخزين أرقام بطاقات أو كلمات مرور في الكوكي كارثة أمنية حتمية.</li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في إدارة الحالة",
    notes_script="خطأ headers already sent سببه ترتيب تدفق بيانات HTTP. وتذكر دائماً أن الكوكي يرسل للمتصفح، فلا يمكن قراءته من مصفوفة الطلب الحالي.",
    notes_list=["سبب وحل headers already sent", "فهم تأخر ظهور الكوكي للطلب التالي", "ضرورة كتابة exit بعد header Location"]
)

# ==========================================
# Slide 23: Section Divider: Homework & Projects
# ==========================================
make_slide(
    index=22,
    title="المشاريع والتطبيقات العملية",
    eyebrow="التطبيق العملي",
    slide_title="المشاريع والتطبيقات العملية (الواجبات)",
    slide_text="حان وقت ترسيخ مهاراتك من خلال 3 واجبات عملية متدرجة تبني بها أنظمة حقيقية:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">واجب 1 (سهل): حفظ تفضيل السمة واللغة بالكوكي</span>
        <span class="pill-badge">واجب 2 (متوسط): نظام مصادقة كامل مع لوحة تحكم محمية</span>
        <span class="pill-badge">واجب 3 (متقدم): متجر إلكتروني وسلة تسوق مع رسائل Flash</span>
      </div>''',
    notes_title="فاصل الواجبات والتطبيقات",
    notes_script="الواجبات اليوم تمثل مشاريع ويب حقيقية: الأول للكوكيز، الثاني لجدار الحماية والمصادقة، والثالث يجمع السلة ورسائل الفلاش في تطبيق متكامل.",
    notes_list=["واجب 1: كوكيز وتفضيلات", "واجب 2: جلسات ومصادقة", "واجب 3: سلة متجر ورسائل Flash"],
    is_divider=True
)

# ==========================================
# Slide 24: Homework 1: Theme & Language Cookie
# ==========================================
make_slide(
    index=23,
    title="واجب 1: حفظ تفضيل السمة واللغة بالكوكي",
    eyebrow="الواجبات العملية &middot; 1 (سهل)",
    slide_title="واجب 1: حفظ إعدادات المظهر واللغة (Cookie Preference)",
    slide_text="بناء صفحة إعدادات تتيح للزائر اختيار مظهر الموقع واللغة المفضلة وحفظها لمدة شهر:",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في الواجب 1</div>
          <ul class="bullet-list" style="margin-top:0.4rem;">
            <li>أنشئ نموذجاً يحتوي على قائمتين منسدلتين: السمة (Dark / Light) واللغة (العربية / English).</li>
            <li>عند إرسال النموذج، احفظ الاختيارات في كوكيز باسم <code>user_theme</code> و <code>user_lang</code> لمدة 30 يوماً مع تفعيل <code>httponly</code>.</li>
            <li>في الصفحة الرئيسية، اقرأ الكوكيز وطبق فئة CSS المناسبة <code>&lt;body class="dark"&gt;</code> وغير لغة نصوص الترحيب.</li>
            <li>وفّر زراً لإعادة ضبط الإعدادات يحذف الكوكيز بتعيين تاريخ ماضٍ.</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">hw1_settings.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// 1. استقبال الاختيارات وتعيين الكوكيز</span>
<span class="tok-kw">if</span> (<span class="tok-var">$_SERVER</span>[<span class="tok-str">'REQUEST_METHOD'</span>] === <span class="tok-str">'POST'</span>) {
    <span class="tok-var">$theme</span> = <span class="tok-var">$_POST</span>[<span class="tok-str">'theme'</span>] ?? <span class="tok-str">'light'</span>;
    <span class="tok-fn">setcookie</span>(<span class="tok-str">'user_theme'</span>, <span class="tok-var">$theme</span>, <span class="tok-fn">time</span>() + (<span class="tok-num">86400</span> * <span class="tok-num">30</span>), <span class="tok-str">'/'</span>);
    <span class="tok-fn">header</span>(<span class="tok-str">"Location: index.php"</span>);
    <span class="tok-kw">exit</span>;
}

<span class="tok-cmt">// 2. قراءة الكوكي في العرض</span>
<span class="tok-var">$currentTheme</span> = <span class="tok-var">$_COOKIE</span>[<span class="tok-str">'user_theme'</span>] ?? <span class="tok-str">'light'</span>;</pre>
        </div>
      </div>''',
    notes_title="واجب 1: حفظ تفضيل السمة واللغة",
    notes_script="تطبيق كلاسيكي على الكوكيز؛ يوضح كيف يتذكر المتصفح شكل الموقع المناسب للمستخدم حتى لو أغلق جهازه وعاد بعد أسابيع.",
    notes_list=["حفظ الإعدادات بـ setcookie", "قراءة القيم وتطبيق CSS المناسب", "إتاحة زر حذف الكوكي"]
)

# ==========================================
# Slide 25: Homework 2: Protected Dashboard & Auth
# ==========================================
make_slide(
    index=24,
    title="واجب 2: لوحة تحكم محمية ونظام مصادقة كامل",
    eyebrow="الواجبات العملية &middot; 2 (متوسط)",
    slide_title="واجب 2: نظام تسجيل دخول ولوحة تحكم محمية",
    slide_text="بناء نظام متكامل لتسجيل الدخول والخروج مع حماية الصفحات وتجديد المعرف الأمني:",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في الواجب 2</div>
          <ul class="bullet-list" style="margin-top:0.3rem;">
            <li>صفحة <code>login.php</code>: نموذج دخول يفحص (اسم المستخدم وكلمة المرور) مقابل بيانات مسجلة.</li>
            <li>عند نجاح الدخول: استدعِ <code>session_regenerate_id(true)</code> وخزن الاسم وحالة الدخول في <code>$_SESSION</code>.</li>
            <li>صفحة <code>dashboard.php</code>: محمية بالكامل؛ إذا دخلها زائر بدون تسجيل يتم طرده لـ <code>login.php</code>.</li>
            <li>صفحة <code>logout.php</code>: تفرغ المصفوفة، تمسح كوكي الجلسة، وتدمر الجلسة بالكامل مع التحويل لصفحة الدخول.</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">hw2_auth.php</span>
          </div>
          <pre class="code-body"><span class="tok-fn">session_start</span>();

<span class="tok-cmt">// فحص الدخول الآمن</span>
<span class="tok-kw">if</span> (<span class="tok-var">$user_is_valid</span>) {
    <span class="tok-fn">session_regenerate_id</span>(<span class="tok-kw">true</span>);
    <span class="tok-var">$_SESSION</span>[<span class="tok-str">'logged_in'</span>] = <span class="tok-kw">true</span>;
    <span class="tok-var">$_SESSION</span>[<span class="tok-str">'user'</span>]      = <span class="tok-var">$username</span>;
    <span class="tok-fn">header</span>(<span class="tok-str">"Location: dashboard.php"</span>);
    <span class="tok-kw">exit</span>;
}</pre>
        </div>
      </div>''',
    notes_title="واجب 2: نظام المصادقة المحمي",
    notes_script="هذا الواجب هو المشروع الأكثر طلباً في مشاريع التخرج ومقابلات العمل: بوابة دخول آمنة مع لوحة تحكم محمية وجدار حماية.",
    notes_list=["تطبيق جدار الحماية Auth Guard", "استخدام session_regenerate_id", "برمجة تسجيل الخروج الكامل"]
)

# ==========================================
# Slide 26: Homework 3: Full Shopping Cart & Flash Messages
# ==========================================
make_slide(
    index=25,
    title="واجب 3: متجر إلكتروني وسلة تسوق مع Flash Messages",
    eyebrow="الواجبات العملية &middot; 3 (متقدم)",
    slide_title="واجب 3: متجر مصغر متكامل (Cart & Flash Messages)",
    slide_text="مشروع تطبيقي يجمع كل مفاهيم المحاضرة: إدارة السلة، رسائل الفلاش، وحفظ المظهر بكوكي:",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في الواجب 3</div>
          <ul class="bullet-list" style="margin-top:0.3rem;">
            <li>قائمة منتجات بـ 3 أصناف وزر «إضافة للسلة».</li>
            <li>عند إضافة منتج: خزنه في <code>$_SESSION['cart']</code> مع زيادة الكمية، وضع رسالة فلاش: «تمت إضافة X للسلة بنجاح!».</li>
            <li>صفحة السلة: تعرض جدول المنتجات، الكميات، وإجمالي الحساب، مع زر حذف منتج وزر تفريغ السلة.</li>
            <li>احفظ تفضيل سمة الموقع (Dark/Light) في كوكي ليبقى مظهر المتجر ثابتاً للمستخدم.</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">hw3_store.php</span>
          </div>
          <pre class="code-body"><span class="tok-fn">session_start</span>();

<span class="tok-cmt">// إضافة وتوجيه مع Flash Message</span>
<span class="tok-kw">if</span> (<span class="tok-kw">isset</span>(<span class="tok-var">$_GET</span>[<span class="tok-str">'add'</span>])) {
    <span class="tok-var">$id</span> = <span class="tok-var">$_GET</span>[<span class="tok-str">'add'</span>];
    <span class="tok-var">$_SESSION</span>[<span class="tok-str">'cart'</span>][<span class="tok-var">$id</span>] = (<span class="tok-var">$_SESSION</span>[<span class="tok-str">'cart'</span>][<span class="tok-var">$id</span>] ?? <span class="tok-num">0</span>) + <span class="tok-num">1</span>;
    <span class="tok-var">$_SESSION</span>[<span class="tok-str">'flash'</span>] = <span class="tok-str">"تمت إضافة المنتج بنجاح! 🛒"</span>;
    <span class="tok-fn">header</span>(<span class="tok-str">"Location: cart_view.php"</span>);
    <span class="tok-kw">exit</span>;
}</pre>
        </div>
      </div>''',
    notes_title="واجب 3: متجر إلكتروني متكامل",
    notes_script="المشروع التتويجي للمحاضرة؛ يدمج الجلسات لإدارة السلة والرسائل المؤقتة، مع الكوكيز للمظهر العام.",
    notes_list=["إدارة مصفوفة السلة المركبة بالجلسة", "تطبيق رسائل Flash التفاعلية", "تكامل الكوكيز والجلسات في تطبيق واحد"]
)

# ==========================================
# Slide 27: Section Divider: Review Time
# ==========================================
make_slide(
    index=26,
    title="وقت المراجعة والنقاش التقني",
    eyebrow="نقاش ومراجعة",
    slide_title="وقت المراجعة والتأمل التقني",
    slide_text="قبل أن نختتم، اختبر استيعابك للمفاهيم الهندسية التي ناقشناها اليوم:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">لو قام المستخدم بتعطيل الكوكيز في متصفحه تماماً، هل ستعمل الـ Sessions الافتراضية؟ ولماذا؟</span>
        <span class="pill-badge">لماذا لا تظهر قيمة الكوكي المنشأ في نفس الطلب عبر $_COOKIE؟</span>
        <span class="pill-badge">ما هو الغرض الأمني الجوهري من استدعاء session_regenerate_id(true) عند تسجيل الدخول؟</span>
      </div>''',
    notes_title="فاصل المراجعة التقنية",
    notes_script="أسئلة نقاشية عميقة تضمن استيعاب الطلاب للعلاقة بين كوكي PHPSESSID وملف الجلسة على الخادم، وتؤكد على المفاهيم الأمنية.",
    notes_list=["سؤال تأثير تعطيل الكوكيز على الجلسات", "سؤال توقيت ظهور الكوكيز في $_COOKIE", "سؤال حماية Session Fixation"]
)

# ==========================================
# Slide 28: Summary: What We Learned Today
# ==========================================
make_slide(
    index=27,
    title="اللي اتعلمناه النهاردة",
    eyebrow="ملخص المحاضرة 09",
    slide_title="اللي اتعلمناه النهاردة في المحاضرة 09",
    slide_text="خلاصة أهم 4 محاور تم إتقانها اليوم في إدارة حالة تطبيقات الويب في PHP:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">طبيعة الويب عديم الحالة</div>
            <div class="topic-desc">فهم سلوك HTTP Stateless وضرورة ربط الطلبات ببطاقة هوية للمستخدم</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">الكوكيز (Cookies)</div>
            <div class="topic-desc">تخزين المتصفح، دالة setcookie()، ضوابط الأمان HttpOnly، وحظر تخزين الأسرار</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">الجلسات (Sessions)</div>
            <div class="topic-desc">أمان الخادم، معرف PHPSESSID، مصفوفة $_SESSION، والتحصين بـ session_regenerate_id</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">التطبيقات الحية</div>
            <div class="topic-desc">بناء جدار المصادقة Auth Guard، ميزة تذكرني، سلة المشتريات، ورسائل الفلاش المؤقتة</div>
          </div>
        </div>
      </div>''',
    notes_title="ملخص المحاضرة 09",
    notes_script="اليوم انتقلتم من كتابة نصوص وأكواد برمجية عادية إلى بناء تطبيقات ويب حقيقية تحتفظ بالدخول والمشتريات وتوفر تجربة مستخدم متكاملة وآمنة.",
    notes_list=["فهم Stateless HTTP", "التمكن من Cookies", "التمكن من Sessions والأمان", "بناء التطبيقات الحقيقية"]
)

# ==========================================
# Slide 29: Conclusion & Thank You
# ==========================================
make_slide(
    index=28,
    title="شكرًا لكم &mdash; نهاية المحاضرة 09",
    eyebrow="الخاتمة &middot; المحاضرة 09",
    slide_title="شكرًا لكم! أبدعتم في إتقان إدارة الحالة",
    slide_text="اليوم امتلكتم مفتاح بناء التطبيقات التفاعلية الحقيقية. حلّوا الواجبات الثلاثة وشاركونا إبداعاتكم في المتجر ولوحة التحكم!",
    body_content='''<div class="badge-row">
        <span class="pill-badge">Stateless HTTP &amp; State</span>
        <span class="pill-badge">Cookies: setcookie &amp; HttpOnly</span>
        <span class="pill-badge">Sessions: $_SESSION &amp; Security</span>
        <span class="pill-badge">المحاضرة القادمة: قواعد البيانات ومحرك MySQL 🚀</span>
      </div>''',
    notes_title="خاتمة المحاضرة 09",
    notes_script="شكراً لكم على تركيزكم وحماسكم. في المحاضرة العاشرة القادمة سننتقل للخطوة الكبرى التالية: قواعد البيانات ومحرك MySQL وتخزين ملايين البيانات بشكل دائم. إلى اللقاء!",
    notes_list=["شكر وتشجيع الطلاب", "الحث على حل المشاريع الثلاثة", "التشويق للمحاضرة العاشرة: MySQL"],
    is_divider=True
)

print("All 29 slides generated successfully for Lecture 09!")
