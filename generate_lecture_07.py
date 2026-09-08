# -*- coding: utf-8 -*-
from build_lecture_07 import make_slide

# Slide 01: Cover
make_slide(
    index=0,
    title="التعامل مع نماذج HTML في PHP",
    eyebrow="أساسيات PHP &middot; المحاضرة 07",
    slide_title="التعامل مع نماذج HTML (HTML Forms)",
    slide_text="هنتعلم إزاي نبني نماذج إدخال احترافية ونربطها مع PHP &mdash; من الفروق الجوهرية بين GET و POST، للتعامل مع الـ Superglobals ($_POST و $_GET و $_SERVER)، وصولاً للتحقق والتعقيم الأمني لمنع هجمات XSS و SQL Injection.",
    body_content='''<div class="cover-mark">
        <div><div class="num">04</div><div class="lbl">محاور رئيسية</div></div>
        <div><div class="num">03</div><div class="lbl">واجبات عملية</div></div>
        <div><div class="num">~60 د</div><div class="lbl">المدة التقديرية</div></div>
      </div>''',
    notes_title="المحاضرة 07: التعامل مع نماذج HTML في PHP",
    notes_script="أهلاً بكم في المحاضرة السابعة من كورس PHP. موضوع اليوم هو قلب أي موقع ديناميكي: النماذج (Forms). من خلالها يستقبل السيرفر بيانات المستخدمين ويعالجها بأمان.",
    notes_list=["بناء عناصر ونماذج HTML", "مقارنة شاملة بين GET و POST", "الـ Superglobals", "التحقق والتعقيم الأمني لمكافحة XSS و SQLi"],
    is_cover=True
)

# Slide 02: Roadmap
make_slide(
    index=1,
    title="خريطة المحاضرة 07",
    eyebrow="نظرة عامة &middot; محتويات المحاضرة",
    slide_title="خريطة المحاضرة 07",
    slide_text="أربعة محاور رئيسية سنتعلمها اليوم لربط نماذج HTML بلغة PHP ومعالجتها بأعلى درجات الأمان:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">نماذج HTML وعناصر الإدخال</div>
            <div class="topic-desc">عناصر Form، خصائص action و method و name و enctype</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">مقارنة شاملة: GET مقابل POST</div>
            <div class="topic-desc">طرق الإرسال، حدود الروابط، التخزين المؤقت، والأمان</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">الـ Superglobals</div>
            <div class="topic-desc">التعامل مع $_POST و $_GET و $_SERVER وفحص isset و empty</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">التحقق والتعقيم الأمني (Security)</div>
            <div class="topic-desc">دوال filter_var و htmlspecialchars والحماية من XSS و SQLi</div>
          </div>
        </div>
      </div>''',
    notes_title="خريطة المحاضرة 07",
    notes_script="هذه هي محاورنا الأربعة. سنبدأ بالواجهة الأمامية وتجهيز الفورم، ثم الفروق في بروتوكول HTTP بين GET و POST، ثم كيفية قراءة البيانات داخل PHP، وأخيراً أهم درس أمني في حياة المطور: تنظيف وفحص المدخلات.",
    notes_list=["نماذج HTML", "GET vs POST", "Superglobals", "Validation & Sanitization"]
)

# Slide 03: HTML Forms Overview & Attributes
make_slide(
    index=2,
    title="خصائص الوسم form الأساسية",
    eyebrow="نماذج HTML &middot; 1",
    slide_title="خصائص الوسم &lt;form&gt; الأساسية",
    slide_text="النموذج (Form) هو الحاوية الرئيسية التي تجمع حقول الإدخال لتغليفها وإرسالها إلى خادم الويب لمعالجتها.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>خاصية <code>action</code>: رابط أو مسار ملف PHP الذي سيعالج البيانات المجمعة</li>
          <li>خاصية <code>method</code>: بروتوكول الإرسال (إما <code>GET</code> أو <code>POST</code>)</li>
          <li>خاصية <code>name</code>: اسم النموذج لتمييزه عند الحاجة</li>
          <li>خاصية <code>enctype</code>: تشفير البيانات، إجبارية عند رفع الملفات: <code>multipart/form-data</code></li>
          <li>زر الإرسال <code>&lt;button type="submit"&gt;</code>: الزناد الذي يطلق عملية الإرسال</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">form_structure.html</span>
          </div>
          <pre class="code-body">&lt;<span class="tok-kw">form</span> <span class="tok-fn">action</span>=<span class="tok-str">"process.php"</span> <span class="tok-fn">method</span>=<span class="tok-str">"POST"</span>&gt;
    &lt;<span class="tok-kw">label</span> <span class="tok-fn">for</span>=<span class="tok-str">"user"</span>&gt;اسم المستخدم:&lt;/<span class="tok-kw">label</span>&gt;
    &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"text"</span> <span class="tok-fn">id</span>=<span class="tok-str">"user"</span> <span class="tok-fn">name</span>=<span class="tok-str">"username"</span>&gt;
    
    &lt;<span class="tok-kw">button</span> <span class="tok-fn">type</span>=<span class="tok-str">"submit"</span>&gt;إرسال&lt;/<span class="tok-kw">button</span>&gt;
&lt;/<span class="tok-kw">form</span>&gt;</pre>
        </div>
      </div>''',
    notes_title="خصائص وسم form",
    notes_script="أي فورم يحتاج وجهة يروح لها (action) وطريقة يوصل بها (method). إذا تركت الـ action فارغة، يرسل الفورم لنفس الصفحة الحالية.",
    notes_list=["خصائص action و method", "خاصية enctype لرفع الملفات", "ضرورة زر submit"]
)

# Slide 04: Basic Elements & Labels
make_slide(
    index=3,
    title="عناصر الإدخال الأساسية ووسم label",
    eyebrow="نماذج HTML &middot; 1",
    slide_title="عناصر الإدخال الأساسية ووسم &lt;label&gt;",
    slide_text="تتنوع حقول الإدخال لتلائم طبيعة البيانات، مع ضرورة ربط كل حقل بـ label لتحسين تجربة المستخدم وسهولة الوصول (Accessibility).",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>&lt;input type="text|email|password|number"&gt;</code>: حقول أحادية السطر</li>
          <li><code>&lt;textarea name="..."&gt;</code>: للنصوص الطويلة والمتعددة الأسطر كالرسائل والتعليقات</li>
          <li><code>&lt;select name="..."&gt;</code>: القوائم المنسدلة لاختيار عنصر أو أكثر بـ <code>&lt;option&gt;</code></li>
          <li>الوسم <code>&lt;label for="fieldId"&gt;</code>: يربط العنوان بالحقل برمجياً ويسهل النقر باللمس والفأرة</li>
          <li><strong>خاصية name إجبارية:</strong> بدونها لن تستطيع PHP التعرف على الحقل إطلاقاً!</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">elements.html</span>
          </div>
          <pre class="code-body">&lt;<span class="tok-kw">label</span> <span class="tok-fn">for</span>=<span class="tok-str">"bio"</span>&gt;نبذة عنك:&lt;/<span class="tok-kw">label</span>&gt;
&lt;<span class="tok-kw">textarea</span> <span class="tok-fn">id</span>=<span class="tok-str">"bio"</span> <span class="tok-fn">name</span>=<span class="tok-str">"user_bio"</span>&gt;&lt;/<span class="tok-kw">textarea</span>&gt;

&lt;<span class="tok-kw">label</span> <span class="tok-fn">for</span>=<span class="tok-str">"country"</span>&gt;الدولة:&lt;/<span class="tok-kw">label</span>&gt;
&lt;<span class="tok-kw">select</span> <span class="tok-fn">id</span>=<span class="tok-str">"country"</span> <span class="tok-fn">name</span>=<span class="tok-str">"country"</span>&gt;
    &lt;<span class="tok-kw">option</span> <span class="tok-fn">value</span>=<span class="tok-str">"EG"</span>&gt;مصر&lt;/<span class="tok-kw">option</span>&gt;
    &lt;<span class="tok-kw">option</span> <span class="tok-fn">value</span>=<span class="tok-str">"SA"</span>&gt;السعودية&lt;/<span class="tok-kw">option</span>&gt;
&lt;/<span class="tok-kw">select</span>&gt;</pre>
        </div>
      </div>''',
    notes_title="عناصر الإدخال الأساسية و label",
    notes_script="مهم نؤكد للطلاب: id يفيد التصميم وربط الـ label و JS، لكن name هو الوحيد اللي PHP بتبحث عنه في السيرفر.",
    notes_list=["حقول الإدخال المختلفة", "وسم textarea و select", "أهمية label لسهولة الوصول Accessibility", "خاصية name كمعرف لـ PHP"]
)

# Slide 05: Checkboxes, Radios, Files & Hidden Fields
make_slide(
    index=4,
    title="حقول الاختيار، الملفات، والحقول المخفية",
    eyebrow="نماذج HTML &middot; 1",
    slide_title="حقول الاختيار، الملفات، والحقول المخفية",
    slide_text="أنواع إضافية توفر خيارات متعددة في جمع البيانات، رفع الملفات، وتمرير البيانات الخلفية بأمان.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>type="radio"</code>: اختيار أحادي فقط؛ تشترك جميع الخيارات في نفس الـ <code>name</code></li>
          <li><code>type="checkbox"</code>: اختيار متعدد؛ في PHP نضع أقواس مصفوفة: <code>skills[]</code></li>
          <li><code>type="file"</code>: لرفع الملفات (يتطلب حتماً <code>enctype="multipart/form-data"</code>)</li>
          <li><code>type="hidden"</code>: حقل خفي لتمرير معرّف (ID) أو رمز أمان CSRF Token دون إظهاره للمستخدم</li>
          <li>سمات التحقق في HTML5: <code>required</code>، <code>pattern</code>، <code>min</code>، <code>max</code></li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">advanced_inputs.html</span>
          </div>
          <pre class="code-body">&lt;<span class="tok-cmt">&lt;!-- Radio: قيمة واحدة فقط --&gt;</span>
&lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"radio"</span> <span class="tok-fn">name</span>=<span class="tok-str">"gender"</span> <span class="tok-fn">value</span>=<span class="tok-str">"m"</span>&gt; ذكر
&lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"radio"</span> <span class="tok-fn">name</span>=<span class="tok-str">"gender"</span> <span class="tok-fn">value</span>=<span class="tok-str">"f"</span>&gt; أنثى

&lt;<span class="tok-cmt">&lt;!-- Checkbox: مصفوفة مهارات --&gt;</span>
&lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"checkbox"</span> <span class="tok-fn">name</span>=<span class="tok-str">"skills[]"</span> <span class="tok-fn">value</span>=<span class="tok-str">"php"</span>&gt; PHP
&lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"checkbox"</span> <span class="tok-fn">name</span>=<span class="tok-str">"skills[]"</span> <span class="tok-fn">value</span>=<span class="tok-str">"sql"</span>&gt; SQL

&lt;<span class="tok-cmt">&lt;!-- حقل مخفي --&gt;</span>
&lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"hidden"</span> <span class="tok-fn">name</span>=<span class="tok-str">"post_id"</span> <span class="tok-fn">value</span>=<span class="tok-str">"42"</span>&gt;</pre>
        </div>
      </div>''',
    notes_title="أنواع مدخلات متقدمة",
    notes_script="عند عمل checkbox متعدد، لو نسيت القوسين [] في الـ name، هتستلم PHP آخر خيار اختاره المستخدم فقط وتهمل الباقي!",
    notes_list=["radio يشترك في نفس name", "checkbox يحتاج skills[] لاستلام مصفوفة", "حقل hidden لتمرير بيانات السيرفر"]
)

