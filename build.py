#!/usr/bin/env python3
"""Static site generator for Avyra Company / شركة أفيرا (Arabic + English).

Run `python3 build.py` after editing the content below. It rewrites every
HTML page, sitemap.xml, robots.txt and 404.html. No dependencies beyond Python 3.
"""
import json, os, hashlib

def _v(p): return hashlib.md5(open(p, "rb").read()).hexdigest()[:8]
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
CSS = "/assets/css/style.css?v=" + _v("assets/css/style.css")
JS = "/assets/js/main.js?v=" + _v("assets/js/main.js")

# ---------------------------------------------------------------- settings (EDIT THESE)
SITE = "https://avyra.sa"            # PLACEHOLDER: set the real domain
EMAIL = "info@avyra.sa"              # PLACEHOLDER
PRIVACY_EMAIL = "privacy@avyra.sa"   # PLACEHOLDER
PHONE_DISPLAY = "+966 50 020 9038"                   # e.g. "+966 5X XXX XXXX"; empty hides the phone rows
PHONE_TEL = "+966500209038"                       # e.g. "+9665XXXXXXXX"
LINKEDIN_URL = ""                    # empty hides the LinkedIn row
BOOKING_URL = ""                     # Cal.com / Calendly link; empty hides the "book a call" button
CR = "7050745707"                    # same legal entity as Maya AI / Sahm Alkarar
# Contact form: empty endpoint = opens the visitor's email app. For Web3Forms use
# FORM_ENDPOINT = "https://api.web3forms.com/submit" and put the access key in FORM_KEY.
FORM_ENDPOINT = ""
FORM_KEY = ""

_P = lambda f: f'<link rel="preload" href="/assets/fonts/{f}-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
PRELOAD = {"ar": _P("ibm-plex-sans-arabic-arabic-400") + _P("reem-kufi-arabic-700"),
           "en": _P("ibm-plex-sans-latin-400") + _P("ibm-plex-sans-latin-600")}

ICONS = {
 "ai": '<svg class="icon" viewBox="0 0 48 48" aria-hidden="true"><rect x="12" y="12" width="24" height="24"/><rect x="19" y="19" width="10" height="10"/><path d="M18 12V5M24 12V5M30 12V5M18 43v-7M24 43v-7M30 43v-7M12 18H5M12 24H5M12 30H5M43 18h-7M43 24h-7M43 30h-7"/></svg>',
 "geo": '<svg class="icon" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="16"/><path d="M8 24h32M24 8c-7 5-7 27 0 32M24 8c7 5 7 27 0 32"/></svg>',
 "gov": '<svg class="icon" viewBox="0 0 48 48" aria-hidden="true"><rect x="8" y="30" width="32" height="10"/><rect x="12" y="18" width="24" height="10"/><rect x="16" y="6" width="16" height="10"/></svg>',
}