# Slide 06: Example 1: Building a Simple Contact Form
make_slide(
    index=5,
    title="مثال 1: نموذج تواصل بسيط",
    eyebrow="نماذج HTML &middot; مثال 1",
    slide_title="مثال 1: نموذج تواصل بسيط (Contact Form)",
    slide_text="بناء استمارة اتصال قياسية تستقبل اسم المستخدم، بريده الإلكتروني، ورسالته بأسلوب منظم.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">الهدف</div>
          <p>بناء استمارة تواصل بـ POST ترسل إلى <code>contact.php</code>، تحتوي على حقول الاسم والبريد ونص الرسالة مع سمات required وتسميات واضحة.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">contact.html</span>
          </div>
          <pre class="code-body">&lt;<span class="tok-kw">form</span> <span class="tok-fn">action</span>=<span class="tok-str">"contact.php"</span> <span class="tok-fn">method</span>=<span class="tok-str">"POST"</span>&gt;
  &lt;<span class="tok-kw">label</span> <span class="tok-fn">for</span>=<span class="tok-str">"name"</span>&gt;الاسم:&lt;/<span class="tok-kw">label</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"text"</span> <span class="tok-fn">id</span>=<span class="tok-str">"name"</span> <span class="tok-fn">name</span>=<span class="tok-str">"sender_name"</span> <span class="tok-fn">required</span>&gt;

  &lt;<span class="tok-kw">label</span> <span class="tok-fn">for</span>=<span class="tok-str">"email"</span>&gt;البريد:&lt;/<span class="tok-kw">label</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"email"</span> <span class="tok-fn">id</span>=<span class="tok-str">"email"</span> <span class="tok-fn">name</span>=<span class="tok-str">"sender_email"</span> <span class="tok-fn">required</span>&gt;

  &lt;<span class="tok-kw">label</span> <span class="tok-fn">for</span>=<span class="tok-str">"msg"</span>&gt;الرسالة:&lt;/<span class="tok-kw">label</span>&gt;
  &lt;<span class="tok-kw">textarea</span> <span class="tok-fn">id</span>=<span class="tok-str">"msg"</span> <span class="tok-fn">name</span>=<span class="tok-str">"message"</span> <span class="tok-fn">required</span>&gt;&lt;/<span class="tok-kw">textarea</span>&gt;

  &lt;<span class="tok-kw">button</span> <span class="tok-fn">type</span>=<span class="tok-str">"submit"</span>&gt;إرسال الرسالة&lt;/<span class="tok-kw">button</span>&gt;
&lt;/<span class="tok-kw">form</span>&gt;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/contact.html</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.5rem;font-size:0.85rem;">
الاسم: [ عمر الشريف ]
البريد: [ omar@example.com ]
الرسالة: [ استفسار بخصوص الدورة ]
[ زر: إرسال الرسالة 📨 ]
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال نموذج تواصل بسيط",
    notes_script="هذا النموذج الأساسي يمثل 80% من النماذج التي يحتاجها أي موقع للاتصال بالدعم الفني أو إرسال استفسار.",
    notes_list=["حقول name و email و message", "استخدام method=POST لحماية الرسالة", "استخدام required للتحقق المبدئي"]
)

# Slide 07: Example 2: Registration Form with Multiple Types
make_slide(
    index=6,
    title="مثال 2: استمارة تسجيل متكاملة",
    eyebrow="نماذج HTML &middot; مثال 2",
    slide_title="مثال 2: استمارة تسجيل بأنواع متعددة",
    slide_text="بناء استمارة تسجيل عضوية تشمل حقول النصوص، كلمة المرور، القوائم المنسدلة، وحقول الاختيار.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">الهدف</div>
          <p>إنشاء نموذج تسجيل يجمع: اسم المستخدم، البريد، كلمة المرور، الدولة عبر <code>select</code>، وتأكيد الموافقة على الشروط عبر <code>checkbox</code>.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">register.html</span>
          </div>
          <pre class="code-body">&lt;<span class="tok-kw">form</span> <span class="tok-fn">action</span>=<span class="tok-str">"register.php"</span> <span class="tok-fn">method</span>=<span class="tok-str">"POST"</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"text"</span> <span class="tok-fn">name</span>=<span class="tok-str">"user"</span> <span class="tok-fn">placeholder</span>=<span class="tok-str">"الاسم"</span> <span class="tok-fn">required</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"email"</span> <span class="tok-fn">name</span>=<span class="tok-str">"email"</span> <span class="tok-fn">placeholder</span>=<span class="tok-str">"البريد"</span> <span class="tok-fn">required</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"password"</span> <span class="tok-fn">name</span>=<span class="tok-str">"pass"</span> <span class="tok-fn">placeholder</span>=<span class="tok-str">"كلمة المرور"</span> <span class="tok-fn">required</span>&gt;
  
  &lt;<span class="tok-kw">select</span> <span class="tok-fn">name</span>=<span class="tok-str">"country"</span>&gt;
    &lt;<span class="tok-kw">option</span> <span class="tok-fn">value</span>=<span class="tok-str">"EG"</span>&gt;مصر&lt;/<span class="tok-kw">option</span>&gt;
    &lt;<span class="tok-kw">option</span> <span class="tok-fn">value</span>=<span class="tok-str">"SA"</span>&gt;السعودية&lt;/<span class="tok-kw">option</span>&gt;
  &lt;/<span class="tok-kw">select</span>&gt;
  
  &lt;<span class="tok-kw">label</span>&gt;&lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"checkbox"</span> <span class="tok-fn">name</span>=<span class="tok-str">"agree"</span> <span class="tok-fn">value</span>=<span class="tok-str">"1"</span> <span class="tok-fn">required</span>&gt; أوافق على الشروط&lt;/<span class="tok-kw">label</span>&gt;
  &lt;<span class="tok-kw">button</span> <span class="tok-fn">type</span>=<span class="tok-str">"submit"</span>&gt;تسجيل حساب&lt;/<span class="tok-kw">button</span>&gt;
&lt;/<span class="tok-kw">form</span>&gt;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/register.html</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.5rem;font-size:0.82rem;">
[ الاسم: أحمد محمود ]
[ البريد: ahmed@mail.com ]
[ كلمة المرور: &bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull; ]
[ الدولة: مصر ▼ ]
☑ أوافق على الشروط
[ زر: تسجيل حساب 🚀 ]
            </div>
          </div>
        </div>
      </div>''',
    notes_title="استمارة تسجيل متكاملة",
    notes_script="جمعنا هنا أنواع مختلفة من المدخلات لاختبار كيفية معالجة كل نوع داخل ملف register.php لاحقاً.",
    notes_list=["حقول الإدخال المتنوعة", "قائمة منسدلة للدول", "مربع تأكيد الشروط checkbox"]
)

# Slide 08: Common Mistakes in HTML Forms
make_slide(
    index=7,
    title="أخطاء شائعة في نماذج HTML",
    eyebrow="احذر هذه الأخطاء &middot; 1",
    slide_title="أخطاء شائعة في نماذج HTML",
    slide_text="ثلاثة أخطاء رئيسية تفسد عمل النموذج قبل أن تصل بياناته إلى كود PHP:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ نسيان خاصية name على الحقول</div>
          <ul class="bullet-list">
            <li>الحقل الذي لا يملك <code>name</code> يتم تجاهله تماماً عند الإرسال!</li>
            <li>كود خاطئ: <code>&lt;input type="text" id="email"&gt;</code></li>
            <li>PHP لن تجد شيئاً في <code>$_POST['email']</code> إطلاقاً!</li>
            <li><strong>التصحيح:</strong> ضع دائماً: <code>name="email"</code></li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ نسيان enctype أو إهمال method</div>
          <ul class="bullet-list">
            <li>عند رفع ملف بـ <code>&lt;input type="file"&gt;</code> بدون <code>enctype="multipart/form-data"</code>، سيصل اسم الملف كنص عادي وتفشل مصفوفة <code>$_FILES</code>!</li>
            <li>إذا نسيت كتابة <code>method</code>، سيتحول النموذج تلقائياً إلى <code>GET</code> وتنكشف البيانات في شريط العنوان!</li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في نماذج HTML",
    notes_script="أشهر خطأ يسأل عنه الطلاب في البداية: الكود شغال في HTML بس PHP مش شايفة القيمة! والسبب دائماً نسيان خاصية name.",
    notes_list=["نسيان name يمنع إرسال الحقل لـ PHP", "نسيان enctype يمنع رفع الملفات", "إهمال method يحول الفورم لـ GET افتراضياً"]
)

# Slide 09: Understanding GET Method
make_slide(
    index=8,
    title="طريقة الإرسال GET",
    eyebrow="طرق الإرسال &middot; 2",
    slide_title="متى ولماذا نستخدم طريقة GET؟",
    slide_text="طريقة <code>GET</code> تُرسل البيانات كجزء علني ومكشوف من الرابط (Query String) بعد علامة الاستفهام <code>?</code>.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>تظهر البيانات مباشرة في شريط عنوان المتصفح: <code>search.php?q=php&amp;page=2</code></li>
          <li>سهولة حفظ الرابط في المفضلة (Bookmarkable) ومشاركته مع الآخرين</li>
          <li>تُخزّن مؤقتاً في المتصفح وسيرفرات الكاش (Cachable) لتحسين السرعة</li>
          <li><strong>مبدأ الـ Idempotency:</strong> استدعاؤها لا يغير حالة السيرفر (قراءة فقط)</li>
          <li>محدودة الطول: أقصى طول مسموح به في معظم المتصفحات هو <strong>~2048 حرفاً</strong></li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">get_example.html</span>
          </div>
          <pre class="code-body">&lt;<span class="tok-cmt">&lt;!-- نموذج بحث باستخدام GET --&gt;</span>
&lt;<span class="tok-kw">form</span> <span class="tok-fn">action</span>=<span class="tok-str">"search.php"</span> <span class="tok-fn">method</span>=<span class="tok-str">"GET"</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"text"</span> <span class="tok-fn">name</span>=<span class="tok-str">"q"</span> <span class="tok-fn">placeholder</span>=<span class="tok-str">"ابحث هنا..."</span>&gt;
  &lt;<span class="tok-kw">button</span> <span class="tok-fn">type</span>=<span class="tok-str">"submit"</span>&gt;بحث&lt;/<span class="tok-kw">button</span>&gt;
&lt;/<span class="tok-kw">form</span>&gt;

<span class="tok-cmt">&lt;!-- الرابط الناتج بعد الإرسال: --&gt;</span>
<span class="tok-cmt">&lt;!-- search.php?q=php+course --&gt;</span></pre>
        </div>
      </div>''',
    notes_title="طريقة GET واستخداماتها",
    notes_script="GET ممتازة لأي عملية استرجاع بيانات: زي محرك البحث، فلترة المنتجات حسب السعر، أو التنقل بين صفحات المقالات.",
    notes_list=["ظهور البيانات في الرابط", "سهولة المشاركة والمفضلة", "حدود طول الرابط 2048 حرف", "عدم مناسبتها للبيانات السرية"]
)