# ---------------------------------------------------------------- content
T = {
"ar": {
 "dir": "rtl", "lang": "ar", "base": "/", "other": "en", "other_label": "English", "locale": "ar_SA", "other_locale": "en_US",
 "brand": "شركة أفيرا", "brand_core": "أفيرا", "co": "شركة", "skip": "انتقل إلى المحتوى", "home_label": "الرئيسية",
 "nav": [("about", "عن الشركة"), ("services", "خدماتنا"), ("projects", "خبراتنا"), ("team", "الفريق"), ("contact", "تواصل معنا")],
 "nav_services": "خدماتنا",
 "title": "شركة أفيرا | الذكاء الاصطناعي المؤسسي والذكاء الجيومكاني وحوكمة المحافظ والمشاريع في الرياض",
 "desc": "شركة أفيرا شركة سعودية في الرياض تجمع حلول الذكاء الاصطناعي المؤسسي، والذكاء الاصطناعي الجيومكاني (GeoAI)، وحوكمة المحافظ والمشاريع لدعم برامج التحول الرقمي والبيئة في رؤية 2030.",
 "eyebrow": "الرياض · المملكة العربية السعودية",
 "h1": "من البيانات المعقدة إلى قرارات محوكمة",
 "lead": "الذكاء الاصطناعي المؤسسي والجيومكاني (GeoAI) وحوكمة المحافظ والمشاريع للجهات الحكومية والشركات والمنشآت الصغيرة والمتوسطة والمكاتب المهنية. نحوّل التعقيد إلى ذكاء محوكم، والذكاء إلى أثر مستدام.",
 "cta1": "تواصل معنا", "cta2": "خدماتنا", "logo_alt": "شعار أفيرا",
 "trust": ["اعتمادات PfMP · PgMP · PMP في إدارة المحافظ والبرامج والمشاريع", "شركة سعودية مسجلة في الرياض", "تصميم متوافق مع ضوابط NCA-ECC", "تنفيذ بالشراكة مع شركاء تقنيين من الولايات المتحدة وألمانيا"],
 "about_eyebrow": "عن الشركة", "about_h": "الرؤية والرسالة",
 "vision_h": "رؤيتنا", "vision": "أن نكون الشريك الموثوق للمملكة في تمكين القرار، عبر حلول ذكية ومستدامة وفعّالة اقتصاديًا تتحول إلى محافظ منظّمة تقودها البيانات.",
 "mission_h": "رسالتنا", "mission": "نطوّر وننشر أنظمة ذكاء الأعمال بالذكاء الاصطناعي وحلول GeoAI وأطر حوكمة المحافظ والمشاريع، لتساعد الجهات السعودية على التعامل مع بياناتها بوصفها أصلًا استراتيجيًا. وبدمج الهندسة المتقدمة للذكاء الاصطناعي المؤسسي مع GeoAI وإدارة المحافظ والبرامج والمشاريع المعتمدة، نحوّل البيانات المعقدة إلى معلومات جاهزة لمجلس الإدارة.",
 "gap_h": "لماذا وُجدنا", "gap": "معظم الجهات تقدّم قطعة واحدة من الصورة. شركات الاستشارات الهندسية التقليدية تقدّم دراسات فنية دون حوكمة للمحافظ، وشركات الذكاء الاصطناعي تبني النماذج دون فهم لعدم اليقين في البيانات البيئية والمكانية. نحن نجمع الأمور الثلاثة: الحوكمة، وGeoAI، والنشر التشغيلي للذكاء الاصطناعي، في كيان سعودي واحد.",
 "svc_eyebrow": "خدماتنا", "svc_h": "ثلاث ركائز متكاملة",
 "pillars": [
  {"icon": "ai", "tag": "الركيزة أ", "h": "الذكاء الاصطناعي المؤسسي والتحول الرقمي والنشر السيادي",
   "items": [("وكلاء الذكاء الاصطناعي وأتمتة سير العمل", "أتمتة تحت إشراف بشري لعمليات الجهة وموافقاتها وتنفيذ خدماتها."),
             ("التحول الرقمي للشركات", "نساعد الشركات على تقييم وضعها الحالي وتحديد الأولويات وتطبيق أساليب عمل رقمية مدعومة بالذكاء الاصطناعي، من إعادة تصميم الإجراءات حتى التبني."),
             ("تطوير المنصات المخصصة", "تصميم وبناء منصات وتطبيقات مخصصة مدعومة بالذكاء الاصطناعي حول طريقة عمل جهتك، من هندسة النظام حتى النشر."),
             ("ذكاء المعرفة والمستندات", "استرجاع مستندات المؤسسة وذكاء محتوى متعدد اللغات (عربي/إنجليزي) للجهات التي تدير منظومات مستندات ضخمة، من الجهات التنظيمية إلى المكاتب القانونية."),
             ("النشر الخاص والسيادي للذكاء الاصطناعي", "نشر على السحابة والسحابة الخاصة والبنية المحلية والهجينة، مصمَّم ليتوافق مع NCA-ECC وإرشادات سدايا ونظام حماية البيانات الشخصية، وهو أمر حاسم للجهات الحكومية.")],
   "outcome": "ذكاء اصطناعي مؤسسي يعمل داخل محيط الأمن والحوكمة لديك."},
  {"icon": "geo", "tag": "الركيزة ب", "h": "الاستشارات في الذكاء الاصطناعي الجيومكاني (GeoAI)",
   "items": [("النمذجة المعززة بـ GeoAI لحلول الأعمال والحلول الذكية", "دمج صور الأقمار الصناعية وبيانات الاستشعار عن بعد مع نماذج تحليلية متقدمة، لدعم قرارات الأعمال وتطوير الحلول الذكية."),
             ("تصميم قواعد البيانات الجيومكانية والبنية المكانية", "تصميم قواعد بيانات جيومكانية وبنية بيانات مكانية (SDI) تجعل بيانات الجهة قابلة للمشاركة والتحليل."),
             ("الذكاء المكاني والتشغيلي", "مراقبة البنية التحتية، والوعي بالعمليات الميدانية، ورؤية بيئية للأصول الموزعة."),
             ("مفاهيم التوأم الرقمي للبنية التحتية", "تقييم الجاهزية وتصميم البنية وخارطة طريق التنفيذ للتوائم الرقمية للبنية التحتية.")],
   "outcome": "من بيانات الأقمار الصناعية إلى قرار مجلس الإدارة، في أسابيع لا سنوات."},
  {"icon": "gov", "tag": "الركيزة ج", "h": "حوكمة المحافظ والبرامج والمشاريع",
   "items": [("تقييم نضج الحوكمة", "تقييم واقع إدارة المحافظ والبرامج لديكم مقابل أفضل الممارسات، وتحديد الفجوات ذات الأولوية."),
             ("تصميم أطر الحوكمة", "بناء أطر لإدارة المحافظ والبرامج والمشاريع تناسب حجم الجهة وهيكلها."),
             ("حوكمة التحول الرقمي", "دمج حوكمة المحافظ والمشاريع داخل برامج التحول الرقمي، لإبقاء المبادرات ضمن الجدول الزمني والمساءلة."),
             ("الدعم الاستشاري المعتمد", "دعم مكاتب إدارة المشاريع بخبرة معتمدة في PfMP وPgMP وPMP.")],
   "outcome": "محفظة مشاريع تُدار بوضوح، من الأولوية إلى الأثر."},
 ],
 "proj_eyebrow": "خبراتنا", "proj_h": "نماذج من خبراتنا",
 "proj_note": "تحافظ أفيرا على السرية. تُشارك المراجع التفصيلية ودراسات الحالة مباشرة، بعد توقيع اتفاقيات السرية المناسبة. وتمثل الفئات أدناه الخبرة المجمّعة لقيادة الشركة وفرق شركائها.",
 "proj_cols": ("القطاع", "نوع المشروع", "دورنا"),
 "proj": [("الذكاء الاصطناعي المؤسسي (السعودية)", "وكلاء ذكاء اصطناعي لسير عمل الخدمات", "نشر تشغيلي للذكاء الاصطناعي"),
          ("أنظمة ذكاء اصطناعي مخصصة", "تطوير تطبيقات ذكاء اصطناعي متكاملة", "هندسة النظام ونشره"),
          ("أنظمة GeoAI مخصصة", "حلول GeoAI", "بناء النظام مع شريك التطوير"),
          ("التحول الرقمي", "برامج التحول الرقمي للشركات", "الاستشارات ودعم التنفيذ")],
 "team_eyebrow": "الفريق", "team_h": "القيادة",
 "team": [("م. خالد عبدالرحمن", "الرئيس التنفيذي", "قاد عمليات الشركة في المملكة وشراكتها الدولية على مدى أكثر من عشر سنوات في تسليم برمجيات المؤسسات والتحول الرقمي الحكومي."),
          ("د. محمد عبدالله", "المدير الفني", "حاصل على اعتمادات PfMP وPgMP وPMP في إدارة المحافظ والبرامج والمشاريع.")],
 "network": "يقود فريقنا الأساسي كل مشروع، ويُنفَّذ بدعم مهندسين ومحللين متخصصين في الذكاء الاصطناعي وتطوير التطبيقات المتكاملة والاستشعار عن بعد ونظم المعلومات الجغرافية، وخبراء في البيئة والبنية التحتية.",
 "why_eyebrow": "لماذا أفيرا", "why_h": "الميزة السعودية",
 "why": [("شركة سعودية مسجلة ومقرها الرياض", "نعمل داخل بيئتكم التنظيمية وبيئة المشتريات."),
         ("متوافقون مع رؤية 2030", "يدعم عملنا مباشرة أهداف الاستدامة البيئية والتحول الرقمي."),
         ("نشر سيادي للذكاء الاصطناعي", "تصميم متوافق مع NCA-ECC ونظام حماية البيانات الشخصية، وقابل للنشر محليًا أو على سحابة خاصة، وهو حاسم للجهات الحكومية."),
         ("ثلاث كفاءات في مكان واحد", "حوكمة المحافظ والمشاريع، وGeoAI، والذكاء الاصطناعي المؤسسي في فريق واحد."),
         ("تنفيذ بثلاث لغات", "العربية والإنجليزية والألمانية، مع ملخصات تنفيذية تناسب صانع القرار السعودي."),
         ("عمق تقني أمريكي وألماني", "تمنحنا شراكتنا التقنية في فرجينيا وألمانيا عمقًا هندسيًا، بينما تبقى المسؤولية والتنفيذ داخل المملكة.")],
 "contact_eyebrow": "تواصل معنا", "contact_h": "لنناقش مشروعك", "contact_p": "اكتب لنا عن احتياجك. يرد فريقنا في الرياض وفرجينيا خلال يوم عمل واحد، وتُعامل جميع الاستفسارات بسرية تامة.",
 "book": "احجز مكالمة تشخيصية مدتها 30 دقيقة", "linkedin": "لينكدإن",
 "labels": {"email": "البريد الإلكتروني", "phone": "الهاتف", "hq": "الموقع", "hq_val": "حي العليا، الرياض، المملكة العربية السعودية", "cr": "السجل التجاري",
            "contact_h": "تواصل", "company_h": "الشركة", "privacy": "سياسة الخصوصية", "rights": "جميع الحقوق محفوظة", "links_h": "روابط"},
 "form": {"h": "أرسل لنا طلبك", "name": "الاسم", "org": "الجهة أو الشركة", "email": "البريد الإلكتروني", "phone": "الهاتف (اختياري)",
          "interest": "الخدمة المطلوبة", "msg": "رسالتك", "msg_ph": "اكتب هنا عن احتياجك أو المشروع الذي تعمل عليه.",
          "consent": "أوافق على استخدام بياناتي للرد على طلبي وفق", "send": "إرسال", "sending": "جارٍ الإرسال...",
          "ok": "وصلنا طلبك، وسنعود إليك قريبًا.", "err": "تعذر الإرسال. أرسل لنا على البريد مباشرة: " + EMAIL,
          "mail_note": "سيفتح الإرسال تطبيق البريد لديك برسالة جاهزة.", "req": "هذا الحقل مطلوب", "subject": "استفسار جديد من موقع أفيرا",
          "opts": ["الذكاء الاصطناعي المؤسسي", "GeoAI", "إدارة المحافظ", "أخرى"]},
 "privacy": {
  "title": "سياسة الخصوصية | شركة أفيرا", "desc": "سياسة الخصوصية لشركة أفيرا: كيف نتعامل مع البيانات التي تصلنا عبر البريد الإلكتروني ونموذج التواصل، وما الذي لا نجمعه، وكيف تمارس حقوقك.",
  "h1": "سياسة الخصوصية", "effective": "تاريخ السريان: نوفمبر 2026",
  "body": [
   ("1. من نحن", "تُشغّل شركة أفيرا (الرياض، المملكة العربية السعودية) هذا الموقع والخدمات المرتبطة به. وتشير عبارتا «شركة أفيرا» و«نحن» إلى هذه الجهة."),
   ("2. المعلومات التي نجمعها", "لا يستخدم هذا الموقع ملفات تعريف الارتباط ولا أدوات تحليل أو تتبع إعلاني، وتُقدَّم الخطوط والملفات من خادمنا نفسه لا من أطراف ثالثة. ومثل أي موقع، يسجّل مزوّد الاستضافة بيانات تقنية معتادة (مثل عنوان الشبكة والتاريخ والوقت والصفحة المطلوبة) لأغراض الأمان والتشغيل. وإذا راسلتنا عبر البريد الإلكتروني أو النموذج، فإننا نستلم الاسم وجهة العمل وبيانات التواصل ومضمون رسالتك."),
   ("3. كيف نستخدم معلوماتك", "نستخدم المعلومات التي تصلنا للرد على استفسارك وتقييم فرص التعاون وحفظ سجل المراسلات المؤسسية. ولا نبيع بياناتك الشخصية ولا نؤجرها ولا نشاركها مع أطراف ثالثة لأغراض تسويقية."),
   ("4. مكان معالجة البيانات", "تُعالج البيانات التي تصلنا عبر هذا الموقع وفق متطلبات نظام حماية البيانات الشخصية (PDPL) وإرشادات الهيئة السعودية للبيانات والذكاء الاصطناعي (سدايا) المعمول بها."),
   ("5. حقوقك", "يحق لك طلب الاطلاع على بياناتك الشخصية أو تصحيحها أو حذفها أو تقييد معالجتها وفق الأنظمة المعمول بها. لممارسة هذه الحقوق تواصل معنا على " + PRIVACY_EMAIL + "."),
   ("6. التواصل", "لأي استفسار عن الخصوصية راسلنا على " + PRIVACY_EMAIL + "."),
  ]},
 "nf_h": "الصفحة غير موجودة",
},
"en": {
 "dir": "ltr", "lang": "en", "base": "/en/", "other": "ar", "other_label": "العربية", "locale": "en_US", "other_locale": "ar_SA",
 "brand": "Avyra Company", "brand_core": "AVYRA", "co": "Company", "skip": "Skip to content", "home_label": "Home",
 "nav": [("about", "About"), ("services", "Services"), ("projects", "Experience"), ("team", "Team"), ("contact", "Contact")],
 "nav_services": "Services",
 "title": "Avyra Company | Enterprise AI, GeoAI and Portfolio and Project Governance in Riyadh",
 "desc": "Avyra Company is a Saudi company in Riyadh combining enterprise AI deployment, GeoAI and portfolio and project governance for Vision 2030 digital transformation and environmental programs.",
 "eyebrow": "Riyadh · Saudi Arabia",
 "h1": "From complex data to governed decisions.",
 "lead": "Enterprise AI, GeoAI and portfolio and project governance for government, corporates, SMEs and professional firms. We turn complexity into governed intelligence, and intelligence into sustainable impact.",
 "cta1": "Contact us", "cta2": "Our services", "logo_alt": "Avyra logo",
 "trust": ["PfMP · PgMP · PMP certified portfolio, program and project management", "Saudi-registered, Riyadh-based", "Designed to align with NCA-ECC", "Delivering with US and German technology partners"],
 "about_eyebrow": "About", "about_h": "Vision and mission",
 "vision_h": "Our vision", "vision": "To be the Kingdom's trusted partner in enabling decisions, through smart, sustainable and economically sound solutions that become governed, data-driven portfolios.",
 "mission_h": "Our mission", "mission": "We develop and deploy AI business-intelligence systems, GeoAI solutions and portfolio governance frameworks that help Saudi organizations treat data as a strategic asset. By combining enterprise-grade AI engineering, GeoAI, and certified portfolio, program and project management, we turn complex data into boardroom-ready intelligence.",
 "gap_h": "Why we exist", "gap": "Most firms offer one piece of the puzzle. Traditional engineering consultancies deliver technical studies but lack portfolio and project governance. Pure AI firms build models but do not understand real-world uncertainty in environmental and spatial data. We bring all three together under one Saudi-registered entity: governance, GeoAI and operational AI deployment.",
 "svc_eyebrow": "Services", "svc_h": "Three integrated pillars",
 "pillars": [
  {"icon": "ai", "tag": "Pillar A", "h": "Enterprise AI, digital transformation and sovereign deployment",
   "items": [("AI agents and workflow automation", "Human-supervised automation for operations, approvals and service execution."),
             ("Digital transformation for companies", "Helping companies assess where they stand, set priorities and roll out digital and AI-enabled ways of working, from process redesign to adoption."),
             ("Custom platform development", "Designing and building custom AI-powered platforms and applications around how your organization works, from architecture to deployment."),
             ("Knowledge and document intelligence", "Enterprise document retrieval and multilingual (Arabic/English) content intelligence for organizations managing large document estates, from regulators to law firms."),
             ("Private and sovereign AI deployment", "Cloud, private cloud, on-premises and hybrid deployment, designed to align with NCA-ECC, SDAIA guidance and PDPL. Critical for government clients.")],
   "outcome": "Enterprise-grade AI that operates inside your security and governance perimeter."},
  {"icon": "geo", "tag": "Pillar B", "h": "GeoAI advisory",
   "items": [("GeoAI-enabled modeling for business and smart solutions", "Combining satellite imagery and remote-sensing data with advanced analytical models to support business decisions and smart solutions."),
             ("Geospatial database and SDI design", "Designing geospatial databases and spatial data infrastructure that make an organization's data shareable and analyzable."),
             ("Spatial and operational intelligence", "Infrastructure monitoring, field operations awareness and environmental visibility for distributed assets."),
             ("Digital twin concepts for infrastructure", "Readiness assessment, architecture design and an implementation roadmap for infrastructure digital twins.")],
   "outcome": "From satellite data to a boardroom decision, in weeks, not years."},
  {"icon": "gov", "tag": "Pillar C", "h": "Portfolio, Program and Project Governance",
   "items": [("Governance maturity assessment", "Assessing your current portfolio and program management against leading practice, and prioritizing the gaps that matter."),
             ("Governance framework design", "Building portfolio, program and project governance frameworks sized to your organization."),
             ("Digital transformation governance", "Embedding portfolio and project governance into digital transformation programs, keeping initiatives on schedule and accountable."),
             ("Certified advisory support", "Supporting PMOs with certified PfMP, PgMP and PMP expertise.")],
   "outcome": "A portfolio managed with clarity, from priority to impact."},
 ],
 "proj_eyebrow": "Experience", "proj_h": "Representative experience",
 "proj_note": "Avyra prioritizes confidentiality. Specific organizational references and detailed case studies are shared directly under appropriate confidentiality agreements. The categories below represent the combined track record of our leadership and partner teams.",
 "proj_cols": ("Sector", "Project type", "Our role"),
 "proj": [("Enterprise AI (KSA)", "AI agents for service workflows", "Operational AI deployment"),
          ("Custom AI systems", "Full-stack AI application development", "System architecture and deployment"),
          ("Custom GeoAI systems", "GeoAI solutions", "System build with our development partner"),
          ("Digital transformation", "Digital transformation programs for companies", "Advisory and delivery support")],
 "team_eyebrow": "Team", "team_h": "Leadership",
 "team": [("Eng. Khalid Abdelrahman", "Chief Executive Officer", "Has led the company’s operations in the Kingdom and its international partnership for over a decade, in enterprise software delivery and government digital transformation."),
          ("Dr. Mohammed Abdallah", "Technical Director", "Holds PfMP, PgMP and PMP certifications in portfolio, program and project management.")],
 "network": "Every engagement is led by our core team and delivered with specialist engineers and analysts in AI, full-stack development, GIS and remote sensing, and infrastructure and environmental advisory.",
 "why_eyebrow": "Why Avyra", "why_h": "The Saudi advantage",
 "why": [("Saudi-registered, Riyadh-based", "We operate inside your regulatory and procurement environment."),
         ("Vision 2030-aligned", "Our work directly supports environmental sustainability and digital transformation goals."),
         ("Sovereign AI deployment", "Designed to align with NCA-ECC and PDPL, and deployable on-premises or in private cloud. Critical for government clients."),
         ("Three competencies in one team", "Portfolio and project governance, GeoAI and enterprise AI together."),
         ("Trilingual delivery", "English, German and Arabic, with executive summaries tailored for Saudi decision-makers."),
         ("US and German technology depth", "Our technology partnerships in Virginia and Germany bring engineering depth, while delivery and accountability stay in the Kingdom.")],
 "contact_eyebrow": "Contact", "contact_h": "Let's discuss your project", "contact_p": "Tell us what you need. Our teams in Riyadh and Virginia respond within one business day, and all inquiries are handled with strict confidentiality.",
 "book": "Book a 30-minute diagnostic call", "linkedin": "LinkedIn",
 "labels": {"email": "Email", "phone": "Phone", "hq": "Location", "hq_val": "Al Olaya, Riyadh, Saudi Arabia", "cr": "C.R. number",
            "contact_h": "Contact", "company_h": "Company", "privacy": "Privacy policy", "rights": "All rights reserved", "links_h": "Links"},
 "form": {"h": "Send us a message", "name": "Name", "org": "Organization", "email": "Email", "phone": "Phone (optional)",
          "interest": "Service of interest", "msg": "Your message", "msg_ph": "Tell us about your need or the project you are working on.",
          "consent": "I agree that my data is used to answer my request, as described in the", "send": "Send", "sending": "Sending...",
          "ok": "We received your message and will get back to you shortly.", "err": "Could not send. Please email us directly: " + EMAIL,
          "mail_note": "Sending opens your email app with a ready message.", "req": "This field is required", "subject": "New enquiry from the Avyra website",
          "opts": ["Enterprise AI", "GeoAI", "Portfolio management", "Other"]},
 "privacy": {
  "title": "Privacy Policy | Avyra Company", "desc": "Avyra Company's privacy policy: how we handle data sent by email and through the contact form, what we do not collect, and how to exercise your rights.",
  "h1": "Privacy policy", "effective": "Effective: November 2026",
  "body": [
   ("1. Who we are", "Avyra Company (Riyadh, Saudi Arabia) operates this website and its related services. References to \"Avyra Company\" and \"we\" mean this entity."),
   ("2. Information we collect", "This website does not use cookies, analytics or advertising trackers, and its fonts and files are served from our own server, not third parties. Like any website, our hosting provider logs routine technical data (such as network address, date and time, and the page requested) for security and operations. If you write to us by email or the contact form, we receive your name, organization, contact details and the content of your message."),
   ("3. How we use your information", "We use the information we receive to answer your enquiry, assess collaboration opportunities and keep a record of business correspondence. We do not sell or rent your personal data, and we do not share it with third parties for marketing."),
   ("4. Where data is processed", "Data sent through this website is handled in line with the Personal Data Protection Law (PDPL) and applicable SDAIA guidance."),
   ("5. Your rights", "You may ask to access, correct, delete or restrict the processing of your personal data under applicable law. To exercise these rights, contact us at " + PRIVACY_EMAIL + "."),
   ("6. Contact", "For any privacy question, write to " + PRIVACY_EMAIL + "."),
  ]},
 "nf_h": "Page not found",
},
}