# Slide 10: Understanding POST Method
make_slide(
    index=9,
    title="طريقة الإرسال POST",
    eyebrow="طرق الإرسال &middot; 2",
    slide_title="متى ولماذا نستخدم طريقة POST؟",
    slide_text="طريقة <code>POST</code> تُرسل البيانات خفية داخل جسم طلب الـ HTTP (Request Body) دون إظهارها في شريط العنوان.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>البيانات محجوبة عن شريط العنوان وتاريخ المتصفح (Browser History)</li>
          <li>لا توجد قيود على حجم البيانات (مثالية لرفع الملفات والرسائل الضخمة)</li>
          <li>تُستخدم للعمليات التي تُغير حالة السيرفر (إنشاء حساب، حفظ، تعديل، حذف)</li>
          <li>المتصفح يحذر المستخدم إذا حاول عمل Refresh لتجنب تكرار الدفع أو الإرسال</li>
          <li><strong>إجبارية للبيانات الحساسة:</strong> كلمات المرور، تفاصيل البطاقات، وتعديل الحسابات</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">post_example.html</span>
          </div>
          <pre class="code-body">&lt;<span class="tok-cmt">&lt;!-- نموذج تسجيل دخول بـ POST --&gt;</span>
&lt;<span class="tok-kw">form</span> <span class="tok-fn">action</span>=<span class="tok-str">"login.php"</span> <span class="tok-fn">method</span>=<span class="tok-str">"POST"</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"email"</span> <span class="tok-fn">name</span>=<span class="tok-str">"email"</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"password"</span> <span class="tok-fn">name</span>=<span class="tok-str">"password"</span>&gt;
  &lt;<span class="tok-kw">button</span> <span class="tok-fn">type</span>=<span class="tok-str">"submit"</span>&gt;دخول&lt;/<span class="tok-kw">button</span>&gt;
&lt;/<span class="tok-kw">form</span>&gt;

<span class="tok-cmt">&lt;!-- الرابط يظل نظيفاً: login.php --&gt;</span></pre>
        </div>
      </div>''',
    notes_title="طريقة POST واستخداماتها",
    notes_script="POST تُستخدم عندما ننشئ شيئاً جديداً أو نرسل معلومات خاصة. البيانات لا تظهر في الرابط ولا في الـ History، ولها سعة ضخمة.",
    notes_list=["إرسال البيانات في Request Body", "سعة غير محدودة للبيانات والملفات", "مناسبة لتسجيل الدخول والعمليات الحساسة"]
)

# Slide 11: GET vs POST Detailed Comparison
make_slide(
    index=10,
    title="مقارنة جوهرية: GET مقابل POST",
    eyebrow="مقارنة شاملة &middot; 2",
    slide_title="مقارنة جوهرية: GET مقابل POST",
    slide_text="جدول الفروق الجوهرية التي تحكم اختيارك بين الطريقتين في مشاريع الويب الحقيقية:",
    body_content='''<div class="compare-card">
        <div class="compare-header">
          <span class="badge-echo" style="color:var(--accent);">طريقة GET</span>
          <span class="vs-badge">VS</span>
          <span class="badge-print" style="color:#a78bfa;">طريقة POST</span>
        </div>
        <div class="compare-rows">
          <div class="compare-row">
            <div class="compare-item">في شريط الرابط (Query String)</div>
            <div class="compare-feature">مكان الإرسال</div>
            <div class="compare-item">داخل جسم الطلب (Request Body)</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">مكشوفة ومرئية في الـ History</div>
            <div class="compare-feature">الخصوصية</div>
            <div class="compare-item">مخفية عن الرابط وتاريخ المتصفح</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">محدودة بـ ~2048 حرف فقط</div>
            <div class="compare-feature">سعة البيانات</div>
            <div class="compare-item">غير محدودة (حسب إعدادات السيرفر)</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">نعم &mdash; يمكن حفظها ومشاركتها</div>
            <div class="compare-feature">المفضلة والمشاركة</div>
            <div class="compare-item">لا &mdash; لا يمكن حفظ الرابط بالبيانات</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">تُخزن في الكاش لتحسين السرعة</div>
            <div class="compare-feature">التخزين (Caching)</div>
            <div class="compare-item">لا تُخزن في الكاش إطلاقاً</div>
          </div>
          <div class="compare-row">
            <div class="compare-item">محركات البحث، الفلترة، التصفح</div>
            <div class="compare-feature">الاستخدام الأنسب</div>
            <div class="compare-item">تسجيل الدخول، الدفع، التعديل</div>
          </div>
        </div>
      </div>''',
    notes_title="مقارنة تفصيلية بين GET و POST",
    notes_script="هذا الجدول هو السؤال الكلاسيكي في أي مقابلة عمل لمطور PHP. ركز على أن POST ليست مشفرة بذاتها ولكنها تخفي البيانات عن شريط الرابط وسجلات السيرفر.",
    notes_list=["الفروق الستة الجوهرية", "حجم البيانات والتخزين المؤقت", "الاستخدام المثالي لكل بروتوكول"]
)

# Slide 12: Example 1: GET for Search Form
make_slide(
    index=11,
    title="مثال 1: استخدام GET في البحث",
    eyebrow="طرق الإرسال &middot; مثال 1",
    slide_title="مثال 1: استخدام GET في شريط البحث",
    slide_text="استخدام طريقة GET لبناء شريط بحث يتيح للمستخدم مشاركة رابط نتائج البحث مع زملائه.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">الهدف</div>
          <p>بناء نموذج بحث بسيط يرسل كلمة البحث بواسطة <code>GET</code> إلى صفحة <code>search.php</code>، وملاحظة كيف تظهر في شريط العنوان.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">search_form.php</span>
          </div>
          <pre class="code-body">&lt;<span class="tok-kw">form</span> <span class="tok-fn">action</span>=<span class="tok-str">"search.php"</span> <span class="tok-fn">method</span>=<span class="tok-str">"GET"</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"text"</span> <span class="tok-fn">name</span>=<span class="tok-str">"keyword"</span> <span class="tok-fn">placeholder</span>=<span class="tok-str">"كلمة البحث..."</span>&gt;
  &lt;<span class="tok-kw">button</span> <span class="tok-fn">type</span>=<span class="tok-str">"submit"</span>&gt;بحث 🔍&lt;/<span class="tok-kw">button</span>&gt;
&lt;/<span class="tok-kw">form</span>&gt;

&lt;?<span class="tok-kw">php</span>
<span class="tok-kw">if</span> (<span class="tok-fn">isset</span>(<span class="tok-var">$_GET</span>[<span class="tok-str">'keyword'</span>])) {
    <span class="tok-kw">echo</span> <span class="tok-str">"نتائج البحث عن: "</span> . <span class="tok-var">$_GET</span>[<span class="tok-str">'keyword'</span>];
}
?&gt;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/search.php?keyword=laravel</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.6rem;">
[ مربع البحث: laravel ] [ بحث 🔍 ]
----------------------------------------
نتائج البحث عن: laravel
(يمكنك نسخ الرابط ومشاركته مباشرة!)
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال استخدام GET في البحث",
    notes_script="لاحظ كيف أن الرابط في شريط العنوان أصبح يحمل ?keyword=laravel، مما يجعل الصفحة قابلة للحفظ في المفضلة والمشاركة.",
    notes_list=["ظهور البارامتر في الرابط", "استلام القيمة عبر $_GET['keyword']", "ميزة المشاركة للروابط"]
)

# Slide 13: Example 2: POST for User Login
make_slide(
    index=12,
    title="مثال 2: استخدام POST في تسجيل الدخول",
    eyebrow="طرق الإرسال &middot; مثال 2",
    slide_title="مثال 2: استخدام POST في تسجيل الدخول",
    slide_text="استخدام طريقة POST لتأمين بيانات تسجيل الدخول ومنع تسرب كلمة المرور إلى شريط العنوان وسجلات الخادم.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">الهدف</div>
          <p>بناء شاشة تسجيل دخول تستقبل البريد وكلمة المرور عبر <code>POST</code>، والتحقق من استقبالها بالخادم دون كشفها في الرابط.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">login.php</span>
          </div>
          <pre class="code-body">&lt;<span class="tok-kw">form</span> <span class="tok-fn">action</span>=<span class="tok-str">"login.php"</span> <span class="tok-fn">method</span>=<span class="tok-str">"POST"</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"email"</span> <span class="tok-fn">name</span>=<span class="tok-str">"email"</span> <span class="tok-fn">placeholder</span>=<span class="tok-str">"البريد"</span>&gt;
  &lt;<span class="tok-kw">input</span> <span class="tok-fn">type</span>=<span class="tok-str">"password"</span> <span class="tok-fn">name</span>=<span class="tok-str">"pass"</span> <span class="tok-fn">placeholder</span>=<span class="tok-str">"السر"</span>&gt;
  &lt;<span class="tok-kw">button</span> <span class="tok-fn">type</span>=<span class="tok-str">"submit"</span>&gt;دخول&lt;/<span class="tok-kw">button</span>&gt;
&lt;/<span class="tok-kw">form</span>&gt;

&lt;?<span class="tok-kw">php</span>
<span class="tok-kw">if</span> (<span class="tok-var">$_SERVER</span>[<span class="tok-str">'REQUEST_METHOD'</span>] === <span class="tok-str">'POST'</span>) {
    <span class="tok-kw">echo</span> <span class="tok-str">"تم الاستلام بأمان لـ: "</span> . <span class="tok-var">$_POST</span>[<span class="tok-str">'email'</span>];
}
?&gt;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/login.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.6rem;">
[ البريد: user@logharitm.com ]
[ السر: &bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull; ] [ دخول ]
----------------------------------------
تم الاستلام بأمان لـ: user@logharitm.com
(الرابط نظيف تماماً ولم تظهر كلمة المرور!)
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال استخدام POST في تسجيل الدخول",
    notes_script="لاحظ كيف أن الرابط ظل localhost/login.php بدون أي علامات استفهام ولا بيانات، وحافظنا على سرية كلمة المرور.",
    notes_list=["حماية كلمة المرور من الظهور بالرابط", "فحص REQUEST_METHOD للتأكد من نوع الطلب", "استلام البيانات عبر $_POST"]
)

# Slide 14: Common Mistakes in GET vs POST
make_slide(
    index=13,
    title="أخطاء شائعة في GET و POST",
    eyebrow="احذر هذه الأخطاء &middot; 2",
    slide_title="أخطاء شائعة في GET و POST",
    slide_text="أخطاء كارثية قد تكلفك اختراق موقعك أو تعطيل تجربة تصفح المستخدمين:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ إرسال كلمات المرور عبر GET</div>
          <ul class="bullet-list">
            <li>إرسال كلمة المرور بـ GET يجعلها تظهر في شريط الرابط لأي شخص بجوارك!</li>
            <li>تُسجل الكلمة صريحة في <strong>Server Access Logs</strong> وسجل تصفح المتصفح</li>
            <li>لو ضغط المستخدم على رابط خارجي، تنتقل كلمة المرور في ترويسة <code>Referer</code>!</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ الاعتقاد بأن POST مشفرة بذاتها</div>
          <ul class="bullet-list">
            <li>طريقة POST <strong>لا تشفر البيانات</strong> على الشبكة إطلاقاً! هي فقط تخفيها عن الرابط</li>
            <li>البيانات تسير كنص صريح (Plaintext) ويمكن لأي متلصص اعتراضها بسهولة</li>
            <li><strong>الحل الحقيقي:</strong> استخدام بروتوكول <code>HTTPS (SSL/TLS)</code> لتشفير اتصال الموقع كاملاً</li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في طرق الإرسال",
    notes_script="نؤكد دائماً: POST ليست أماناً كاملاً، بل هي أمان ضد الظهور العرضي. الأمان الحقيقي على الشبكة لا يتحقق إلا بتفعيل HTTPS.",
    notes_list=["كارثة إرسال الباسورد في GET", "POST ليست بديلاً لشهادات التشفير HTTPS"]
)

# Slide 15: Introduction to PHP Superglobals
make_slide(
    index=14,
    title="المتغيرات الفائقة Superglobals",
    eyebrow="المصفوفات الفائقة &middot; 3",
    slide_title="المتغيرات الفائقة (Superglobals)",
    slide_text="المتغيرات الفائقة هي مصفوفات مترابطة (Associative Arrays) خاصة ومدمجة في PHP، متاحة تلقائياً في أي مكان دون قيود النطاق.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>متاحة في <strong>جميع النطاقات (Global &amp; Local)</strong> دون الحاجة لكتابة <code>global</code></li>
          <li>تبدأ دائماً بـ <code>$_</code> متبوعة بأحرف كبيرة (Uppercase)</li>
          <li>المفاتيح بداخلها تمثل قيمة خاصية <code>name</code> في حقول النموذج</li>
          <li>أهم المصفوفات الفائقة:
            <code>$_POST</code>، <code>$_GET</code>، <code>$_SERVER</code>، <code>$_FILES</code>، <code>$_SESSION</code>، <code>$_COOKIE</code>
          </li>
          <li>تُنشأ تلقائياً مع كل طلب HTTP وتُهيأ ببيانات المستخدم وبيئة الخادم</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">superglobals.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// تعمل داخل الدوال دون global!</span>
<span class="tok-kw">function</span> <span class="tok-fn">getCurrentUser</span>() {
    <span class="tok-kw">if</span> (<span class="tok-fn">isset</span>(<span class="tok-var">$_POST</span>[<span class="tok-str">'username'</span>])) {
        <span class="tok-kw">return</span> <span class="tok-var">$_POST</span>[<span class="tok-str">'username'</span>];
    }
    <span class="tok-kw">return</span> <span class="tok-str">"زائر"</span>;
}

<span class="tok-kw">echo</span> <span class="tok-fn">getCurrentUser</span>();</pre>
        </div>
      </div>''',
    notes_title="المتغيرات الفائقة Superglobals",
    notes_script="مفهوم Superglobal يعني أن هذه المتغيرات تكسر قواعد النطاق العادية، فهي متاحة أينما كنت داخل مشروع PHP.",
    notes_list=["مصفوفات جاهزة في PHP", "متاحة في كل النطاقات", "تعتمد على خاصية name للمفاتيح"]
)