# ---------------------------------------------------------------- helpers
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
def path_for(lang, key):
    base = T[lang]["base"]; return base if key == "home" else f"{base}{key}/"
def url(lang, key): return SITE + path_for(lang, key)
def write(rel, content):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

def org_ld(lang):
    d = {"@context": "https://schema.org", "@type": "Organization", "name": "Avyra Company", "alternateName": "شركة أفيرا",
         "url": SITE + "/", "logo": SITE + "/assets/img/icon-512.png", "email": EMAIL,
         "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"}, "areaServed": "SA"}
    if PHONE_TEL: d["telephone"] = PHONE_TEL
    if CR: d["identifier"] = CR
    return d

def head(lang, key, title, desc, ld=None):
    t = T[lang]; o = t["other"]
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (ld or []))
    return f'''<!doctype html>
<html lang="{t["lang"]}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url(lang, key)}">
<link rel="alternate" hreflang="{lang}" href="{url(lang, key)}">
<link rel="alternate" hreflang="{o}" href="{url(o, key)}">
<link rel="alternate" hreflang="x-default" href="{url('ar', key)}">
<meta name="theme-color" content="#0b0b0d">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(t["brand"])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url(lang, key)}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:locale:alternate" content="{t["other_locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/assets/img/og-image.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
{PRELOAD[lang]}<link rel="stylesheet" href="{CSS}">
<script>document.documentElement.classList.add("js")</script>
{ldh}</head>
'''

MENU = {"ar": ("القائمة", "إغلاق القائمة"), "en": ("Menu", "Close menu")}

def header(lang, key):
    t = T[lang]; b = t["base"]; o = t["other"]
    links = "".join(f'<a href="{path_for(lang, k)}"' + (' aria-current="page"' if key == k else "") + f'>{n}</a>' for k, n in t["nav"])
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header class="site">
  <a class="brand" href="{b}" aria-label="{esc(t["brand"])} - {t["home_label"]}"><img src="/assets/img/mark.png" alt="" width="46" height="48"><span class="brand-txt"><span class="brand-name">{esc(t["brand_core"])}</span><span class="brand-co">{t["co"]}</span></span></a>
  <button class="menu-btn" type="button" hidden aria-label="{MENU[lang][0]}" aria-expanded="false" aria-controls="site-nav" data-open="{MENU[lang][0]}" data-close="{MENU[lang][1]}"><span class="bars" aria-hidden="true"></span></button>
  <nav class="main" id="site-nav" aria-label="{'التنقل الرئيسي' if lang == 'ar' else 'Main'}">
    {links}
    <a class="lang" href="{path_for(o, key)}" hreflang="{o}" lang="{o}">{t["other_label"]}</a>
  </nav>
</header>
'''

def contact_items(lang):
    t = T[lang]; L = t["labels"]; rows = [(L["email"], f'<a href="mailto:{EMAIL}"><bdi>{EMAIL}</bdi></a>')]
    if PHONE_TEL: rows.append((L["phone"], f'<a href="tel:{PHONE_TEL}"><bdi>{PHONE_DISPLAY}</bdi></a>'))
    if LINKEDIN_URL: rows.append((t["linkedin"], f'<a href="{LINKEDIN_URL}" target="_blank" rel="noopener">LinkedIn</a>'))
    rows.append((L["hq"], L["hq_val"]))
    if CR: rows.append((L["cr"], f"<bdi>{CR}</bdi>"))
    return rows

def footer(lang):
    t = T[lang]; L = t["labels"]; b = t["base"]
    nav = "".join(f'<li><a href="{path_for(lang, k)}">{n}</a></li>' for k, n in t["nav"][:4])
    contact = "".join(f"<li>{v}</li>" for k, v in contact_items(lang) if k != L["cr"])
    return f'''<footer class="site">
  <div class="wrap">
    <div class="stack g12"><a class="brand" href="{b}"><img src="/assets/img/mark.png" alt="" width="34" height="36" loading="lazy"><span class="brand-txt"><span class="brand-name" style="font-size:20px">{esc(t["brand_core"])}</span><span class="brand-co">{t["co"]}</span></span></a>
      <p>{L["hq_val"]}</p></div>
    <div><h2>{L["links_h"]}</h2><ul>{nav}</ul></div>
    <div><h2>{L["contact_h"]}</h2><ul>{contact}</ul></div>
    <div><h2>{L["company_h"]}</h2><ul>{"<li>" + L["cr"] + ": <bdi>" + CR + "</bdi></li>" if CR else ""}<li><a href="{path_for(lang, "privacy")}">{L["privacy"]}</a></li></ul></div>
    <p class="fine">© 2026 {esc(t["brand"])}. {L["rights"]}.</p>
  </div>