# Slide 16: $_GET and $_POST with isset and empty
make_slide(
    index=15,
    title="التعامل مع GET و POST وفحص isset",
    eyebrow="المصفوفات الفائقة &middot; 3",
    slide_title="التعامل مع $_GET و $_POST وفحص isset()",
    slide_text="قبل قراءة أي عنصر من مصفوفات المدخلات، يجب التحقق من وجوده أولاً لتفادي رسائل التحذير والأخطاء البرمجية.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li>الوصول للقيمة باستخدام اسم الحقل كمفتاح: <code>$user = $_POST['user'];</code></li>
          <li><code>isset($var)</code>: تفحص هل المفتاح موجود بالفعل داخل المصفوفة وليس <code>null</code></li>
          <li><code>empty($var)</code>: تفحص هل القيمة فارغة (مثل <code>""</code> أو <code>0</code> أو مصفوفة فارغة)</li>
          <li>محاولة قراءة مفتاح غير موجود تؤدي لـ:
            <br><code>Warning: Undefined array key "..."</code>
          </li>
          <li>النمط القياسي الموصى به: <code>if (isset($_POST['submit'])) { ... }</code></li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">check_inputs.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// تحقق آمن من وجود القيمة وامتلائها</span>
<span class="tok-kw">if</span> (<span class="tok-fn">isset</span>(<span class="tok-var">$_POST</span>[<span class="tok-str">'email'</span>]) &amp;&amp; !<span class="tok-fn">empty</span>(<span class="tok-var">$_POST</span>[<span class="tok-str">'email'</span>])) {
    <span class="tok-var">$email</span> = <span class="tok-var">$_POST</span>[<span class="tok-str">'email'</span>];
    <span class="tok-kw">echo</span> <span class="tok-str">"البريد المدخل: "</span> . <span class="tok-var">$email</span>;
} <span class="tok-kw">else</span> {
    <span class="tok-kw">echo</span> <span class="tok-str">"يرجى إدخال البريد أولاً!"</span>;
}</pre>
        </div>
      </div>''',
    notes_title="التعامل مع المدخلات وفحص isset و empty",
    notes_script="وضح للطلاب الفرق: isset تفحص الوجود في الذاكرة، بينما empty تفحص المحتوى هل هو خالي أم يحتوي قيمة حقيقية.",
    notes_list=["تجنب خطأ Undefined array key", "الفرق بين isset و empty", "النمط السليم لفحص إرسال النموذج"]
)

# Slide 17: $_REQUEST & $_SERVER
make_slide(
    index=16,
    title="مصفوفة REQUEST ومصفوفة SERVER",
    eyebrow="المصفوفات الفائقة &middot; 3",
    slide_title="مصفوفة $_REQUEST ومصفوفة $_SERVER",
    slide_text="تجمع <code>$_REQUEST</code> بين مدخلات الروابط والفورم، بينما تكشف <code>$_SERVER</code> أسرار بيئة الخادم والطلب.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>$_REQUEST</code>: مصفوفة مدمجة تجمع عناصر <code>$_GET</code> و <code>$_POST</code> و <code>$_COOKIE</code> معاً</li>
          <li><strong>مخاطر $_REQUEST:</strong> خلط المصادر قد يسمح للمهاجم بتمرير متغير عبر الرابط يغطي على فورم الـ POST! الأفضل دائماً التحديد الصريح</li>
          <li><code>$_SERVER['REQUEST_METHOD']</code>: ترجع نوع الطلب (<code>"GET"</code> أو <code>"POST"</code>)</li>
          <li><code>$_SERVER['HTTP_USER_AGENT']</code>: معلومات متصفح ونظام تشغيل الزائر</li>
          <li><code>$_SERVER['REMOTE_ADDR']</code>: عنوان الـ IP الحقيقي للزائر</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">server_vars.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// التأكد أن الصفحة استُدعيت عبر POST</span>
<span class="tok-kw">if</span> (<span class="tok-var">$_SERVER</span>[<span class="tok-str">'REQUEST_METHOD'</span>] === <span class="tok-str">'POST'</span>) {
    <span class="tok-kw">echo</span> <span class="tok-str">"تم إرسال الفورم!&lt;br&gt;"</span>;
}

<span class="tok-cmt">// قراءة الـ IP ونوع المتصفح</span>
<span class="tok-kw">echo</span> <span class="tok-str">"IP: "</span> . <span class="tok-var">$_SERVER</span>[<span class="tok-str">'REMOTE_ADDR'</span>];</pre>
        </div>
      </div>''',
    notes_title="مصفوفتي REQUEST و SERVER",
    notes_script="مصفوفة $_SERVER بمثابة صندوق المعلومات الاستخباراتية لسيرفرك؛ تعرف منها كل شيء عن الطلب الحالي وهوية الزائر وطريقة وصوله.",
    notes_list=["مخاطر $_REQUEST وعدم التحديد", "أهم متغيرات $_SERVER", "فحص نوع الطلب برمجياً"]
)

# Slide 18: Example 1: Form Data Handling with $_POST
make_slide(
    index=17,
    title="مثال 1: استلام بيانات النموذج بـ POST",
    eyebrow="المصفوفات الفائقة &middot; مثال 1",
    slide_title="مثال 1: استلام بيانات النموذج بـ $_POST",
    slide_text="قراءة حقول النموذج القادمة عبر POST وطباعة بطاقة تأكيد الاستلام.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>استقبل اسم الطالب ودرجته من نموذج POST، وافحص هل تم إرسالهما بـ <code>isset()</code>، ثم اعرضهما في رسالة ترحيبية.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">student_post.php</span>
          </div>
          <pre class="code-body">&lt;?<span class="tok-kw">php</span>
<span class="tok-kw">if</span> (<span class="tok-var">$_SERVER</span>[<span class="tok-str">'REQUEST_METHOD'</span>] === <span class="tok-str">'POST'</span>) {
    <span class="tok-var">$name</span>  = <span class="tok-var">$_POST</span>[<span class="tok-str">'name'</span>]  ?? <span class="tok-str">'غير محدد'</span>;
    <span class="tok-var">$score</span> = <span class="tok-var">$_POST</span>[<span class="tok-str">'score'</span>] ?? <span class="tok-num">0</span>;
    
    <span class="tok-kw">echo</span> <span class="tok-str">"مرحباً بالطالب: "</span> . <span class="tok-var">$name</span> . <span class="tok-str">"&lt;br&gt;"</span>;
    <span class="tok-kw">echo</span> <span class="tok-str">"الدرجة المسجلة: "</span> . <span class="tok-var">$score</span>;
}
?&gt;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/student_post.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.6rem;">
مرحباً بالطالب: يوسف علي
الدرجة المسجلة: 95
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال استلام بيانات النموذج بـ POST",
    notes_script="استخدمنا هنا معامل الدمج ?? لحماية الكود وتعيين قيمة افتراضية إن لم تتوفر البيانات، مع التأكد من نوع الطلب POST.",
    notes_list=["فحص REQUEST_METHOD", "استخدام ?? مع مصفوفة $_POST", "عرض البيانات"]
)

# Slide 19: Example 2: Detecting Browser with $_SERVER
make_slide(
    index=18,
    title="مثال 2: كشف معلومات المتصفح بـ SERVER",
    eyebrow="المصفوفات الفائقة &middot; مثال 2",
    slide_title="مثال 2: كشف تفاصيل الزائر بـ $_SERVER",
    slide_text="استعراض المتغيرات المفيدة في <code>$_SERVER</code> لتخصيص المحتوى بناءً على جهاز المستخدم.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>اكتب سكربت PHP يطبع نوع الطلب الحالي المستخدم لفتح الصفحة، ونوع المتصفح المستعمل بواسطة <code>$_SERVER</code>.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">agent_info.php</span>
          </div>
          <pre class="code-body">&lt;?<span class="tok-kw">php</span>
<span class="tok-var">$method</span> = <span class="tok-var">$_SERVER</span>[<span class="tok-str">'REQUEST_METHOD'</span>];
<span class="tok-var">$agent</span>  = <span class="tok-var">$_SERVER</span>[<span class="tok-str">'HTTP_USER_AGENT'</span>];

<span class="tok-kw">echo</span> <span class="tok-str">"طريقة الطلب: "</span> . <span class="tok-var">$method</span> . <span class="tok-str">"&lt;br&gt;"</span>;
<span class="tok-kw">echo</span> <span class="tok-str">"بيانات المتصفح: "</span> . <span class="tok-var">$agent</span>;
?&gt;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/agent_info.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:ltr;text-align:start;padding:0.6rem;font-size:0.75rem;">
طريقة الطلب: GET
بيانات المتصفح: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال كشف بيانات المتصفح",
    notes_script="هذه المعلومات تُستخدم في المواقع الحقيقية لمعرفة هل المستخدم يتصفح من موبايل أم كمبيوتر، أو لتتبع محاولات الاختراق.",
    notes_list=["قراءة HTTP_USER_AGENT", "قراءة REQUEST_METHOD", "تطبيقات تخصيص واجهات العرض"]
)

# Slide 20: Common Mistakes in Superglobals
make_slide(
    index=19,
    title="أخطاء شائعة في المصفوفات الفائقة",
    eyebrow="احذر هذه الأخطاء &middot; 3",
    slide_title="أخطاء شائعة في المصفوفات الفائقة",
    slide_text="تجنب هذه العثرات المتكررة عند قراءة مدخلات النماذج في كودك:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ القراءة المباشرة دون فحص isset</div>
          <ul class="bullet-list">
            <li>كتابة <code>$email = $_POST['email'];</code> بمجرد فتح الصفحة يطلق تحذيراً:
              <br><code>Warning: Undefined array key "email"</code>
            </li>
            <li>لأن المستخدم لم يضغط زر الإرسال بعد، فالمصفوفة فارغة تماماً!</li>
            <li><strong>التصحيح:</strong> افحص دوماً: <code>if ($_SERVER['REQUEST_METHOD'] === 'POST')</code></li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ استخدام $_REQUEST والخلط بين الفحصين</div>
          <ul class="bullet-list">
            <li>استخدام <code>$_REQUEST</code> يجعلك لا تعرف هل القيمة جاءت من الرابط أم من جسم الفورم أم من الكوكيز!</li>
            <li><strong>الخلط بين isset و empty:</strong>
              <br>لو أرسل المستخدم نصاً فارغاً <code>""</code>:
              <br><code>isset()</code> سترجع <code>true</code>! لكن <code>empty()</code> سترجع <code>true</code> أيضاً.
            </li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء شائعة في التعامل مع Superglobals",
    notes_script="نذكر الطلاب دائماً: صفحة الـ PHP تُنفذ مرتين؛ مرة عند الفتح الأولي بـ GET وتكون المصفوفة فارغة، ومرة بعد الضغط على الإرسال بـ POST.",
    notes_list=["التحقق من وجود المفاتيح", "تجنب خطأ Undefined array key", "تفضيل $_POST المباشرة على $_REQUEST"]
)