</footer>
'''

def form_html(lang):
    f = T[lang]["form"]; t = T[lang]
    opts = "".join(f'<option value="{esc(o)}">{o}</option>' for o in f["opts"])
    action = FORM_ENDPOINT or f"mailto:{EMAIL}"
    return f'''<form class="form" id="f-home" method="post" action="{action}" data-endpoint="{FORM_ENDPOINT}" data-key="{FORM_KEY}" data-subject="{esc(f["subject"])}" data-ok="{esc(f["ok"])}" data-err="{esc(f["err"])}" data-sending="{esc(f["sending"])}" data-req="{esc(f["req"])}" novalidate>
  <h2>{f["h"]}</h2>
  <div class="fields">
    <label for="f-name">{f["name"]}<input id="f-name" name="name" type="text" autocomplete="name" required></label>
    <label for="f-org">{f["org"]}<input id="f-org" name="organization" type="text" autocomplete="organization"></label>
    <label for="f-email">{f["email"]}<input id="f-email" name="email" type="email" autocomplete="email" dir="ltr" required></label>
    <label for="f-phone">{f["phone"]}<input id="f-phone" name="phone" type="tel" autocomplete="tel" dir="ltr"></label>
    <label for="f-int" class="full">{f["interest"]}<select id="f-int" name="division">{opts}</select></label>
    <label for="f-msg" class="full">{f["msg"]}<textarea id="f-msg" name="message" rows="5" placeholder="{esc(f["msg_ph"])}" required></textarea></label>
  </div>
  <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
  <label class="consent" for="f-ok"><input id="f-ok" name="consent" type="checkbox" required><span>{f["consent"]} <a href="{path_for(lang, "privacy")}">{t["labels"]["privacy"]}</a></span></label>
  <div class="actions"><button class="btn gold" type="submit">{f["send"]}</button>{'' if FORM_ENDPOINT else '<p class="note">' + f["mail_note"] + '</p>'}</div>
  <p class="status" role="status" aria-live="polite"></p>