# Slide 21: Validation vs Sanitization
make_slide(
    index=20,
    title="القاعدة الذهبية: لا تثق أبداً في المستخدم",
    eyebrow="الأمان والتحقق &middot; 4",
    slide_title="القاعدة الذهبية: لا تثق بمدخلات المستخدم!",
    slide_text="\"Never Trust User Input\" &mdash; أهم قاعدة في أمن الويب. كل مدخل قد يكون خطأً غير مقصود أو محاولة اختراق مدروسة!",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><strong>التحقق (Validation):</strong> هل البيانات تطابق الشروط؟ (هل هو إيميل صحيح؟ هل كلمة المرور 8 خانات على الأقل؟)</li>
          <li><strong>التعقيم (Sanitization):</strong> تنظيف البيانات وإزالة الحروف والرموز الضارة قبل تخزينها</li>
          <li><strong>الهروب (Output Escaping):</strong> تحويل الرموز الخطرة قبل طباعتها في المتصفح لمنع تنفيذها ككود</li>
          <li><strong>تحذير قاطع:</strong> التحقق عبر JavaScript في المتصفح غير كافٍ إطلاقاً؛ يمكن تجاوزه بسهولة!</li>
          <li>التحقق من جهة الخادم (Server-Side Validation) هو خط الدفاع الحقيقي والإجباري</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">security_pipeline.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// 1. استقبال المدخل</span>
<span class="tok-var">$input</span> = <span class="tok-var">$_POST</span>[<span class="tok-str">'email'</span>] ?? <span class="tok-str">''</span>;

<span class="tok-cmt">// 2. تنظيف المسافات</span>
<span class="tok-var">$cleanEmail</span> = <span class="tok-fn">trim</span>(<span class="tok-var">$input</span>);

<span class="tok-cmt">// 3. فحص الصلاحية Validation</span>
<span class="tok-kw">if</span> (!<span class="tok-fn">filter_var</span>(<span class="tok-var">$cleanEmail</span>, <span class="tok-kw">FILTER_VALIDATE_EMAIL</span>)) {
    <span class="tok-kw">echo</span> <span class="tok-str">"البريد غير صالح!"</span>;
}</pre>
        </div>
      </div>''',
    notes_title="مبدأ الأمان الذهبي والفرق بين Validation و Sanitization",
    notes_script="الفارق الجوهري: Validation يجيب بنعم أو لا (هل هو بريد سليم؟)، أما Sanitization فيعدل القيمة وينظفها، و Escaping يمنع تشغيلها في المتصفح.",
    notes_list=["مبدأ Never Trust User Input", "الفرق بين Validation و Sanitization و Escaping", "حتمية التحقق من جهة الخادم Server-Side"]
)

# Slide 22: Sanitizing Tools: htmlspecialchars, strip_tags, trim
make_slide(
    index=21,
    title="أدوات التنظيف والتعقيم",
    eyebrow="الأمان والتحقق &middot; 4",
    slide_title="أدوات التنظيف: trim و htmlspecialchars",
    slide_text="دوال PHP القياسية لتنظيف النصوص وحماية الصفحة من ثغرات حقن النصوص البرمجية (XSS).",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>trim($str)</code>: إزالة المسافات البيضاء والأسطر الفارغة من البداية والنهاية</li>
          <li><code>htmlspecialchars($str)</code>: تحويل الرموز الحساسة (<code>&lt; &gt; &amp; " '</code>) إلى رموز HTML مشفرة (Entities)</li>
          <li>تمنع المتصفح من تشغيل وسوم <code>&lt;script&gt;</code> وتحولها لنص عادي للقراءة فقط</li>
          <li><code>strip_tags($str)</code>: حذف كافة وسوم HTML تماماً من النص</li>
          <li><strong>القاعدة:</strong> طبق <code>htmlspecialchars()</code> دائماً قبل طباعة أي مدخل في المتصفح</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">sanitization.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$comment</span> = <span class="tok-str">' &lt;script&gt;alert("Hacked!");&lt;/script&gt; '</span>;

<span class="tok-cmt">// 1. تنظيف المسافات</span>
<span class="tok-var">$trimmed</span> = <span class="tok-fn">trim</span>(<span class="tok-var">$comment</span>);

<span class="tok-cmt">// 2. حماية XSS بالتعقيم</span>
<span class="tok-var">$safe</span> = <span class="tok-fn">htmlspecialchars</span>(<span class="tok-var">$trimmed</span>, <span class="tok-kw">ENT_QUOTES</span>, <span class="tok-str">'UTF-8'</span>);

<span class="tok-kw">echo</span> <span class="tok-var">$safe</span>;
<span class="tok-cmt">// يطبع النص كأحرف عادية ولا ينفذ الكود!</span></pre>
        </div>
      </div>''',
    notes_title="دوال التعقيم والهروب الأساسية",
    notes_script="htmlspecialchars هي السلاح الأول ضد ثغرة XSS؛ فبدلاً من أن يرى المتصفح علامة أصغر من كبداية كود، يراها &lt; فيطبعها للمستخدم بأمان.",
    notes_list=["دالة trim لإزالة المسافات", "دالة htmlspecialchars لمنع تنفيذ السكربتات", "دالة strip_tags لحذف الوسوم بالكامل"]
)

# Slide 23: Validation with filter_var() and filter_input()
make_slide(
    index=22,
    title="الفحص المتقدم بـ filter_var",
    eyebrow="الأمان والتحقق &middot; 4",
    slide_title="الفحص المتقدم: filter_var و filter_input",
    slide_text="توفر PHP محرك فلاتر احترافي مدمج للتحقق من أنواع البيانات بدقة وأداء فائقين.",
    body_content='''<div class="grid-2">
        <ul class="bullet-list">
          <li><code>filter_var($var, FILTER_VALIDATE_EMAIL)</code>: فحص دقة تنسيق البريد الإلكتروني</li>
          <li><code>filter_var($var, FILTER_VALIDATE_URL)</code>: فحص صحة الروابط والمواقع</li>
          <li><code>filter_var($var, FILTER_VALIDATE_INT)</code>: فحص هل القيمة عدد صحيح حقيقي</li>
          <li>ترجع الدالة القيمة نفسها إذا كانت صحيحة، أو ترجع <code>false</code> إذا فشل الفحص</li>
          <li><code>filter_input(INPUT_POST, 'key', FILTER_...)</code>: قراءة وفحص مباشرة من المصفوفة الفائقة</li>
        </ul>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">filter_var.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$email</span> = <span class="tok-str">"ali@domain.com"</span>;
<span class="tok-var">$age</span>   = <span class="tok-str">"25"</span>;

<span class="tok-kw">if</span> (<span class="tok-fn">filter_var</span>(<span class="tok-var">$email</span>, <span class="tok-kw">FILTER_VALIDATE_EMAIL</span>)) {
    <span class="tok-kw">echo</span> <span class="tok-str">"بريد صحيح ✅&lt;br&gt;"</span>;
}

<span class="tok-kw">if</span> (<span class="tok-fn">filter_var</span>(<span class="tok-var">$age</span>, <span class="tok-kw">FILTER_VALIDATE_INT</span>)) {
    <span class="tok-kw">echo</span> <span class="tok-str">"عمر رقمي صالح ✅"</span>;
}</pre>
        </div>
      </div>''',
    notes_title="محرك الفلاتر filter_var و filter_input",
    notes_script="بدل ما تكتب Regular Expressions معقدة بنفسك لفحص البريد أو الرابط، PHP جهزت لك filter_var السريعة والمجربة ملايين المرات.",
    notes_list=["FILTER_VALIDATE_EMAIL للبريد", "FILTER_VALIDATE_URL للروابط", "FILTER_VALIDATE_INT للأرقام", "دالة filter_input المباشرة"]
)