</form>'''

# ---------------------------------------------------------------- pages
PAGES = ["about", "services", "projects", "team", "contact"]
GO = {
 "ar": {"about": "رؤيتنا ورسالتنا، ولماذا نجمع الحوكمة وGeoAI والذكاء الاصطناعي المؤسسي في فريق واحد.",
        "services": "ثلاث ركائز متكاملة: الذكاء الاصطناعي المؤسسي، والاستشارات في GeoAI، وحوكمة المحافظ والمشاريع.",
        "projects": "فئات المشاريع التي نعمل فيها ودورنا في كل منها.",
        "team": "قيادة الشركة والشبكة الفنية التي تدعمها.",
        "contact": "اكتب لنا عن مشروعك، ونرد خلال يوم عمل واحد.", "more": "اعرف المزيد", "explore_h": "استكشف أفيرا"},
 "en": {"about": "Our vision and mission, and why we bring governance, GeoAI and enterprise AI into one team.",
        "services": "Three integrated pillars: enterprise AI, GeoAI advisory, and portfolio and project governance.",
        "projects": "The project categories we work in and our role in each.",
        "team": "The company's leadership and the technical network behind it.",
        "contact": "Tell us about your project. We reply within one business day.", "more": "Learn more", "explore_h": "Explore Avyra"},
}

def sec_about(t):
    why = "".join(f'<div class="card"><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for a, b in t["why"])
    return f'''<section class="alt"><div class="wrap stack g48">
  <div class="cols"><div class="stack g12"><h2 style="font-size:28px">{t["vision_h"]}</h2><p class="muted">{t["vision"]}</p></div><div class="stack g12"><h2 style="font-size:28px">{t["mission_h"]}</h2><p class="muted">{t["mission"]}</p></div></div>
  <div class="stack g12 gap-note"><h3>{t["gap_h"]}</h3><p class="muted">{t["gap"]}</p></div>
</div></section>
<section><div class="wrap stack g48">
  <div class="stack g12" style="max-width:640px"><p class="eyebrow">{t["why_eyebrow"]}</p><h2>{t["why_h"]}</h2></div>
  <div class="cards">{why}</div>
</div></section>
'''

def sec_services(t):
    pillars = ""
    for p in t["pillars"]:
        items = "".join(f'<div class="principle"><h3>{esc(a)}</h3><p>{esc(c)}</p></div>' for a, c in p["items"])
        pillars += f'''<div class="card pillar">{ICONS[p["icon"]]}<p class="eyebrow">{p["tag"]}</p><h2>{esc(p["h"])}</h2><div class="stack">{items}</div><p class="outcome">{esc(p["outcome"])}</p></div>
'''
    return f'<section><div class="wrap"><div class="cards two">{pillars}</div></div></section>\n'

def sec_projects(t):
    c = t["proj_cols"]
    proj = "".join(f'<div class="card"><p class="eyebrow">{esc(a)}</p><h2>{esc(b)}</h2><p><strong>{c[2]}:</strong> {esc(r)}</p></div>' for a, b, r in t["proj"])
    return f'<section><div class="wrap stack g48"><p class="muted" style="max-width:72ch">{t["proj_note"]}</p><div class="cards">{proj}</div></div></section>\n'

def sec_team(t):
    team = ""
    for n, r, note in t["team"]:
        lines = []
        if PHONE_TEL: lines.append(f'<li><a href="tel:{PHONE_TEL}"><bdi>{PHONE_DISPLAY}</bdi></a></li>')
        lines.append(f'<li><a href="mailto:{EMAIL}"><bdi>{EMAIL}</bdi></a></li>')
        team += f'<div class="card"><h2>{esc(n)}</h2><p class="eyebrow">{esc(r)}</p><p class="muted">{esc(note)}</p><ul>{"".join(lines)}</ul></div>\n'
    return f'<section><div class="wrap stack g48"><div class="cards">{team}</div><p class="muted" style="max-width:70ch">{t["network"]}</p></div></section>\n'

def sec_contact(lang, t):
    rows = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in contact_items(lang))
    book = f'<div class="btns"><a class="btn" href="{BOOKING_URL}" target="_blank" rel="noopener">{t["book"]}</a></div>' if BOOKING_URL else ""
    return f'''<section><div class="wrap cols">
    <div class="stack g28"><p class="muted">{t["contact_p"]}</p><dl class="rows">{rows}</dl>{book}</div>
    {form_html(lang)}
  </div></section>
'''

HEAD = {"about": ("about_eyebrow", "about_h"), "services": ("svc_eyebrow", "svc_h"), "projects": ("proj_eyebrow", "proj_h"),
        "team": ("team_eyebrow", "team_h"), "contact": ("contact_eyebrow", "contact_h")}
SUB = {"services": "svc_h"}

def page(lang, key):
    t = T[lang]; eb, hh = HEAD[key]
    sec = {"about": lambda: sec_about(t), "services": lambda: sec_services(t), "projects": lambda: sec_projects(t),
           "team": lambda: sec_team(t), "contact": lambda: sec_contact(lang, t)}[key]()
    title = f'{(t["nav_services"] if key in SUB else t[hh])} | {t["brand"]}'
    desc = {"about": t["vision"], "services": t["gap"][:0] + GO[lang]["services"], "projects": GO[lang]["projects"],
            "team": GO[lang]["team"], "contact": t["contact_p"]}[key]
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["home_label"], "item": url(lang, "home")},
        {"@type": "ListItem", "position": 2, "name": t["nav_services"] if key in SUB else t[hh], "item": url(lang, key)}]}
    body = f'''<body>
{header(lang, key)}<main id="main">
<section class="page-hero"><div class="wrap stack g20"><nav class="crumbs" aria-label="breadcrumb"><a href="{t["base"]}">{t["home_label"]}</a><span aria-hidden="true">/</span><span>{t["nav_services"] if key in SUB else t[hh]}</span></nav><p class="eyebrow">{t[eb]}</p><h1>{t["nav_services"] if key in SUB else t[hh]}</h1>{('<p class="lead">' + t[SUB[key]] + '</p>') if key in SUB else ''}</div></section>
{sec}</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, key, title, desc, [crumb]) + body