# Slide 24: Security: XSS & SQL Injection
make_slide(
    index=23,
    title="الحماية من XSS و SQL Injection",
    eyebrow="الأمان والتحقق &middot; 4",
    slide_title="الحماية من XSS و SQL Injection",
    slide_text="أخطر هجومين يستهدفان تطبيقات الويب عبر النماذج، وكيفية التصدي لهما نهائياً:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">🛡️ هجوم XSS (Cross-Site Scripting)</div>
          <ul class="bullet-list">
            <li><strong>الخطر:</strong> كتابة المستخدم كود <code>&lt;script&gt;</code> لسرقة كوكيز وجلسات الزوار الآخرين</li>
            <li><strong>خط الدفاع:</strong> استخدام <code>htmlspecialchars($data, ENT_QUOTES, 'UTF-8')</code> عند طباعة أي مدخل للمستخدم</li>
            <li>تشفير الوسوم يمنع المتصفح من تنفيذ الكود ويجعله يقرأه كنص جامد فقط</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">🛡️ هجوم SQL Injection</div>
          <ul class="bullet-list">
            <li><strong>الخطر:</strong> حقن أوامر SQL (مثل <code>' OR 1=1 --</code>) للتلاعب بقاعدة البيانات وسرقتها أو مسحها</li>
            <li><strong>خط الدفاع:</strong> استخدام <strong>Prepared Statements و Parameter Binding</strong> عبر مكتبة PDO</li>
            <li><strong>ممنوع منعاً باتاً:</strong> دمج مدخلات المستخدم مباشرة في نص استعلام SQL عبر علامة <code>.</code></li>
          </ul>
        </div>
      </div>''',
    notes_title="التصدي لـ XSS و SQL Injection",
    notes_script="هاتان الثغرتان تمثلان أكبر خطرين في قائمة OWASP Top 10. معالجة الأولى بـ htmlspecialchars، ومعالجة الثانية بـ Prepared Statements.",
    notes_list=["حماية XSS بتعقيم العرض", "حماية SQL Injection بـ Prepared Statements", "فصل كود الاستعلام عن بيانات المدخلات"]
)

# Slide 25: Example 1: User Registration Validation
make_slide(
    index=24,
    title="مثال 1: التحقق من استمارة تسجيل",
    eyebrow="الأمان والتحقق &middot; مثال 1",
    slide_title="مثال 1: التحقق الصارم من استمارة التسجيل",
    slide_text="كود متكامل من جهة الخادم يفحص الاسم والبريد وطول كلمة المرور ويجمع الأخطاء في مصفوفة.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">الهدف</div>
          <p>تحقق من أن: الاسم غير فارغ، البريد صالح بـ <code>filter_var</code>، وكلمة المرور لا تقل عن 8 خانات، واعرض رسائل الأخطاء إن وجدت.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">validate_register.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$errors</span> = [];
<span class="tok-var">$name</span>  = <span class="tok-fn">trim</span>(<span class="tok-var">$_POST</span>[<span class="tok-str">'name'</span>] ?? <span class="tok-str">''</span>);
<span class="tok-var">$email</span> = <span class="tok-fn">trim</span>(<span class="tok-var">$_POST</span>[<span class="tok-str">'email'</span>] ?? <span class="tok-str">''</span>);
<span class="tok-var">$pass</span>  = <span class="tok-var">$_POST</span>[<span class="tok-str">'pass'</span>] ?? <span class="tok-str">''</span>;

<span class="tok-kw">if</span> (<span class="tok-fn">empty</span>(<span class="tok-var">$name</span>)) { <span class="tok-var">$errors</span>[] = <span class="tok-str">"الاسم مطلوب"</span>; }
<span class="tok-kw">if</span> (!<span class="tok-fn">filter_var</span>(<span class="tok-var">$email</span>, <span class="tok-kw">FILTER_VALIDATE_EMAIL</span>)) { <span class="tok-var">$errors</span>[] = <span class="tok-str">"البريد غير صحيح"</span>; }
<span class="tok-kw">if</span> (<span class="tok-fn">strlen</span>(<span class="tok-var">$pass</span>) &lt; <span class="tok-num">8</span>) { <span class="tok-var">$errors</span>[] = <span class="tok-str">"كلمة المرور يجب أن تكون 8 خانات فأكثر"</span>; }

<span class="tok-kw">if</span> (<span class="tok-fn">empty</span>(<span class="tok-var">$errors</span>)) {
    <span class="tok-kw">echo</span> <span class="tok-str">"تم التسجيل بنجاح! 🎉"</span>;
} <span class="tok-kw">else</span> {
    <span class="tok-kw">echo</span> <span class="tok-fn">implode</span>(<span class="tok-str">"&lt;br&gt;"</span>, <span class="tok-var">$errors</span>);
}</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/validate_register.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:rtl;text-align:start;padding:0.6rem;color:#e11d48;">
❌ البريد غير صحيح
❌ كلمة المرور يجب أن تكون 8 خانات فأكثر
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال التحقق من استمارة التسجيل",
    notes_script="لاحظ كيف جمعنا الأخطاء في مصفوفة $errors، هذا يسمح بعرض كل الملاحظات للمستخدم مرة واحدة بدلاً من إيقاف الكود عند أول خطأ فقط.",
    notes_list=["مصفوفة تجميع الأخطاء $errors", "فحص الطول بـ strlen", "فحص البريد بـ filter_var", "رسائل واضحة ومحددة"]
)

# Slide 26: Example 2: Sanitizing User Comments Before Display
make_slide(
    index=25,
    title="مثال 2: تعقيم التعليقات قبل العرض",
    eyebrow="الأمان والتحقق &middot; مثال 2",
    slide_title="مثال 2: تعقيم التعليقات قبل العرض",
    slide_text="تطبيق الهروب والتعقيم على نصوص التعليقات التي يدخلها المستخدمون لمنع هجمات XSS.",
    body_content='''<div class="exercise-grid">
        <div class="question-card">
          <div class="qlabel">السؤال</div>
          <p>استقبل تعليق مستخدم قد يحتوي على وسوم خبيثة مثل <code>&lt;script&gt;</code> أو <code>&lt;b&gt;</code>، وعقمه بـ <code>htmlspecialchars</code> واعرضه بأمان.</p>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">safe_comment.php</span>
          </div>
          <pre class="code-body">&lt;?<span class="tok-kw">php</span>
<span class="tok-var">$rawComment</span> = <span class="tok-var">$_POST</span>[<span class="tok-str">'comment'</span>] ?? <span class="tok-str">''</span>;

<span class="tok-cmt">// 1. إزالة المسافات الزائدة</span>
<span class="tok-var">$trimmed</span> = <span class="tok-fn">trim</span>(<span class="tok-var">$rawComment</span>);

<span class="tok-cmt">// 2. تعقيم وتأمين العرض</span>
<span class="tok-var">$safeComment</span> = <span class="tok-fn">htmlspecialchars</span>(<span class="tok-var">$trimmed</span>, <span class="tok-kw">ENT_QUOTES</span>, <span class="tok-str">'UTF-8'</span>);

<span class="tok-kw">echo</span> <span class="tok-str">"&lt;div class='comment-box'&gt;"</span> . <span class="tok-var">$safeComment</span> . <span class="tok-str">"&lt;/div&gt;"</span>;
?&gt;</pre>
        </div>
        <div class="browser-window">
          <div class="browser-titlebar">
            <div class="browser-dots"><span class="r"></span><span class="y"></span><span class="g"></span></div>
            <div class="browser-address">localhost/safe_comment.php</div>
          </div>
          <div class="browser-viewport">
            <div class="output-ascii" style="direction:ltr;text-align:start;padding:0.6rem;">
&lt;script&gt;alert("XSS")&lt;/script&gt;
----------------------------------------
(ظهر الكود كنص عادي مأمون بدون تنفيذ أي نافذة تحذيرية!)
            </div>
          </div>
        </div>
      </div>''',
    notes_title="مثال تعقيم التعليقات لمنع XSS",
    notes_script="عندما حاول المخترق حقن كود جافاسكريبت، قام المتصفح برسم الأحرف كنص عادي لأن PHP حولت الأقواس إلى &lt; و &gt;.",
    notes_list=["استقبال التعليق الخام", "تطبيق trim و htmlspecialchars", "طباعة آمنة تماماً في المتصفح"]
)

# Slide 27: Common Mistakes in Validation & Security
make_slide(
    index=26,
    title="أخطاء شائعة في الأمان والتحقق",
    eyebrow="احذر هذه الأخطاء &middot; 4",
    slide_title="أخطاء شائعة في الأمان والتحقق",
    slide_text="احذر هذه الثغرات الكلاسيكية التي تهدد أمن تطبيقات PHP:",
    body_content='''<div class="naming-grid">
        <div class="naming-card rules">
          <div class="naming-card-title">❌ الاعتماد على فحص JavaScript فقط</div>
          <ul class="bullet-list">
            <li>أي تحقق بالمتصفح (Client-side) يمكن تجاوزه بضغطة زر أو بأداة مثل Postman و cURL</li>
            <li>الاعتماد على HTML <code>required</code> وحدها دون فحص في PHP = موقع مخترق بسهولة!</li>
            <li><strong>القاعدة:</strong> فحص المتصفح لتجربة الاستخدام، وفحص السيرفر للأمان الفعلي</li>
          </ul>
        </div>
        <div class="naming-card conventions">
          <div class="naming-card-title">⚠️ الثقة في الحقول المخفية وإهمال التعقيم</div>
          <ul class="bullet-list">
            <li>الحقول المخفية (Hidden Inputs) ليست سرية؛ يستطيع المستخدم تعديل قيمتها بسهولة عبر Inspect Element!</li>
            <li>إهمال <code>htmlspecialchars()</code> عند طباعة الأسماء والتعليقات يفتح الباب واسعاً لهجمات Stored XSS</li>
          </ul>
        </div>
      </div>''',
    notes_title="أخطاء أمنية شائعة",
    notes_script="الخطأ الأكبر الذي يقع فيه المطور هو تخيل أن المستخدم سيرسل البيانات فقط عبر النموذج المصمم له؛ فالمخترق قد يرسل الطلب مباشرة إلى ملف الـ PHP متجاوزاً كل شروط الـ HTML.",
    notes_list=["حتمية الفحص من جهة السيرفر Server-Side", "الحقول المخفية قابلة للتعديل من المستخدم", "التعقيم عند العرض إلزامي"]
)

# Slide 28: Divider: Homework Assignments
make_slide(
    index=27,
    title="الواجبات العملية",
    eyebrow="تطبيقات وتكليفات عملية",
    slide_title="الواجبات العملية (Homework)",
    slide_text="3 واجبات برمجية عملية متدرجة في الصعوبة لتطبيق كل ما تعلمته اليوم حول النماذج وطرق الإرسال والأمان:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">واجب 1: نموذج تواصل بسيط (سهل)</span>
        <span class="pill-badge">واجب 2: مقارنة GET و POST (سهل)</span>
        <span class="pill-badge">واجب 3: استمارة تسجيل آمنة (متوسط)</span>
      </div>''',
    notes_title="فاصل الواجبات العملية",
    notes_script="ننتقل الآن لقسم الواجبات والتطبيقات العملية. اطلب من الطلاب كتابة الأكواد بأنفسهم واختبار الحالات المختلفة لكل نموذج.",
    notes_list=["واجب 1: نموذج تواصل واستعراض المدخلات", "واجب 2: مقارنة عملية بين GET و POST", "واجب 3: بناء نظام تسجيل مستخدم آمن ومتكامل"],
    is_divider=True
)

# Slide 29: Homework 1 (Easy): Creating Your First Contact Form
make_slide(
    index=28,
    title="واجب 1: بناء أول نموذج تواصل",
    eyebrow="الواجبات العملية &middot; 1 (سهل)",
    slide_title="واجب 1: إنشاء أول نموذج تواصل",
    slide_text="إنشاء نموذج HTML بسيط لإرسال بيانات التواصل إلى سكربت PHP واستعراض البيانات المدخلة بنجاح.",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في الواجب 1</div>
          <ul class="bullet-list" style="margin-top:0.4rem;">
            <li>أنشئ نموذج HTML يحتوي حقول: الاسم (name)، البريد (email)، والرسالة (message)</li>
            <li>اربط النموذج بسكربت PHP عبر طريقة <code>POST</code></li>
            <li>استقبل البيانات واعرضها للمستخدم بشكل منسق بعد الإرسال مع فحص <code>isset()</code></li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">hw1_contact.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">&lt;!-- 1. بناء النموذج مع خاصية action و method="POST" --&gt;</span>

<span class="tok-cmt">&lt;!-- 2. إضافة حقول: name, email, message مع وسم label لكل حقل --&gt;</span>

<span class="tok-cmt">&lt;!-- 3. كود PHP: فحص هل تم الإرسال بـ $_SERVER['REQUEST_METHOD'] --&gt;</span>

<span class="tok-cmt">&lt;!-- 4. استلام القيم بـ $_POST وتطبيق trim() وعرضها في الصفحة --&gt;</span></pre>
        </div>
      </div>''',
    notes_title="واجب 1: نموذج تواصل بسيط",
    notes_script="تأكد أن الطلاب ربطوا حقول الإدخال بخاصية name مطابقة تماماً للمفاتيح المستدعاة في $_POST.",
    notes_list=["إنشاء فورم تواصل بـ POST", "استلام البيانات وطباعتها", "التأكد من خاصية name و method"]
)

# Slide 30: Homework 2 (Easy): Understanding GET and POST Differences
make_slide(
    index=29,
    title="واجب 2: المقارنة العملية بين GET و POST",
    eyebrow="الواجبات العملية &middot; 2 (سهل)",
    slide_title="واجب 2: فهم الفروق بين GET و POST",
    slide_text="بناء صفحتين مستقلتين لاختبار سلوك البيانات في شريط العنوان وسجلات المتصفح.",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في الواجب 2</div>
          <ul class="bullet-list" style="margin-top:0.4rem;">
            <li>أنشئ صفحة أولى تستقبل كلمة بحث عبر <code>GET</code> وتعرضها</li>
            <li>أنشئ صفحة ثانية لتسجيل الدخول تستقبل البريد وكلمة المرور عبر <code>POST</code></li>
            <li>لاحظ كيف تظهر البيانات في الرابط مع GET وتختفي مع POST</li>
            <li>اكتب تعليقاً في ملفك يوثق متى نفضل استخدام كل طريقة برمجياً</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">hw2_get_vs_post.php</span>
          </div>
          <pre class="code-body"><span class="tok-cmt">// صفحة 1: search.php بـ GET</span>
<span class="tok-cmt">// لاحظ شكل الرابط: search.php?keyword=phone</span>

<span class="tok-cmt">// صفحة 2: login.php بـ POST</span>
<span class="tok-cmt">// لاحظ شكل الرابط: login.php (البيانات مخفية)</span>

<span class="tok-cmt">/*
توثيقك:
- نستخدم GET في: ...
- نستخدم POST في: ...
*/</span></pre>
        </div>
      </div>''',
    notes_title="واجب 2: تجربة GET مقابل POST",
    notes_script="هذا التمرين يرسخ الفارق البصري بين الطريقتين؛ سيرى الطالب بنفسه متى تنكشف البيانات في الرابط ومتى تكون خفية.",
    notes_list=["تطبيق GET للبحث", "تطبيق POST لتسجيل الدخول", "توثيق السيناريو الأنسب لكل طريقة"]
)

# Slide 31: Homework 3 (Medium): Building a Secure Registration Form
make_slide(
    index=30,
    title="واجب 3: بناء استمارة تسجيل آمنة",
    eyebrow="الواجبات العملية &middot; 3 (متوسط)",
    slide_title="واجب 3: استمارة تسجيل مستخدم آمنة",
    slide_text="بناء نموذج تسجيل متكامل يطبق جميع معايير التحقق، التعقيم، وفحص تكرار البيانات.",
    body_content='''<div class="homework-grid">
        <div class="question-card">
          <div class="qlabel">المطلوب في الواجب 3</div>
          <ul class="bullet-list" style="margin-top:0.3rem;">
            <li>حقول: username, email, password, confirm_password بـ POST</li>
            <li>تحقق السيرفر: عدم الفراغ، بريد صالح بـ filter_var، طول كلمة المرور وتطابقها</li>
            <li>تعقيم جميع المدخلات بـ trim و htmlspecialchars وعرض الأخطاء بوضوح</li>
            <li><strong>محاكاة فحص التكرار:</strong> أنشئ مصفوفة مستخدمين موجودين وتحقق أن الاسم والبريد غير مكررين بـ in_array()</li>
          </ul>
        </div>
        <div class="code-window">
          <div class="code-titlebar">
            <span class="code-dot red"></span><span class="code-dot yellow"></span><span class="code-dot green"></span>
            <span class="code-filename">hw3_secure_register.php</span>
          </div>
          <pre class="code-body"><span class="tok-var">$existingUsers</span> = [<span class="tok-str">'admin'</span>, <span class="tok-str">'ali'</span>, <span class="tok-str">'sara'</span>];
<span class="tok-var">$existingEmails</span> = [<span class="tok-str">'admin@test.com'</span>, <span class="tok-str">'ali@test.com'</span>];

<span class="tok-cmt">// 1. استقبال المدخلات وتعقيمها</span>

<span class="tok-cmt">// 2. التحقق من صحة الشروط وتطابق الباسورد</span>

<span class="tok-cmt">// 3. فحص التكرار بـ in_array($user, $existingUsers)</span>

<span class="tok-cmt">// 4. عرض الأخطاء أو رسالة النجاح</span></pre>
        </div>
      </div>''',
    notes_title="واجب 3: استمارة تسجيل آمنة",
    notes_script="هذا الواجب يحاكي بيئة العمل الحقيقية في تسجيل الحسابات؛ فحص شامل للأمان وصلاحية البيانات ومحاكاة عدم التكرار.",
    notes_list=["التحقق الكامل من الحقول", "مطابقة كلمتي المرور", "محاكاة فحص التكرار بمصفوفة", "عرض رسائل أخطاء واضحة"]
)

# Slide 32: Divider: Review Time
make_slide(
    index=31,
    title="وقت المراجعة",
    eyebrow="نقاش ومراجعة",
    slide_title="وقت المراجعة",
    slide_text="قبل أن نختم، فكّر في هذين السؤالين وتأكد من استيعابك الكامل للفروق الجوهرية:",
    body_content='''<div class="badge-row">
        <span class="pill-badge">لماذا لا يجب مطلقاً إرسال كلمات المرور عبر GET؟</span>
        <span class="pill-badge">ما الفرق الجوهري بين Validation و Sanitization و Output Escaping؟</span>
      </div>''',
    notes_title="فاصل المراجعة",
    notes_script="أسئلة سريعة لإشراك الطلاب والتحقق من فهمهم لمفاهيم الأمان وسلوك البروتوكول.",
    notes_list=["سؤال خطورة إرسال الباسورد في GET", "سؤال الفرق بين Validation و Sanitization و Escaping"],
    is_divider=True
)

# Slide 33: Summary
make_slide(
    index=32,
    title="اللي اتعلمناه النهاردة",
    eyebrow="ملخص المحاضرة",
    slide_title="اللي اتعلمناه النهاردة",
    slide_text="خلاصة أهم 4 ركائز أتقناها اليوم في التعامل مع نماذج الويب في PHP:",
    body_content='''<div class="topics-grid">
        <div class="topic-item">
          <div class="topic-num">01</div>
          <div class="topic-info">
            <div class="topic-title">نماذج HTML وعناصر الإدخال</div>
            <div class="topic-desc">الوسم form وخصائص action و method و name وإلزامية enctype</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">02</div>
          <div class="topic-info">
            <div class="topic-title">مقارنة GET و POST</div>
            <div class="topic-desc">فهم إرسال البيانات بالرابط مقابل الجسم وسعة التخزين والأمان</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">03</div>
          <div class="topic-info">
            <div class="topic-title">المصفوفات الفائقة Superglobals</div>
            <div class="topic-desc">الوصول لـ $_POST و $_GET و $_SERVER مع حتمية فحص isset</div>
          </div>
        </div>
        <div class="topic-item">
          <div class="topic-num">04</div>
          <div class="topic-info">
            <div class="topic-title">التحقق والتعقيم الأمني</div>
            <div class="topic-desc">قاعدة عدم الثقة بالمدخلات، فلاتر filter_var وتأمين XSS و SQLi</div>
          </div>
        </div>
      </div>''',
    notes_title="ملخص المحاضرة 07",
    notes_script="نراجع مع الطلاب النقاط الأربع الكبرى: عناصر الفورم، بروتوكولات الإرسال، مصفوفات الـ Superglobals، والدرع الأمني للتحقق والتعقيم.",
    notes_list=["نماذج HTML", "GET vs POST", "المصفوفات الفائقة", "الأمان والتحقق والتعقيم"]
)

# Slide 34: Ending / Thank You
make_slide(
    index=33,
    title="شكرًا لكم",
    eyebrow="نهاية المحاضرة 07",
    slide_title="شكرًا لكم",
    slide_text="النماذج هي بوابة تفاعل المستخدم مع موقعك، وإتقان تأمينها ومعالجتها يضعك على أول دروب بناء التطبيقات التجارية الحقيقية &mdash; استمروا في التطبيق والتدريب!",
    body_content='''<div class="badge-row">
        <span class="pill-badge">المحاضرة 07</span>
        <span class="pill-badge">نماذج HTML في PHP</span>
        <span class="pill-badge">لوغاريتم للتدريب البرمجي</span>
      </div>''',
    notes_title="خاتمة المحاضرة 07",
    notes_script="شكر الطلاب على تركيزهم وتشجيعهم على إتمام الواجبات الثلاثة وتسليمها قبل المحاضرة القادمة.",
    notes_list=["شكر وتقدير", "التشجيع على حل الواجبات", "تمهيد للمحاضرة القادمة"],
    is_divider=True
)

print("All 34 slides for Lecture 07 generated successfully!")