def home(lang):
    t = T[lang]; g = GO[lang]
    arrow = "←" if lang == "ar" else "→"
    trust = "".join("<li>" + esc(x).replace("PfMP · PgMP · PMP", "<bdi>PfMP · PgMP · PMP</bdi>") + "</li>" for x in t["trust"])
    logo = f"/assets/img/logo-{lang}.png"
    dims = {"ar": (440, 486), "en": (440, 573)}[lang]
    names = dict(t["nav"])
    cards = "".join(f'<div class="card link"><h3>{names[k]}</h3><p>{g[k]}</p><a class="more stretch" href="{path_for(lang, k)}">{g["more"]} {arrow}</a></div>' for k in PAGES[:4])
    body = f'''<body>
{header(lang, "home")}<main id="main">
<section class="hero">
  <div class="wrap cols" style="align-items:center">
    <div class="stack g28">
      <p class="eyebrow">{t["eyebrow"]}</p>
      <h1>{t["h1"]}</h1>
      <p class="lead">{t["lead"]}</p>
      <div class="btns"><a class="btn gold" href="{path_for(lang, "contact")}">{t["cta1"]}</a><a class="btn" href="{path_for(lang, "services")}">{t["cta2"]}</a></div>
    </div>
    <div class="hero-art"><div class="emb"><img src="{logo}" alt="{t["logo_alt"]}" width="{dims[0]}" height="{dims[1]}" fetchpriority="high"><span class="sheen" style="--m:url({logo})" aria-hidden="true"></span></div></div>
  </div>
</section>
<section class="trustbar"><div class="wrap"><ul>{trust}</ul></div></section>
<section><div class="wrap stack g48"><h2>{g["explore_h"]}</h2><div class="cards">{cards}</div></div></section>
<section class="alt cta"><div class="wrap"><div class="stack g12"><h2>{t["contact_h"]}</h2><p class="muted">{g["contact"]}</p></div><div class="btns"><a class="btn gold" href="{path_for(lang, "contact")}">{t["cta1"]}</a></div></div></section>
</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, "home", t["title"], t["desc"], [org_ld(lang)]) + body

def privacy(lang):
    t = T[lang]; p = t["privacy"]
    paras = "".join(f"<h2>{a}</h2><p>{c}</p>" for a, c in p["body"])
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["home_label"], "item": url(lang, "home")},
        {"@type": "ListItem", "position": 2, "name": t["labels"]["privacy"], "item": url(lang, "privacy")}]}
    body = f'''<body>
{header(lang, "privacy")}<main id="main">
<section class="page-hero"><div class="wrap stack g20"><h1>{p["h1"]}</h1><p class="muted">{p["effective"]}</p></div></section>
<section><div class="wrap prose">{paras}</div></section>
</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, "privacy", p["title"], p["desc"], [crumb]) + body

def notfound():
    return f'''<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>الصفحة غير موجودة | Page not found</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="preload" href="/assets/fonts/ibm-plex-sans-arabic-arabic-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{CSS}"></head>
<body><main id="main" style="min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:40px 20px">
<div class="stack g20" style="align-items:center"><img src="/assets/img/mark.png" alt="" width="84" height="88">
<h1 style="font-size:44px">الصفحة غير موجودة</h1><p class="muted">Page not found</p>
<div class="btns" style="justify-content:center"><a class="btn gold" href="/">الرئيسية</a><a class="btn" href="/en/">Home (English)</a></div></div></main></body></html>
'''

def sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for lang in ("ar", "en"):
        for k in ["home"] + PAGES + ["privacy"]:
            o = T[lang]["other"]
            out.append(f'<url><loc>{url(lang, k)}</loc><xhtml:link rel="alternate" hreflang="{lang}" href="{url(lang, k)}"/>'
                       f'<xhtml:link rel="alternate" hreflang="{o}" href="{url(o, k)}"/><xhtml:link rel="alternate" hreflang="x-default" href="{url("ar", k)}"/></url>')
    out.append("</urlset>")
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    for lang in ("ar", "en"):
        b = T[lang]["base"].lstrip("/")
        write(f"{b}index.html", home(lang))
        for k in PAGES: write(f"{b}{k}/index.html", page(lang, k))
        write(f"{b}privacy/index.html", privacy(lang))
    write("404.html", notfound())
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write("site.webmanifest", json.dumps({"name": "Avyra Company | شركة أفيرا", "short_name": "Avyra", "start_url": "/", "display": "browser",
        "background_color": "#0b0b0d", "theme_color": "#0b0b0d",
        "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False, indent=2) + "\n")
    write("_headers", """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; script-src 'self' 'unsafe-inline'; script-src-attr 'none'; base-uri 'self'; form-action 'self' mailto: https://formspree.io https://api.web3forms.com; connect-src 'self' https://formspree.io https://api.web3forms.com; frame-ancestors 'none'; object-src 'none'
/assets/*
  Cache-Control: public, max-age=31536000, immutable
""")
    print("built")
